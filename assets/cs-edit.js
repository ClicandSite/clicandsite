/* MyCreativeSite · moteur de contenu des sites clients (06/11/2026).
   - CSEdit.extract(doc)        : lit le contenu modifiable d'une page (textes, chiffres, prix, horaires, coordonnées, photos)
   - CSEdit.apply(doc, content) : applique un contenu enregistré à la page
   - Sur un site client, ce script se charge avec data-site="identifiant" : il récupère le contenu publié
     depuis l'espace client et met la page à jour. Aucune donnée personnelle n'est lue ni envoyée. */
(function () {
  var API = 'https://avcynjwcyygygkjuxsdt.supabase.co';
  var KEY = 'sb_publishable_fdSM-pnUtZRKX7K6nOf5Ag_i1TQgqLO';

  function q(root, sel) { try { return root.querySelector(sel); } catch (e) { return null; } }
  function qa(root, sel) { try { return [].slice.call(root.querySelectorAll(sel)); } catch (e) { return []; } }
  function txt(el) { return el ? el.textContent.replace(/\s+/g, ' ').trim() : ''; }
  function setTxt(el, v) { if (el && typeof v === 'string') el.textContent = v.slice(0, 2000); }
  function safeUrl(u) { return typeof u === 'string' && /^(https:\/\/|blob:|data:image\/(jpeg|png|webp);base64,)/.test(u) ? u : null; }
  function setImg(el, u) { u = safeUrl(u); if (el && u) el.style.setProperty('--img', 'url("' + u.replace(/"/g, '%22') + '")'); }

  // Champs simples : clé → sélecteur
  var TEXT = {
    logo: 'header.top .logo',
    kicker: '.photo.hero .kicker',
    title: '.photo.hero h1',
    subtitle: '.photo.hero p',
    team_t: '.team h2',
    team_d: '.team p',
    cta_t: '.cta h2',
    cta_d: '.cta p',
    address: '.addr .v',
    footer: 'footer .wrap > span:first-child'
  };
  // Listes : conteneur d'éléments + champs de chaque élément
  var LISTS = {
    stats: { items: '.stats > .stat', f: { v: 'b', l: 'span' } },
    contacts: { items: '.cinfo > div', f: { l: '.l', v: '.v' } },
    cards: { items: '.cards > .card', f: { t: 'h3', d: 'p', p: '.price' }, img: '.photo', add: true },
    items: { items: '.vgrid > .car, .props > .prop', f: { t: 'h3', p: '.prx' }, meta: '.meta', img: '.photo', add: true },
    hours: { items: '.hrow', f: { l: 'span:nth-child(1)', v: 'span:nth-child(2)' }, add: true }
  };

  function readItem(el, def) {
    var o = {};
    Object.keys(def.f).forEach(function (k) { o[k] = txt(q(el, def.f[k])); });
    if (def.meta) o.meta = qa(el, def.meta + ' > span').map(txt).join(' · ');
    if (def.img) o.img = null;
    return o;
  }
  function writeItem(el, def, o) {
    Object.keys(def.f).forEach(function (k) { if (o[k] !== undefined) setTxt(q(el, def.f[k]), String(o[k])); });
    if (def.meta && typeof o.meta === 'string') {
      var box = q(el, def.meta);
      if (box) { box.textContent = ''; o.meta.split('·').map(function (s) { return s.trim(); }).filter(Boolean).slice(0, 6).forEach(function (s) { var sp = el.ownerDocument.createElement('span'); sp.textContent = s; box.appendChild(sp); }); }
    }
    if (def.img && o.img) setImg(q(el, def.img) || (el.classList.contains('photo') ? el : null), o.img);
  }
  // Ajuste le nombre d'éléments d'une liste (copie du dernier / suppression)
  function fit(nodes, n, max) {
    n = Math.max(0, Math.min(n, max || 40));
    if (!nodes.length) return nodes;
    var parent = nodes[0].parentNode, last = nodes[nodes.length - 1];
    while (nodes.length < n) { var c = last.cloneNode(true); parent.insertBefore(c, last.nextSibling); last = c; nodes.push(c); }
    while (nodes.length > Math.max(n, 1)) nodes.pop().remove();
    nodes.forEach(function (e) { e.hidden = false; });
    if (n === 0) nodes[0].hidden = true; // garde un modèle caché pour pouvoir en rajouter
    return n === 0 ? [] : nodes;
  }

  function extract(doc) {
    var c = { v: 1, text: {}, prices: [], photos: {} };
    Object.keys(TEXT).forEach(function (k) { var el = q(doc, TEXT[k]); if (el) c.text[k] = txt(el); });
    Object.keys(LISTS).forEach(function (k) { var d = LISTS[k]; var els = qa(doc, d.items); if (els.length) c[k] = els.map(function (e) { return readItem(e, d); }); });
    qa(doc, '.prices').forEach(function (box) {
      c.prices.push(qa(box, ':scope > .row').map(function (r) { return { t: txt(q(r, '.t')), d: txt(q(r, '.d')), p: txt(q(r, '.p')) }; }));
    });
    if (q(doc, '.photo.hero')) c.photos.hero = null;
    if (q(doc, '.team .photo')) c.photos.team = null;
    var g = qa(doc, '.gallery > .photo'); if (g.length) c.photos.gallery = g.map(function () { return null; });
    return c;
  }

  function apply(doc, c) {
    if (!c || typeof c !== 'object') return;
    var t = c.text || {};
    Object.keys(TEXT).forEach(function (k) { if (typeof t[k] === 'string') setTxt(q(doc, TEXT[k]), t[k]); });
    Object.keys(LISTS).forEach(function (k) {
      var d = LISTS[k], arr = c[k]; if (!Array.isArray(arr)) return;
      var els = qa(doc, d.items); if (!els.length) return;
      if (d.add) els = fit(els, arr.length, 40); else arr = arr.slice(0, els.length);
      arr.forEach(function (o, i) { if (els[i] && o) writeItem(els[i], d, o); });
      if (k === 'hours') els.forEach(function (e, i) { var v = (arr[i] && arr[i].v || '').toLowerCase(); e.classList.toggle('closed', /ferm/.test(v)); });
    });
    if (Array.isArray(c.prices)) qa(doc, '.prices').forEach(function (box, gi) {
      var arr = c.prices[gi]; if (!Array.isArray(arr)) return;
      var rows = fit(qa(box, ':scope > .row'), arr.length, 60);
      arr.forEach(function (o, i) { var r = rows[i]; if (!r || !o) return; setTxt(q(r, '.t'), o.t || ''); setTxt(q(r, '.d'), o.d || ''); setTxt(q(r, '.p'), o.p || ''); });
    });
    var p = c.photos || {};
    if (p.hero) setImg(q(doc, '.photo.hero'), p.hero);
    if (p.team) setImg(q(doc, '.team .photo'), p.team);
    if (Array.isArray(p.gallery)) qa(doc, '.gallery > .photo').forEach(function (e, i) { if (p.gallery[i]) setImg(e, p.gallery[i]); });
    if (c.style && doc.documentElement) doc.documentElement.setAttribute('data-style', String(c.style).replace(/[^a-z]/g, ''));
    var ev; try { ev = new Event('cs:applied'); doc.dispatchEvent(ev); } catch (e) {}
  }

  window.CSEdit = { extract: extract, apply: apply, TEXT: TEXT, LISTS: LISTS };

  // Site client : charge le contenu publié
  var me = document.currentScript;
  var slug = me && me.getAttribute('data-site');
  if (slug) {
    fetch(API + '/rest/v1/rpc/cs_site_content', {
      method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY },
      body: JSON.stringify({ p_slug: slug })
    }).then(function (r) { return r.ok ? r.json() : null; }).then(function (c) {
      if (!c) return;
      var go = function () { apply(document, c); };
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
    }).catch(function () { /* le site garde son contenu d'origine */ });
  }
})();
