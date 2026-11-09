// MyCreativeSite — envoi automatique des mails de prospection (09/11/2026), même principe que le robot EPS.
// - Envoi par la boîte OVH contact@mycreativesite.fr en SMTP (mot de passe saisi dans l'admin → clicandsite.secrets 'smtp_password', ou secret SMTP_PASSWORD ; SMTP_USER/HOST/PORT facultatifs, ssl0.ovh.net:465),
//   ou à défaut par l'API Gmail (GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, GMAIL_REFRESH_TOKEN). CS_FROM = adresse d'envoi.
// - Jours ouvrés, 9 h – 18 h (Paris), envois étalés (objectif proportionnel à l'heure, 2 mails max par passage).
// - Limite par jour et métiers ciblés : table clicandsite.mail_settings (réglable dans l'admin). Robot éteint par défaut.
// - Cible : prospects « nouveau » / « à contacter » avec e-mail, sans site moderne, jamais écrits, hors opposition.
// - Désinscription en 1 clic (lien signé + en-tête List-Unsubscribe) ou réponse STOP ; rapport quotidien par Gmail.
// Appels : cron (POST, en-tête x-cs-key = secret mail_internal) ; GET ?health=1 ; GET ?u=<id>&k=<signature> (désinscription) ;
//          POST {mode:"test", to, trade} pour un mail d'essai (adresses autorisées seulement) ; POST {mode:"preview", trade}.
import postgres from "https://deno.land/x/postgresjs@v3.4.5/mod.js";

const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });
const FN_URL = "https://avcynjwcyygygkjuxsdt.supabase.co/functions/v1/cs-prospecting";
const SITE = "https://mycreativesite.fr";
const NAME = "MyCreativeSite";
const START_H = 9, END_H = 18, MAX_PER_TICK = 2, MAX_ATTEMPTS = 2, LOCK_SECONDS = 150;
const PERMANENT = /invalid|not found|does not exist|recipient address rejected|invalid to header/i;
const TEST_TO = ["docheanthony@gmail.com", "abracadeal@gmail.com", "contact@mycreativesite.fr"];

const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { "content-type": "application/json; charset=utf-8" } });
const html = (b: string, s = 200) => new Response(b, { status: s, headers: { "content-type": "text/html; charset=utf-8" } });
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));
const from = () => (Deno.env.get("CS_FROM") || "contact@mycreativesite.fr").trim();

// ---------- Modèles de mail (par métier) ----------
type Tpl = { key: string; subject: string; body: string; btn: { label: string; url: string } };
const TRADE: Record<string, { label: string; page: string; pack: boolean; plus: string }> = {
  vtc: { label: "chauffeur VTC", page: "/site-internet-vtc/", pack: false, plus: "un formulaire de réservation de courses" },
  restaurant: { label: "restaurant", page: "/site-internet-restaurant/", pack: false, plus: "votre carte en ligne et un agenda de réservation de tables" },
  garage: { label: "garage", page: "/site-internet-garage/", pack: true, plus: "un agenda de rendez-vous atelier et vos véhicules diffusés sur Abracadeal" },
  immobilier: { label: "agence immobilière", page: "/site-internet-agence-immobiliere/", pack: true, plus: "vos biens diffusés automatiquement sur Abracadeal" },
  batiment: { label: "artisan du bâtiment", page: "/site-internet-artisan-batiment/", pack: false, plus: "vos réalisations en photos et un formulaire de devis" },
  veterinaire: { label: "clinique vétérinaire", page: "/site-internet-veterinaire/", pack: false, plus: "la prise de rendez-vous en ligne et vos horaires d'urgence" },
};
function template(p: { name: string; trade: string; city: string; site_status: string | null; segment: string | null }): Tpl {
  const t = TRADE[p.trade] || TRADE.restaurant;
  let page = t.page;
  if (p.segment === "concession") page = "/site-internet-concession-automobile/";
  if (p.segment === "moto") page = "/site-internet-concession-moto/";
  const hasSite = p.site_status === "date" || p.site_status === "injoignable";
  const who = p.name || "votre entreprise";
  const where = p.city ? " à " + p.city : "";
  const price = t.pack
    ? "Le Pack Auto, Moto & Immo est à 99 € par mois : le site et les annonces illimitées sur Abracadeal."
    : "Les formules commencent à 29 € par mois.";
  const intro = hasSite
    ? (p.site_status === "injoignable"
      ? `En cherchant ${who}${where}, je suis tombé sur votre site internet, mais il ne s'affiche plus.`
      : `En cherchant ${who}${where}, je suis tombé sur votre site internet : il commence à dater, surtout sur téléphone.`)
    : `En cherchant ${who}${where}, je n'ai pas trouvé de site internet à votre nom.`;
  const body = [
    "Bonjour,",
    "",
    intro,
    "",
    `Je m'appelle Anthony, je dirige MyCreativeSite : nous créons des sites internet pour les professionnels, livrés en 48 h. Vous les modifiez vous-même en un clic depuis votre téléphone (photos, textes, horaires), et nous gardons la main pour toute réparation.`,
    "",
    `Pour ${/^(clinique|agence)/.test(t.label) ? "une" : "un"} ${t.label}, le site comprend ${t.plus}.`,
    "",
    price,
    "",
    "Vous pouvez voir des exemples de sites avec le bouton ci-dessous. Si cela vous intéresse, il suffit de répondre à ce mail.",
    "",
    "Bonne journée,",
    "Anthony",
    "MyCreativeSite",
  ].join("\n");
  const subject = hasSite ? `${who} : un site internet neuf en 48 h` : `${who} : votre site internet en 48 h`;
  return { key: p.trade + (hasSite ? "-refonte" : "-creation"), subject, body, btn: { label: "Voir des exemples de sites", url: SITE + page } };
}

// ---------- Signature des liens de désinscription ----------
async function sign(id: string): Promise<string> {
  const key = (await sql`select value from clicandsite.secrets where name='mail_internal'`)[0]?.value || "";
  const k = await crypto.subtle.importKey("raw", new TextEncoder().encode(key), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const s = new Uint8Array(await crypto.subtle.sign("HMAC", k, new TextEncoder().encode("unsub:" + id)));
  return Array.from(s.slice(0, 12)).map((b) => b.toString(16).padStart(2, "0")).join("");
}
const unsubUrl = async (id: string) => `${FN_URL}?u=${id}&k=${await sign(id)}`;

// ---------- Gmail ----------
function b64urlUtf8(s: string) { const b = new TextEncoder().encode(s); let x = ""; for (const c of b) x += String.fromCharCode(c); return btoa(x).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, ""); }
function b64Mime(s: string) { const b = new TextEncoder().encode(s); let x = ""; for (const c of b) x += String.fromCharCode(c); return (btoa(x).match(/.{1,76}/g) || []).join("\r\n"); }
const encHeader = (s: string) => "=?UTF-8?B?" + btoa(String.fromCharCode(...new TextEncoder().encode(s.replace(/[\r\n]/g, " ")))) + "?=";
function buildHtml(body: string, btn: Tpl["btn"], unsub: string) {
  const paras = body.split("\n\n").map((p) => `<p style="margin:0 0 14px">${esc(p).replace(/\n/g, "<br>")}</p>`).join("");
  return `<!doctype html><html><body style="margin:0;background:#f5f3fa;font-family:Arial,Helvetica,sans-serif;color:#1d1630">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#fff;border-radius:14px">
<tr><td style="padding:26px 28px 6px;font-size:15px;line-height:1.55">${paras}
<p style="margin:22px 0 8px"><a href="${esc(btn.url)}" style="display:inline-block;background:#6d28d9;color:#fff;text-decoration:none;font-weight:bold;padding:12px 20px;border-radius:10px">${esc(btn.label)}</a></p>
</td></tr><tr><td style="padding:14px 28px 22px;font-size:12px;color:#7a7290;border-top:1px solid #eee">
${NAME} · Création de sites internet pour les professionnels · <a href="${SITE}" style="color:#6d28d9">mycreativesite.fr</a><br>
Vous recevez ce message car votre entreprise est référencée dans l'annuaire officiel des entreprises.
<a href="${esc(unsub)}" style="color:#7a7290">Ne plus recevoir nos messages</a> (ou répondez STOP).
</td></tr></table></td></tr></table></body></html>`;
}
function buildMime(to: string, t: Tpl, unsub: string) {
  const q = "cs_" + crypto.randomUUID().replace(/-/g, "");
  const text = t.body + "\n\n" + t.btn.label + " : " + t.btn.url + "\n\n—\n" + NAME + " · " + SITE + "\nNe plus recevoir nos messages : " + unsub + " (ou répondez STOP)";
  const m = [
    ...stdHeaders(), `From: ${NAME} <${from()}>`, `Reply-To: ${from()}`, `To: ${to}`, `Subject: ${encHeader(t.subject)}`,
    `List-Unsubscribe: <${unsub}>, <mailto:${from()}?subject=STOP>`, "List-Unsubscribe-Post: List-Unsubscribe=One-Click",
    "MIME-Version: 1.0", `Content-Type: multipart/alternative; boundary="${q}"`, "",
    "--" + q, "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(text),
    "--" + q, "Content-Type: text/html; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(buildHtml(t.body, t.btn, unsub)),
    "--" + q + "--", "",
  ].join("\r\n");
  return m;
}
const stdHeaders = () => [`Date: ${new Date().toUTCString().replace("GMT", "+0000")}`, `Message-ID: <${crypto.randomUUID()}@mycreativesite.fr>`];
async function gmailTokenOnce() {
  const a = (Deno.env.get("GMAIL_CLIENT_ID") || "").trim(), b = (Deno.env.get("GMAIL_CLIENT_SECRET") || "").trim(), c = (Deno.env.get("GMAIL_REFRESH_TOKEN") || "").trim().replace(/^["']|["']$/g, "");
  if (!a || !b || !c) throw new Error("Gmail OAuth secrets missing");
  const r = await fetch("https://oauth2.googleapis.com/token", { method: "POST", headers: { "content-type": "application/x-www-form-urlencoded" }, body: new URLSearchParams({ client_id: a, client_secret: b, refresh_token: c, grant_type: "refresh_token" }) });
  const d = await r.json().catch(() => ({}));
  if (!r.ok || !d.access_token) throw new Error("Gmail token: " + (d.error || r.status) + " " + (d.error_description || ""));
  return d.access_token as string;
}
async function gmailToken() {
  let last: unknown;
  for (let i = 0; i < 3; i++) {
    try { return await gmailTokenOnce(); } catch (e) {
      last = e; if (/invalid_grant|invalid_client|unauthorized_client|secrets missing/i.test(String(e))) break;
      await new Promise((r) => setTimeout(r, 4000 * (i + 1)));
    }
  }
  throw last;
}
async function gmailSendRaw(tok: string, raw: string) {
  const r = await fetch("https://gmail.googleapis.com/gmail/v1/users/me/messages/send", { method: "POST", headers: { authorization: `Bearer ${tok}`, "content-type": "application/json" }, body: JSON.stringify({ raw }) });
  const d = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error("Gmail " + r.status + ": " + (d?.error?.message || JSON.stringify(d).slice(0, 200)));
  return d.id as string;
}
async function sendText(tok: string, to: string, subject: string, text: string) {
  const m = [...stdHeaders(), `From: ${NAME} <${from()}>`, `To: ${to}`, `Subject: ${encHeader(subject)}`, "MIME-Version: 1.0", "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(text), ""].join("\r\n");
  return sendMime(tok, to, m);
}

// ---------- Transport : SMTP (boîte OVH, prioritaire si SMTP_PASSWORD est posé) ou API Gmail ----------
let SMTP_PASS = "";
async function loadSmtpPass() { SMTP_PASS = Deno.env.get("SMTP_PASSWORD") || (await sql`select value from clicandsite.secrets where name='smtp_password'`)[0]?.value || ""; }
const useSmtp = () => Boolean(SMTP_PASS);
async function smtpSend(to: string | null, mime: string): Promise<string> {
  const host = Deno.env.get("SMTP_HOST") || "ssl0.ovh.net", port = Number(Deno.env.get("SMTP_PORT") || "465");
  const user = Deno.env.get("SMTP_USER") || from(), pass = SMTP_PASS;
  const conn = await Deno.connectTls({ hostname: host, port });
  const enc = new TextEncoder(), dec = new TextDecoder();
  let buf = "";
  const read = async (): Promise<string> => {
    const chunk = new Uint8Array(4096);
    for (;;) {
      const lines = buf.split("\r\n");
      for (let i = 0; i < lines.length - 1; i++) if (/^\d{3} /.test(lines[i])) { const out = lines.slice(0, i + 1).join("\n"); buf = lines.slice(i + 1).join("\r\n"); return out; }
      const n = await conn.read(chunk); if (n === null) throw new Error("SMTP: connexion fermée");
      buf += dec.decode(chunk.subarray(0, n));
    }
  };
  const cmd = async (c: string | null, ok: number[]) => {
    if (c !== null) await conn.write(enc.encode(c + "\r\n"));
    const r = await read(); const code = Number(r.slice(-200).match(/(\d{3}) [^\n]*$/)?.[1] || r.slice(0, 3));
    if (!ok.includes(code)) throw new Error("SMTP " + code + ": " + r.slice(0, 200));
    return r;
  };
  try {
    await cmd(null, [220]); await cmd("EHLO mycreativesite.fr", [250]);
    await cmd("AUTH LOGIN", [334]); await cmd(btoa(user), [334]); await cmd(btoa(pass), [235]);
    if (to === null) { try { await cmd("QUIT", [221]); } catch (_) { /* ignore */ } return "login-ok"; }
    await cmd(`MAIL FROM:<${from()}>`, [250]); await cmd(`RCPT TO:<${to}>`, [250, 251]); await cmd("DATA", [354]);
    const body = mime.replace(/\r?\n/g, "\r\n").split("\r\n").map((l) => (l.startsWith(".") ? "." + l : l)).join("\r\n");
    const r = await cmd(body + "\r\n.", [250]);
    try { await cmd("QUIT", [221]); } catch (_) { /* ignore */ }
    return "smtp:" + (r.match(/queued as ([^\s]+)/i)?.[1] || "ok");
  } finally { try { conn.close(); } catch (_) { /* ignore */ } }
}
async function getToken(): Promise<string> { return useSmtp() ? "" : await gmailToken(); }
async function sendMime(tok: string, to: string, mime: string) { return useSmtp() ? await smtpSend(to, mime) : await gmailSendRaw(tok, b64urlUtf8(mime)); }

function parisNow() {
  const p = new Intl.DateTimeFormat("en-CA", { timeZone: "Europe/Paris", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23", weekday: "short" }).formatToParts(new Date());
  const g = (t: string) => p.find((x) => x.type === t)?.value ?? "";
  return { date: `${g("year")}-${g("month")}-${g("day")}`, hour: Number(g("hour")), minute: Number(g("minute")), weekday: g("weekday") };
}
const frDate = (d: string) => d.split("-").reverse().join("/");

async function pending(trades: string[], limit: number) {
  if (limit <= 0) return [];
  return await sql`select p.id, lower(trim(p.email)) email, p.name, p.trade, p.city, p.site_status, p.segment
    from clicandsite.prospects p
    where p.email is not null and lower(trim(p.email)) ~ '^[^[:space:]@]+@[^[:space:]@]+[.][^[:space:]@]+$'
      and p.status in ('nouveau','a_contacter') and coalesce(p.site_status,'aucun') <> 'moderne' and p.trade = any(${trades})
      and not exists (select 1 from clicandsite.opposition o where lower(o.value) = lower(trim(p.email)))
      and not exists (select 1 from clicandsite.mail_recipients r where r.prospect_id = p.id and (r.status in ('envoyé','en cours','désinscrit') or r.attempts >= ${MAX_ATTEMPTS}))
      and not exists (select 1 from clicandsite.mail_recipients r2 where lower(r2.email) = lower(trim(p.email)) and r2.status in ('envoyé','désinscrit'))
    order by (p.status = 'a_contacter') desc, p.score desc nulls last, p.created_at asc limit ${limit}`;
}

async function report(date: string, to: string, tok: string) {
  const run = (await sql`select sent, failed, report_sent_at from clicandsite.mail_runs where run_date = ${date}::date`)[0];
  if (!run || run.report_sent_at) return;
  const st = (await sql`select (select count(*)::int from clicandsite.mail_recipients where status='envoyé') total,
    (select count(*)::int from clicandsite.mail_recipients where status='désinscrit') unsub`)[0];
  const s = (await sql`select trades from clicandsite.mail_settings where id=1`)[0];
  const left = (await pending(s.trades, 10000)).length;
  const fails = await sql`select p.name, r.email, r.last_error from clicandsite.mail_recipients r join clicandsite.prospects p on p.id = r.prospect_id
    where r.status = 'échec' and (r.created_at at time zone 'Europe/Paris')::date = ${date}::date limit 15`;
  const lines = [`Rapport prospection MyCreativeSite du ${frDate(date)}`, "", `Mails envoyés aujourd'hui : ${run.sent}`, `Échecs aujourd'hui : ${run.failed}`,
    `Total envoyé depuis le début : ${st.total}`, `Désinscriptions : ${st.unsub}`, `Pros avec e-mail restant à contacter : ${left}`,
    left < 40 ? "Attention : il reste moins de 2 jours d'envois, le robot de recherche doit trouver plus d'e-mails." : ""];
  if (fails.length) { lines.push("", "Adresses en échec :"); for (const f of fails) lines.push(`- ${f.name || "?"} <${f.email}> : ${String(f.last_error).slice(0, 120)}`); }
  lines.push("", "Robot de prospection MyCreativeSite");
  await sendText(tok, to, `Prospection MyCreativeSite — ${run.sent} envoyés le ${frDate(date)}`, lines.join("\n"));
  await sql`update clicandsite.mail_runs set report_sent_at = now() where run_date = ${date}::date`;
}

async function unsubscribe(id: string, k: string) {
  const page = (t: string, m: string) => html(`<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><title>${t}</title><body style="font-family:Arial,sans-serif;max-width:520px;margin:60px auto;padding:0 20px;color:#1d1630"><h1 style="font-size:22px">${t}</h1><p>${m}</p><p><a href="${SITE}" style="color:#6d28d9">mycreativesite.fr</a></p></body>`);
  if (!/^[0-9a-f-]{36}$/.test(id) || k !== (await sign(id))) return page("Lien invalide", "Ce lien de désinscription n'est pas valide. Répondez simplement STOP à notre message.");
  const p = (await sql`select email from clicandsite.prospects where id = ${id}::uuid`)[0];
  if (p?.email) {
    await sql`insert into clicandsite.opposition(value, reason) values (lower(trim(${p.email})), 'désinscription mail de prospection') on conflict (value) do nothing`;
    await sql`update clicandsite.prospects set status = 'refus', updated_at = now() where id = ${id}::uuid and status not in ('client','interesse')`;
    await sql`update clicandsite.mail_recipients set status = 'désinscrit' where prospect_id = ${id}::uuid`;
    await sql`insert into clicandsite.interactions(prospect_id, kind, content) values (${id}::uuid, 'note', 'Désinscription par le lien du mail de prospection')`;
  }
  return page("C'est noté", "Vous ne recevrez plus de messages de MyCreativeSite. Désolé pour le dérangement.");
}

Deno.serve(async (req: Request) => {
  try {
    await loadSmtpPass();
    const u = new URL(req.url);
    if (u.searchParams.get("u")) {
      if (req.method === "GET" || req.method === "POST") return await unsubscribe(u.searchParams.get("u")!, u.searchParams.get("k") || "");
    }
    if (req.method === "GET" && u.searchParams.get("health") === "1") {
      let ok = false, er = "";
      try { if (useSmtp()) await smtpSend(null, ""); else await gmailToken(); ok = true; } catch (e) { er = e instanceof Error ? e.message : String(e); }
      const s = (await sql`select enabled, daily_limit, trades from clicandsite.mail_settings where id=1`)[0];
      return json({ ok, transport: useSmtp() ? "smtp" : "gmail", error: er || undefined, from: from(), settings: s, smtp_password_saved: Boolean(SMTP_PASS), secrets_present: Object.fromEntries(["SMTP_PASSWORD", "SMTP_USER", "GMAIL_CLIENT_ID", "GMAIL_CLIENT_SECRET", "GMAIL_REFRESH_TOKEN", "CS_FROM"].map((x) => [x, Boolean(Deno.env.get(x))])) }, ok ? 200 : 503);
    }
    if (req.method !== "POST") return json({ error: "POST required" }, 405);
    const key = (await sql`select value from clicandsite.secrets where name='mail_internal'`)[0]?.value;
    if (!key || req.headers.get("x-cs-key") !== key) return json({ error: "Unauthorized" }, 401);
    const br = await req.json().catch(() => ({}));
    const sample = { id: "00000000-0000-0000-0000-000000000000", name: br?.name || "Garage du Port", trade: br?.trade || "garage", city: br?.city || "Cannes", site_status: br?.site_status || "aucun", segment: null };

    if (br?.mode === "preview") { const t = template(sample); return json({ subject: t.subject, body: t.body, button: t.btn }); }
    if (br?.mode === "test") {
      const to = String(br?.to || "").toLowerCase().trim();
      if (!TEST_TO.includes(to)) return json({ error: "test recipient not allowed" }, 400);
      const tok = await getToken(); const t = template(sample);
      const id = await sendMime(tok, to, buildMime(to, { ...t, subject: "[TEST] " + t.subject }, SITE));
      return json({ ok: true, test: true, to, gmail_id: id });
    }

    const s = (await sql`select enabled, daily_limit, trades, report_to from clicandsite.mail_settings where id=1`)[0];
    if (!s?.enabled) return json({ ok: true, skipped: "robot arrêté" });
    const np = parisNow(), manual = br?.mode === "manual";
    if (!manual && (np.hour < START_H || np.hour >= END_H)) return json({ ok: true, skipped: "hors horaires", paris: np });
    if (!manual && (np.weekday === "Sat" || np.weekday === "Sun")) return json({ ok: true, skipped: "week-end" });

    await sql`insert into clicandsite.mail_runs(run_date) values (${np.date}::date) on conflict do nothing`;
    const already = (await sql`select count(*)::int n from clicandsite.mail_recipients where status='envoyé' and (sent_at at time zone 'Europe/Paris')::date = ${np.date}::date`)[0].n as number;
    const limit = s.daily_limit as number;
    const lastTick = !manual && np.hour === END_H - 1 && np.minute >= 50;
    const windowMin = (END_H - START_H) * 60, elapsed = (np.hour - START_H) * 60 + np.minute + 10;
    const target = Math.min(limit, Math.ceil(limit * Math.min(elapsed, windowMin) / windowMin));
    const take = manual ? Math.min(10, limit - already) : Math.min(MAX_PER_TICK, target - already);

    const lk = await sql`update clicandsite.mail_runs set status='running', started_at=now() where run_date=${np.date}::date and (status<>'running' or started_at < now() - make_interval(secs => ${LOCK_SECONDS})) returning run_date`;
    if (!lk.length) return json({ ok: true, skipped: "passage déjà en cours" });

    let tok: string;
    try { tok = await getToken(); } catch (e) {
      const m = e instanceof Error ? e.message : String(e);
      const r = (await sql`update clicandsite.mail_runs set status='partial', token_failures=token_failures+1, details=${JSON.stringify({ error: m })}::jsonb where run_date=${np.date}::date returning token_failures`)[0];
      console.error("cs-prospecting token", m, r?.token_failures);
      return json({ ok: false, error: m }, 500);
    }
    await sql`update clicandsite.mail_runs set token_failures=0 where run_date=${np.date}::date`;
    await sql`update clicandsite.mail_recipients set status='échec', last_error='Envoi interrompu, nouvel essai automatique' where status='en cours' and sent_at is null`;

    let sent = 0, failed = 0;
    const list = take > 0 ? await pending(s.trades, take) : [];
    if (!manual && list.length) await new Promise((r) => setTimeout(r, Math.floor(Math.random() * 20000)));
    for (const p of list) {
      const t = template(p as any);
      await sql`insert into clicandsite.mail_recipients(prospect_id, email, status, attempts, template) values (${p.id}::uuid, ${p.email}, 'en cours', 1, ${t.key})
        on conflict (prospect_id) do update set status='en cours', attempts=clicandsite.mail_recipients.attempts+1, email=excluded.email, template=excluded.template`;
      try {
        const gid = await sendMime(tok, p.email, buildMime(p.email, t, await unsubUrl(p.id)));
        await sql`update clicandsite.mail_recipients set status='envoyé', sent_at=now(), gmail_id=${gid}, last_error=null where prospect_id=${p.id}::uuid`;
        await sql`update clicandsite.prospects set status='contacte', last_contact_at=now(), updated_at=now() where id=${p.id}::uuid and status in ('nouveau','a_contacter')`;
        await sql`insert into clicandsite.interactions(prospect_id, kind, content) values (${p.id}::uuid, 'mail', ${"Mail de prospection envoyé (" + t.key + ") : " + t.subject})`;
        await sql`update clicandsite.mail_runs set sent=sent+1 where run_date=${np.date}::date`;
        sent++;
      } catch (e) {
        const m = (e instanceof Error ? e.message : String(e)).slice(0, 500);
        await sql`update clicandsite.mail_recipients set status='échec', last_error=${m}, attempts=case when ${PERMANENT.test(m)} then ${MAX_ATTEMPTS} else attempts end where prospect_id=${p.id}::uuid`;
        await sql`update clicandsite.mail_runs set failed=failed+1 where run_date=${np.date}::date`;
        failed++;
      }
      if (list.length > 1) await new Promise((r) => setTimeout(r, manual ? 3000 : 8000 + Math.floor(Math.random() * 7000)));
    }
    const total = already + sent;
    const done = total >= limit || lastTick || (take > 0 && list.length < take);
    await sql`update clicandsite.mail_runs set status=${done ? "completed" : "partial"}, finished_at=now(), details=${JSON.stringify({ target, take, sent, failed })}::jsonb where run_date=${np.date}::date`;
    if (done) { try { await report(np.date, s.report_to, tok); } catch (e) { console.error("cs-prospecting report", String(e)); } }
    return json({ ok: true, sent, failed, sent_today: total, target });
  } catch (e) {
    console.error("cs-prospecting", e instanceof Error ? e.message : String(e));
    return json({ ok: false, error: e instanceof Error ? e.message : String(e) }, 500);
  }
});
