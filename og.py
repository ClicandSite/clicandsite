"""Images de partage (WhatsApp, Facebook, Google Discover) 1200x630, style carte postale du site."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "node_modules", "@fontsource")
SERIF = os.path.join(FONTS, "young-serif", "files", "young-serif-latin-400-normal.woff")
SANS = os.path.join(FONTS, "public-sans", "files", "public-sans-latin-700-normal.woff")
COULEURS = {"azur": "#2a78ad", "pin": "#2e5b45", "ocre": "#93600f", "encre": "#13324b"}
OCRE, ENCRE = "#e0a243", "#13324b"
W, H = 1200, 630


def _wrap(draw, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def make(path, titre, sous_titre, timbre, couleur="azur"):
    im = Image.new("RGB", (W, H), COULEURS.get(couleur, COULEURS["azur"]))
    d = ImageDraw.Draw(im, "RGBA")
    # lignes obliques comme sur le site
    for x in range(-H, W + H, 34):
        d.line([(x, H), (x + H * 0.18, 0)], fill=(255, 255, 255, 18), width=3)
    # timbre perforé
    sx, sy, sw, sh = W - 210, 50, 150, 180
    d.rectangle([sx, sy, sx + sw, sy + sh], fill="white")
    bg = COULEURS.get(couleur, COULEURS["azur"])
    for i in range(0, sw + 1, 15):
        for y in (sy, sy + sh):
            d.ellipse([sx + i - 5, y - 5, sx + i + 5, y + 5], fill=bg)
    for j in range(0, sh + 1, 15):
        for x in (sx, sx + sw):
            d.ellipse([x - 5, sy + j - 5, x + 5, sy + j + 5], fill=bg)
    d.rectangle([sx + 14, sy + 14, sx + sw - 14, sy + sh - 14], outline=OCRE, width=3)
    fs = ImageFont.truetype(SERIF, 64 if len(timbre) <= 2 else 40)
    tw = d.textlength(timbre, font=fs)
    d.text((sx + (sw - tw) / 2, sy + sh / 2 - (36 if len(timbre) <= 2 else 24)), timbre, font=fs, fill=ENCRE)
    # marque
    fb = ImageFont.truetype(SERIF, 44)
    d.text((64, 52), "Clic", font=fb, fill="white")
    x = 64 + d.textlength("Clic", font=fb)
    d.text((x, 52), "&", font=fb, fill=OCRE)
    x += d.textlength("&", font=fb)
    d.text((x, 52), "Site", font=fb, fill="white")
    # titre
    size = 104
    while True:
        ft = ImageFont.truetype(SERIF, size)
        lines = _wrap(d, titre, ft, W - 140)
        fits = all(d.textlength(l, font=ft) <= W - 140 for l in lines)
        # la 1re ligne ne doit pas passer sous le timbre
        first_ok = d.textlength(lines[0], font=ft) <= W - 330 or len(lines) <= 2
        if (len(lines) <= 3 and fits and first_ok) or size <= 48:
            break
        size -= 8
    lh = int(size * 1.05)
    fsub = ImageFont.truetype(SANS, 34)
    sub = _wrap(d, sous_titre, fsub, W - 140)[:2]
    y = H - 70 - len(sub) * 44 - 24 - len(lines) * lh
    for l in lines:
        d.text((64, y), l, font=ft, fill="white")
        y += lh
    y += 24
    for l in sub:
        d.text((64, y), l, font=fsub, fill=(255, 255, 255, 225))
        y += 44
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.save(path, "JPEG", quality=86, optimize=True, progressive=True)
