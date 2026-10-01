"""Page model, shared layout and block helpers for the ADA static build."""
import html
import json
import os
import re

from .icons import icon, LOGO, LOGO_LIGHT

# ---------------------------------------------------------------------------
# Site settings — edit here
# ---------------------------------------------------------------------------
SITE = {
    "name": "African Digital Archives",
    "short": "ADA",
    "tagline": "La mémoire numérique de l'Afrique",
    # Adresse de contact (formulaires, lettre d'information, pages légales)
    "email": "assa@eletude.org",
    # Optionnel : adresse d'un service de réception de formulaires (ex. https://formspree.io/f/xxxxxxx).
    # Vide = les formulaires ouvrent la messagerie du visiteur avec un message prérempli.
    "form_endpoint": "",
    # Liens des réseaux sociaux : seuls ceux renseignés sont affichés dans le pied de page.
    "social": {"linkedin": "", "facebook": "", "youtube": "", "whatsapp": ""},
    # Comptes en ligne ARCHIVA360 (Appwrite Cloud, offre gratuite) — voir README, section « Comptes en ligne ».
    # Vide = les pages de connexion affichent « comptes en cours d'activation ».
    "appwrite": {"endpoint": "", "project": "", "team": "archiva360"},
    "city": "Abidjan, Côte d'Ivoire",
    "base_url": "https://paledebouna-lang.github.io/african-digital-archives/",
    "theme": "wp-content/themes/ada-archives/",
    "uploads": "wp-content/uploads/2026/09/",
    "version": "1.5.0",
}

PAGES = []          # every generated page, in registration order
POSTS = []          # blog posts (also in PAGES)
_page_ids = iter(range(12, 10000, 7))


class Page:
    def __init__(self, path, title, body, *, description="", crumbs=None, hero="", body_class="page",
                 seo_title=None, kind="page", nav=None, search=True, date=None, extra_head="", scripts=""):
        self.path = path.strip("/") + "/" if path.strip("/") else ""
        self.title = title
        self.body = body
        self.description = description
        self.crumbs = crumbs
        self.hero = hero
        self.body_class = body_class
        self.seo_title = seo_title
        self.kind = kind
        self.nav = nav if nav is not None else (self.path.split("/")[0] if self.path else "")
        self.search = search
        self.date = date
        self.extra_head = extra_head
        self.scripts = scripts
        self.id = next(_page_ids)

    @property
    def depth(self):
        return self.path.count("/")

    @property
    def root(self):
        return "../" * self.depth


def add(page):
    PAGES.append(page)
    return page


def get(path):
    path = path.strip("/") + "/" if path.strip("/") else ""
    for p in PAGES:
        if p.path == path:
            return p
    raise KeyError(path)


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------
MENU = [
    {
        "title": "Solutions", "url": "solutions/", "key": "solutions",
        "intro": ("Solutions", "De la numérisation à la préservation longue durée : une chaîne complète pour vos documents papier et numériques.", "Toutes les solutions"),
        "items": [
            ("solutions/ged/", "GED", "Gérer et partager au quotidien", "folder"),
            ("solutions/sae/", "Archivage électronique (SAE)", "Conserver avec valeur probante", "archive"),
            ("solutions/records-management/", "Records management", "Règles, cycle de vie, sort final", "hourglass"),
            ("solutions/capture-numerisation/", "Capture et numérisation", "Scan, OCR, indexation", "scan"),
            ("solutions/archives-physiques/", "Archives physiques", "Boîtes, rayonnages, QR codes", "box"),
            ("solutions/ia-documentaire/", "IA documentaire", "Lire, classer, extraire, résumer", "sparkles"),
            ("solutions/securite/", "Sécurité et coffre-fort", "Chiffrement, MFA, audit", "shield"),
            ("solutions/preservation-numerique/", "Préservation numérique", "Lisible dans 30 ans (OAIS)", "layers"),
            ("solutions/workflow-courrier/", "Workflow et courrier", "Circuits de validation, signature", "workflow"),
        ],
    },
    {
        "title": "ARCHIVA360", "url": "archiva360/", "key": "archiva360",
        "intro": ("ARCHIVA360", "La plateforme africaine de gestion documentaire et d'archivage, en SaaS, en cloud privé ou sur site.", "Découvrir la plateforme"),
        "cols": 2,
        "items": [
            ("archiva360/", "Vue d'ensemble", "Capture, gestion, archivage, IA", "blocks"),
            ("archiva360/modules/", "Les 20 modules", "Du tableau de bord au portail public", "layers"),
            ("archiva360/archiva-ai/", "ARCHIVA AI", "L'assistant documentaire", "sparkles"),
            ("archiva360/archiva-go/", "ARCHIVA GO", "L'application mobile", "smartphone"),
            ("archiva360/offres-et-tarifs/", "Offres et tarifs", "Start, Business, Enterprise, Government", "briefcase"),
            ("archiva360/demo-interactive/", "Démo interactive", "Essayez la plateforme maintenant", "play"),
            ("archiva360/demo/", "Démonstration personnalisée", "Sur vos propres documents", "users"),
        ],
    },
    {
        "title": "Secteurs", "url": "secteurs/", "key": "secteurs",
        "intro": ("Secteurs", "Des réponses adaptées aux obligations et aux documents de chaque métier.", "Tous les secteurs"),
        "items": [
            ("secteurs/gouvernement/", "Gouvernement", "Ministères, mairies, collectivités", "landmark"),
            ("secteurs/banque/", "Banque", "Dossiers clients, crédits, conformité", "bank"),
            ("secteurs/assurance/", "Assurance", "Polices, sinistres, pièces", "umbrella"),
            ("secteurs/sante/", "Santé", "Hôpitaux, cliniques, laboratoires", "heart-pulse"),
            ("secteurs/education/", "Éducation", "Universités, écoles, diplômes", "graduation"),
            ("secteurs/industrie/", "Industrie et énergie", "Plans, maintenance, inspections", "factory"),
            ("secteurs/immobilier/", "Immobilier", "Titres, actes, permis, plans", "home"),
            ("secteurs/juridique/", "Juridique", "Cabinets, contentieux, actes", "scale"),
            ("secteurs/ong/", "ONG et organismes internationaux", "Projets, bailleurs, audits", "hands"),
            ("secteurs/patrimoine/", "Patrimoine", "Bibliothèques, musées, archives", "library"),
        ],
    },
    {
        "title": "Services", "url": "services/", "key": "services",
        "intro": ("Services", "Nos équipes interviennent chez vous ou dans notre centre de numérisation d'Abidjan.", "Tous les services"),
        "cols": 2,
        "items": [
            ("services/audit-documentaire/", "Audit documentaire", "Diagnostic, inventaire, plan d'action", "eye"),
            ("services/numerisation/", "Numérisation", "Centre de numérisation d'Abidjan", "scan"),
            ("services/migration/", "Migration", "Reprise de fonds et de systèmes", "refresh"),
            ("services/conseil/", "Conseil", "Plan de classement, politique d'archivage", "compass"),
            ("services/formation/", "Formation", "Archivistes, IT, utilisateurs", "presentation"),
            ("services/hebergement/", "Hébergement", "Cloud, cloud privé, sur site, hybride", "server"),
        ],
    },
    {
        "title": "Ressources", "url": "ressources/", "key": "ressources",
        "intro": ("Ressources", "Guides, articles et outils pour mieux gérer, conserver et protéger vos documents.", "Toutes les ressources"),
        "cols": 2,
        "items": [
            ("blog/", "Blog", "Actualités et analyses", "file"),
            ("ressources/guides/", "Guides", "Méthodes pas à pas", "book"),
            ("ressources/livres-blancs/", "Livres blancs", "Dossiers approfondis", "download"),
            ("ressources/webinars/", "Webinars", "Programme des sessions", "play"),
            ("ressources/glossaire/", "Glossaire", "Le vocabulaire de l'archivage", "library"),
            ("ressources/document-health-check/", "Document Health Check", "Évaluez votre maturité en 5 minutes", "target"),
        ],
    },
    {
        "title": "Entreprise", "url": "entreprise/", "key": "entreprise",
        "intro": ("African Digital Archives", "Une infrastructure africaine de confiance documentaire, née à Abidjan.", "Qui sommes-nous ?"),
        "cols": 2,
        "items": [
            ("entreprise/", "Qui sommes-nous ?", "Vision, mission, valeurs", "users"),
            ("entreprise/notre-approche/", "Notre approche", "Commencer par un pilote", "target"),
            ("entreprise/equipe/", "Équipe et carrières", "Les métiers qui font ADA", "briefcase"),
            ("entreprise/afrique/", "Expansion africaine", "De la Côte d'Ivoire au continent", "globe"),
            ("academy/", "ARCHIVA Academy", "Formations et certificats", "graduation"),
            ("contact/", "Contact", "Demander un audit", "mail"),
        ],
    },
]


def _menu_html(page):
    out = ['<ul id="primary-menu" class="menu nav-menu">']
    for m in MENU:
        cur = page.nav == m["key"] or (m["key"] == "ressources" and page.nav in ("blog", "ressources")) \
            or (m["key"] == "entreprise" and page.nav in ("entreprise", "academy", "contact"))
        cls = "menu-item menu-item-type-post_type menu-item-has-children menu-item-mega"
        if cur:
            cls += " current-menu-ancestor current-menu-parent"
        intro_t, intro_p, intro_btn = m["intro"]
        items = []
        for url, t, d, ic in m["items"]:
            icls = "menu-item menu-item-type-post_type"
            if page.path == url:
                icls += " current-menu-item"
            items.append(
                f'<li class="{icls}"><a href="~/{url}"><span class="menu-icon">{icon(ic)}</span>'
                f'<span><span class="menu-item-title">{t}</span><span class="menu-item-description">{d}</span></span></a></li>')
        colcls = " cols-2" if m.get("cols") == 2 else ""
        out.append(
            f'<li class="{cls}"><a href="~/{m["url"]}" aria-haspopup="true" aria-expanded="false">{m["title"]}{icon("chevron-down", "chev")}</a>'
            f'<div class="sub-menu-wrap"><div class="container"><div class="mega-menu">'
            f'<div class="mega-menu__intro"><h3>{intro_t}</h3><p>{intro_p}</p>'
            f'<a class="more-link" href="~/{m["url"]}">{intro_btn} {icon("arrow-right")}</a></div>'
            f'<ul class="sub-menu{colcls}">{"".join(items)}</ul></div></div></div></li>')
    out.append("</ul>")
    return "".join(out)


# ---------------------------------------------------------------------------
# Block helpers
# ---------------------------------------------------------------------------
def btn(text, href, style=None, arrow=True, small=False, attrs=""):
    cls = "wp-block-button"
    if style:
        cls += f" is-style-{style}"
    if small:
        cls += " is-small"
    arr = icon("arrow-right") if arrow else ""
    return f'<div class="{cls}"><a class="wp-block-button__link wp-element-button" href="{href}"{attrs}>{text}{arr}</a></div>'


def buttons(*b, center=False):
    c = " is-content-justification-center" if center else ""
    return f'<div class="wp-block-buttons{c}">{"".join(b)}</div>'


def section(inner, bg="white", cls="", id=None, container=""):
    idattr = f' id="{id}"' if id else ""
    ccls = f"container {container}".strip()
    return (f'<div class="wp-block-group section has-{bg}-background-color {cls}"{idattr}>'
            f'<div class="{ccls}">{inner}</div></div>')


def intro(h2, p="", eyebrow="", center=False, split=False, tag="h2"):
    cls = "section-intro"
    if center:
        cls += " has-text-align-center"
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    if split:
        return (f'<div class="{cls} split"><div>{eb}<{tag} class="wp-block-heading">{h2}</{tag}></div>'
                f'<div><p>{p}</p></div></div>')
    pp = f"<p>{p}</p>" if p else ""
    return f'<div class="{cls}">{eb}<{tag} class="wp-block-heading">{h2}</{tag}>{pp}</div>'


def cols(*items, n=None, cls=""):
    n = n or len(items)
    return (f'<div class="wp-block-columns cols-{n} {cls}" style="--cols:{n}">'
            + "".join(f'<div class="wp-block-column">{i}</div>' for i in items) + "</div>")


def card(title, text="", ic=None, href=None, link="En savoir plus", extra="", tag="", dark=False, flat=False):
    icon_html = f'<div class="card__icon">{icon(ic)}</div>' if ic else ""
    tag_html = f'<span class="card__tag">{tag}</span>' if tag else ""
    cls = "card" + (" is-dark" if dark else "") + (" is-flat" if flat else "")
    t = f"<p>{text}</p>" if text else ""
    if href:
        return (f'<a class="{cls}" href="{href}">{tag_html}{icon_html}<h3>{title}</h3>{t}{extra}'
                f'<span class="more-link">{link} {icon("arrow-right")}</span></a>')
    return f'<div class="{cls}">{tag_html}{icon_html}<h3>{title}</h3>{t}{extra}</div>'


def feature(title, text, ic="check", h="h3"):
    return (f'<div class="feature"><div class="feature__icon">{icon(ic)}</div>'
            f'<div><{h}>{title}</{h}><p>{text}</p></div></div>')


def ul(items, style="check", cls=""):
    return f'<ul class="wp-block-list is-style-{style} {cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def chips(items):
    return '<ul class="chips">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def img(name, alt, w=1600, h=1000, frame=False, url_label="app.archiva360.africa", caption="", cls="", lazy=True):
    loading = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    tag = (f'<img width="{w}" height="{h}" src="~/{SITE["uploads"]}{name}" alt="{html.escape(alt, quote=True)}"'
           f' class="wp-image-{abs(hash(name)) % 900 + 100}"{loading}>')
    if frame:
        tag = (f'<div class="browser-frame"><div class="browser-frame__bar"><i></i><i></i><i></i>'
               f'<span>{url_label}</span></div>{tag}</div>')
    cap = f'<figcaption class="wp-element-caption">{caption}</figcaption>' if caption else ""
    return f'<figure class="wp-block-image size-large {cls}">{tag}{cap}</figure>'


def media_text(media, content, right=False):
    cls = "wp-block-media-text is-stacked-on-mobile" + (" has-media-on-the-right" if right else "")
    return (f'<div class="{cls}"><div class="wp-block-media-text__media">{media}</div>'
            f'<div class="wp-block-media-text__content">{content}</div></div>')


def cta_band(h, p, *b):
    return (f'<div class="cta-band"><div><h2>{h}</h2><p>{p}</p></div>'
            f'{buttons(*b)}</div>')


def steps(items, h="h3"):
    return '<ol class="steps">' + "".join(
        f"<li><div><{h}>{t}</{h}><p>{d}</p></div></li>" for t, d in items) + "</ol>"


def faq(items):
    return "".join(
        f'<details class="wp-block-details"><summary>{q}</summary><div><p>{a}</p></div></details>' for q, a in items)


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<figure class="wp-block-table {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></figure>'


def notice(text, kind=""):
    k = f" is-{kind}" if kind else ""
    return f'<div class="notice{k}"><p>{text}</p></div>'


def stat(value, label):
    return f'<div class="stat"><span class="stat__value">{value}</span><span class="stat__label">{label}</span></div>'


def tiles(items):
    return '<div class="tiles">' + "".join(
        f'<a class="sector-tile" href="~/{u}"><span class="card__icon">{icon(ic)}</span>{t}{icon("arrow-right", "arrow")}</a>'
        for u, t, ic in items) + "</div>"


def page_hero(title, lead="", crumbs=None, eyebrow="", btns="", media="", light=False):
    cls = "page-hero" + (" has-media" if media else "") + (" is-light" if light else "")
    bc = breadcrumbs(crumbs) if crumbs else ""
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    ld = f'<p class="page-hero__lead">{lead}</p>' if lead else ""
    text = f'<div class="page-hero__text">{bc}{eb}<h1 class="entry-title">{title}</h1>{ld}{btns}</div>'
    med = f'<div class="page-hero__media">{media}</div>' if media else ""
    return f'<header class="{cls}"><div class="container">{text}{med}</div></header>'


def breadcrumbs(crumbs):
    parts = ['<span><a href="~/">Accueil</a></span>']
    for i, (label, url) in enumerate(crumbs):
        if i == len(crumbs) - 1 or not url:
            parts.append(f'<span class="breadcrumb_last" aria-current="page">{label}</span>')
        else:
            parts.append(f'<span><a href="~/{url}">{label}</a></span>')
    sep = ' <span class="sep">›</span> '
    return f'<nav class="yoast-breadcrumbs" aria-label="Fil d\'Ariane"><span>{sep.join(parts)}</span></nav>'


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
def _header(page):
    return f'''<a class="skip-link screen-reader-text" href="#primary">Aller au contenu</a>
<div class="top-bar">
  <div class="container">
    <div class="top-bar__left">
      <span class="top-bar__item">{icon("map-pin")}{SITE["city"]}</span>
      <a class="top-bar__item" href="mailto:{SITE["email"]}">{icon("mail")}{SITE["email"]}</a>
      <span class="top-bar__item">{icon("clock")}Lun – Ven, 8 h – 17 h (GMT)</span>
    </div>
    <div class="top-bar__right">
      <a class="top-bar__item" href="~/ressources/document-health-check/">{icon("target")}Document Health Check</a>
      <a class="top-bar__item" href="~/espace-client/">{icon("user")}Espace client</a>
      <div class="lang-switcher" aria-label="Langue">
        <span class="current-lang" lang="fr" aria-current="true">FR</span>
        <span class="lang-soon" lang="en" title="English version coming soon">EN</span>
      </div>
    </div>
  </div>
</div>
<header id="masthead" class="site-header">
  <div class="container">
    <div class="site-branding">
      <a href="~/" class="custom-logo-link" rel="home" aria-label="{SITE["name"]} — accueil">
        {LOGO}
        <span class="site-title-wrap"><span class="site-title">ADA</span><span class="site-description">African Digital Archives</span></span>
      </a>
    </div>
    <nav id="site-navigation" class="main-navigation" aria-label="Menu principal">
      {_menu_html(page)}
    </nav>
    <div class="header-actions">
      <button class="search-toggle" aria-expanded="false" aria-controls="header-search" aria-label="Rechercher">{icon("search")}</button>
      {btn("Demander un audit", "~/contact/?sujet=audit", arrow=False, small=True)}
      <button class="menu-toggle" aria-controls="site-navigation" aria-expanded="false" aria-label="Ouvrir le menu">{icon("menu")}</button>
    </div>
  </div>
  <div class="header-search" id="header-search">
    <div class="container">
      <form role="search" method="get" class="search-form" action="~/recherche/">
        <label class="screen-reader-text" for="header-search-field">Rechercher :</label>
        <input type="search" id="header-search-field" class="search-field" placeholder="Rechercher une solution, un secteur, un article…" name="s">
        <button type="submit" class="button">Rechercher</button>
      </form>
    </div>
  </div>
</header>'''


def _social():
    names = {"linkedin": "LinkedIn", "facebook": "Facebook", "youtube": "YouTube", "whatsapp": "WhatsApp"}
    links = "".join(f'<a href="{html.escape(u, quote=True)}" aria-label="{names[k]}" target="_blank" rel="noopener">{icon(k)}</a>'
                    for k, u in SITE["social"].items() if u)
    return f'<div class="social-links">{links}</div>' if links else ""


def _footer(page):
    def col(title, links):
        lis = "".join(f'<li><a href="~/{u}">{t}</a></li>' for u, t in links)
        return f'<section class="widget widget_nav_menu"><h2 class="widget-title">{title}</h2><ul class="menu">{lis}</ul></section>'
    sol = [(u, t) for u, t, _, _ in MENU[0]["items"][:7]]
    sec = [(u, t) for u, t, _, _ in MENU[2]["items"][:7]]
    ent = [("entreprise/", "Qui sommes-nous ?"), ("archiva360/", "ARCHIVA360"), ("services/", "Services"),
           ("academy/", "ARCHIVA Academy"), ("blog/", "Blog"), ("entreprise/equipe/", "Carrières"), ("contact/", "Contact")]
    footer_cta = "" if page.path.startswith("contact/") else f'''
  <div class="footer-cta"><div class="container">
    <div><h2>Parlons de vos archives.</h2><p>Diagnostic gratuit, audit documentaire, projet pilote : commençons par un premier échange.</p></div>
    {buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"), btn("Voir ARCHIVA360", "~/archiva360/", "outline"))}
  </div></div>'''
    return f'''<footer id="colophon" class="site-footer">{footer_cta}
  <div class="footer-widgets"><div class="container">
    <section class="widget widget_about">
      <a href="~/" class="custom-logo-link" rel="home">{LOGO_LIGHT}<span class="site-title-wrap"><span class="site-title">ADA</span><span class="site-description">African Digital Archives</span></span></a>
      <p>ADA accompagne les organisations africaines dans la transformation de leurs archives physiques et numériques en un patrimoine documentaire sécurisé, organisé, accessible et durable.</p>
      {_social()}
    </section>
    {col("Solutions", sol)}
    {col("Secteurs", sec)}
    {col("ADA", ent)}
    <section class="widget widget_newsletter">
      <h2 class="widget-title">Lettre d'information</h2>
      <p>Un e-mail par mois : méthodes d'archivage, cadre réglementaire, nouveautés ARCHIVA360.</p>
      <form class="newsletter-form" novalidate>
        <label class="screen-reader-text" for="nl-email-{page.id}">Adresse e-mail</label>
        <input type="email" id="nl-email-{page.id}" name="email" placeholder="Votre e-mail professionnel" autocomplete="email">
        <button type="submit" class="button">S'inscrire</button>
        <p class="nl-msg" aria-live="polite"></p>
      </form>
    </section>
  </div></div>
  <div class="site-info"><div class="container">
    <span>© <span class="current-year">2026</span> African Digital Archives (ADA). Tous droits réservés.</span>
    <ul>
      <li><a href="~/mentions-legales/">Mentions légales</a></li>
      <li><a href="~/politique-de-confidentialite/">Politique de confidentialité</a></li>
      <li><a href="~/politique-de-confidentialite/#cookies">Cookies</a></li>
      <li><a href="~/plan-du-site/">Plan du site</a></li>
    </ul>
  </div></div>
</footer>
<div id="cookie-notice" role="dialog" aria-live="polite" aria-label="Cookies">
  <p class="cn-title">Votre vie privée</p>
  <p>Ce site utilise uniquement des cookies techniques nécessaires à son fonctionnement et, avec votre accord, des cookies de mesure d'audience. <a href="~/politique-de-confidentialite/#cookies">En savoir plus</a></p>
  <div class="cn-buttons">
    <button class="button cn-button" data-cookie-set="accept">Accepter</button>
    <button class="button cn-button cn-refuse" data-cookie-set="refuse">Refuser</button>
  </div>
</div>
<button id="scroll-up" aria-label="Retour en haut de page">{icon("arrow-up")}</button>'''


def render(page):
    r = page.root
    if page.kind == "404":
        # 404.html is served for any missing URL, so it needs absolute links
        from urllib.parse import urlparse
        r = urlparse(SITE["base_url"]).path
    seo = page.seo_title or f"{page.title} | {SITE['name']}"
    desc = html.escape(page.description, quote=True)
    canonical = SITE["base_url"] + page.path
    body_class = f"{page.body_class} page-id-{page.id} wp-custom-logo wp-embed-responsive"
    og_type = "article" if page.kind == "post" else "website"
    settings = json.dumps({"contactEmail": SITE["email"], "formEndpoint": SITE["form_endpoint"], "root": r or "./"}, ensure_ascii=False)
    schema = ""
    if page.path == "":
        schema = ('<script type="application/ld+json" class="yoast-schema-graph">' + json.dumps({
            "@context": "https://schema.org", "@type": "Organization", "name": SITE["name"],
            "alternateName": "ADA", "url": SITE["base_url"], "slogan": SITE["tagline"],
            "address": {"@type": "PostalAddress", "addressLocality": "Abidjan", "addressCountry": "CI"}},
            ensure_ascii=False) + "</script>")
    if page.kind == "app":
        doc = f'''<!doctype html>
<html lang="fr-FR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(seo)}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="stylesheet" href="~/{SITE['theme']}assets/css/archiva360-demo.css?ver={SITE['version']}">
<link rel="icon" href="~/wp-content/uploads/2026/09/cropped-ada-icon-32x32.png" sizes="32x32">
</head>
<body class="{body_class}">
{page.body}
{page.scripts}
</body>
</html>
'''
        return doc.replace('href="~/', f'href="{r or "./"}').replace('src="~/', f'src="{r or "./"}')
    doc = f'''<!doctype html>
<html lang="fr-FR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="profile" href="https://gmpg.org/xfn/11">
<title>{html.escape(seo)}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:locale" content="fr_FR">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{html.escape(seo, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:image" content="{SITE['base_url']}{SITE['uploads']}og-ada.png">
<meta name="twitter:card" content="summary_large_image">
{schema}
<link rel="preload" href="~/{SITE['theme']}assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" id="ada-archives-style-css" href="~/{SITE['theme']}style.css?ver={SITE['version']}" media="all">
<link rel="icon" href="~/wp-content/uploads/2026/09/cropped-ada-icon-32x32.png" sizes="32x32">
<link rel="icon" href="~/wp-content/uploads/2026/09/cropped-ada-icon-192x192.png" sizes="192x192">
<link rel="apple-touch-icon" href="~/wp-content/uploads/2026/09/cropped-ada-icon-180x180.png">
{page.extra_head}
</head>
<body class="{body_class}">
<div id="page" class="site">
{_header(page)}
<div id="content" class="site-content">
{page.hero}
<main id="primary" class="site-main">
{page.body}
</main>
</div>
{_footer(page)}
</div>
<script id="ada-theme-js-extra">var adaSettings = {settings};</script>
{page.scripts}
<script src="~/{SITE['theme']}assets/js/theme.js?ver={SITE['version']}" id="ada-theme-js"></script>
</body>
</html>
'''
    doc = doc.replace('href="~/', f'href="{r or "./"}').replace('src="~/', f'src="{r or "./"}') \
             .replace('action="~/', f'action="{r or "./"}').replace('data-base="~/', f'data-base="{r or "./"}')
    return doc


def text_of(page):
    t = re.sub(r"<(script|style|svg)[\s\S]*?</\1>", " ", page.hero + " " + page.body)
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(re.sub(r"\s+", " ", t)).strip()
    return t


def write_all(out_dir):
    index = []
    for p in PAGES:
        dest = os.path.join(out_dir, p.path, "index.html") if p.kind != "404" else os.path.join(out_dir, "404.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(render(p))
        if p.search:
            index.append({"u": p.path, "t": p.title, "d": p.description, "c": text_of(p)[:3500]})
    js = "window.adaSearchIndex = " + json.dumps(index, ensure_ascii=False, separators=(",", ":")) + ";\n"
    with open(os.path.join(out_dir, SITE["theme"], "assets/js/search-index.js"), "w", encoding="utf-8") as f:
        f.write(js)
    # sitemap + robots
    urls = "".join(
        f"<url><loc>{SITE['base_url']}{p.path}</loc></url>" for p in PAGES if p.kind != "404" and not p.path.startswith(("archiva360/espace/", "archiva360/connexion/")))
    with open(os.path.join(out_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                + urls + "</urlset>\n")
    with open(os.path.join(out_dir, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nDisallow: /tools/\nDisallow: /espace-client/\nDisallow: /archiva360/espace/\n\nSitemap: {SITE['base_url']}sitemap.xml\n")
    return len(PAGES)
