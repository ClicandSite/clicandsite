/* 12/11/2026 (Claude, Anthony : « mets un compteur aussi sur MyCreativeSite ») — compteur de visiteurs.
   1 visite par visiteur, page et jour (identifiant anonyme dans le navigateur, aucune donnée personnelle).
   Pas comptés : robots et navigateurs automatisés, l'appareil d'Anthony (marqué en ouvrant l'admin,
   ou avec mycreativesite.fr/?moi=1 ; ?moi=0 pour annuler). Résultats : admin, bloc « Visiteurs du site ».
   13/11/2026 (Anthony, « comme sur Clic&Site ») : aussi #nostats (exclure) / #stats (recompter) sur n'importe quelle page,
   et lien secret sur son nom dans les mentions légales (window.csStatsToggle). */
(function () {
  'use strict';
  var NC = 'cs_not_counted';
  var toast = function (msg) {
    try {
      var t = document.createElement('div'); t.textContent = msg; t.setAttribute('role', 'status');
      t.style.cssText = 'position:fixed;left:50%;bottom:calc(24px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:2147483647;background:#12162B;color:#fff;padding:12px 18px;border-radius:12px;font:600 15px/1.35 system-ui,-apple-system,sans-serif;box-shadow:0 12px 30px -12px rgba(0,0,0,.5);max-width:calc(100% - 32px);text-align:center';
      (document.body || document.documentElement).appendChild(t); setTimeout(function () { t.remove(); }, 3500);
    } catch (_) {}
  };
  var setMe = function (excluded) {
    try { if (excluded) localStorage.setItem(NC, '1'); else localStorage.removeItem(NC); } catch (_) {}
    toast(excluded ? '✓ Cet appareil n\'est plus compté dans les statistiques' : 'Cet appareil est de nouveau compté');
  };
  window.csStatsToggle = function () { var ex = false; try { ex = localStorage.getItem(NC) === '1'; } catch (_) {} setMe(!ex); };
  var fromHash = function () {
    var h = (location.hash || '').toLowerCase();
    if (h !== '#nostats' && h !== '#stats') return false;
    setMe(h === '#nostats');
    try { history.replaceState(null, '', location.pathname + location.search); } catch (_) {}
    return true;
  };
  window.addEventListener('hashchange', fromHash);
  window.csTrack = function () {};
  try {
    var q = new URLSearchParams(location.search);
    if (q.get('moi') === '1') localStorage.setItem(NC, '1');
    else if (q.get('moi') === '0') localStorage.removeItem(NC);
    var go = function () { fromHash(); };
    if (document.body) go(); else document.addEventListener('DOMContentLoaded', go);
    if (localStorage.getItem(NC) === '1' || /^#nostats$/i.test(location.hash)) return;
    if (navigator.webdriver || /bot|crawl|spider|slurp|headless|lighthouse|pagespeed|preview|facebookexternalhit|phantomjs|puppeteer|playwright|selenium|inspectiontool|googleother|google-read-aloud|google-site-verification|bingpreview|petalsearch|yandex/i.test(navigator.userAgent || '')) return;
    if (window.self !== window.top) return; // modèle affiché dans un cadre (aperçu)
    var path = location.pathname.replace(/index\.html$/, '') || '/';
    var day = new Date().toISOString().slice(0, 10), k = 'cs_visit_' + day + '_' + path;
    var v = localStorage.getItem('cs_vid');
    // identifiant anonyme renouvelé au bout de 13 mois (recommandation CNIL pour la mesure d'audience)
    var vt = +localStorage.getItem('cs_vid_t') || 0; if (v && (!vt || Date.now() - vt > 395 * 864e5)) { if (vt) v = null; else localStorage.setItem('cs_vid_t', String(Date.now())); }
    if (!v) { v = (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + Math.random().toString(36).slice(2)); localStorage.setItem('cs_vid', v); localStorage.setItem('cs_vid_t', String(Date.now())); }
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
    var send = function (pth, source, key) {
      fetch('https://avcynjwcyygygkjuxsdt.supabase.co/rest/v1/rpc/cs_track_visit', {
        method: 'POST', keepalive: true,
        headers: { 'Content-Type': 'application/json', apikey: 'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO' },
        body: JSON.stringify({ p_visitor: v, p_path: pth, p_source: source, p_mobile: mobile, p_ref_host: source === 'interne' ? null : (host || null) })
      }).then(function (r) { if (r.ok) localStorage.setItem(key, '1'); }).catch(function () {});
    };
    if (!localStorage.getItem(k)) send(path, src, k);
    /* 12/11/2026 (Anthony : « quelles pages amènent des visiteurs et des commandes ») : étapes vers la commande,
       enregistrées comme pages virtuelles « /_… », une fois par visiteur et par jour. Admin : bloc « Ce qui amène des commandes ». */
    window.csTrack = function (ev) {
      try { var kk = 'cs_visit_' + day + '_/_' + ev; if (!localStorage.getItem(kk)) send('/_' + ev, 'interne', kk); } catch (_) {}
    };
    document.addEventListener('click', function (e) {
      if (!e.target || !e.target.closest) return;
      if (e.target.closest('.tabs [data-k], .gcard')) { window.csTrack('modele-vu'); return; }  // aperçu d'un modèle sur l'accueil
      var a = e.target.closest('a[href]'); if (!a) return;
      var h = a.getAttribute('href') || '';
      if (/(^|\/)espace\/\?[^#]*demo=/.test(h)) window.csTrack('essai-espace');
      else if (/(^|\/)modeles\//.test(h)) window.csTrack('modele-vu');
      else if (/#commande$/.test(h)) window.csTrack('clic-commander');
    }, true);
  } catch (_) {}
})();
