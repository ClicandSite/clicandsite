from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
import subprocess
F = TTFont('/tmp/young.ttf'); GS = F.getGlyphSet(); CM = F.getBestCmap(); UPM = 1000
ENCRE, OCRE, CREME, BLEU, ROUGE = "#13324b", "#e0a243", "#f6efe2", "#2a5ca8", "#c8323c"

def text_path(s, size, x, y):
    """Texte -> chemins SVG, ligne de base en y. Retourne (liste de (d, char), largeur)."""
    sc = size / UPM; out = []; cx = 0
    for ch in s:
        g = CM[ord(ch)]; pen = SVGPathPen(GS)
        GS[g].draw(pen)
        out.append((f'<path transform="translate({x+cx*sc:.2f} {y:.2f}) scale({sc:.5f} {-sc:.5f})" d="{pen.getCommands()}"', ch))
        cx += F['hmtx'][g][0]
    return out, cx * sc

def glyph_box(ch):
    bp = BoundsPen(GS); GS[CM[ord(ch)]].draw(bp); return bp.bounds

def stamp(x, y, s, mid, paper=CREME):
    """Timbre carré perforé, côté s, en (x,y)."""
    r = s * 0.045; n = 9; step = s / n
    holes = "".join(f'<circle cx="{x+step*(i+.5):.2f}" cy="{yy:.2f}" r="{r:.2f}"/>' for i in range(n) for yy in (y, y+s)) + \
            "".join(f'<circle cx="{xx:.2f}" cy="{y+step*(i+.5):.2f}" r="{r:.2f}"/>' for i in range(n) for xx in (x, x+s)) + \
            "".join(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r*1.6:.2f}"/>' for cx in (x, x+s) for cy in (y, y+s))
    m = s * 0.11; inner = s - 2*m
    # esperluette centrée
    x0, y0, x1, y1 = glyph_box('&'); size = inner * 0.86; sc = size / UPM
    gx = x + s/2 - (x0 + x1)/2*sc; gy = y + m + inner*0.47 + (y1 - y0)/2*sc - y1*sc + (y1-y0)*sc*0.0
    gy = y + s/2 + ((y1 + y0)/2)*sc - s*0.045
    amp, _ = text_path('&', size, gx, gy)
    band_h = s * 0.055; by = y + s - m - band_h*1.6; bw = inner * 0.5; bx = x + s/2 - bw/2
    return f'''<defs><mask id="perf{mid}"><rect x="{x-1}" y="{y-1}" width="{s+2}" height="{s+2}" fill="#fff"/><g fill="#000">{holes}</g></mask></defs>
<g mask="url(#perf{mid})"><rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{paper}"/></g>
<rect x="{x+m}" y="{y+m}" width="{inner}" height="{inner}" fill="{ENCRE}" rx="{s*0.02}"/>
<g fill="{OCRE}">{"".join(p + "/>" for p, _ in amp)}</g>
<rect x="{bx:.2f}" y="{by:.2f}" width="{bw/3:.2f}" height="{band_h:.2f}" fill="{BLEU}"/><rect x="{bx+bw/3:.2f}" y="{by:.2f}" width="{bw/3:.2f}" height="{band_h:.2f}" fill="#fff"/><rect x="{bx+2*bw/3:.2f}" y="{by:.2f}" width="{bw/3:.2f}" height="{band_h:.2f}" fill="{ROUGE}"/>'''

def svg(w, h, body): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" width="{w:.0f}" height="{h:.0f}">{body}</svg>'

# 1. Icône carrée
open('icone.svg','w').write(svg(512, 512, stamp(16, 16, 480, 'a')))

# 2. Logo horizontal (texte clair ou foncé)
def horiz(textcol, name, paper=CREME):
    H = 120; s = 104; body = stamp(8, 8, s, name, paper)
    parts, w = text_path('Clic&Site', 74, s + 34, 86)
    txt = "".join(p + f' fill="{OCRE if ch == "&" else textcol}"/>' for p, ch in parts)
    open(name, 'w').write(svg(s + 34 + w + 10, H, body + txt))
horiz('#ffffff', 'logo-clair.svg'); horiz(ENCRE, 'logo-fonce.svg', '#d9c6a0')
for f, wpx in (('icone.svg', 512), ('logo-clair.svg', 800), ('logo-fonce.svg', 800)):
    subprocess.run(['rsvg-convert', '-w', str(wpx), f, '-o', f.replace('.svg', '.png')], check=True)
# favicon 64
subprocess.run(['rsvg-convert', '-w', '64', 'icone.svg', '-o', 'favicon-64.png'], check=True)
