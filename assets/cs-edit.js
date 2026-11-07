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
    footer: 'footer .wrap > span:first-child',
    avis_t: '#avis .head h2',
    avis_d: '#avis .head p'
  };
  // Listes : conteneur d'éléments + champs de chaque élément
  var LISTS = {
    stats: { items: '.stats > .stat', f: { v: 'b', l: 'span' } },
    contacts: { items: '.cinfo > div', f: { l: '.l', v: '.v' } },
    cards: { items: '.cards > .card', f: { t: 'h3', d: 'p', p: '.price' }, img: '.photo', add: true },
    items: { items: '.vgrid > .car, .props > .prop', f: { t: 'h3', p: '.prx' }, meta: '.meta', img: '.photo', add: true },
    hours: { items: '.hrow', f: { l: 'span:nth-child(1)', v: 'span:nth-child(2)' }, add: true },
    reviews: { items: '#avis .reviews > .rev', f: { s: '.s', d: 'p', who: '.who' }, add: true }
  };
  // Avis Google (07/11/2026, comme sur le site EPS) : avis recopiés par le pro + note et liens vers sa fiche Google
  var DEF_AVIS = 'Ce que disent nos clients sur Google.';
  function gUrl(u) { return typeof u === 'string' && /^https:\/\/([a-z0-9-]+\.)*(google\.[a-z.]+|goo\.gl|g\.page)\//i.test(u.trim()) ? u.trim() : null; }
  function stars(n) { n = Math.max(1, Math.min(5, Math.round(n || 5))); return '★★★★★'.slice(0, n) + '☆☆☆☆☆'.slice(0, 5 - n); }
  function google(doc, g) {
    var head = q(doc, '#avis .head'); if (!head) return;
    var old = q(head, '.cs-gg'); if (old) old.remove();
    g = g || {}; var url = gUrl(g.url), rv = gUrl(g.review), score = parseFloat(String(g.score || '').replace(',', '.'));
    if (!url && !rv) return;
    var box = doc.createElement('div'); box.className = 'cs-gg';
    box.style.cssText = 'display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px';
    if (url) {
      var a = doc.createElement('a'); a.href = url; a.target = '_blank'; a.rel = 'noopener';
      a.style.cssText = 'display:inline-flex;align-items:baseline;gap:8px;color:inherit;text-decoration:none;font-weight:700';
      if (score > 0 && score <= 5) {
        var n = doc.createElement('span'); n.textContent = score.toFixed(1).replace('.', ','); n.style.fontSize = '1.7em';
        var st = doc.createElement('span'); st.textContent = stars(score); st.style.cssText = 'color:var(--accent);letter-spacing:2px'; st.setAttribute('aria-label', score + ' sur 5');
        a.append(n, st);
      }
      var c = doc.createElement('span'); var cnt = parseInt(g.count, 10);
      c.textContent = (cnt > 0 ? cnt + ' avis' : 'Voir nos avis') + ' sur Google'; c.style.cssText = 'font-weight:500;text-decoration:underline;opacity:.85';
      a.appendChild(c); box.appendChild(a);
    }
    if (rv) { var b = doc.createElement('a'); b.className = 'btn'; b.href = rv; b.target = '_blank'; b.rel = 'noopener'; b.textContent = 'Laisser un avis'; box.appendChild(b); }
    head.appendChild(box);
  }

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
    if (c.text.avis_d && /^Exemples/.test(c.text.avis_d)) c.text.avis_d = DEF_AVIS;
    if (q(doc, '#avis')) c.google = { url: '', review: '', score: '', count: '' };
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
    if (!Array.isArray(c.reviews)) c = Object.assign({}, c, { reviews: [] }); // pas d'avis d'exemple sur un vrai site
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
    var ad = q(doc, '#avis .head p'); if (ad && typeof t.avis_d !== 'string' && /^Exemples/.test(txt(ad))) ad.textContent = DEF_AVIS;
    google(doc, c.google);
    var av = q(doc, '#avis'); if (av) av.hidden = !c.reviews.length && !(c.google && (gUrl(c.google.url) || gUrl(c.google.review)));
    var p = c.photos || {};
    if (p.hero) setImg(q(doc, '.photo.hero'), p.hero);
    if (p.team) setImg(q(doc, '.team .photo'), p.team);
    if (Array.isArray(p.gallery)) qa(doc, '.gallery > .photo').forEach(function (e, i) { if (p.gallery[i]) setImg(e, p.gallery[i]); });
    if (c.style && doc.documentElement) doc.documentElement.setAttribute('data-style', String(c.style).replace(/[^a-z]/g, ''));
    var ev; try { ev = new Event('cs:applied'); doc.dispatchEvent(ev); } catch (e) {}
  }

  // 07/11/2026 : icône automatique du site client (onglet, favoris, écran d'accueil du téléphone).
  // Logo carré envoyé par le pro (photos.icon) ; sinon monogramme : 1re lettre du nom, sur la couleur du style.
  function siteIcon(doc, c) {
    try {
      var name = ((c.text && c.text.logo) || txt(q(doc, TEXT.logo)) || '').trim();
      var cs = getComputedStyle(doc.documentElement), acc = (cs.getPropertyValue('--accent') || '').trim() || '#12162B';
      var put = function (url) {
        qa(doc, 'link[rel="icon"],link[rel="shortcut icon"],link[rel="apple-touch-icon"]').forEach(function (l) { l.remove(); });
        [['icon', '32x32'], ['icon', '180x180'], ['apple-touch-icon', '180x180']].forEach(function (r) {
          var l = doc.createElement('link'); l.rel = r[0]; l.sizes = r[1]; l.type = 'image/png'; l.href = url; doc.head.appendChild(l); });
        var m = q(doc, 'meta[name="apple-mobile-web-app-title"]'); if (!m) { m = doc.createElement('meta'); m.name = 'apple-mobile-web-app-title'; doc.head.appendChild(m); }
        m.content = name.slice(0, 30) || 'Mon site';
      };
      var cv = doc.createElement('canvas'); cv.width = cv.height = 180; var g = cv.getContext('2d');
      var src = c.photos && safeUrl(c.photos.icon);
      if (src) {
        var im = new Image(); im.crossOrigin = 'anonymous';
        im.onload = function () { try { g.fillStyle = '#fff'; g.fillRect(0, 0, 180, 180); var k = Math.min(156 / im.width, 156 / im.height), w = im.width * k, h = im.height * k; g.drawImage(im, (180 - w) / 2, (180 - h) / 2, w, h); put(cv.toDataURL('image/png')); } catch (e) { put(src); } };
        im.onerror = function () { put(src); }; im.src = src; return;
      }
      var tmp = doc.createElement('span'); tmp.style.color = acc; doc.body.appendChild(tmp); var rgb = (getComputedStyle(tmp).color.match(/\d+/g) || [18, 22, 43]).map(Number); tmp.remove();
      var lum = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255;
      g.fillStyle = 'rgb(' + rgb.slice(0, 3).join(',') + ')'; g.fillRect(0, 0, 180, 180);
      g.fillStyle = lum > 0.6 ? '#12162B' : '#fff'; g.textAlign = 'center'; g.textBaseline = 'middle';
      g.font = '700 112px ' + (cs.fontFamily || 'system-ui, sans-serif');
      var L = (name.replace(/^(le|la|les|l'|chez|maison|garage|atelier|studio)\s+/i, '').match(/[A-Za-zÀ-ÿ0-9]/) || ['M'])[0].toUpperCase();
      g.fillText(L, 90, 98); put(cv.toDataURL('image/png'));
    } catch (e) { /* pas d'icône, tant pis */ }
  }

  window.CSEdit = { extract: extract, apply: apply, TEXT: TEXT, LISTS: LISTS, gUrl: gUrl, siteIcon: siteIcon };

  // Site client : charge le contenu publié
  var me = document.currentScript;
  var slug = me && me.getAttribute('data-site');
  if (slug) {
    fetch(API + '/rest/v1/rpc/cs_site_content', {
      method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY },
      body: JSON.stringify({ p_slug: slug })
    }).then(function (r) { return r.ok ? r.json() : null; }).then(function (c) {
      if (!c) return;
      var go = function () { apply(document, c); siteIcon(document, c); if (c.shop) initShop(slug, c.shop); if (c.pay) { window.CS_PAY = c.pay; if (window.CS_PAY_INIT) window.CS_PAY_INIT(); } };
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', go); else go();
    }).catch(function () { /* le site garde son contenu d'origine */ });
    initLeads(slug);
  }

  /* 07/11/2026 (Claude) : boutique en ligne. Le panier est géré par la page (window.CSShop) ;
     ici on envoie la commande à MyCreativeSite, qui recalcule les prix et ouvre le paiement par carte
     sur le compte Stripe du commerçant (ou l'enregistre « à régler sur place » si la carte n'est pas activée). */
  var SHOP_FN = API + '/functions/v1/cs-shop';
  function initShop(slug, cfg) {
    var S = window.CSShop, f = document.getElementById('cartform');
    if (!S || !f) return;
    S.config({ ship: cfg.ship, free: cfg.free, pickup: cfg.pickup, delivery: cfg.delivery });
    var pay = document.getElementById('payBtn'), legal = q(f, '.legal'), okc = document.getElementById('okc');
    if (!cfg.card) {
      if (pay) pay.textContent = 'Envoyer ma commande';
      if (legal) legal.textContent = 'Vous réglez au retrait ou à la livraison. La boutique vous confirme la commande par e-mail.';
    }
    var u = new URL(location.href), st = u.searchParams.get('commande'), sess = u.searchParams.get('cs_session');
    function msg(t) { if (okc) { okc.textContent = t; okc.hidden = false; } }
    if (st) {
      u.searchParams.delete('commande'); u.searchParams.delete('cs_session'); history.replaceState(null, '', u.pathname + u.search + u.hash);
      if (st === 'ok') {
        S.clear(); S.open();
        var body = document.getElementById('cartBody'); if (body) body.hidden = false;
        msg('Merci ! Votre paiement est accepté et votre commande est transmise à la boutique. Vous recevez une confirmation par e-mail.');
        if (sess) fetch(SHOP_FN, { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY }, body: JSON.stringify({ action: 'confirm', slug: slug, session: sess }) }).catch(function () {});
      } else { S.open(); msg('Paiement annulé : votre panier est toujours là.'); }
    }
    f.addEventListener('submit', function (e) {
      e.preventDefault(); e.stopImmediatePropagation();
      if (!f.reportValidity()) return;
      var p = S.payload(); if (!p.items.length) return;
      var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
      pay.disabled = true; var old = pay.textContent; pay.textContent = 'Un instant…'; if (okc) okc.hidden = true;
      fetch(SHOP_FN, { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY },
        body: JSON.stringify({ action: 'checkout', slug: slug, items: p.items, mode: p.mode, name: v('o-name'), email: v('o-mail'), phone: v('o-tel'), address: v('o-addr'), note: v('o-note'), back: location.origin + location.pathname })
      }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); }).then(function (r) {
        if (!r.ok) throw new Error(r.j && r.j.message || 'Commande impossible');
        if (r.j.url) { location.href = r.j.url; return; }
        pay.disabled = false; pay.textContent = old; S.clear();
        var body = document.getElementById('cartBody'); if (body) body.hidden = false;
        msg('Merci ! Votre commande est transmise à la boutique, qui vous confirme par e-mail. Vous réglerez au ' + (p.mode === 'livraison' ? 'moment de la livraison.' : 'retrait.'));
      }).catch(function (x) { pay.disabled = false; pay.textContent = old; msg((x && x.message && !/fetch/i.test(x.message)) ? x.message : 'La commande n\'est pas partie. Vérifiez votre connexion et réessayez.'); });
    }, true);
  }

  /* 07/11/2026 (Claude, demande d'Anthony) : demandes des visiteurs (réservation, devis, rendez-vous…).
     Sur un site client, chaque formulaire demande les coordonnées du visiteur puis envoie la demande
     dans l'espace client du pro (liste « Mes clients », suivi complet en formule Premium).
     Sur les modèles de démonstration (sans data-site), rien ne change et rien n'est envoyé. */
  function initLeads(slug) {
    var SKIP = { search: 1, cartform: 1 };
    function kindOf(form) {
      var b = q(form, '[type="submit"]'), t = (txt(b) + ' ' + form.id).toLowerCase();
      if (/devis/.test(t)) return 'devis';
      if (/rappel/.test(t)) return 'rappel';
      if (/estimation|estform/.test(t)) return 'estimation';
      if (/reprise/.test(t)) return 'reprise';
      if (/rendez-vous/.test(t)) return 'rendez-vous';
      if (/table|prix|trajet/.test(t)) return 'reservation';
      if (/côté|command/.test(t)) return 'commande';
      if (/réserv/.test(t)) return 'rendez-vous';
      return 'contact';
    }
    function pad(n) { return (n < 10 ? '0' : '') + n; }
    function niceDate(v, withTime) {
      var m = /^(\d{4})-(\d{2})-(\d{2})(?:T(\d{2}):(\d{2}))?/.exec(v || '');
      if (!m) return v;
      return m[3] + '/' + m[2] + '/' + m[1] + (withTime && m[4] ? ' à ' + m[4] + 'h' + m[5] : '');
    }
    function labelFor(form, el) {
      var l = el.id && q(form, 'label[for="' + el.id + '"]');
      return txt(l) || el.getAttribute('aria-label') || el.name || '';
    }
    function collect(form) {
      var out = [], tel = '';
      qa(form, 'input,select,textarea').forEach(function (el) {
        if (el.type === 'hidden' || el.type === 'submit' || el.type === 'button' || el.closest('.cs-lead')) return;
        var v = el.tagName === 'SELECT' ? txt(el.options[el.selectedIndex]) : String(el.value || '').trim();
        if (el.type === 'date') v = niceDate(v, false);
        if (el.type === 'datetime-local') v = niceDate(v, true);
        if (el.type === 'tel' && !tel) tel = v;
        if (v) out.push({ l: labelFor(form, el), v: v });
      });
      return { fields: out, tel: tel };
    }
    // Les champs des modèles sont pré-remplis avec des exemples : sur le vrai site ils deviennent des indications.
    function prepare(form) {
      var today = new Date(), iso = today.getFullYear() + '-' + pad(today.getMonth() + 1) + '-' + pad(today.getDate());
      qa(form, 'input').forEach(function (el) {
        if (el.type === 'date' || el.type === 'datetime-local') {
          el.min = el.type === 'date' ? iso : iso + 'T00:00';
          el.value = ''; el.required = true; return;
        }
        if (!el.type || el.type === 'text' || el.type === 'tel') {
          if (el.value && !el.placeholder) el.placeholder = 'Ex. : ' + el.value;
          el.value = '';
        }
      });
      qa(form, '.ok').forEach(function (o) { o.hidden = true; });
    }
    var css = '.cs-lead{position:fixed;inset:0;z-index:2147483000;background:rgba(10,12,20,.55);display:flex;align-items:center;justify-content:center;padding:16px max(16px,env(safe-area-inset-right,0px)) 16px max(16px,env(safe-area-inset-left,0px))}' +
      '.cs-lead .cs-box{background:#fff;color:#16181f;width:100%;max-width:420px;max-height:calc(100dvh - 32px);overflow:auto;border-radius:18px;padding:22px 20px;box-shadow:0 24px 60px rgba(0,0,0,.3);font:15px/1.45 inherit;font-family:inherit;text-align:left}' +
      '.cs-lead h3{margin:0 0 4px;font-size:1.2rem;color:#16181f}.cs-lead p{margin:0 0 14px;color:#5a5f6e;font-size:.9rem}' +
      '.cs-lead label{display:block;font-size:.8rem;font-weight:600;color:#5a5f6e;margin:10px 0 4px}' +
      '.cs-lead input,.cs-lead textarea{display:block;width:100%;box-sizing:border-box;padding:11px 12px;border:1px solid #d6d9e3;border-radius:10px;font:inherit;color:#16181f;background:#fff}' +
      '.cs-lead textarea{min-height:70px;resize:vertical}.cs-lead .cs-hp{position:absolute;left:-9999px;width:1px;height:1px;opacity:0}' +
      '.cs-lead .cs-act{display:flex;gap:8px;margin-top:16px;flex-wrap:wrap}.cs-lead .cs-act .btn{flex:1;justify-content:center}' +
      '.cs-lead .cs-cancel{background:none;border:0;color:#5a5f6e;font:inherit;font-weight:600;cursor:pointer;padding:10px}' +
      '.cs-lead .cs-err{color:#b42318;font-size:.86rem;margin-top:10px}.cs-lead .cs-small{font-size:.76rem;color:#7a7f8e;margin:12px 0 0}' +
      '.cs-lead .cs-pay{display:grid;gap:2px;background:#f2f7f3;border:1px solid #cfe5d5;border-radius:12px;padding:10px 12px;margin:0 0 4px}.cs-lead .cs-pay b{font-size:1.05rem;color:#14532d}.cs-lead .cs-pay span{font-size:.82rem;color:#3f5e48}' +
      '.cs-bk{font-size:.85rem!important;padding:8px 14px!important;min-height:0!important;margin-top:6px}' +
      '.cs-banner{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(16px + env(safe-area-inset-bottom,0px));z-index:2147483001;width:min(560px,calc(100% - 32px));background:#16181f;color:#fff;border-radius:14px;padding:14px 44px 14px 16px;font:15px/1.45 inherit;font-family:inherit;box-shadow:0 18px 40px rgba(0,0,0,.3)}.cs-banner.ok{background:#14532d}.cs-banner button{position:absolute;top:8px;right:8px;background:none;border:0;color:inherit;font-size:18px;cursor:pointer;padding:6px}';
    var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    function bizName() { return txt(q(document, 'header.top .logo')) || document.title.split(/[·|–-]/)[0].trim(); }
    function cents(p) { var m = /^(\d{1,6})(?:[,.](\d{1,2}))?€?$/.exec(String(p || '').replace(/\s/g, '')); return m ? (+m[1]) * 100 + (m[2] ? +(m[2] + '0').slice(0, 2) : 0) : 0; }
    function eur(c) { return (c / 100).toFixed(2).replace('.', ',').replace(',00', '') + ' €'; }
    // 07/11/2026 : formule Pro — combien payer en ligne (null = simple demande)
    function payFor(item, kind) {
      var P = window.CS_PAY; if (!P) return null;
      if (item) { if (P.forfait === 'off' || !item.price) return null;
        var dep = P.forfait === 'deposit' && P.pct < 100, a = dep ? Math.round(item.price * P.pct / 100) : item.price;
        return { amount: a, note: dep ? 'Acompte de ' + P.pct + ' % sur ' + eur(item.price) + ', le reste est réglé le jour de la prestation.' : 'Prix total de la prestation.' }; }
      if (P.deposit >= 100 && (kind === 'reservation' || kind === 'rendez-vous')) return { amount: P.deposit, note: 'Acompte pour confirmer votre réservation, déduit du prix final.' };
      return null;
    }
    function open(form, item) {
      var data = form ? collect(form) : { fields: [], tel: '' }, kind = form ? kindOf(form) : 'reservation', pay = payFor(item, kind);
      var wrap = document.createElement('div'); wrap.className = 'cs-lead'; wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true');
      wrap.innerHTML = '<form class="cs-box" novalidate><h3>' + (item ? 'Réserver : ' + esc(item.t) : (pay ? 'Réserver et payer' : 'Vos coordonnées')) + '</h3><p>' + (pay ? 'Paiement sécurisé par carte, directement à ' + esc(bizName()) + '.' : 'Pour que ' + esc(bizName()) + ' vous réponde.') + '</p>' +
        (pay ? '<div class="cs-pay"><b>À payer maintenant : ' + eur(pay.amount) + '</b><span>' + esc(pay.note) + '</span></div>' : '') +
        (item ? '<label for="cs-d">Date et heure souhaitées</label><input id="cs-d" type="datetime-local" required>' : '') +
        '<label for="cs-n">Nom</label><input id="cs-n" autocomplete="name" required maxlength="120">' +
        '<label for="cs-t">Téléphone</label><input id="cs-t" type="tel" autocomplete="tel" inputmode="tel" maxlength="30">' +
        '<label for="cs-e">E-mail' + (pay ? ' (pour votre reçu)' : '') + '</label><input id="cs-e" type="email" autocomplete="email" maxlength="160">' +
        '<label for="cs-m">Message (facultatif)</label><textarea id="cs-m" maxlength="2000"></textarea>' +
        '<input class="cs-hp" id="cs-w" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<div class="cs-err" role="alert" hidden></div>' +
        '<div class="cs-act"><button type="button" class="cs-cancel">Annuler</button><button class="btn" type="submit">' + (pay ? 'Payer ' + eur(pay.amount) + ' et réserver' : 'Envoyer ma demande') + '</button></div>' +
        '<p class="cs-small">Vos coordonnées sont transmises uniquement à ' + esc(bizName()) + ' pour répondre à votre demande.' + (pay ? ' Le paiement est traité par Stripe.' : '') + '</p></form>';
      document.body.appendChild(wrap);
      var f = q(wrap, 'form'), err = q(wrap, '.cs-err');
      if (q(wrap, '#cs-d')) { var t0 = new Date(Date.now() + 864e5); q(wrap, '#cs-d').min = t0.getFullYear() + '-' + pad(t0.getMonth() + 1) + '-' + pad(t0.getDate()) + 'T00:00'; }
      if (data.tel) q(wrap, '#cs-t').value = data.tel;
      setTimeout(function () { q(wrap, item ? '#cs-d' : '#cs-n').focus(); }, 30);
      function close() { wrap.remove(); document.removeEventListener('keydown', onKey); }
      function onKey(e) { if (e.key === 'Escape') close(); }
      document.addEventListener('keydown', onKey);
      q(wrap, '.cs-cancel').onclick = close;
      wrap.addEventListener('click', function (e) { if (e.target === wrap) close(); });
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var n = q(wrap, '#cs-n').value.trim(), t = q(wrap, '#cs-t').value.trim(), m = q(wrap, '#cs-e').value.trim(), d = q(wrap, '#cs-d');
        err.hidden = true;
        if (d && !d.value) { err.textContent = 'Choisissez la date et l\'heure.'; err.hidden = false; return; }
        if (!n) { err.textContent = 'Indiquez votre nom.'; err.hidden = false; return; }
        if (pay && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m)) { err.textContent = 'Indiquez votre e-mail pour recevoir le reçu de paiement.'; err.hidden = false; return; }
        if (!t && !m) { err.textContent = 'Indiquez un téléphone ou un e-mail pour être recontacté.'; err.hidden = false; return; }
        var fields = data.fields.slice(); if (d) fields.unshift({ l: 'Date et heure', v: niceDate(d.value, true) });
        var b = q(f, '[type="submit"]'), lbl = b.textContent; b.disabled = true; b.textContent = pay ? 'Ouverture du paiement…' : 'Envoi…';
        var req = pay
          ? fetch(SHOP_FN, { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY }, body: JSON.stringify({ action: 'book', slug: slug, item: item ? { src: item.src, g: item.g, i: item.i, t: item.t } : null, kind: kind, name: n, phone: t, email: m, message: q(wrap, '#cs-m').value, fields: fields, back: location.origin + location.pathname }) })
          : fetch(API + '/rest/v1/rpc/cs_lead_submit', { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY },
              body: JSON.stringify({ p_slug: slug, p_kind: kind, p_name: n, p_phone: t, p_email: m, p_message: q(wrap, '#cs-m').value, p_fields: fields, p_page: location.pathname, p_hp: q(wrap, '#cs-w').value }) });
        req.then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); }).then(function (r) {
          if (!r.ok) throw new Error((r.j && r.j.message) || 'Envoi impossible');
          if (pay) { if (!r.j.url) throw new Error('Paiement indisponible'); location.href = r.j.url; return; }
          close();
          var ok = form && q(form, '.ok');
          if (form && !ok) { ok = document.createElement('div'); ok.className = 'ok'; form.appendChild(ok); }
          if (ok) { ok.textContent = 'Merci ' + n + ', votre demande est bien envoyée. ' + bizName() + ' vous recontacte rapidement.'; ok.hidden = false; }
        }).catch(function (x) {
          b.disabled = false; b.textContent = lbl;
          err.textContent = (x && x.message && !/fetch/i.test(x.message)) ? x.message : 'La demande n\'est pas partie. Vérifiez votre connexion et réessayez.';
          err.hidden = false;
        });
      });
    }
    // Boutons « Réserver » sur les tarifs et prestations à prix fixe, et retour du paiement
    function banner(t, good) { var d = document.createElement('div'); d.className = 'cs-banner' + (good ? ' ok' : ''); d.setAttribute('role', 'status'); d.textContent = t;
      var x = document.createElement('button'); x.type = 'button'; x.setAttribute('aria-label', 'Fermer'); x.textContent = '✕'; x.onclick = function () { d.remove(); }; d.appendChild(x); document.body.appendChild(d); }
    window.CS_PAY_INIT = function () {
      var P = window.CS_PAY; if (!P) return;
      var u = new URL(location.href), st = u.searchParams.get('paiement'), sess = u.searchParams.get('cs_session');
      if (st) {
        u.searchParams.delete('paiement'); u.searchParams.delete('cs_session'); history.replaceState(null, '', u.pathname + u.search + u.hash);
        if (st === 'ok') { banner('Merci ! Votre paiement est accepté et votre réservation est transmise à ' + bizName() + '. Vous recevez le reçu par e-mail.', true);
          if (sess) fetch(SHOP_FN, { method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY }, body: JSON.stringify({ action: 'confirm', slug: slug, session: sess }) }).catch(function () {}); }
        else banner('Paiement annulé : rien n\'a été débité. Votre demande a tout de même été transmise, ' + bizName() + ' peut vous recontacter.', false);
      }
      if (P.forfait === 'off' || q(document, '.dish')) return;
      var add = function (el, item, place) { if (!item.price || q(el, '.cs-bk')) return; var b = document.createElement('button'); b.type = 'button'; b.className = 'btn cs-bk'; b.textContent = 'Réserver';
        b.addEventListener('click', function () { open(null, item); }); place(b); };
      qa(document, '.prices').forEach(function (box, g) { qa(box, ':scope > .row').forEach(function (r, i) { if (r.hidden) return;
        add(r, { src: 'price', g: g, i: i, t: txt(q(r, '.t')), price: cents(txt(q(r, '.p'))) }, function (b) { b.style.gridColumn = '1/-1'; b.style.justifySelf = 'start'; r.appendChild(b); }); }); });
      qa(document, '.cards > .card').forEach(function (c, i) { if (c.hidden) return; var pe = q(c, '.price');
        add(c, { src: 'card', i: i, t: txt(q(c, 'h3')), price: cents(txt(pe)) }, function (b) { (pe || c).insertAdjacentElement('afterend', b); }); });
    };
    function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
    function ready() {
      qa(document, 'form').forEach(function (f) { if (!SKIP[f.id]) prepare(f); });
      document.addEventListener('submit', function (e) {
        var form = e.target;
        if (!form || form.tagName !== 'FORM' || SKIP[form.id] || form.closest('.cs-lead')) return;
        e.preventDefault(); e.stopPropagation();
        if (typeof form.reportValidity === 'function' && !form.reportValidity()) return;
        open(form);
      }, true);
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', ready); else ready();
  }
})();
