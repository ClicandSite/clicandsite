/* MyCreativeSite · statistiques de visites des sites clients — 13/11/2026 (Anthony : « rajoute ça dans les sites »).
   Chargé par cs-edit.js sur un site client (data-site="identifiant"). 1 visite par visiteur, page et jour,
   identifiant anonyme gardé dans le navigateur, aucune donnée personnelle, aucun cookie publicitaire.
   Le pro n'est pas compté :
   - lien secret : toucher le nom de l'entreprise dans le pied de page (« © 2026 … ») active / désactive ;
   - adresses : votre-site.fr/#nostats (ne plus compter cet appareil), votre-site.fr/#stats (recompter) ;
   - l'espace client propose aussi le bouton « Ne plus compter ce téléphone » (ouvre le site avec #nostats).
   Résultats : espace client, onglet « Statistiques ». */
(function () {
  'use strict';
  var me = document.currentScript, slug = me && me.getAttribute('data-site');
  if (!slug) return;
  var API = 'https://avcynjwcyygygkjuxsdt.supabase.co', KEY = 'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO';
  var NC = 'cs_not_counted';
  var en = function () { return (document.documentElement.lang || '').slice(0, 2) === 'en'; };
  var toast = function (msg) {
    try {
      var t = document.createElement('div'); t.textContent = msg; t.setAttribute('role', 'status');
      t.style.cssText = 'position:fixed;left:50%;bottom:calc(24px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:2147483647;background:#12162B;color:#fff;padding:12px 18px;border-radius:12px;font:600 15px/1.35 system-ui,-apple-system,sans-serif;box-shadow:0 12px 30px -12px rgba(0,0,0,.5);max-width:calc(100% - 32px);text-align:center';
      (document.body || document.documentElement).appendChild(t); setTimeout(function () { t.remove(); }, 3500);
    } catch (_) {}
  };
  var excluded = function () { try { return localStorage.getItem(NC) === '1'; } catch (_) { return false; } };
  var setMe = function (ex) {
    try { if (ex) localStorage.setItem(NC, '1'); else localStorage.removeItem(NC); } catch (_) {}
    toast(ex ? (en() ? '✓ This device is no longer counted in the statistics' : '✓ Cet appareil n\'est plus compté dans les statistiques')
             : (en() ? 'This device is counted again' : 'Cet appareil est de nouveau compté'));
  };
  window.csStatsToggle = function () { setMe(!excluded()); };
  var fromHash = function () {
    var h = (location.hash || '').toLowerCase();
    if (h !== '#nostats' && h !== '#stats') return false;
    setMe(h === '#nostats');
    try { history.replaceState(null, '', location.pathname + location.search); } catch (_) {}
    return true;
  };
  window.addEventListener('hashchange', fromHash);
  // Lien secret : le nom de l'entreprise dans le pied de page, sans changer son apparence
  var secret = function () {
    var s = document.querySelector('footer .wrap > span:first-child'); if (!s || s.__cs) return; s.__cs = 1;
    s.addEventListener('click', function () { window.csStatsToggle(); });
  };
  var ready = function () { fromHash(); secret(); };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();

  try {
    if (excluded() || /^#nostats$/i.test(location.hash)) return;
    if (navigator.webdriver || /bot|crawl|spider|slurp|headless|lighthouse|pagespeed|preview|facebookexternalhit|phantomjs|puppeteer|playwright|selenium|inspectiontool|googleother|google-read-aloud|bingpreview|petalsearch|yandex/i.test(navigator.userAgent || '')) return;
    if (window.self !== window.top) return; // site affiché dans l'espace client
    if (/(^|\.)mycreativesite\.fr$/.test(location.hostname) && /^\/(espace|modeles|apercu)\//.test(location.pathname)) return;
    var path = location.pathname.replace(/index\.html$/, '') || '/';
    var day = new Date().toISOString().slice(0, 10), k = 'cs_sv_' + slug + '_' + day + '_' + path;
    if (localStorage.getItem(k)) return;
    var v = localStorage.getItem('cs_vid');
    // identifiant anonyme renouvelé au bout de 13 mois (recommandation CNIL pour la mesure d'audience)
    var vt = +localStorage.getItem('cs_vid_t') || 0; if (v && (!vt || Date.now() - vt > 395 * 864e5)) { if (vt) v = null; else localStorage.setItem('cs_vid_t', String(Date.now())); }
    if (!v) { v = (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2)); localStorage.setItem('cs_vid', v); localStorage.setItem('cs_vid_t', String(Date.now())); }
    var host = '', src = 'direct', self = location.hostname.replace(/^www\./, '');
    try { host = document.referrer ? new URL(document.referrer).hostname.replace(/^www\./, '').toLowerCase() : ''; } catch (_) {}
    var q = new URLSearchParams(location.search), utm = (q.get('utm_source') || '') + ' ' + (q.get('utm_medium') || '');
    if (host === self) { src = 'interne'; host = ''; }
    else if (/mail/i.test(utm)) src = 'email';
    else if (/facebook|fb/i.test(utm)) src = 'facebook';
    else if (/instagram|ig/i.test(utm)) src = 'instagram';
    else if (!host) src = 'direct';
    else if (/(^|\.)google\./.test(host)) src = 'google';
    else if (/chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google|copilot\.microsoft|mistral\.ai/.test(host)) src = 'ia';
    else if (/bing\.|duckduckgo|qwant|ecosia|yahoo|brave\.com|startpage|lilo/.test(host)) src = 'bing';
    else if (/facebook|(^|\.)fb\.|messenger/.test(host)) src = 'facebook';
    else if (/instagram/.test(host)) src = 'instagram';
    else if (/mail\.|outlook\.|webmail|zimbra/.test(host)) src = 'email';
    else src = 'autre_site';
    var mobile = matchMedia('(max-width:760px),(pointer:coarse)').matches;
    fetch(API + '/rest/v1/rpc/cs_site_track', {
      method: 'POST', keepalive: true, headers: { 'Content-Type': 'application/json', apikey: KEY },
      body: JSON.stringify({ p_slug: slug, p_visitor: v, p_path: path, p_source: src, p_mobile: mobile, p_ref_host: host || null })
    }).then(function (r) { if (r.ok) localStorage.setItem(k, '1'); }).catch(function () {});
  } catch (_) {}
})();
