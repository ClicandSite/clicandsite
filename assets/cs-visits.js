/* 12/11/2026 (Claude, Anthony : « mets un compteur aussi sur MyCreativeSite ») — compteur de visiteurs.
   1 visite par visiteur, page et jour (identifiant anonyme dans le navigateur, aucune donnée personnelle).
   Pas comptés : robots et navigateurs automatisés, l'appareil d'Anthony (marqué en ouvrant l'admin,
   ou avec mycreativesite.fr/?moi=1 ; ?moi=0 pour annuler). Résultats : admin, bloc « Visiteurs du site ». */
(function () {
  'use strict';
  try {
    var q = new URLSearchParams(location.search);
    if (q.get('moi') === '1') localStorage.setItem('cs_not_counted', '1');
    else if (q.get('moi') === '0') localStorage.removeItem('cs_not_counted');
    if (localStorage.getItem('cs_not_counted') === '1') return;
    if (navigator.webdriver || /bot|crawl|spider|slurp|headless|lighthouse|pagespeed|preview|facebookexternalhit|phantomjs|puppeteer|playwright|selenium/i.test(navigator.userAgent || '')) return;
    if (window.self !== window.top) return; // modèle affiché dans un cadre (aperçu)
    var path = location.pathname.replace(/index\.html$/, '') || '/';
    var day = new Date().toISOString().slice(0, 10), k = 'cs_visit_' + day + '_' + path;
    if (localStorage.getItem(k)) return;
    var v = localStorage.getItem('cs_vid');
    if (!v) { v = (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2)); localStorage.setItem('cs_vid', v); }
    var host = '', src = 'direct';
    try { host = document.referrer ? new URL(document.referrer).hostname.replace(/^www\./, '').toLowerCase() : ''; } catch (_) {}
    var utm = (q.get('utm_source') || '') + ' ' + (q.get('utm_medium') || '');
    if (/prospect/i.test(utm) || q.get('s')) src = 'prospection';
    else if (/mail/i.test(utm)) src = 'email';
    else if (!host || /(^|\.)mycreativesite\.fr$/.test(host)) { src = 'direct'; host = ''; }
    else if (/(^|\.)abracadeal\.(fr|com)$/.test(host)) src = 'abracadeal';
    else if (/(^|\.)google\./.test(host)) src = 'google';
    else if (/chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai|gemini\.google|copilot\.microsoft|mistral\.ai/.test(host)) src = 'ia';
    else if (/bing\.|duckduckgo|qwant|ecosia|yahoo|brave\.com|startpage|lilo/.test(host)) src = 'bing';
    else if (/facebook|(^|\.)fb\.|messenger/.test(host)) src = 'facebook';
    else if (/instagram/.test(host)) src = 'instagram';
    else if (/mail\.|outlook\.|webmail|zimbra/.test(host)) src = 'email';
    else src = 'autre_site';
    // Navigation interne : on ne garde la provenance que pour la page d'arrivée.
    if (src === 'direct' && document.referrer && /(^|\.)mycreativesite\.fr$/.test(new URL(document.referrer).hostname.replace(/^www\./, ''))) src = 'interne';
    var mobile = matchMedia('(max-width:760px),(pointer:coarse)').matches;
    var body = JSON.stringify({ p_visitor: v, p_path: path, p_source: src, p_mobile: mobile, p_ref_host: host || null });
    fetch('https://avcynjwcyygygkjuxsdt.supabase.co/rest/v1/rpc/cs_track_visit', {
      method: 'POST', keepalive: true,
      headers: { 'Content-Type': 'application/json', apikey: 'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO' },
      body: body
    }).then(function (r) { if (r.ok) localStorage.setItem(k, '1'); }).catch(function () {});
  } catch (_) {}
})();
