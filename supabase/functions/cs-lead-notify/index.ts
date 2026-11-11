// MyCreativeSite — prévient le pro par mail à chaque nouvelle demande reçue sur son site (11/11/2026).
// Avant : les demandes (contact, rendez-vous, estimation, reprise…) n'arrivaient que dans « Mes clients », alors que le site annonce « par mail et dans Mes clients ».
// Envoi par la boîte OVH contact@mycreativesite.fr (même mot de passe que la prospection : clicandsite.secrets 'smtp_password').
// Destinataire : sites.owner_email. Réponse directe possible au client (Reply-To = e-mail du client s'il l'a laissé).
// Appel : cron chaque minute (POST, en-tête x-cs-key = secret mail_internal) ; GET ?health=1.
import postgres from "https://deno.land/x/postgresjs@v3.4.5/mod.js";

const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });
const SITE = "https://mycreativesite.fr";
const FROM = (Deno.env.get("CS_FROM") || "contact@mycreativesite.fr").trim();
const PER_TICK = 20, MAX_ATTEMPTS = 3;
const KIND: Record<string, string> = { contact: "Message", reservation: "Réservation", "rendez-vous": "Rendez-vous", devis: "Demande de devis", commande: "Commande", rappel: "Rappel demandé", estimation: "Demande d'estimation", reprise: "Demande de reprise" };

const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { "content-type": "application/json; charset=utf-8" } });
const esc = (s: unknown) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c] as string));
const enc = new TextEncoder();
const b64 = (s: string) => { const b = enc.encode(s); let o = ""; for (let i = 0; i < b.length; i += 0x8000) o += String.fromCharCode(...b.subarray(i, i + 0x8000)); return btoa(o); };
const b64Mime = (s: string) => (b64(s).match(/.{1,76}/g) || []).join("\r\n");
const encHeader = (s: string) => "=?UTF-8?B?" + b64(s.replace(/[\r\n]/g, " ")) + "?=";
const okMail = (s: unknown) => typeof s === "string" && /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(s);

async function smtpSend(pass: string, to: string, mime: string) {
  const host = Deno.env.get("SMTP_HOST") || "ssl0.ovh.net", port = Number(Deno.env.get("SMTP_PORT") || "465");
  const user = Deno.env.get("SMTP_USER") || FROM;
  const conn = await Deno.connectTls({ hostname: host, port });
  const dec = new TextDecoder(); let buf = "";
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
    await cmd(`MAIL FROM:<${FROM}>`, [250]); await cmd(`RCPT TO:<${to}>`, [250, 251]); await cmd("DATA", [354]);
    const body = mime.replace(/\r?\n/g, "\r\n").split("\r\n").map((l) => (l.startsWith(".") ? "." + l : l)).join("\r\n");
    await cmd(body + "\r\n.", [250]);
    try { await cmd("QUIT", [221]); } catch (_) { /* rien */ }
  } finally { try { conn.close(); } catch (_) { /* rien */ } }
}

function message(l: any) {
  const kind = KIND[l.kind] || "Demande";
  const rows: [string, string][] = [];
  if (l.name) rows.push(["Nom", l.name]);
  if (l.phone) rows.push(["Téléphone", l.phone]);
  if (l.email) rows.push(["E-mail", l.email]);
  for (const f of Array.isArray(l.fields) ? l.fields : []) if (f && f.v) rows.push([String(f.l || "Info"), String(f.v)]);
  if (l.message) rows.push(["Message", l.message]);
  if (l.page) rows.push(["Page", l.page]);
  const espace = `${SITE}/espace/?site=${encodeURIComponent(l.slug)}`;
  const subject = `${kind} sur votre site${l.name ? " · " + l.name : ""}`;
  const text = [`Nouvelle demande sur le site ${l.site_name || l.slug} : ${kind}.`, "", ...rows.map(([k, v]) => `${k} : ${v}`), "",
    l.email ? "Répondez simplement à ce mail pour écrire au client." : "Le client n'a pas laissé d'e-mail : rappelez-le.",
    `Retrouvez toutes vos demandes dans « Mes clients » : ${espace}`, "", "MyCreativeSite"].join("\n");
  const tel = l.phone ? String(l.phone).replace(/[^0-9+]/g, "") : "";
  const htmlBody = `<div style="font-family:Arial,sans-serif;color:#12162B;max-width:560px;margin:0 auto;padding:20px">
<p style="margin:0 0 6px;font-size:13px;color:#7C3AED;font-weight:bold;text-transform:uppercase;letter-spacing:.06em">${esc(kind)}</p>
<h1 style="margin:0 0 16px;font-size:20px">Nouvelle demande sur ${esc(l.site_name || l.slug)}</h1>
<table style="border-collapse:collapse;width:100%;font-size:15px">${rows.map(([k, v]) => `<tr><td style="padding:7px 10px 7px 0;color:#5C627A;vertical-align:top;white-space:nowrap">${esc(k)}</td><td style="padding:7px 0;border-bottom:1px solid #E1E4EE">${esc(v).replace(/\n/g, "<br>")}</td></tr>`).join("")}</table>
<p style="margin:20px 0 0">${tel ? `<a href="tel:${esc(tel)}" style="display:inline-block;background:#12162B;color:#fff;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:bold;margin:0 8px 8px 0">Appeler</a>` : ""}<a href="${esc(espace)}" style="display:inline-block;background:#7C3AED;color:#fff;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:bold;margin:0 0 8px">Ouvrir Mes clients</a></p>
<p style="margin:14px 0 0;font-size:13px;color:#5C627A">${l.email ? "Répondez simplement à ce mail pour écrire au client." : "Le client n'a pas laissé d'e-mail : rappelez-le."}</p>
<p style="margin:18px 0 0;font-size:12px;color:#9AA1BC">MyCreativeSite · vous recevez ce mail car une demande a été envoyée depuis votre site.</p></div>`;
  const bd = "cs" + crypto.randomUUID().replace(/-/g, "");
  const headers = [`From: ${encHeader("MyCreativeSite")} <${FROM}>`, `To: <${l.owner_email}>`, `Subject: ${encHeader(subject)}`,
    ...(okMail(l.email) ? [`Reply-To: <${l.email}>`] : []), `Date: ${new Date().toUTCString()}`, `Message-ID: <${crypto.randomUUID()}@mycreativesite.fr>`,
    "MIME-Version: 1.0", `Content-Type: multipart/alternative; boundary="${bd}"`];
  return [...headers, "", `--${bd}`, "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(text),
    `--${bd}`, "Content-Type: text/html; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(htmlBody), `--${bd}--`, ""].join("\r\n");
}

Deno.serve(async (req) => {
  const url = new URL(req.url);
  if (req.method === "GET" && url.searchParams.get("health")) {
    const r = (await sql`select count(*) filter (where notified_at is null and notify_attempts < ${MAX_ATTEMPTS} and created_at > now() - interval '2 days')::int waiting,
      count(*) filter (where notified_at > now() - interval '1 day')::int sent_24h from clicandsite.leads`)[0];
    return json({ ok: true, ...r });
  }
  const key = (await sql`select value from clicandsite.secrets where name='mail_internal'`)[0]?.value;
  if (!key || req.headers.get("x-cs-key") !== key) return json({ error: "forbidden" }, 403);
  const pass = Deno.env.get("SMTP_PASSWORD") || (await sql`select value from clicandsite.secrets where name='smtp_password'`)[0]?.value || "";
  if (!pass) return json({ error: "mot de passe SMTP absent" }, 503);
  // On réserve les lignes (notify_attempts + 1) pour ne jamais envoyer deux fois le même mail si deux passages se croisent
  const rows = await sql`update clicandsite.leads l set notify_attempts = l.notify_attempts + 1, notify_try_at = now()
    from clicandsite.sites s
    where l.id in (select l2.id from clicandsite.leads l2 join clicandsite.sites s2 on s2.id = l2.site_id
                   where l2.notified_at is null and l2.notify_attempts < ${MAX_ATTEMPTS} and l2.created_at > now() - interval '2 days'
                     and s2.owner_email is not null and (l2.notify_try_at is null or l2.notify_try_at < now() - interval '5 minutes')
                   order by l2.created_at limit ${PER_TICK} for update of l2 skip locked)
      and s.id = l.site_id
    returning l.id, l.kind, l.name, l.phone, l.email, l.message, l.fields, l.page, s.slug, s.name site_name, lower(trim(s.owner_email)) owner_email`;
  let sent = 0; const errors: string[] = [];
  for (const l of rows) {
    if (!okMail(l.owner_email)) { await sql`update clicandsite.leads set notify_attempts = ${MAX_ATTEMPTS}, notify_error = 'adresse du pro invalide' where id = ${l.id}`; continue; }
    try { await smtpSend(pass, l.owner_email, message(l)); await sql`update clicandsite.leads set notified_at = now(), notify_error = null where id = ${l.id}`; sent++; }
    catch (e) { const m = (e instanceof Error ? e.message : String(e)).slice(0, 300); errors.push(m); await sql`update clicandsite.leads set notify_error = ${m} where id = ${l.id}`; }
  }
  return json({ ok: true, picked: rows.length, sent, errors });
});
