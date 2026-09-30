"""HTML mockups of the ARCHIVA360 interface, rendered to PNG by tools/shoot.js."""
import os
import random

from .icons import icon

FONT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../wp-content/themes/ada-archives/assets/fonts/inter-latin.woff2"))

CSS = """
@font-face{font-family:Inter;src:url(file://__FONT__) format("woff2");font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
body{font:13px/1.45 Inter,sans-serif;color:#1B2233;background:#F4F6FA;-webkit-font-smoothing:antialiased;width:1280px;height:800px;overflow:hidden}
svg{width:16px;height:16px;flex-shrink:0}
.app{display:grid;grid-template-columns:232px 1fr;height:800px}
.side{background:#0A1541;color:#AEB8DA;padding:18px 14px;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:10px;color:#fff;font-weight:800;font-size:16px;letter-spacing:-.02em;padding:4px 8px 20px}
.brand i{width:30px;height:30px;border-radius:7px;background:#006EEF;display:grid;place-items:center;font-style:normal;font-size:15px}
.org{background:rgba(255,255,255,.06);border-radius:8px;padding:10px 12px;margin-bottom:18px;font-size:12px}
.org b{display:block;color:#fff;font-size:13px}
.nav a{display:flex;align-items:center;gap:11px;padding:8.5px 10px;border-radius:7px;color:#AEB8DA;text-decoration:none;font-weight:500;margin-bottom:1px}
.nav a.on{background:#006EEF;color:#fff}
.nav .sep{font-size:10.5px;text-transform:uppercase;letter-spacing:.1em;color:#6C76A0;margin:16px 10px 6px;font-weight:700}
.nav .n{margin-left:auto;background:rgba(255,255,255,.1);border-radius:10px;padding:1px 7px;font-size:11px}
.side .foot{margin-top:auto;font-size:11px;color:#6C76A0;padding:0 8px}
.main{display:flex;flex-direction:column;min-width:0}
.top{height:60px;background:#fff;border-bottom:1px solid #E1E5EE;display:flex;align-items:center;gap:16px;padding:0 24px}
.search{flex:1;max-width:560px;display:flex;align-items:center;gap:10px;background:#F4F6FA;border:1px solid #E1E5EE;border-radius:8px;padding:9px 14px;color:#6C728D}
.search b{color:#1B2233;font-weight:500}
.top .ic{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;color:#4A5170;position:relative}
.top .ic .dot{position:absolute;top:6px;right:7px;width:8px;height:8px;border-radius:50%;background:#E0655A;border:2px solid #fff}
.me{display:flex;align-items:center;gap:9px;font-weight:600;font-size:12.5px;margin-left:auto}
.av{width:32px;height:32px;border-radius:50%;background:#E6F0FE;color:#006EEF;display:grid;place-items:center;font-weight:700;font-size:12px}
.content{padding:22px 24px;flex:1;overflow:hidden}
h1{font-size:20px;letter-spacing:-.02em;color:#0A1541;margin-bottom:2px}
.sub{color:#6C728D;font-size:12.5px}
.head{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:18px}
.btn{display:inline-flex;align-items:center;gap:7px;background:#006EEF;color:#fff;border-radius:7px;padding:8px 14px;font-weight:600;font-size:12.5px}
.btn.o{background:#fff;color:#0A1541;border:1px solid #D5DAE6}
.btns{display:flex;gap:8px}
.grid{display:grid;gap:14px}
.kpis{grid-template-columns:repeat(4,1fr);margin-bottom:14px}
.box{background:#fff;border:1px solid #E1E5EE;border-radius:10px;padding:16px}
.box h3{font-size:13.5px;color:#0A1541;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between}
.box h3 small{font-weight:500;color:#006EEF;font-size:12px}
.kpi small{color:#6C728D;font-size:12px;display:flex;align-items:center;gap:6px}
.kpi b{display:block;font-size:24px;letter-spacing:-.03em;color:#0A1541;margin:4px 0 2px}
.kpi .up{color:#11875D;font-size:11.5px;font-weight:600}
.kpi .warn{color:#B7791F;font-size:11.5px;font-weight:600}
table{width:100%;border-collapse:collapse}
th{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:#6C728D;text-align:left;padding:8px 10px;border-bottom:1px solid #E1E5EE;font-weight:600}
td{padding:9px 10px;border-bottom:1px solid #EEF1F6;font-size:12.5px;vertical-align:middle}
tr:last-child td{border-bottom:0}
.fi{display:flex;align-items:center;gap:9px;font-weight:500;color:#1B2233}
.ft{width:26px;height:30px;border-radius:4px;display:grid;place-items:center;font-size:8.5px;font-weight:800;color:#fff;flex-shrink:0}
.pdf{background:#D9473A}.doc{background:#2B6CD4}.xls{background:#1E8A4F}.img{background:#8B5CF6}.tif{background:#6C728D}
.tag{display:inline-block;font-size:11px;font-weight:600;padding:2px 8px;border-radius:20px;background:#F4F6FA;color:#4A5170}
.tag.g{background:#E3F4EC;color:#11875D}.tag.b{background:#E6F0FE;color:#0057C2}.tag.a{background:#FBF1DE;color:#A56A12}.tag.r{background:#FBE7E5;color:#B83227}.tag.n{background:#0A1541;color:#fff}
.muted{color:#6C728D}
.bar{height:8px;border-radius:5px;background:#EEF1F6;overflow:hidden}
.bar i{display:block;height:100%;background:#006EEF;border-radius:5px}
.qr{display:grid;grid-template-columns:repeat(21,1fr);width:100%;aspect-ratio:1}
.qr i{background:#0A1541}.qr u{background:transparent}
"""


def qr(seed=7, size=21):
    rnd = random.Random(seed)
    cells = []
    for y in range(size):
        for x in range(size):
            finder = None
            for fx, fy in ((0, 0), (size - 7, 0), (0, size - 7)):
                if fx <= x < fx + 7 and fy <= y < fy + 7:
                    dx, dy = x - fx, y - fy
                    finder = dx in (0, 6) or dy in (0, 6) or (2 <= dx <= 4 and 2 <= dy <= 4)
            if finder is None:
                if (x == 7 or y == 7 or x == size - 8 or y == size - 8) and (x < 8 or y < 8):
                    on = False
                elif x == 6 or y == 6:
                    on = (x + y) % 2 == 0
                else:
                    on = rnd.random() < .48
            else:
                on = finder
            cells.append("<i></i>" if on else "<u></u>")
    return f'<div class="qr">{"".join(cells)}</div>'


def shell(active, content, org="Organisation démo", user="AK"):
    items = [
        ("Tableau de bord", "chart", None), ("Documents", "files", "12 480"), ("Dossiers", "folder", None),
        ("Recherche", "search", None), ("Workflows", "workflow", "7"), ("Courrier", "inbox", "3"),
        ("SEP", "Archivage", None), ("Records management", "hourglass", None), ("Conservation", "clock", None),
        ("Archives physiques", "box", None), ("Coffre-fort", "lock", None),
        ("SEP", "Pilotage", None), ("ARCHIVA AI", "sparkles", None), ("Audit trail", "eye", None),
        ("Conformité", "shield", None), ("Administration", "blocks", None),
    ]
    nav = []
    for t, ic, n in items:
        if t == "SEP":
            nav.append(f'<div class="sep">{ic}</div>')
            continue
        on = ' class="on"' if t == active else ""
        nn = f'<span class="n">{n}</span>' if n else ""
        nav.append(f'<a{on}>{icon(ic)}{t}{nn}</a>')
    return f'''<div class="app"><aside class="side">
<div class="brand"><i>A</i>ARCHIVA360</div>
<div class="org"><span>Espace</span><b>{org}</b></div>
<nav class="nav">{"".join(nav)}</nav>
<div class="foot">v1.4 · Hébergement : Abidjan (CI)</div></aside>
<div class="main"><div class="top">
<div class="search">{icon("search")}<span>Rechercher dans 1 248 530 documents, dossiers et boîtes…</span></div>
<div class="ic">{icon("sparkles")}</div><div class="ic">{icon("inbox")}<span class="dot"></span></div>
<div class="me"><div class="av">{user}</div><div>Awa Koné<div class="muted" style="font-weight:500;font-size:11px">Archiviste</div></div></div>
</div><div class="content">{content}</div></div></div>'''


def ftype(t):
    return f'<span class="ft {t}">{t.upper()}</span>'


def dashboard():
    kpis = [("files", "Documents gérés", "1 248 530", '<span class="up">+ 18 420 ce mois</span>'),
            ("archive", "Archivés (SAE)", "846 212", '<span class="up">67,8 % du fonds</span>'),
            ("clock", "Échéances à 90 jours", "1 250", '<span class="warn">À examiner</span>'),
            ("hard-drive", "Stockage utilisé", "3,4 To", '<span class="muted" style="font-size:11.5px">sur 5 To</span>')]
    k = "".join(f'<div class="box kpi"><small>{icon(i)}{l}</small><b>{v}</b>{s}</div>' for i, l, v, s in kpis)
    bars = [38, 52, 44, 61, 58, 72, 66, 80, 74, 88, 83, 96]
    months = "J F M A M J J A S O N D".split()
    chart = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;flex:1"><div style="width:100%;max-width:26px;height:{b*1.45}px;background:{"#006EEF" if i==8 else "#CFE2FD"};border-radius:4px 4px 0 0"></div><span class="muted" style="font-size:10.5px">{months[i]}</span></div>' for i, b in enumerate(bars))
    rows = [("pdf", "Contrat fournisseur 2026-0045", "Juridique", '<span class="tag b">Actif</span>', "il y a 12 min"),
            ("tif", "Registre des délibérations 1987", "Archives historiques", '<span class="tag n">Permanent</span>', "il y a 40 min"),
            ("xls", "États financiers 2025", "Finance", '<span class="tag g">Archivé</span>', "il y a 1 h"),
            ("doc", "Procès-verbal CA 14/09/2026", "Direction générale", '<span class="tag a">En validation</span>', "il y a 2 h"),
            ("pdf", "Facture FAC-0045 — ABC SA", "Comptabilité", '<span class="tag g">Archivé</span>', "il y a 3 h"),
            ("img", "Plan bâtiment B — niveau 2", "Technique", '<span class="tag b">Actif</span>', "hier")]
    tr = "".join(f'<tr><td><div class="fi">{ftype(t)}{n}</div></td><td class="muted">{d}</td><td>{s}</td><td class="muted">{w}</td></tr>' for t, n, d, s, w in rows)
    alerts = [("r", "4 documents : contrôle d'intégrité à refaire"), ("a", "1 250 documents arrivent à échéance dans 90 jours"),
              ("a", "14 utilisateurs avec des droits à revoir"), ("g", "Sauvegarde hors site vérifiée — 03:00")]
    al = "".join(f'<div style="display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-bottom:1px solid #EEF1F6"><span class="tag {c}" style="width:8px;height:8px;padding:0;margin-top:5px;border-radius:50%;background:{ {"r":"#D9473A","a":"#E5A93A","g":"#11875D"}[c] }"></span><span>{t}</span></div>' for c, t in alerts)
    content = f'''<div class="head"><div><h1>Tableau de bord</h1><div class="sub">Mardi 29 septembre 2026 · Vue d'ensemble de l'organisation</div></div>
<div class="btns"><span class="btn o">{icon("download")}Exporter</span><span class="btn">{icon("scan")}Importer / numériser</span></div></div>
<div class="grid kpis">{k}</div>
<div class="grid" style="grid-template-columns:1.55fr 1fr;margin-bottom:14px">
<div class="box"><h3>Documents archivés par mois <small>2026</small></h3><div style="display:flex;align-items:flex-end;gap:10px;height:160px">{chart}</div></div>
<div class="box"><h3>Alertes <small>Voir tout</small></h3>{al}</div></div>
<div class="box"><h3>Activité récente <small>Journal complet</small></h3><table><thead><tr><th>Document</th><th>Service</th><th>Statut</th><th>Modifié</th></tr></thead><tbody>{tr}</tbody></table></div>'''
    return shell("Tableau de bord", content)


def document():
    fields = [("Type de document", "Facture fournisseur", 99), ("Fournisseur", "ABC SA", 98), ("Numéro", "FAC-0045", 99),
              ("Date", "12/04/2023", 97), ("Montant TTC", "4 500 000 FCFA", 96), ("TVA", "686 441 FCFA", 94),
              ("Devise", "XOF (FCFA)", 99), ("N° de commande", "BC-2023-118", 91), ("Service", "Comptabilité", 88)]
    fr = "".join(f'<div style="display:grid;grid-template-columns:130px 1fr 44px;gap:8px;align-items:center;padding:7px 0;border-bottom:1px solid #EEF1F6"><span class="muted">{l}</span><span style="font-weight:600;background:#F4F6FA;border-radius:5px;padding:5px 8px">{v}</span><span style="font-size:11px;color:{"#11875D" if c>=95 else "#A56A12"};font-weight:700">{c} %</span></div>' for l, v, c in fields)
    invoice = f'''<div style="background:#fff;width:400px;height:560px;margin:0 auto;box-shadow:0 8px 30px rgba(10,21,65,.18);padding:30px 30px;font-size:10.5px;color:#333;position:relative">
<div style="display:flex;justify-content:space-between"><div><b style="font-size:15px;color:#111">ABC SA</b><div>Zone industrielle de Yopougon</div><div>Abidjan, Côte d'Ivoire</div></div><div style="text-align:right"><b style="font-size:17px;color:#111">FACTURE</b><div style="background:rgba(0,110,239,.14);outline:1.5px solid #006EEF;padding:1px 3px;margin-top:4px">N° FAC-0045</div><div style="background:rgba(0,110,239,.14);outline:1.5px solid #006EEF;padding:1px 3px;margin-top:4px">Date : 12/04/2023</div></div></div>
<div style="margin:26px 0 16px;padding:10px;background:#f6f6f6"><b>Client</b><br>Organisation démo — Direction financière<br>Réf. commande : <span style="background:rgba(0,110,239,.14);outline:1.5px solid #006EEF;padding:0 3px">BC-2023-118</span></div>
<table style="font-size:10px"><thead><tr><th style="font-size:9px">Désignation</th><th style="font-size:9px;text-align:right">Qté</th><th style="font-size:9px;text-align:right">Montant</th></tr></thead><tbody>
<tr><td style="font-size:10px;padding:6px">Rayonnages mobiles d'archives</td><td style="text-align:right;font-size:10px">4</td><td style="text-align:right;font-size:10px">2 400 000</td></tr>
<tr><td style="font-size:10px;padding:6px">Boîtes de conservation neutres</td><td style="text-align:right;font-size:10px">600</td><td style="text-align:right;font-size:10px">900 000</td></tr>
<tr><td style="font-size:10px;padding:6px">Installation et transport</td><td style="text-align:right;font-size:10px">1</td><td style="text-align:right;font-size:10px">513 559</td></tr></tbody></table>
<div style="margin-top:18px;margin-left:auto;width:190px;font-size:10.5px"><div style="display:flex;justify-content:space-between;padding:3px 0"><span>Total HT</span><span>3 813 559</span></div>
<div style="display:flex;justify-content:space-between;padding:3px 0;background:rgba(0,110,239,.14);outline:1.5px solid #006EEF"><span>TVA 18 %</span><span>686 441</span></div>
<div style="display:flex;justify-content:space-between;padding:5px 0;font-weight:700;font-size:12px;border-top:1px solid #333;margin-top:4px;background:rgba(0,110,239,.14);outline:1.5px solid #006EEF"><span>Total TTC</span><span>4 500 000 FCFA</span></div></div>
<div style="position:absolute;bottom:26px;left:30px;right:30px;font-size:9px;color:#888;border-top:1px solid #ddd;padding-top:8px">RCCM CI-ABJ-XX-XXXX · Conditions : paiement à 30 jours</div></div>'''
    content = f'''<div class="head"><div><div class="sub">Documents › Finance › Factures fournisseurs › 2023</div><h1>Facture_2023_0045.pdf</h1></div>
<div class="btns"><span class="btn o">{icon("workflow")}Lancer un workflow</span><span class="btn">{icon("archive")}Archiver</span></div></div>
<div class="grid" style="grid-template-columns:1fr 440px">
<div class="box" style="background:#E9ECF2;padding:22px">{invoice}</div>
<div class="box"><h3>{icon("sparkles")} Métadonnées extraites par ARCHIVA AI <small>OCR 100 %</small></h3>{fr}
<div style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap"><span class="tag g">Classement proposé : Finance › Factures fournisseurs</span><span class="tag b">Règle : conservation 10 ans</span><span class="tag">Confidentialité : interne</span></div>
<div style="margin-top:14px;background:#F4F6FA;border-radius:8px;padding:10px 12px;font-size:11.5px"><b>SHA-256</b> <span class="muted" style="font-family:monospace">1D2B4517 5CCAB27C 064EFB72 5422CFE3…</span></div>
<div style="margin-top:12px;display:flex;gap:8px"><span class="btn" style="flex:1;justify-content:center">{icon("check")}Valider les métadonnées</span><span class="btn o">Corriger</span></div></div></div>'''
    return shell("Documents", content)


def search():
    res = [("pdf", "Facture FAC-0092 — SOTRA Équipements", "12 800 000 FCFA", "03/11/2025", "Factures fournisseurs"),
           ("pdf", "Facture FAC-0045 — ABC SA", "4 500 000 → exclu", "12/04/2023", ""),
           ("pdf", "Facture F-2025-311 — Bâtir CI", "27 350 000 FCFA", "18/09/2025", "Factures fournisseurs"),
           ("pdf", "Facture 000781 — Imprimerie du Plateau", "6 120 000 FCFA", "02/07/2025", "Factures fournisseurs"),
           ("tif", "Facture n° 2024-77 (scannée)", "9 400 000 FCFA", "21/02/2024", "Factures fournisseurs"),
           ("pdf", "Facture FAC-0101 — Réseaux & Énergie", "15 000 000 FCFA", "30/01/2026", "Factures fournisseurs")]
    res = [r for r in res if "exclu" not in r[2]]
    rows = "".join(f'<tr><td><div class="fi">{ftype(t)}<div>{n}<div class="muted" style="font-size:11px;font-weight:400">Finance › {c}</div></div></div></td><td style="font-weight:700;color:#0A1541">{m}</td><td class="muted">{d}</td><td><span class="tag g">Archivé</span></td></tr>' for t, n, m, d, c in res)
    facets = [("Type de document", [("Facture fournisseur", 214), ("Facture client", 37)]), ("Année", [("2026", 41), ("2025", 118), ("2024", 92)]),
              ("Service", [("Comptabilité", 190), ("Achats", 61)]), ("Montant", [("5 – 10 M FCFA", 139), ("10 – 50 M FCFA", 98), ("> 50 M FCFA", 14)])]
    fc = "".join(f'<div style="margin-bottom:14px"><div style="font-weight:700;font-size:12px;color:#0A1541;margin-bottom:6px">{t}</div>' + "".join(f'<div style="display:flex;justify-content:space-between;padding:3px 0"><span style="display:flex;gap:7px;align-items:center"><span style="width:14px;height:14px;border:1.5px solid {"#006EEF" if i==0 else "#C6CCDB"};background:{"#006EEF" if i==0 else "#fff"};border-radius:3px"></span>{l}</span><span class="muted">{n}</span></div>' for i, (l, n) in enumerate(o)) + "</div>" for t, o in facets)
    content = f'''<div class="box" style="padding:18px 20px;margin-bottom:14px;border-color:#006EEF;box-shadow:0 0 0 4px rgba(0,110,239,.1)">
<div style="display:flex;align-items:center;gap:12px;font-size:17px;font-weight:600;color:#0A1541">{icon("sparkles")}Factures supérieures à 5 millions FCFA<span style="margin-left:auto" class="btn">{icon("search")}Rechercher</span></div>
<div style="margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;font-size:12px"><span class="muted">Compris comme :</span><span class="tag b">Type = Facture</span><span class="tag b">Montant &gt; 5 000 000 FCFA</span><span class="tag">Tous services</span><span class="tag">Toutes années</span></div></div>
<div class="grid" style="grid-template-columns:230px 1fr">
<div class="box">{fc}</div>
<div class="box"><h3>251 résultats <small>Trier : montant décroissant</small></h3><table><thead><tr><th>Document</th><th>Montant</th><th>Date</th><th>Statut</th></tr></thead><tbody>{rows}</tbody></table>
<div class="muted" style="margin-top:12px;font-size:11.5px">Recherche plein texte, OCR et métadonnées · 0,21 s · Seuls les documents auxquels vous avez accès sont affichés.</div></div></div>'''
    return shell("Recherche", content)


def retention():
    rows = [("pdf", "Contrat A — maintenance ascenseurs", "Contrats · 10 ans", "12/2028", '<span class="tag a">Examiner</span>'),
            ("pdf", "Facture B — FAC-0045", "Pièces comptables · 10 ans", "04/2033", '<span class="tag g">Conserver</span>'),
            ("doc", "Dossier C — marché public 2025-14", "Marchés publics · 10 ans", "2035", '<span class="tag b">Conservation longue</span>'),
            ("tif", "Archive D — registre d'état civil 1962", "État civil · permanent", "Permanente", '<span class="tag n">Préserver</span>'),
            ("pdf", "Dossier du personnel — matricule 0412", "Dossiers RH · durée fixée par le juriste", "03/2027", '<span class="tag a">Examiner</span>'),
            ("xls", "Relevés bancaires 2016", "Comptabilité · 10 ans", "12/2026", '<span class="tag r">Gel juridique</span>')]
    tr = "".join(f'<tr><td><div class="fi">{ftype(t)}{n}</div></td><td class="muted">{r}</td><td style="font-weight:600">{d}</td><td>{a}</td></tr>' for t, n, r, d, a in rows)
    stages = [("Actif", 402118, "#CFE2FD"), ("Semi-actif", 309400, "#7FB2F7"), ("Archivé", 471880, "#3D8CF2"), ("Préservation", 65132, "#0A1541")]
    tot = sum(s[1] for s in stages)
    sb = "".join(f'<div style="width:{v/tot*100:.1f}%;background:{c}"></div>' for _, v, c in stages)
    lg = "".join(f'<div style="display:flex;align-items:center;gap:7px"><span style="width:10px;height:10px;border-radius:3px;background:{c}"></span>{l} <b>{v:,}</b></div>'.replace(",", " ") for l, v, c in stages)
    content = f'''<div class="head"><div><h1>Retention Center</h1><div class="sub">Cycle de vie et échéances de conservation</div></div><div class="btns"><span class="btn o">{icon("hourglass")}Règles de conservation</span><span class="btn">{icon("check")}Examiner la sélection</span></div></div>
<div class="box" style="background:#FBF1DE;border-color:#EFD7A8;display:flex;align-items:center;gap:14px;margin-bottom:14px"><span style="color:#A56A12">{icon("alert")}</span><div><b>1 250 documents arrivent à échéance dans 90 jours.</b> <span class="muted">Chaque décision (conserver, transférer, détruire) est validée par un responsable habilité et tracée dans le journal d'audit.</span></div></div>
<div class="box" style="margin-bottom:14px"><h3>Répartition par étape du cycle de vie</h3><div style="display:flex;height:16px;border-radius:6px;overflow:hidden;margin-bottom:12px">{sb}</div><div style="display:flex;gap:22px;font-size:12px">{lg}</div></div>
<div class="box"><h3>Documents à échéance <small>Filtrer</small></h3><table><thead><tr><th>Document</th><th>Règle appliquée</th><th>Échéance</th><th>Action proposée</th></tr></thead><tbody>{tr}</tbody></table></div>'''
    return shell("Conservation", content)


def physical():
    items = [("Contrats fournisseurs — lot 1 (A à F)", "2024", "Numérisé"), ("Contrats fournisseurs — lot 2 (G à M)", "2024", "Numérisé"),
             ("Avenants et résiliations", "2024", "Numérisé"), ("Correspondances juridiques", "2023–2024", "À numériser"),
             ("Pièces de marché (originaux signés)", "2024", "Original conservé")]
    li = "".join(f'<tr><td><div class="fi">{icon("folder")}{n}</div></td><td class="muted">{y}</td><td><span class="tag {"g" if s=="Numérisé" else ("a" if s=="À numériser" else "b")}">{s}</span></td></tr>' for n, y, s in items)
    loc = [("Site", "Abidjan"), ("Bâtiment", "B"), ("Salle", "03"), ("Rayon", "12"), ("Étagère", "04"), ("Boîte", "457")]
    lc = "".join(f'<div style="text-align:center;padding:10px 6px;border-right:1px solid #E1E5EE"><div class="muted" style="font-size:11px">{a}</div><b style="font-size:17px;color:#0A1541">{b}</b></div>' for a, b in loc)
    moves = [("29/09/2026 08:45", "Consultation sur place — Awa Koné"), ("14/08/2026 10:12", "Retour en rayon après numérisation"),
             ("02/08/2026 09:30", "Sortie pour numérisation — Scan Center Abidjan"), ("11/03/2025 15:04", "Versement par la Direction juridique")]
    mv = "".join(f'<div style="display:flex;gap:10px;padding:7px 0;border-bottom:1px solid #EEF1F6"><span class="muted" style="width:120px;flex-shrink:0">{d}</span><span>{t}</span></div>' for d, t in moves)
    content = f'''<div class="head"><div><div class="sub">Archives physiques › Abidjan › Bâtiment B › Salle 03</div><h1>Boîte CI-ABJ-PLT-2026-000457</h1></div><div class="btns"><span class="btn o">{icon("qr")}Imprimer l'étiquette</span><span class="btn">{icon("box")}Demander la boîte</span></div></div>
<div class="grid" style="grid-template-columns:1fr 300px;margin-bottom:14px">
<div class="box"><h3>Localisation</h3><div style="display:grid;grid-template-columns:repeat(6,1fr);border:1px solid #E1E5EE;border-radius:8px;overflow:hidden;margin-bottom:14px">{lc}</div>
<div class="grid" style="grid-template-columns:repeat(3,1fr);gap:10px;font-size:12.5px"><div><span class="muted">Service versant</span><br><b>Direction juridique</b></div><div><span class="muted">Conservation</span><br><b>Jusqu'en 2034, puis examen</b></div><div><span class="muted">Statut</span><br><span class="tag g">En rayon</span></div></div></div>
<div class="box" style="text-align:center"><div style="width:170px;margin:4px auto 10px">{qr(457)}</div><b style="font-size:12px;color:#0A1541">CI-ABJ-PLT-2026-000457</b><div class="muted" style="font-size:11px">Scannez pour ouvrir la fiche</div></div></div>
<div class="grid" style="grid-template-columns:1.3fr 1fr"><div class="box"><h3>Contenu de la boîte <small>5 dossiers</small></h3><table><tbody>{li}</tbody></table></div><div class="box"><h3>Mouvements</h3>{mv}</div></div>'''
    return shell("Archives physiques", content)


def audit():
    ev = [("08:42", "Jean Kouassi", "CONSULTATION", "Contrat fournisseur 2026-0045", "Abidjan · 10.0.4.21", "b"),
          ("08:44", "Jean Kouassi", "TÉLÉCHARGEMENT", "Contrat fournisseur 2026-0045", "Abidjan · 10.0.4.21", "b"),
          ("08:51", "Marie Diallo", "MODIFICATION MÉTADONNÉES", "Contrat fournisseur 2026-0045 · champ « échéance »", "Bouaké · 10.2.1.7", "a"),
          ("09:05", "Administrateur", "VALIDATION", "Contrat fournisseur 2026-0045 → version 3", "Abidjan · 10.0.1.2", "g"),
          ("09:18", "ARCHIVA AI", "PROPOSITION DE CLASSEMENT", "Lot de 500 factures · en attente de validation humaine", "Service interne", "n"),
          ("09:26", "Awa Koné", "ARCHIVAGE", "États financiers 2025 · empreinte SHA-256 scellée", "Abidjan · 10.0.4.9", "g"),
          ("09:40", "Inconnu", "ÉCHEC DE CONNEXION", "Compte m.traore · 3 tentatives · MFA exigée", "IP externe 196.47.x.x", "r")]
    tr = "".join(f'<tr><td style="font-weight:600">29/09/2026<br><span class="muted" style="font-weight:500">{h}</span></td><td><div class="fi"><span class="av" style="width:26px;height:26px;font-size:10px">{"".join(w[0] for w in u.split()[:2])}</span>{u}</div></td><td><span class="tag {c}">{a}</span></td><td>{o}</td><td class="muted">{w}</td></tr>' for h, u, a, o, w, c in ev)
    content = f'''<div class="head"><div><h1>Audit trail</h1><div class="sub">Qui ? Quoi ? Quand ? Depuis où ? Quelle action ? — journal inaltérable</div></div><div class="btns"><span class="btn o">{icon("calendar")}29/09/2026</span><span class="btn">{icon("download")}Exporter pour l'auditeur</span></div></div>
<div class="grid kpis"><div class="box kpi"><small>{icon("eye")}Événements aujourd'hui</small><b>4 812</b></div><div class="box kpi"><small>{icon("download")}Téléchargements</small><b>318</b></div><div class="box kpi"><small>{icon("pen")}Modifications</small><b>96</b></div><div class="box kpi"><small>{icon("alert")}Anomalies</small><b style="color:#B83227">2</b></div></div>
<div class="box"><table><thead><tr><th>Date / heure</th><th>Utilisateur</th><th>Action</th><th>Objet</th><th>Origine</th></tr></thead><tbody>{tr}</tbody></table></div>'''
    return shell("Audit trail", content)


def workflow():
    steps = [("Dépôt", "Employé", "file", "#6C728D"), ("Contrôle", "Assistant juridique", "check", "#006EEF"), ("Responsable", "Chef de service", "user", "#006EEF"),
             ("Juridique", "Direction juridique", "scale", "#006EEF"), ("Direction", "Directeur général", "briefcase", "#006EEF"), ("Signature", "Prestataire de confiance", "pen", "#11875D"), ("Archivage", "SAE — 10 ans", "archive", "#0A1541")]
    nodes = ""
    for i, (t, w, ic, c) in enumerate(steps):
        arrow = '' if i == len(steps) - 1 else '<div style="flex:0 0 26px;height:2px;background:#C6CCDB;position:relative"><span style="position:absolute;right:-1px;top:-4px;border-left:7px solid #C6CCDB;border-top:5px solid transparent;border-bottom:5px solid transparent"></span></div>'
        sel = "box-shadow:0 0 0 3px rgba(0,110,239,.25);border-color:#006EEF;" if i == 3 else ""
        nodes += f'<div style="flex:1;background:#fff;border:1px solid #E1E5EE;border-radius:10px;padding:12px 10px;text-align:center;{sel}"><div style="width:34px;height:34px;border-radius:9px;background:{c};color:#fff;display:grid;place-items:center;margin:0 auto 8px">{icon(ic)}</div><b style="font-size:12.5px;color:#0A1541">{t}</b><div class="muted" style="font-size:10.5px;line-height:1.3;margin-top:2px">{w}</div></div>{arrow}'
    pal = ["Étape de validation", "Condition (montant, type)", "Signature électronique", "Horodatage", "Notification", "Archivage automatique", "Délai / relance"]
    pl = "".join(f'<div style="border:1px dashed #C6CCDB;border-radius:7px;padding:8px 10px;margin-bottom:7px;display:flex;gap:8px;align-items:center;background:#fff">{icon("blocks")}{p}</div>' for p in pal)
    content = f'''<div class="head"><div><div class="sub">Workflows › Modèles</div><h1>Circuit de validation des contrats</h1></div><div class="btns"><span class="btn o">Tester</span><span class="btn">{icon("check")}Publier le workflow</span></div></div>
<div class="grid" style="grid-template-columns:210px 1fr 260px">
<div class="box" style="background:#F9FAFC"><h3>Blocs</h3>{pl}<div class="muted" style="font-size:11px;margin-top:8px">Glissez-déposez un bloc sur le circuit.</div></div>
<div class="box" style="background-image:radial-gradient(#DCE1EB 1px,transparent 1px);background-size:16px 16px;min-height:600px"><div style="display:flex;align-items:center;margin-top:170px">{nodes}</div>
<div style="margin:36px auto 0;width:300px;border:1px solid #EFD7A8;background:#FBF1DE;border-radius:9px;padding:10px 12px;font-size:12px"><b>Condition</b> · si montant &gt; 50 000 000 FCFA → ajouter l'étape « Conseil d'administration »</div></div>
<div class="box"><h3>Étape : Juridique</h3><div style="font-size:12.5px;display:grid;gap:12px"><div><span class="muted">Valideurs</span><br><b>Direction juridique (groupe)</b></div><div><span class="muted">Délai</span><br><b>3 jours ouvrés, relance à J+2</b></div><div><span class="muted">Actions possibles</span><br><span class="tag g">Valider</span> <span class="tag r">Refuser</span> <span class="tag">Demander une correction</span></div><div><span class="muted">Si refus</span><br><b>Retour au dépositaire avec commentaire</b></div><div><span class="muted">Traçabilité</span><br><b>Chaque décision est inscrite à l'audit trail</b></div></div></div></div>'''
    return shell("Workflows", content)


def ai():
    content = f'''<div class="head"><div><h1>ARCHIVA AI</h1><div class="sub">Assistant documentaire — répond à partir des seuls documents auxquels vous avez accès</div></div><div class="btns"><span class="btn o">{icon("folder")}Dossier : Projet autoroute Abidjan–Lagos</span></div></div>
<div class="grid" style="grid-template-columns:1fr 300px">
<div class="box" style="display:flex;flex-direction:column;gap:14px;min-height:620px">
<div style="align-self:flex-end;background:#006EEF;color:#fff;border-radius:12px 12px 2px 12px;padding:10px 14px;max-width:70%">Construis la chronologie de ce dossier et signale les documents qui arrivent à échéance.</div>
<div style="display:flex;gap:10px;max-width:88%"><div style="width:30px;height:30px;border-radius:8px;background:#0A1541;color:#fff;display:grid;place-items:center;flex-shrink:0">{icon("sparkles")}</div>
<div style="background:#F4F6FA;border-radius:12px 12px 12px 2px;padding:12px 16px"><b>Chronologie du dossier (38 documents analysés)</b>
<div style="margin-top:8px;display:grid;gap:6px">
<div><span class="tag b">03/2024</span> Convention de financement signée <span class="muted">[Convention_2024-03.pdf]</span></div>
<div><span class="tag b">09/2024</span> Étude d'impact environnemental remise <span class="muted">[EIE_rapport_final.pdf]</span></div>
<div><span class="tag b">02/2025</span> Marché de travaux lot 2 attribué <span class="muted">[PV_attribution_lot2.pdf]</span></div>
<div><span class="tag b">11/2025</span> Avenant n° 1 — délai prolongé de 6 mois <span class="muted">[Avenant_01.pdf]</span></div></div>
<div style="margin-top:10px;background:#FBF1DE;border-radius:8px;padding:8px 10px"><b>À surveiller :</b> 2 garanties bancaires expirent le 15/12/2026.</div>
<div class="muted" style="font-size:11px;margin-top:8px">Sources citées · aucune modification effectuée · proposition à valider</div></div></div>
<div style="align-self:flex-end;background:#006EEF;color:#fff;border-radius:12px 12px 2px 12px;padding:10px 14px;max-width:70%">Classe automatiquement les 500 documents importés ce matin.</div>
<div style="display:flex;gap:10px;max-width:88%"><div style="width:30px;height:30px;border-radius:8px;background:#0A1541;color:#fff;display:grid;place-items:center;flex-shrink:0">{icon("sparkles")}</div>
<div style="background:#F4F6FA;border-radius:12px 12px 12px 2px;padding:12px 16px">J'ai préparé une proposition de classement : <b>471 documents</b> avec un niveau de confiance élevé, <b>29</b> à vérifier. <br>Rien n'est déplacé tant qu'un archiviste n'a pas validé.
<div style="margin-top:10px;display:flex;gap:8px"><span class="btn" style="padding:6px 12px">Revoir la proposition</span><span class="btn o" style="padding:6px 12px">Voir les 29 cas</span></div></div></div>
<div style="margin-top:auto;display:flex;gap:10px;align-items:center;border:1px solid #D5DAE6;border-radius:10px;padding:10px 14px;color:#6C728D">{icon("sparkles")}Posez une question sur vos documents…<span class="btn" style="margin-left:auto;padding:6px 10px">{icon("arrow-right")}</span></div></div>
<div class="box"><h3>Suggestions</h3><div style="display:grid;gap:8px">{"".join(f'<div style="border:1px solid #E1E5EE;border-radius:8px;padding:9px 11px">{s}</div>' for s in ["Résume ce contrat", "Trouve les obligations du fournisseur", "Compare ces deux versions", "Identifie les doublons", "Quels documents arrivent à échéance ?", "Extrais les noms des fournisseurs"])}</div>
<div style="margin-top:16px;background:#0A1541;color:#C3CBE6;border-radius:9px;padding:12px;font-size:11.5px"><b style="color:#fff">Règle ARCHIVA</b><br>L'IA assiste, elle ne décide pas : ni destruction, ni classement définitif, ni droits d'accès sans validation humaine.</div></div></div>'''
    return shell("ARCHIVA AI", content)


def compliance():
    items = [("r", "4 documents dont l'intégrité doit être contrôlée", "Empreinte SHA-256 différente de l'empreinte scellée"),
             ("a", "25 documents sans métadonnées obligatoires", "Service Achats · import du 21/09"),
             ("a", "14 utilisateurs avec des droits excessifs", "Accès au coffre-fort RH sans justification"),
             ("a", "3 200 documents arrivent à échéance", "Dans les 12 prochains mois"),
             ("a", "12 sauvegardes non vérifiées", "Test de restauration à planifier"),
             ("g", "Chiffrement au repos et en transit", "Actif sur 100 % des espaces"),
             ("g", "Authentification multifacteur", "Obligatoire pour 100 % des administrateurs"),
             ("g", "Copie hors site (règle 3-2-1)", "Dernière réplication : aujourd'hui 03:00")]
    col = {"r": "#D9473A", "a": "#E5A93A", "g": "#11875D"}
    lab = {"r": "Risque", "a": "Action nécessaire", "g": "Conforme"}
    li = "".join(f'<div style="display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid #EEF1F6"><span style="width:10px;height:10px;border-radius:50%;background:{col[c]};flex-shrink:0"></span><div style="flex:1"><b style="color:#0A1541">{t}</b><div class="muted" style="font-size:11.5px">{d}</div></div><span class="tag {c if c!="a" else "a"}">{lab[c]}</span></div>' for c, t, d in items)
    gauge = f'<svg viewBox="0 0 120 120" style="width:150px;height:150px;transform:rotate(-90deg)"><circle cx="60" cy="60" r="50" fill="none" stroke="#EEF1F6" stroke-width="12"/><circle cx="60" cy="60" r="50" fill="none" stroke="#006EEF" stroke-width="12" stroke-dasharray="314" stroke-dashoffset="69" stroke-linecap="round"/></svg>'
    content = f'''<div class="head"><div><h1>Compliance Center</h1><div class="sub">État de conformité de l'organisation · mis à jour il y a 5 minutes</div></div><div class="btns"><span class="btn">{icon("download")}Rapport de conformité</span></div></div>
<div class="grid" style="grid-template-columns:300px 1fr"><div class="box" style="text-align:center"><h3>Score global</h3><div style="position:relative;width:150px;margin:10px auto">{gauge}<div style="position:absolute;inset:0;display:grid;place-items:center"><div><b style="font-size:32px;color:#0A1541;letter-spacing:-.03em">78</b><div class="muted" style="font-size:11px">/ 100</div></div></div></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:10px;font-size:11.5px"><div><b style="font-size:18px;color:#11875D;display:block">31</b>Conformes</div><div><b style="font-size:18px;color:#A56A12;display:block">9</b>Actions</div><div><b style="font-size:18px;color:#B83227;display:block">1</b>Risque</div></div>
<div style="margin-top:18px;text-align:left;font-size:12px;display:grid;gap:9px">{"".join(f'<div><div style="display:flex;justify-content:space-between"><span>{l}</span><b>{v} %</b></div><div class="bar" style="margin-top:4px"><i style="width:{v}%"></i></div></div>' for l, v in [("Métadonnées", 94), ("Droits d'accès", 71), ("Conservation", 82), ("Sauvegardes", 88), ("Intégrité", 99)])}</div></div>
<div class="box"><h3>Points de contrôle <small>41 règles actives</small></h3>{li}</div></div>'''
    return shell("Conformité", content)


def records():
    tree = [(0, "Organisation démo", "folder"), (1, "Direction générale", "folder"), (1, "Direction financière", "folder"), (2, "Comptabilité", "folder"),
            (3, "Factures clients", "file"), (3, "Factures fournisseurs", "file"), (2, "États financiers", "file"), (2, "Déclarations fiscales", "file"),
            (2, "Audits", "file"), (1, "Ressources humaines", "folder"), (2, "Dossiers du personnel", "lock"), (2, "Recrutement", "file"),
            (1, "Juridique", "folder"), (2, "Contrats", "file"), (2, "Contentieux", "file"), (1, "Archives historiques", "folder")]
    tr = "".join(f'<div style="display:flex;align-items:center;gap:8px;padding:6px 8px;margin-left:{d*16}px;border-radius:6px;{"background:#E6F0FE;color:#0057C2;font-weight:600" if n=="Factures fournisseurs" else ""}">{icon(ic)}{n}</div>' for d, n, ic in tree)
    props = [("Catégorie", "Direction financière"), ("Sous-catégorie", "Comptabilité"), ("Série", "Pièces comptables"), ("Sous-série", "Factures fournisseurs"),
             ("Type de document", "Facture"), ("Durée de conservation", "10 ans (règle validée par le juriste)"), ("Événement déclencheur", "Clôture de l'exercice comptable"),
             ("Sort final", "Destruction après examen"), ("Niveau de confidentialité", "Interne"), ("Propriétaire", "Chef comptable"), ("Service responsable", "Comptabilité")]
    pr = "".join(f'<div style="display:grid;grid-template-columns:180px 1fr;padding:8px 0;border-bottom:1px solid #EEF1F6"><span class="muted">{a}</span><b style="color:#0A1541">{b}</b></div>' for a, b in props)
    meta = ["Titre", "Auteur", "Date de création", "Date de réception", "Date d'archivage", "Numéro", "Fournisseur", "Montant", "Projet", "Localisation", "Confidentialité", "Version", "Empreinte numérique"]
    content = f'''<div class="head"><div><h1>Plan de classement</h1><div class="sub">Records management · version 3 validée le 15/09/2026 par l'archiviste</div></div><div class="btns"><span class="btn o">Historique des versions</span><span class="btn">{icon("check")}Enregistrer</span></div></div>
<div class="grid" style="grid-template-columns:300px 1fr"><div class="box">{tr}</div>
<div class="box"><h3>Série : Factures fournisseurs <small>1 842 documents</small></h3>{pr}
<h3 style="margin-top:18px">Métadonnées obligatoires</h3><div style="display:flex;flex-wrap:wrap;gap:6px">{"".join(f'<span class="tag b">{m}</span>' for m in meta)}</div></div></div>'''
    return shell("Records management", content)


def security():
    rows = [("Awa Koné", "Archiviste", "Abidjan", "Chrome · Windows", "MFA", "Active"), ("Jean Kouassi", "Juriste", "Abidjan", "Edge · Windows", "MFA", "Active"),
            ("Marie Diallo", "Comptable", "Bouaké", "ARCHIVA GO · Android", "MFA", "Active"), ("Auditeur externe", "Auditeur (lecture)", "Dakar", "Firefox · macOS", "MFA", "Expire dans 2 j"),
            ("m.traore", "Employé", "IP externe", "Inconnu", "Bloqué", "3 échecs")]
    tr = "".join(f'<tr><td><div class="fi"><span class="av" style="width:26px;height:26px;font-size:10px">{u[:2].upper()}</span>{u}</div></td><td class="muted">{r}</td><td>{l}</td><td class="muted">{d}</td><td><span class="tag {"g" if m=="MFA" else "r"}">{m}</span></td><td>{s}</td></tr>' for u, r, l, d, m, s in rows)
    k = "".join(f'<div class="box kpi"><small>{icon(i)}{l}</small><b>{v}</b>{s}</div>' for i, l, v, s in [("users", "Sessions actives", "184", '<span class="up">Normal</span>'), ("alert", "Échecs de connexion (24 h)", "7", '<span class="warn">1 compte bloqué</span>'), ("download", "Téléchargements sensibles", "12", '<span class="muted" style="font-size:11.5px">Coffre-fort</span>'), ("lock", "Chiffrement", "AES-256", '<span class="up">Au repos et en transit</span>')])
    content = f'''<div class="head"><div><h1>Security Center</h1><div class="sub">Connexions, sessions, permissions et anomalies</div></div><div class="btns"><span class="btn o">{icon("key")}Politique de mots de passe</span><span class="btn">{icon("shield")}Revue des droits</span></div></div>
<div class="grid kpis">{k}</div>
<div class="grid" style="grid-template-columns:1.6fr 1fr"><div class="box"><h3>Sessions et comptes</h3><table><thead><tr><th>Utilisateur</th><th>Rôle</th><th>Lieu</th><th>Appareil</th><th>Auth.</th><th>État</th></tr></thead><tbody>{tr}</tbody></table></div>
<div class="box"><h3>Sauvegarde et reprise</h3>{"".join(f'<div style="display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid #EEF1F6"><span>{a}</span><b style="color:{c}">{b}</b></div>' for a, b, c in [("Copie 1 — production", "Abidjan", "#0A1541"), ("Copie 2 — autre support", "Abidjan (site B)", "#0A1541"), ("Copie 3 — hors site", "Réplication chiffrée", "#0A1541"), ("Dernier test de restauration", "12/09/2026 · réussi", "#11875D"), ("Objectif de reprise (RTO)", "4 heures", "#0A1541")])}</div></div>'''
    return shell("Coffre-fort", content)


def mobile():
    css = """body{width:420px;height:860px;background:transparent}
.phone{width:390px;height:820px;margin:20px 15px;border-radius:52px;background:#0A1541;padding:12px;box-shadow:0 30px 60px rgba(10,21,65,.35)}
.scr{width:100%;height:100%;border-radius:42px;background:#F4F6FA;overflow:hidden;position:relative}
.notch{position:absolute;left:50%;top:10px;transform:translateX(-50%);width:110px;height:30px;border-radius:20px;background:#0A1541}
.st{display:flex;justify-content:space-between;padding:16px 30px 0;font-weight:600;font-size:13px}
.hd{padding:26px 22px 16px;background:#0A1541;color:#fff;margin-top:-44px;padding-top:62px}
.hd small{color:#AEB8DA}
.hd h2{font-size:22px;letter-spacing:-.02em;margin-top:2px}
.sr{margin-top:14px;background:rgba(255,255,255,.1);border-radius:10px;padding:11px 14px;color:#C3CBE6;display:flex;gap:9px;align-items:center}
.acts{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:16px 18px}
.act{background:#fff;border-radius:14px;padding:12px 4px;text-align:center;font-size:11px;font-weight:600;color:#0A1541;border:1px solid #E1E5EE}
.act span{width:36px;height:36px;border-radius:10px;background:#E6F0FE;color:#006EEF;display:grid;place-items:center;margin:0 auto 6px}
.sec{padding:0 18px}
.sec h4{font-size:13px;color:#0A1541;margin:6px 0 8px;display:flex;justify-content:space-between}
.it{background:#fff;border-radius:12px;padding:12px;display:flex;gap:10px;align-items:center;margin-bottom:8px;border:1px solid #E1E5EE}
.tb{position:absolute;bottom:0;left:0;right:0;height:76px;background:#fff;border-top:1px solid #E1E5EE;display:flex;justify-content:space-around;align-items:center;padding-bottom:14px;color:#6C728D;font-size:10px}
.tb div{text-align:center}.tb .on{color:#006EEF}
.scanbtn{width:54px;height:54px;border-radius:50%;background:#006EEF;color:#fff;display:grid;place-items:center;margin-top:-30px;box-shadow:0 8px 20px rgba(0,110,239,.4)}
.scanbtn svg{width:24px;height:24px}"""
    items = [("pen", "Contrat 2026-0045 à signer", "Workflow · étape Direction", "a", "À faire"),
             ("check", "PV du CA 14/09 à valider", "Demandé par Jean K.", "a", "À faire"),
             ("key", "Accès au dossier RH 0412", "Demande en cours", "b", "Suivi"),
             ("archive", "États financiers 2025", "Archivé · empreinte scellée", "g", "OK")]
    it = "".join(f'<div class="it"><span style="width:34px;height:34px;border-radius:9px;background:#F4F6FA;display:grid;place-items:center;color:#0A1541">{icon(i)}</span><div style="flex:1"><b style="font-size:12.5px;color:#0A1541">{t}</b><div class="muted" style="font-size:11px">{d}</div></div><span class="tag {c}">{s}</span></div>' for i, t, d, c, s in items)
    acts = "".join(f'<div class="act"><span>{icon(i)}</span>{t}</div>' for i, t in [("scan", "Scanner"), ("qr", "QR code"), ("search", "Chercher"), ("fingerprint", "Vérifier")])
    body = f'''<div class="phone"><div class="scr"><div class="notch"></div><div class="st" style="color:#fff;position:relative;z-index:2"><span>9:41</span><span>5G ▮▮▮</span></div>
<div class="hd"><small>Bonjour Awa</small><h2>ARCHIVA GO</h2><div class="sr">{icon("search")}Rechercher un document</div></div>
<div class="acts">{acts}</div>
<div class="sec"><h4>À traiter <span style="color:#006EEF;font-weight:600;font-size:12px">4</span></h4>{it}</div>
<div class="tb"><div class="on">{icon("home")}<br>Accueil</div><div>{icon("files")}<br>Documents</div><div class="scanbtn">{icon("scan")}</div><div>{icon("inbox")}<br>Notifications</div><div>{icon("user")}<br>Profil</div></div></div></div>'''
    return body, css


SHOTS = {
    "archiva360-tableau-de-bord": dashboard,
    "archiva360-document-ocr": document,
    "archiva360-recherche-intelligente": search,
    "archiva360-retention-center": retention,
    "archiva360-archives-physiques": physical,
    "archiva360-audit-trail": audit,
    "archiva360-workflow": workflow,
    "archiva360-archiva-ai": ai,
    "archiva360-compliance-center": compliance,
    "archiva360-plan-de-classement": records,
    "archiva360-security-center": security,
}


def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    css = CSS.replace("__FONT__", FONT)
    jobs = []
    for name, fn in SHOTS.items():
        p = os.path.join(out_dir, name + ".html")
        with open(p, "w", encoding="utf-8") as f:
            f.write(f"<!doctype html><meta charset=utf-8><style>{css}</style>{fn()}")
        jobs.append({"html": p, "png": name + ".png", "w": 1280, "h": 800, "transparent": False})
    body, mcss = mobile()
    p = os.path.join(out_dir, "archiva-go-mobile.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(f"<!doctype html><meta charset=utf-8><style>{css}{mcss}</style>{body}")
    jobs.append({"html": p, "png": "archiva-go-mobile.png", "w": 420, "h": 860, "transparent": True})
    return jobs
