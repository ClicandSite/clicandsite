// 07/11/2026 (Claude, demande d'Anthony) — Site bilingue MyCreativeSite : traduction français → anglais des textes d'un site client.
// POST {site, texts[]} (espace client, connecté) -> {dict: {fr: en}}
// - Réservé au propriétaire du site (ou admin) et aux sites qui ont droit au bilingue (Premium, Boutique, option +10 €/mois).
// - Cache partagé (table clicandsite.tr_cache) : les textes des modèles ne sont traduits qu'une fois pour tous les sites.
// - Traducteur : DeepL si le secret DEEPL_KEY existe (clé gratuite « …:fx » acceptée) ; sinon renvoie {dict, missing}
//   et l'espace client traduit les textes manquants depuis le navigateur (Google Traduction).
import { createClient } from "https://esm.sh/@supabase/supabase-js@2.57.4";

const URL_ = Deno.env.get("SUPABASE_URL")!;
const db = createClient(URL_, Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!, { auth: { persistSession: false } });
const DEEPL = Deno.env.get("DEEPL_KEY") || "";
const cors = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const out = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...cors, "Content-Type": "application/json; charset=utf-8" } });
const fail = (m: string, s = 400) => out({ message: m }, s);

async function deepl(texts: string[]): Promise<string[]> {
  const host = DEEPL.endsWith(":fx") ? "https://api-free.deepl.com" : "https://api.deepl.com";
  const res: string[] = [];
  for (let i = 0; i < texts.length; i += 50) {
    const r = await fetch(host + "/v2/translate", { method: "POST", headers: { Authorization: "DeepL-Auth-Key " + DEEPL, "Content-Type": "application/json" },
      body: JSON.stringify({ text: texts.slice(i, i + 50), source_lang: "FR", target_lang: "EN-GB", preserve_formatting: true }) });
    if (!r.ok) throw new Error("DeepL " + r.status);
    const j = await r.json(); res.push(...j.translations.map((t: { text: string }) => t.text));
  }
  return res;
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  if (req.method !== "POST") return fail("Méthode non permise", 405);
  let b: Record<string, any> = {};
  try { b = await req.json(); } catch { return fail("Requête invalide"); }
  const site = String(b.site || "");
  const user = createClient(URL_, Deno.env.get("SUPABASE_ANON_KEY")!, { global: { headers: { Authorization: req.headers.get("authorization") || "" } }, auth: { persistSession: false } });
  const [{ data: can }, { data: adm }, { data: bi }] = await Promise.all([
    user.rpc("cs_can_edit_site", { p_id: site }), user.rpc("cs_is_admin"), user.rpc("cs_site_bilingual", { p_site: site })]);
  if (can !== true) return fail("Vous ne pouvez pas modifier ce site.", 403);
  if (bi !== true && adm !== true) return fail("La version anglaise est comprise dans les formules Premium et Boutique, ou en option à 10 € par mois.", 403);
  const texts = [...new Set((Array.isArray(b.texts) ? b.texts : []).map((t: unknown) => String(t ?? "").replace(/\s+/g, " ").trim()).filter((t: string) => /\p{L}/u.test(t) && t.length <= 2000))] as string[];
  if (texts.length > 2500 || texts.reduce((a, t) => a + t.length, 0) > 120000) return fail("Trop de textes à traduire d'un coup.");
  if (!texts.length) return out({ dict: {} });
  try {
    const dict: Record<string, string> = {};
    for (let i = 0; i < texts.length; i += 500) {
      const { data } = await db.rpc("cs_tr_cache_get", { p_src: texts.slice(i, i + 500) });
      Object.assign(dict, data || {});
    }
    const todo = texts.filter((t) => !(t in dict));
    if (todo.length) {
      // Sans clé DeepL : Google refuse les appels venant des serveurs, l'espace client traduit le reste depuis le navigateur.
      if (!DEEPL) return out({ dict, missing: todo });
      const tr = await deepl(todo);
      const fresh: Record<string, string> = {};
      todo.forEach((t, i) => { const v = (tr[i] || "").trim(); if (v) { dict[t] = v; fresh[t] = v; } });
      if (Object.keys(fresh).length) await db.rpc("cs_tr_cache_put", { p_rows: fresh });
    }
    return out({ dict });
  } catch (e) {
    return fail("Traduction automatique indisponible pour le moment (" + (e as Error).message + "). Réessayez dans quelques minutes.", 502);
  }
});
