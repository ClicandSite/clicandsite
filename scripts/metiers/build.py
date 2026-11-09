import re, json, html, base64, io, os, sys, subprocess, concurrent.futures as cf
from PIL import Image
sys.path.insert(0, '/tmp/nm')
from trades import T

REPO = '/home/claude/mycreativesite'
SRC = open(f'{REPO}/modeles/veterinaire.html').read()
IMGD = '/tmp/nm/full'; os.makedirs(IMGD, exist_ok=True)
e = lambda s: html.escape(str(s), quote=True)

def fetch(i, w):
    if isinstance(i, str): return i  # photo locale (ex. voiture d'auto-école retouchée)
    p = f'{IMGD}/{i}_{w}.jpg'
    if not os.path.exists(p) or os.path.getsize(p) < 3000:
        subprocess.run(['curl', '-s', '-m', '60', '-o', p, f'https://images.pexels.com/photos/{i}/pexels-photo-{i}.jpeg?auto=compress&cs=tinysrgb&w={w}'], check=True)
    return p

def datauri(i, hero):
    W, H = (1300, 866) if hero else (800, 533)
    im = Image.open(fetch(i, 1600 if hero else 1000)).convert('RGB')
    r = W / H
    if im.width / im.height > r:  # trop large
        nw = int(im.height * r); x = (im.width - nw) // 2; im = im.crop((x, 0, x + nw, im.height))
    else:
        nh = int(im.width / r); y = int((im.height - nh) * 0.3); im = im.crop((0, y, im.width, y + nh))
    im = im.resize((W, H), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=70, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

BASE_SLOTS = ['g1', 'g16', 'g18', 'g6', 'g4', 'g7', 'g9', 'c3', 'g5', 'c2', 'g11', 'c1', 'c4']
STYLE_SLOTS = ['g1', 'g16', 'g18', 'g6']
STYLES = ['luxe', 'riviera', 'chaleureux', 'audacieux']
CARD_SLOTS = ['g7', 'g9', 'c3', 'g5', 'c2', 'g11', 'c1', 'c4']

def plan(t):
    H, P = t['H'], t['P']
    base = {'g20': (H[0], True)}
    for s, i in zip(BASE_SLOTS, P): base[s] = (i, False)
    extra = P[len(BASE_SLOTS):] + P[:len(BASE_SLOTS)]
    sty = {}; k = 0
    for n, st in enumerate(STYLES):
        sty[st] = {'g20': (H[n + 1], True)}
        for s in STYLE_SLOTS:
            # jamais la même photo que la base pour ce créneau
            while extra[k % len(extra)] == base[s][0]: k += 1
            sty[st][s] = (extra[k % len(extra)], False); k += 1
    return base, sty

DATE = {'fleuriste': ('Retrait ou livraison le', 'datetime-local', '2027-01-15T10:30'), 'traiteur': ("Date de l'événement", 'date', '2027-06-12'),
        'nautisme': ('Date', 'date', '2027-07-15'), 'photographe': ('Date souhaitée', 'date', '2027-06-12')}

def fiche(it):
    d = {'desc': it[4], 'feats': '\n'.join(it[5]), 'photos': []}
    return e(json.dumps(d, ensure_ascii=False))

def body(k, t):
    o = []
    nav = ''.join(f'\n      <a class="l" href="{h}">{e(l)}</a>' for h, l in t['nav'])
    o.append(f'''<header class="top">
  <div class="wrap">
    <div class="logo">{e(t['logo'])}</div>
    <nav class="nav">{nav}
      <a class="btn sm" href="#rdv">{e(t['navbtn'])}</a>
    </nav>
  </div>
</header>

<div class="photo hero pimg g20">
  <div class="wrap">
    <span class="kicker">{e(t['kicker'])}</span>
    <h1>{e(t['h1'])}</h1>
    <p>{e(t['lead'])}</p>
  </div>
</div>
''')
    f1, f2 = t['form'][0], t['form'][1]
    sel = lambda i, lab, opts: f'<div class="f"><label for="b-{i}">{e(lab)}</label><select id="b-{i}">' + ''.join(('<option selected>' if n == 0 else '<option>') + e(x) + '</option>' for n, x in enumerate(opts)) + '</select></div>'
    dl, dt, dv = DATE.get(k, ('Jour et heure', 'datetime-local', '2027-01-15T10:30'))
    o.append(f'''<div class="wrap booker" id="rdv">
  <form class="bk garage" id="bookform">
    {sel('type', f1[0], f1[1])}
    {sel('who', f2[0], f2[1])}
    <div class="f"><label for="b-date">{e(dl)}</label><input id="b-date" type="{dt}" value="{dv}"></div>
    <button class="btn" type="submit">{e(t['btn'])}</button>
    <div class="ok" id="ok" hidden>{e(t['ok'])}</div>
  </form>
</div>

<div class="wrap stats">
''' + ''.join(f'  <div class="stat"><b>{e(a)}</b><span>{e(b)}</span></div>\n' for a, b in t['stats']) + '</div>\n')
    cards = ''.join(f'      <div class="card"><div class="photo pimg {s}"></div><h3>{e(h)}</h3><p>{e(p)}</p><span class="price">{e(pr)}</span></div>\n' for s, (h, p, pr) in zip(['g1', 'g16', 'g18'], t['svc']))
    o.append(f'''
<section id="{t['sec_id']}">
  <div class="wrap">
    <div class="head"><h2>{e(t['sec_h'])}</h2><p>{e(t['sec_p'])} <span class="swipe">Glissez pour voir →</span></p></div>
    <div class="cards">
{cards}    </div>
  </div>
</section>
''')
    opts = ''.join(f'<option>{e(c)}</option>' for c in t['cats'])
    arts = ''
    for s, it in zip(CARD_SLOTS, t['items']):
        meta = ''.join(f'<span>{e(m)}</span>' for m in it[2])
        arts += f'      <article class="car" data-fiche="{fiche(it)}" data-type="{e(it[0])}"><div class="photo pimg {s}"><span class="chip on">{e(it[0])}</span></div><h3>{e(it[1])}</h3><div class="meta">{meta}</div><div class="cbot"><span class="prx">{e(it[3])}</span><a class="mini" href="#rdv">{e(t["navbtn"])}</a></div></article>\n'
    o.append(f'''
<section style="padding-top:0" id="carte">
  <div class="wrap">
    <div class="head"><h2>{e(t['cat_h'])}</h2><p>{e(t['cat_p'])}</p></div>
    <div class="vfilters" style="grid-template-columns:minmax(0,1fr);max-width:280px">
      <div class="f"><label for="r-type">{e(t['cat_lbl'])}</label><select id="r-type"><option value="">Tout voir</option>{opts}</select></div>
    </div>
    <p class="vcount" id="vcount" aria-live="polite"></p>
    <div class="vgrid" id="vgrid">
{arts}    </div>
    <p class="note" id="vempty" hidden>Rien dans cette catégorie pour le moment. Appelez-nous, on vous oriente.</p>
    <p class="note">Exemples. Le professionnel ajoute, retire et modifie ses fiches depuis son espace, en quelques secondes.</p>
  </div>
</section>
''')
    tid = 'honoraires' if t.get('info') else 'tarifs'
    grp = ''
    for n, (h, rows) in enumerate(t['tar']):
        grp += f'    <h3 style="margin:{6 if n == 0 else 22}px 0 10px">{e(h)}</h3>\n    <div class="prices">\n' + ''.join(f'      <div class="row"><span class="t">{e(a)}</span><span class="d">{e(b)}</span><span class="p">{e(c)}</span></div>\n' for a, b, c in rows) + '    </div>\n'
    o.append(f'''
<section style="padding-top:0" id="{tid}">
  <div class="wrap">
    <div class="head"><h2>{'Honoraires' if t.get('info') else 'Tarifs'}</h2><p>{e(t['tar_p'])}</p></div>
{grp}    <p class="note">{e(t['tar_note'])}</p>
  </div>
</section>
''')
    lst = ''.join(f'        <div><span>{e(a)}</span><span>{e(b)}</span></div>\n' for a, b in t['lieu'])
    o.append(f'''
<section style="padding-top:0" id="lieu">
  <div class="wrap lieu">
    <div class="photo pimg g6"></div>
    <div>
      <h2>{e(t['lieu_h'])}</h2>
      <div class="list">
{lst}      </div>
    </div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap team">
    <div class="photo pimg g4"></div>
    <div>
      <h2>{e(t['team_h'])}</h2>
      <p style="color:var(--muted);margin-top:14px;max-width:52ch">{e(t['team_p'])}</p>
    </div>
  </div>
</section>
''')
    if t.get('info'):
        rv = ''.join(f'      <div class="rev info"><span class="s" style="letter-spacing:0">{e(a)}</span><p>{e(b)}</p></div>\n' for a, b in t['infos'])
        o.append(f'''
<style>.rev.info::before{{content:none!important}}:root[data-rv="c"] .rev.info{{padding-top:22px}}</style>
<section style="padding-top:0" id="pratique">
  <div class="wrap">
    <div class="head"><h2>Informations pratiques</h2><p>Pour préparer votre rendez-vous.</p></div>
    <div class="reviews">
{rv}    </div>
  </div>
</section>
''')
    else:
        rv = ''.join(f'      <div class="rev"><span class="s">★★★★★</span><p>{e(a)}</p><span class="who">{e(b)}</span></div>\n' for a, b in t['rev'])
        o.append(f'''
<section style="padding-top:0" id="avis">
  <div class="wrap">
    <div class="head"><h2>Avis clients</h2><p>Exemples, remplacés par les avis Google publiés pour l'entreprise.</p></div>
    <div class="reviews">
{rv}    </div>
  </div>
</section>
''')
    hrs = ''.join(f'        <div class="hrow"><span>{e(a)}</span><span>{e(b)}</span></div>\n' for a, b in t['hours'])
    short = t['logo'].title() if t['logo'].isupper() else t['logo']
    o.append(f'''
<section style="padding-top:0" id="infos">
  <div class="wrap hours">
    <div>
      <h2>Horaires</h2>
      <div class="list">
{hrs}      </div>
    </div>
    <div>
      <div class="map">
        <svg viewBox="0 0 400 250" aria-hidden="true">
          <rect width="400" height="250" fill="#dfe5dc"/>
          <path d="M0 180 Q120 160 200 200 T400 210 L400 250 L0 250Z" fill="#b5d1db"/>
          <path d="M0 100 L400 120" stroke="#ffffff" stroke-width="10"/>
          <path d="M170 0 L190 250" stroke="#ffffff" stroke-width="6"/>
          <circle cx="210" cy="112" r="12" fill="#5b7b5a"/><circle cx="210" cy="112" r="4.5" fill="#fff"/>
        </svg>
        <span class="ph">{e(t['brand'])}</span>
      </div>
      <div class="addr"><span class="note" style="margin:0">Adresse</span><span class="v">{e(t['addr'])}</span></div>
    </div>
  </div>
</section>

<div class="cta" id="contact">
  <div class="wrap">
    <div><h2>{e(t['cta_h'])}</h2><p>{e(t['cta_p'])}</p></div>
    <div class="cinfo">
      <div><span class="l">Téléphone</span><span class="v">{e(t['phone'])}</span></div>
      <div><span class="l">Email</span><span class="v">{e(t['email'])}</span></div>
      <a class="btn" href="#rdv">{e(t['cta_btn'])}</a>
    </div>
  </div>
</div>

<div class="mbar"><a class="btn" href="#rdv">{e(t['mbar'][0])}</a><a class="btn wa" href="#contact" style="background:var(--soft);border-color:var(--line);color:var(--ink)">{e(t['mbar'][1])}</a></div>

<footer><div class="wrap"><span>© 2026 {e(t['brand'])} · {e(t['foot'])}</span>''')
    return ''.join(o)

BRAND = {'autoecole': 'Auto-école du Port', 'coach': 'Studio Mouvement', 'photographe': 'Léa Duval Photographie', 'toiletteur': "L'Atelier des Pattes",
         'fleuriste': 'Fleurs de Mai', 'traiteur': 'Maison Émile Traiteur', 'nautisme': 'Cap Bleu Location', 'kine': 'Cabinet du Parc', 'dentiste': 'Cabinet dentaire des Arcades'}

def build(k):
    t = T[k]; t['brand'] = BRAND[k]
    a = SRC.index('<header class="top">'); fs = SRC.index('<footer><div class="wrap"><span>'); fe = SRC.index('</span>', fs)
    pre, post = SRC[:a], SRC[fe:]
    pre = pre.replace('data-trade="veterinaire"', f'data-trade="{k}"', 1).replace('<title>Modèle Vétérinaire MyCreativeSite</title>', f'<title>{e(t["title"])}</title>', 1)
    base, sty = plan(t)
    with cf.ThreadPoolExecutor(12) as ex:
        need = {v for v in base.values()} | {v for s in sty.values() for v in s.values()}
        uris = dict(zip(need, ex.map(lambda v: datauri(*v), need)))
    def sub(m):
        st, slot = m.group(1), m.group(2)
        v = (sty[st] if st else base).get(slot)
        if not v: raise SystemExit(f'créneau inconnu {st} {slot}')
        return f'{m.group(0)[:m.group(0).index("{")]}{{--img:url({uris[v]})}}'
    pre, n = re.subn(r'(?:\:root\[data-p="(\w+)"\] )?\.([gc]\d+)\{--img:url\(data:image/[a-z]+;base64,[A-Za-z0-9+/=]+\)\}', sub, pre)
    assert n == 34, n
    w1, w2 = t['words']
    post = post.replace("n+(n>1?' soins':' soin')", f"n+(n>1?' {w1}':' {w2}')", 1)
    assert w1 in post or w1 == 'soins'
    out = pre + body(k, t) + post
    open(f'{REPO}/modeles/{k}.html', 'w').write(out)
    print(k, len(out) // 1024, 'Ko')

for k in (sys.argv[1:] or T):
    build(k)
