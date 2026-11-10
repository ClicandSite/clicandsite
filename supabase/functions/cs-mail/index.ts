// MyCreativeSite — « Message à tous » envoyé depuis l'espace pro, par la boîte mail du pro (10/11/2026, demande d'Anthony).
// Le pro connecte sa boîte dans son espace (adresse, serveur, mot de passe : table clicandsite.site_mail, jamais renvoyé au navigateur).
// POST (jeton de connexion de l'espace) :
//   {action:"test", site}                     -> connexion à la boîte + mail d'essai au pro lui-même
//   {action:"start", site, subject, body, archived} -> prépare l'envoi (destinataires calculés ici : clients avec e-mail, d'accord pour recevoir)
//   {action:"continue", campaign}             -> envoie la suite (40 par appel), l'espace rappelle jusqu'à la fin
// GET ?u=<site>&e=<email>&k=<signature>      -> désinscription en un clic (le client ne reçoit plus les messages de ce pro)
import postgres from "https://deno.land/x/postgresjs@v3.4.5/mod.js";

const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });
const API = Deno.env.get("SUPABASE_URL") || "https://avcynjwcyygygkjuxsdt.supabase.co";
const ANON = Deno.env.get("SUPABASE_ANON_KEY") || "sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO";
const FN = "https://avcynjwcyygygkjuxsdt.supabase.co/functions/v1/cs-mail";
const PER_CALL = 40, PER_DAY = 300;
const CORS = { "access-control-allow-origin": "*", "access-control-allow-headers": "authorization, apikey, content-type, x-client-info", "access-control-allow-methods": "POST, GET, OPTIONS" };
const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { ...CORS, "content-type": "application/json; charset=utf-8" } });
const html = (b: string) => new Response(b, { headers: { "content-type": "text/html; charset=utf-8" } });
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));
const enc = new TextEncoder();
const b64 = (s: string) => { const b = enc.encode(s); let o = ""; for (let i = 0; i < b.length; i += 0x8000) o += String.fromCharCode(...b.subarray(i, i + 0x8000)); return btoa(o); };
const b64Mime = (s: string) => b64(s).replace(/.{1,76}/g, (l) => l + "\r\n").trim();
const encHeader = (s: string) => "=?UTF-8?B?" + b64(s.replace(/[\r\n]/g, " ")) + "?=";

async function hmac(msg: string) {
  const key = (await sql`select value from clicandsite.secrets where name='mail_unsub_key'`)[0]?.value || "x";
  const k = await crypto.subtle.importKey("raw", enc.encode(key), { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", k, enc.encode(msg)));
  return [...sig.slice(0, 16)].map((x) => x.toString(16).padStart(2, "0")).join("");
}

// ---------- SMTP : 465 (TLS direct) ou 587 (STARTTLS), une connexion pour plusieurs mails ----------
type Box = { email: string; host: string; port: number; username: string; password: string };
class Smtp {
  conn!: Deno.Conn; buf = ""; dec = new TextDecoder();
  constructor(public box: Box) {}
  async read(): Promise<string> {
    const chunk = new Uint8Array(4096);
    for (;;) {
      const lines = this.buf.split("\r\n");
      for (let i = 0; i < lines.length - 1; i++) if (/^\d{3} /.test(lines[i])) { const out = lines.slice(0, i + 1).join("\n"); this.buf = lines.slice(i + 1).join("\r\n"); return out; }
      const n = await this.conn.read(chunk); if (n === null) throw new Error("connexion fermée par le serveur");
      this.buf += this.dec.decode(chunk.subarray(0, n));
    }
  }
  async cmd(c: string | null, ok: number[]) {
    if (c !== null) await this.conn.write(enc.encode(c + "\r\n"));
    const r = await this.read(); const code = Number(r.slice(-300).match(/(\d{3}) [^\n]*$/)?.[1] || r.slice(0, 3));
    if (!ok.includes(code)) { const e = new Error(code + " " + r.slice(0, 220)); (e as any).code = code; throw e; }
    return r;
  }
  async open() {
    const { host, port } = this.box;
    if (port === 465) this.conn = await Deno.connectTls({ hostname: host, port });
    else {
      this.conn = await Deno.connect({ hostname: host, port });
      await this.cmd(null, [220]); await this.cmd("EHLO mycreativesite.fr", [250]); await this.cmd("STARTTLS", [220]);
      this.conn = await Deno.startTls(this.conn as Deno.TcpConn, { hostname: host }); this.buf = "";
      await this.cmd("EHLO mycreativesite.fr", [250]);
    }
    if (port === 465) { await this.cmd(null, [220]); await this.cmd("EHLO mycreativesite.fr", [250]); }
    await this.cmd("AUTH LOGIN", [334]); await this.cmd(btoa(this.box.username), [334]); await this.cmd(btoa(this.box.password), [235]);
  }
  async send(to: string, mime: string) {
    await this.cmd(`MAIL FROM:<${this.box.email}>`, [250]); await this.cmd(`RCPT TO:<${to}>`, [250, 251]); await this.cmd("DATA", [354]);
    const body = mime.replace(/\r?\n/g, "\r\n").split("\r\n").map((l) => (l.startsWith(".") ? "." + l : l)).join("\r\n");
    await this.cmd(body + "\r\n.", [250]);
  }
  async reset() { try { await this.cmd("RSET", [250]); } catch (_) { /* ignore */ } }
  async close() { try { await this.cmd("QUIT", [221]); } catch (_) { /* ignore */ } try { this.conn.close(); } catch (_) { /* ignore */ } }
}
const friendly = (e: unknown) => {
  const m = e instanceof Error ? e.message : String(e);
  if (/^535|^534|authentication|AUTH|Username and Password/i.test(m)) return "Identifiant ou mot de passe refusé par votre messagerie. Pour Gmail, Yahoo ou iCloud, il faut un « mot de passe d'application ».";
  if (/dns|lookup|resolve|refused|timed out|Connection/i.test(m)) return "Impossible de joindre le serveur d'envoi (" + m.slice(0, 80) + "). Vérifiez le serveur et le port.";
  return m.slice(0, 200);
};

function mime(box: Box, siteName: string, to: string, name: string | null, subject: string, body: string, unsub: string) {
  const q = "csb" + crypto.randomUUID().replace(/-/g, "");
  const hello = body.replace(/^Bonjour\s*,/i, "Bonjour" + (name ? " " + name.split(/\s+/)[0] : "") + ",");
  const text = hello.trim() + "\n\n" + siteName + "\n\n—\nVous recevez ce message car vous êtes client de " + siteName + ". Pour ne plus le recevoir : " + unsub;
  const htmlBody = '<div style="font:15px/1.6 -apple-system,Segoe UI,Arial,sans-serif;color:#1f2937;max-width:600px">' +
    esc(hello.trim()).replace(/\n/g, "<br>") + "<br><br><b>" + esc(siteName) + "</b>" +
    '<p style="margin-top:28px;font-size:12px;color:#6b7280">Vous recevez ce message car vous êtes client de ' + esc(siteName) + '. <a href="' + esc(unsub) + '" style="color:#6b7280">Ne plus recevoir ces messages</a></p></div>';
  return [
    `Date: ${new Date().toUTCString()}`, `Message-ID: <${crypto.randomUUID()}@${box.email.split("@")[1]}>`,
    `From: ${encHeader(siteName)} <${box.email}>`, `Reply-To: ${box.email}`, `To: ${to}`, `Subject: ${encHeader(subject)}`,
    `List-Unsubscribe: <${unsub}>, <mailto:${box.email}?subject=STOP>`, "List-Unsubscribe-Post: List-Unsubscribe=One-Click",
    "MIME-Version: 1.0", `Content-Type: multipart/alternative; boundary="${q}"`, "",
    "--" + q, "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(text),
    "--" + q, "Content-Type: text/html; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(htmlBody),
    "--" + q + "--", "",
  ].join("\r\n");
}

async function user(req: Request) {
  const auth = req.headers.get("authorization") || "";
  if (!/^Bearer /.test(auth)) return null;
  const r = await fetch(API + "/auth/v1/user", { headers: { authorization: auth, apikey: ANON } });
  if (!r.ok) return null; const u = await r.json(); return u?.id ? u : null;
}
async function canEdit(uid: string, site: string) {
  return await sql.begin(async (t) => {
    await t`select set_config('request.jwt.claims', ${JSON.stringify({ sub: uid, role: "authenticated" })}, true), set_config('request.jwt.claim.sub', ${uid}, true)`;
    const r = await t`select public.cs_can_edit_site(${site}::uuid) ok`; return r[0]?.ok === true;
  });
}
async function siteName(site: string) {
  const s = (await sql`select name, content from clicandsite.sites where id=${site}`)[0];
  return String(s?.content?.text?.logo || s?.name || "").trim() || "Votre professionnel";
}
async function boxOf(site: string): Promise<Box | null> {
  const b = (await sql`select email, host, port, username, password from clicandsite.site_mail where site_id=${site}`)[0];
  return b?.password ? { email: b.email, host: b.host, port: Number(b.port), username: b.username, password: b.password } : null;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
  const url = new URL(req.url);
  try {
    if (req.method === "GET" || (req.method === "POST" && url.searchParams.get("u"))) {
      const site = url.searchParams.get("u") || "", e = (url.searchParams.get("e") || "").toLowerCase(), k = url.searchParams.get("k") || "";
      if (!site || !e || k !== (await hmac(site + ":" + e))) return html("<p>Lien invalide.</p>");
      await sql`update clicandsite.leads set optout = true, updated_at = now() where site_id = ${site} and lower(email) = ${e}`;
      const n = await siteName(site);
      return html(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Désinscription</title><div style="font:16px/1.6 system-ui,sans-serif;max-width:520px;margin:12vh auto;padding:0 20px;text-align:center"><h1 style="font-size:1.4rem">C'est noté.</h1><p>Vous ne recevrez plus les messages de <b>${esc(n)}</b>.</p></div>`);
    }
    if (req.method !== "POST") return json({ error: "Méthode" }, 405);
    const u = await user(req); if (!u) return json({ error: "Connectez-vous à votre espace." }, 401);
    const b = await req.json().catch(() => ({}));

    if (b.action === "continue") {
      const c = (await sql`select * from clicandsite.mail_campaigns where id=${b.campaign}`)[0];
      if (!c || !(await canEdit(u.id, c.site_id))) return json({ error: "Accès refusé" }, 403);
      return json(await run(c));
    }
    const site = String(b.site || "");
    if (!site || !(await canEdit(u.id, site))) return json({ error: "Accès refusé" }, 403);
    const box = await boxOf(site); if (!box) return json({ error: "Connectez d'abord votre boîte mail." }, 400);

    if (b.action === "test") {
      const s = new Smtp(box);
      try {
        await s.open();
        await s.send(box.email, mime(box, await siteName(site), box.email, null, "Mail d'essai : votre boîte est bien connectée", "Bonjour,\n\nC'est un mail d'essai envoyé depuis votre espace MyCreativeSite. Votre boîte mail est bien connectée : vos messages à vos clients partiront d'ici.", FN));
        await sql`update clicandsite.site_mail set verified_at = now(), last_error = null where site_id = ${site}`;
        return json({ ok: true });
      } catch (e) {
        await sql`update clicandsite.site_mail set verified_at = null, last_error = ${friendly(e)} where site_id = ${site}`;
        return json({ ok: false, error: friendly(e) });
      } finally { await s.close(); }
    }

    if (b.action === "start") {
      const subject = String(b.subject || "").trim().slice(0, 150), body = String(b.body || "").trim().slice(0, 8000);
      if (!subject || body.length < 10) return json({ error: "Écrivez un objet et un message." }, 400);
      const v = (await sql`select verified_at from clicandsite.site_mail where site_id=${site}`)[0];
      if (!v?.verified_at) return json({ error: "Faites d'abord un mail d'essai pour vérifier votre boîte." }, 400);
      const used = Number((await sql`select count(*) n from clicandsite.mail_campaign_to x join clicandsite.mail_campaigns c on c.id=x.campaign_id where c.site_id=${site} and x.sent_at > now() - interval '24 hours'`)[0].n);
      const to = await sql`select distinct on (lower(l.email)) lower(l.email) email, l.name from clicandsite.leads l
        where l.site_id = ${site} and l.email is not null and not l.optout and (${!!b.archived} or l.status <> 'archive')
          and not exists (select 1 from clicandsite.leads o where o.site_id = l.site_id and lower(o.email) = lower(l.email) and o.optout)
        order by lower(l.email), l.created_at desc`;
      if (!to.length) return json({ error: "Aucun client avec une adresse e-mail à prévenir." }, 400);
      if (used + to.length > PER_DAY) return json({ error: `Limite de ${PER_DAY} mails par jour (déjà ${used} envoyés). Réessayez demain, ou envoyez depuis votre messagerie.` }, 400);
      const c = (await sql`insert into clicandsite.mail_campaigns (site_id, created_by, subject, body, total) values (${site}, ${u.email}, ${subject}, ${body}, ${to.length}) returning *`)[0];
      await sql`insert into clicandsite.mail_campaign_to ${sql(to.map((r) => ({ campaign_id: c.id, email: r.email, name: r.name })))}`;
      return json(await run(c));
    }
    return json({ error: "Action inconnue" }, 400);
  } catch (e) { return json({ error: e instanceof Error ? e.message : String(e) }, 500); }
});

async function run(c: any) {
  const box = await boxOf(c.site_id); if (!box) return { error: "Boîte mail non connectée" };
  const list = await sql`select email, name from clicandsite.mail_campaign_to where campaign_id=${c.id} and sent_at is null and error is null limit ${PER_CALL}`;
  const name = await siteName(c.site_id);
  if (list.length) {
    const s = new Smtp(box);
    try { await s.open(); } catch (e) { await s.close(); return { error: friendly(e), id: c.id, total: c.total, sent: c.sent, failed: c.failed }; }
    try {
      for (const r of list) {
        const unsub = FN + "?u=" + c.site_id + "&e=" + encodeURIComponent(r.email) + "&k=" + (await hmac(c.site_id + ":" + r.email));
        try { await s.send(r.email, mime(box, name, r.email, r.name, c.subject, c.body, unsub)); await sql`update clicandsite.mail_campaign_to set sent_at=now() where campaign_id=${c.id} and email=${r.email}`; }
        catch (e) { await sql`update clicandsite.mail_campaign_to set error=${friendly(e)} where campaign_id=${c.id} and email=${r.email}`; await s.reset(); if (/connexion fermée/.test(String(e))) break; }
        await new Promise((ok) => setTimeout(ok, 350));
      }
    } finally { await s.close(); }
  }
  const st = (await sql`select count(*) filter (where sent_at is not null) sent, count(*) filter (where error is not null) failed, count(*) filter (where sent_at is null and error is null) rest from clicandsite.mail_campaign_to where campaign_id=${c.id}`)[0];
  const done = Number(st.rest) === 0;
  await sql`update clicandsite.mail_campaigns set sent=${Number(st.sent)}, failed=${Number(st.failed)}, done_at=${done ? new Date() : null} where id=${c.id}`;
  return { id: c.id, total: c.total, sent: Number(st.sent), failed: Number(st.failed), done };
}
