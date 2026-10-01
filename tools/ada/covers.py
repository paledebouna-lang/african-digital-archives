"""Illustrated covers (blog featured images, Open Graph image, favicons)."""
import os

from .icons import icon, LOGO
from .mockups import FONT

BASE = """@font-face{font-family:Inter;src:url(file://%s) format("woff2");font-weight:100 900}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:Inter,sans-serif;overflow:hidden}""" % FONT


def cover(ic, label, accent="#006EEF", variant=0):
    docs = ""
    for i in range(5):
        x = 640 + i * 70 + (variant * 13 % 40)
        y = 150 + (i % 2) * 60 - variant * 7
        r = -8 + i * 4
        docs += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:210px;height:280px;border-radius:8px;'
                 f'background:rgba(255,255,255,{.05 + i*.025});border:1px solid rgba(255,255,255,.14);transform:rotate({r}deg);padding:22px">'
                 + "".join(f'<div style="height:7px;border-radius:4px;background:rgba(255,255,255,.16);margin-bottom:12px;width:{90 - (j*17+i*9) % 45}%"></div>' for j in range(8))
                 + "</div>")
    return f'''<style>{BASE}body{{width:1200px;height:675px;background:#0A1541;position:relative}}
.g{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px);background-size:48px 48px}}
.glow{{position:absolute;width:900px;height:900px;border-radius:50%;left:{300 + variant*40}px;top:-300px;background:radial-gradient(closest-side,rgba(0,110,239,.5),rgba(0,110,239,0))}}
.ic{{position:absolute;left:96px;top:190px;width:190px;height:190px;border-radius:40px;background:{accent};display:grid;place-items:center;color:#fff;box-shadow:0 30px 60px rgba(0,0,0,.3)}}
.ic svg{{width:96px;height:96px;stroke-width:1.4}}
.lb{{position:absolute;left:96px;top:430px;color:#fff;font-weight:700;font-size:30px;letter-spacing:-.02em}}
.lb small{{display:block;color:#6FB1FF;font-size:16px;text-transform:uppercase;letter-spacing:.14em;margin-bottom:10px}}
</style><div class="g"></div><div class="glow"></div>{docs}<div class="ic">{icon(ic)}</div><div class="lb"><small>ADA · Ressources</small>{label}</div>'''


def og():
    return f'''<style>{BASE}body{{width:1200px;height:630px;background:#0A1541;color:#fff;position:relative;padding:90px}}
.glow{{position:absolute;width:1000px;height:1000px;border-radius:50%;right:-400px;top:-420px;background:radial-gradient(closest-side,rgba(0,110,239,.55),rgba(0,110,239,0))}}
.l{{display:flex;align-items:center;gap:18px;position:relative}}.l svg{{width:72px;height:72px}}
.l b{{font-size:40px;letter-spacing:-.02em}}.l span{{display:block;font-size:18px;color:#AEB8DA;font-weight:500}}
h1{{position:relative;font-size:62px;letter-spacing:-.035em;line-height:1.08;margin-top:70px;max-width:900px}}
h1 em{{font-style:normal;color:#6FB1FF}}p{{position:relative;margin-top:22px;font-size:24px;color:#C3CBE6}}</style>
<div class="glow"></div><div class="l">{LOGO}<div><b>ADA</b><span>African Digital Archives</span></div></div>
<h1>Préserver aujourd'hui. <em>Transmettre demain.</em></h1><p>Gestion documentaire, archivage et préservation pour l'Afrique.</p>'''


def favicon(size):
    return f'<style>{BASE}body{{width:{size}px;height:{size}px;background:transparent}}svg{{width:{size}px;height:{size}px;display:block}}</style>{LOGO}'


COVERS = [
    ("cover-ged-sae-records", "folder", "GED, SAE, records management"),
    ("cover-regle-3-2-1", "hard-drive", "La règle 3-2-1"),
    ("cover-cadre-ivoirien", "scale", "Le cadre ivoirien"),
    ("cover-blockchain-preuve", "fingerprint", "Empreinte et preuve"),
    ("cover-numerisation-mairie", "scan", "Numériser 3 millions de pages"),
    ("cover-durees-conservation", "hourglass", "Durées de conservation"),
    ("cover-oais", "layers", "Préserver pour 30 ans"),
    ("cover-ia-documentaire", "sparkles", "IA documentaire"),
    ("cover-guide-plan-classement", "workflow", "Construire un plan de classement"),
    ("cover-guide-metadonnees", "database", "Les métadonnées essentielles"),
]


def app_icon(size, safe=False):
    """ARCHIVA360 home-screen icon (opaque, so it also works as a maskable / Apple touch icon)."""
    k = size / 512
    tile = (250 if safe else 300) * k
    return f'''<style>{BASE}body{{width:{size}px;height:{size}px;display:grid;place-items:center;
background:radial-gradient(circle at 50% 30%,#1B3A9E 0%,#0A1541 70%)}}
.t{{width:{tile}px;height:{tile}px;border-radius:{tile*.24}px;background:linear-gradient(150deg,#2F8BFF,#006EEF 60%,#0057C2);
display:grid;place-items:center;box-shadow:0 {18*k}px {44*k}px rgba(0,0,0,.35);position:relative}}
.t b{{color:#fff;font-weight:800;font-size:{tile*.62}px;letter-spacing:-.04em;line-height:1;margin-top:-{tile*.06}px}}
.t i{{position:absolute;bottom:{tile*.1}px;left:0;right:0;text-align:center;color:#CFE2FD;font-style:normal;font-weight:700;font-size:{tile*.13}px;letter-spacing:.08em}}
</style><div class="t"><b>A</b><i>360</i></div>'''


APP_ICONS = [("archiva360-app-192.png", 192, False), ("archiva360-app-512.png", 512, False),
             ("archiva360-app-maskable-512.png", 512, True), ("archiva360-app-180.png", 180, False)]


def build_app_icons(out_dir):
    jobs = []
    for name, size, safe in APP_ICONS:
        p = os.path.join(out_dir, name + ".html")
        with open(p, "w", encoding="utf-8") as f:
            f.write("<!doctype html><meta charset=utf-8>" + app_icon(size, safe))
        jobs.append({"html": p, "png": name, "w": size, "h": size, "dpr": 1})
    return jobs


def build(out_dir):
    jobs = []
    for i, (name, ic, label) in enumerate(COVERS):
        p = os.path.join(out_dir, name + ".html")
        with open(p, "w", encoding="utf-8") as f:
            f.write("<!doctype html><meta charset=utf-8>" + cover(ic, label, variant=i))
        jobs.append({"html": p, "png": name + ".png", "w": 1200, "h": 675, "dpr": 1})
    p = os.path.join(out_dir, "og.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write("<!doctype html><meta charset=utf-8>" + og())
    jobs.append({"html": p, "png": "og-ada.png", "w": 1200, "h": 630, "dpr": 1})
    for s in (32, 180, 192):
        p = os.path.join(out_dir, f"fav{s}.html")
        with open(p, "w", encoding="utf-8") as f:
            f.write("<!doctype html><meta charset=utf-8>" + favicon(s))
        jobs.append({"html": p, "png": f"cropped-ada-icon-{s}x{s}.png", "w": s, "h": s, "dpr": 1, "transparent": True})
    jobs += build_app_icons(out_dir)
    return jobs
