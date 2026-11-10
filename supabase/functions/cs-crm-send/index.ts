// cs-crm-send (10/11/2026, demande d'Anthony) : écrire / répondre depuis le CRM MyCreativeSite avec la boîte OVH
// (contact@mycreativesite.fr, ou la 2e boîte si elle est réglée), jamais depuis Gmail. Copie rangée dans « Envoyés » (IMAP).
// GET → boîtes disponibles ; POST {box, to, subject, text, prospect_id?} — réservé à l'admin connecté (cs_is_admin).
import postgres from "https://deno.land/x/postgresjs@v3.4.5/mod.js";
const sql = postgres(Deno.env.get("SUPABASE_DB_URL")!, { prepare: false, max: 1 });
const SB = Deno.env.get("SUPABASE_URL")!, ANON = Deno.env.get("SUPABASE_ANON_KEY")!;
const HOST = Deno.env.get("SMTP_HOST") || "ssl0.ovh.net", PORT = Number(Deno.env.get("SMTP_PORT") || "465");
const CORS = { "access-control-allow-origin": "*", "access-control-allow-headers": "authorization, apikey, content-type, x-client-info", "access-control-allow-methods": "GET, POST, OPTIONS" };
const json = (d: unknown, s = 200) => new Response(JSON.stringify(d), { status: s, headers: { ...CORS, "content-type": "application/json; charset=utf-8" } });
const enc = new TextEncoder(), dec = new TextDecoder();
const b64 = (s: string) => { const b = enc.encode(s); let x = ""; for (let i = 0; i < b.length; i += 0x8000) x += String.fromCharCode(...b.subarray(i, i + 0x8000)); return btoa(x); };
const b64Mime = (s: string) => (b64(s).match(/.{1,76}/g) || []).join("\r\n");
const encHeader = (s: string) => "=?UTF-8?B?" + b64(s.replace(/[\r\n]/g, " ")) + "?=";
type Box = { n: number; email: string; user: string; pass: string };

async function boxes(): Promise<Box[]> {
  const from = (Deno.env.get("CS_FROM") || "contact@mycreativesite.fr").trim();
  const p1 = Deno.env.get("SMTP_PASSWORD") || (await sql`select value from clicandsite.secrets where name='smtp_password'`)[0]?.value || "";
  const out: Box[] = [];
  if (p1) out.push({ n: 1, email: from, user: Deno.env.get("SMTP_USER") || from, pass: p1 });
  const b = (await sql`select s.box2_email, (select value from clicandsite.secrets where name='smtp_password_2') pw from clicandsite.mail_settings s where id=1`)[0];
  if (b?.box2_email && b?.pw) out.push({ n: 2, email: String(b.box2_email).trim(), user: String(b.box2_email).trim(), pass: b.pw });
  return out;
}
async function isAdmin(req: Request) {
  const auth = req.headers.get("authorization") || "";
  if (!/^Bearer /.test(auth)) return false;
  const r = await fetch(SB + "/rest/v1/rpc/cs_is_admin", { method: "POST", headers: { authorization: auth, apikey: ANON, "content-type": "application/json" }, body: "{}" });
  return r.ok && (await r.json().catch(() => false)) === true;
}
async function smtpSend(box: Box, to: string, mime: string) {
  const conn = await Deno.connectTls({ hostname: HOST, port: PORT });
  let buf = "";
  const read = async (): Promise<string> => { const ch = new Uint8Array(4096); for (;;) { const l = buf.split("\r\n"); for (let i = 0; i < l.length - 1; i++) if (/^\d{3} /.test(l[i])) { const o = l.slice(0, i + 1).join("\n"); buf = l.slice(i + 1).join("\r\n"); return o; } const n = await conn.read(ch); if (n === null) throw new Error("SMTP : connexion fermée"); buf += dec.decode(ch.subarray(0, n)); } };
  const cmd = async (c: string | null, ok: number[]) => { if (c !== null) await conn.write(enc.encode(c + "\r\n")); const r = await read(); const code = Number(r.slice(-200).match(/(\d{3}) [^\n]*$/)?.[1] || r.slice(0, 3)); if (!ok.includes(code)) throw new Error("SMTP " + code + " : " + r.slice(0, 200)); return r; };
  try {
    await cmd(null, [220]); await cmd("EHLO mycreativesite.fr", [250]);
    await cmd("AUTH LOGIN", [334]); await cmd(btoa(box.user), [334]); await cmd(btoa(box.pass), [235]);
    await cmd(`MAIL FROM:<${box.email}>`, [250]); await cmd(`RCPT TO:<${to}>`, [250, 251]); await cmd("DATA", [354]);
    await cmd(mime.split("\r\n").map((l) => (l.startsWith(".") ? "." + l : l)).join("\r\n") + "\r\n.", [250]);
    try { await cmd("QUIT", [221]); } catch (_) { /* ignore */ }
  } finally { try { conn.close(); } catch (_) { /* ignore */ } }
}
async function appendSent(box: Box, mime: string): Promise<string | null> {
  for (const host of ["ssl0.ovh.net", "imap.mail.ovh.net"]) {
    let conn: Deno.TlsConn; try { conn = await Deno.connectTls({ hostname: host, port: 993 }); } catch { continue; }
    let txt = "", n = 0;
    const until = async (re: RegExp) => { while (!re.test(txt)) { const ch = new Uint8Array(16384); const k = await conn.read(ch); if (k === null) throw new Error("IMAP fermé"); txt += dec.decode(ch.subarray(0, k)); } const m = re.exec(txt)!; const o = txt.slice(0, m.index + m[0].length); txt = txt.slice(m.index + m[0].length); return o; };
    const w = async (d: Uint8Array | string) => { const b = typeof d === "string" ? enc.encode(d) : d; let o = 0; while (o < b.length) o += await conn.write(b.subarray(o)); };
    const tagRe = (t: string) => new RegExp(`(^|\\r\\n)${t} (OK|NO|BAD)[^\\r\\n]*\\r\\n`);
    const cmd = async (line: string) => { const t = "c" + (++n); await w(`${t} ${line}\r\n`); const r = await until(tagRe(t)); if (!new RegExp(`${t} OK`).test(r)) throw new Error(r.slice(-160)); return r; };
    try {
      await until(/\r\n/);
      const q = (s: string) => `"${s.replace(/["\\]/g, "\\$&")}"`;
      await cmd(`LOGIN ${q(box.user)} ${q(box.pass)}`);
      const list = await cmd(`LIST "" "*"`);
      const folder = /\(([^)]*\\Sent[^)]*)\) "[^"]*" ("[^"]+"|\S+)/i.exec(list)?.[2] || /\) "[^"]*" ("?(?:Sent|Envoy[^"\r\n]*|Sent Items|Sent Messages)"?)\r\n/i.exec(list)?.[1] || '"Sent"';
      const bytes = enc.encode(mime.endsWith("\r\n") ? mime : mime + "\r\n");
      const t = "c" + (++n);
      await w(`${t} APPEND ${folder} (\\Seen) {${bytes.length}}\r\n`); await until(/\r\n/);
      await w(bytes); await w("\r\n");
      const r = await until(tagRe(t));
      await cmd("LOGOUT").catch(() => {});
      return new RegExp(`${t} OK`).test(r) ? null : r.slice(-160);
    } catch (e) { return String((e as Error).message || e).slice(0, 160); }
    finally { try { conn.close(); } catch { /* fermé */ } }
  }
  return "IMAP injoignable";
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { headers: CORS });
  try {
    if (!(await isAdmin(req))) return json({ error: "Accès réservé à l'administrateur" }, 401);
    const list = await boxes();
    if (req.method === "GET") return json({ boxes: list.map((b) => ({ n: b.n, email: b.email })) });
    const b = await req.json().catch(() => ({}));
    const box = list.find((x) => x.n === Number(b.box)) || list[0];
    if (!box) return json({ ok: false, error: "Aucune boîte d'envoi réglée (mot de passe manquant)." });
    const to = String(b.to || "").trim().toLowerCase(), subject = String(b.subject || "").replace(/[\r\n]/g, " ").trim().slice(0, 200), text = String(b.text || "").trim().slice(0, 20000);
    if (!/^[^@\s<>]+@[^@\s<>]+\.[a-z]{2,}$/i.test(to)) return json({ ok: false, error: "Adresse du destinataire invalide" });
    if (!subject || !text) return json({ ok: false, error: "Objet et message obligatoires" });
    const mime = [`Date: ${new Date().toUTCString().replace("GMT", "+0000")}`, `Message-ID: <${crypto.randomUUID()}@${box.email.split("@")[1]}>`,
      `From: MyCreativeSite <${box.email}>`, `Reply-To: ${box.email}`, `To: ${to}`, `Subject: ${encHeader(subject)}`,
      "MIME-Version: 1.0", "Content-Type: text/plain; charset=UTF-8", "Content-Transfer-Encoding: base64", "", b64Mime(text), ""].join("\r\n");
    await smtpSend(box, to, mime);
    const sent = await appendSent(box, mime);
    const pid = typeof b.prospect_id === "string" && /^[0-9a-f-]{36}$/.test(b.prospect_id) ? b.prospect_id : null;
    if (pid) await sql`insert into clicandsite.interactions(prospect_id, kind, content) values (${pid}::uuid, 'mail', ${"Mail envoyé depuis " + box.email + " : " + subject})`;
    return json({ ok: true, message: `Mail envoyé à ${to} depuis ${box.email}.` + (sent ? ` (Copie non rangée dans « Envoyés » : ${sent})` : " Copie rangée dans « Envoyés ».") });
  } catch (e) { return json({ ok: false, error: e instanceof Error ? e.message : String(e) }); }
});
