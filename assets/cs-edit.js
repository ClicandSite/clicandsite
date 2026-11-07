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
      var go = function () { apply(document, c); if (c.shop) initShop(slug, c.shop); };
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
      '.cs-lead .cs-err{color:#b42318;font-size:.86rem;margin-top:10px}.cs-lead .cs-small{font-size:.76rem;color:#7a7f8e;margin:12px 0 0}';
    var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    function bizName() { return txt(q(document, 'header.top .logo')) || document.title.split(/[·|–-]/)[0].trim(); }
    function open(form) {
      var data = collect(form), kind = kindOf(form);
      var wrap = document.createElement('div'); wrap.className = 'cs-lead'; wrap.setAttribute('role', 'dialog'); wrap.setAttribute('aria-modal', 'true');
      wrap.innerHTML = '<form class="cs-box" novalidate><h3>Vos coordonnées</h3><p>Pour que ' + esc(bizName()) + ' vous réponde.</p>' +
        '<label for="cs-n">Nom</label><input id="cs-n" autocomplete="name" required maxlength="120">' +
        '<label for="cs-t">Téléphone</label><input id="cs-t" type="tel" autocomplete="tel" inputmode="tel" maxlength="30">' +
        '<label for="cs-e">E-mail</label><input id="cs-e" type="email" autocomplete="email" maxlength="160">' +
        '<label for="cs-m">Message (facultatif)</label><textarea id="cs-m" maxlength="2000"></textarea>' +
        '<input class="cs-hp" id="cs-w" tabindex="-1" autocomplete="off" aria-hidden="true">' +
        '<div class="cs-err" role="alert" hidden></div>' +
        '<div class="cs-act"><button type="button" class="cs-cancel">Annuler</button><button class="btn" type="submit">Envoyer ma demande</button></div>' +
        '<p class="cs-small">Vos coordonnées sont transmises uniquement à ' + esc(bizName()) + ' pour répondre à votre demande.</p></form>';
      document.body.appendChild(wrap);
      var f = q(wrap, 'form'), err = q(wrap, '.cs-err');
      if (data.tel) q(wrap, '#cs-t').value = data.tel;
      setTimeout(function () { q(wrap, '#cs-n').focus(); }, 30);
      function close() { wrap.remove(); document.removeEventListener('keydown', onKey); }
      function onKey(e) { if (e.key === 'Escape') close(); }
      document.addEventListener('keydown', onKey);
      q(wrap, '.cs-cancel').onclick = close;
      wrap.addEventListener('click', function (e) { if (e.target === wrap) close(); });
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var n = q(wrap, '#cs-n').value.trim(), t = q(wrap, '#cs-t').value.trim(), m = q(wrap, '#cs-e').value.trim();
        err.hidden = true;
        if (!n) { err.textContent = 'Indiquez votre nom.'; err.hidden = false; return; }
        if (!t && !m) { err.textContent = 'Indiquez un téléphone ou un e-mail pour être recontacté.'; err.hidden = false; return; }
        var b = q(f, '[type="submit"]'); b.disabled = true; b.textContent = 'Envoi…';
        fetch(API + '/rest/v1/rpc/cs_lead_submit', {
          method: 'POST', headers: { 'Content-Type': 'application/json', apikey: KEY },
          body: JSON.stringify({ p_slug: slug, p_kind: kind, p_name: n, p_phone: t, p_email: m, p_message: q(wrap, '#cs-m').value, p_fields: data.fields, p_page: location.pathname, p_hp: q(wrap, '#cs-w').value })
        }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, j: j }; }); }).then(function (r) {
          if (!r.ok) throw new Error((r.j && r.j.message) || 'Envoi impossible');
          close();
          var ok = q(form, '.ok');
          if (!ok) { ok = document.createElement('div'); ok.className = 'ok'; form.appendChild(ok); }
          ok.textContent = 'Merci ' + n + ', votre demande est bien envoyée. ' + bizName() + ' vous recontacte rapidement.';
          ok.hidden = false;
        }).catch(function (x) {
          b.disabled = false; b.textContent = 'Envoyer ma demande';
          err.textContent = (x && x.message && !/fetch/i.test(x.message)) ? x.message : 'La demande n\'est pas partie. Vérifiez votre connexion et réessayez.';
          err.hidden = false;
        });
      });
    }
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
