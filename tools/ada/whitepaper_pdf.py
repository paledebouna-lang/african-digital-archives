"""Print layout for the white papers (rendered to PDF by tools/shoot_pdf.js)."""
import os

from .icons import LOGO
from .mockups import FONT
from .whitepapers import WHITEPAPERS

CSS = """@font-face{font-family:Inter;src:url(file://__FONT__) format("woff2");font-weight:100 900}
@page{size:A4;margin:22mm 20mm 22mm 20mm}
*{box-sizing:border-box}
body{margin:0;font:10.5pt/1.6 Inter,sans-serif;color:#363A40}
.cover{height:250mm;background:#0A1541;color:#C3CBE6;margin:0;border-radius:6px;padding:22mm 18mm;display:flex;flex-direction:column;page-break-after:always;position:relative;overflow:hidden}
.cover::before{content:"";position:absolute;right:-60mm;top:-60mm;width:180mm;height:180mm;border-radius:50%;background:radial-gradient(closest-side,rgba(0,110,239,.5),rgba(0,110,239,0))}
.cover .brand{display:flex;align-items:center;gap:12px;color:#fff;font-weight:800;font-size:15pt;position:relative}
.cover .brand svg{width:44px;height:44px}
.cover .brand small{display:block;font-size:9pt;font-weight:500;color:#AEB8DA}
.cover .kind{margin-top:auto;color:#6FB1FF;text-transform:uppercase;letter-spacing:.16em;font-weight:700;font-size:9.5pt;position:relative}
.cover h1{color:#fff;font-size:34pt;line-height:1.08;letter-spacing:-.03em;margin:8px 0 14px;position:relative}
.cover p{font-size:13pt;max-width:140mm;position:relative;margin:0}
.cover .foot{margin-top:24mm;font-size:9pt;color:#8E98BD;position:relative}
.toc{page-break-after:always}
.toc h2{margin-top:0}
.toc ol{padding-left:18px;font-size:11.5pt;line-height:2}
h2{color:#0A1541;font-size:16pt;letter-spacing:-.02em;margin:22px 0 8px;page-break-after:avoid}
h2 .n{color:#006EEF;margin-right:8px}
p,li{orphans:3;widows:3}
table{width:100%;border-collapse:collapse;margin:10px 0 14px;font-size:9.5pt;page-break-inside:avoid}
th{background:#0A1541;color:#fff;text-align:left;padding:7px 9px}
td{border-bottom:1px solid #E1E5EE;padding:7px 9px;vertical-align:top}
ul.is-style-check{list-style:none;padding:0}
ul.is-style-check li{padding-left:22px;position:relative;margin-bottom:5px}
ul.is-style-check li::before{content:"✓";position:absolute;left:0;color:#006EEF;font-weight:700}
strong{color:#161C2D}
.end{margin-top:24px;border-top:2px solid #0A1541;padding-top:12px;font-size:9.5pt;color:#6C728D;page-break-inside:avoid}
"""


def html(w):
    secs = "".join(f'<h2><span class="n">{i:02d}</span>{h}</h2>{b}' for i, (h, b) in enumerate(w["sections"], 1))
    toc = "".join(f"<li>{h}</li>" for h, _ in w["sections"])
    return f"""<!doctype html><html lang="fr"><meta charset="utf-8"><title>{w['title']}</title><style>{CSS.replace('__FONT__', FONT)}</style>
<section class="cover"><div class="brand">{LOGO}<span>ADA<small>African Digital Archives</small></span></div>
<div class="kind">Livre blanc</div><h1>{w['title']}</h1><p>{w['subtitle']}</p>
<div class="foot">African Digital Archives · Abidjan, Côte d'Ivoire · Édition octobre 2026</div></section>
<section class="toc"><h2>Sommaire</h2><ol>{toc}</ol>
<p style="margin-top:20px;color:#6C728D">{w['summary']}</p>
<p style="color:#6C728D;font-size:9.5pt">Ce document a une valeur informative et ne constitue pas un conseil juridique. Chaque organisation doit faire valider son dispositif par un juriste selon son secteur.</p></section>
{secs}
<div class="end">African Digital Archives (ADA) accompagne les organisations africaines dans la transformation de leurs archives physiques et numériques. Diagnostic, audit, numérisation, plateforme ARCHIVA360 : paledebouna-lang.github.io/african-digital-archives</div>
</html>"""


def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    jobs = []
    for w in WHITEPAPERS:
        p = os.path.join(out_dir, "wp-" + w["slug"] + ".html")
        with open(p, "w", encoding="utf-8") as f:
            f.write(html(w))
        jobs.append({"html": p, "pdf": w["slug"] + ".pdf", "title": w["title"]})
    return jobs
