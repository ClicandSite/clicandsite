"""12/11/2026 (Claude, audit) : sort les photos base64 des modèles (3-5 Mo par page) en fichiers WebP
partagés dans modeles/img/<empreinte>.webp. Adresse absolue (https://mycreativesite.fr/…) car les sites
clients générés par cs-build-site.mjs reprennent le HTML du modèle tel quel.
Usage : python3 scripts/externalize_images.py [modeles/xxx.html ...]   (sans argument : tous les modèles)"""
import base64, glob, hashlib, io, os, re, sys
from PIL import Image
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(REPO, 'modeles', 'img'); os.makedirs(IMG, exist_ok=True)
URL = 'https://mycreativesite.fr/modeles/img/'
RX = re.compile(r'data:image/(?:jpeg|png|webp);base64,([A-Za-z0-9+/=]+)')

def store(b64):
    raw = base64.b64decode(b64)
    h = hashlib.sha1(raw).hexdigest()[:16]
    p = os.path.join(IMG, h + '.webp')
    if not os.path.exists(p):
        im = Image.open(io.BytesIO(raw)).convert('RGB')
        im.save(p, 'WEBP', quality=80, method=6)
    return URL + h + '.webp'

def run(f):
    s = open(f, encoding='utf-8').read()
    out, n = RX.subn(lambda m: store(m.group(1)), s)
    if n:
        open(f, 'w', encoding='utf-8').write(out)
    return n, len(s), len(out)

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob(os.path.join(REPO, 'modeles', '*.html')))
    for f in files:
        n, a, b = run(f)
        print(f'{os.path.basename(f)}: {n} photos, {a // 1024} Ko -> {b // 1024} Ko')
