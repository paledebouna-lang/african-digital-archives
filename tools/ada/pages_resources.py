import datetime

from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons,
                   faq, page_hero, notice, chips, POSTS as REG, SITE)
from .icons import icon
from .posts import POSTS, CATEGORIES

MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]


def fdate(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def post_card(p, heading="h3"):
    return (f'<article class="post-card post type-post status-publish category-{p["cat"][0]}" data-cat="{p["cat"][0]}">'
            f'<a class="post-thumbnail" href="~/blog/{p["slug"]}/" tabindex="-1" aria-hidden="true">'
            f'<img width="1200" height="675" src="~/{SITE["uploads"]}{p["cover"]}" alt="" loading="lazy" decoding="async"></a>'
            f'<div class="entry-wrap"><div class="entry-meta"><span class="cat-links"><a href="~/blog/categorie/{p["cat"][0]}/">{p["cat"][1]}</a></span>'
            f'<span class="posted-on"><time datetime="{p["date"]}">{fdate(p["date"])}</time></span></div>'
            f'<{heading} class="entry-title"><a href="~/blog/{p["slug"]}/" rel="bookmark">{p["title"]}</a></{heading}>'
            f'<div class="entry-summary"><p>{p["excerpt"]}</p></div>'
            f'<a class="read-more" href="~/blog/{p["slug"]}/">Lire l\'article {icon("arrow-right")}</a></div></article>')


def sidebar(current=None):
    counts = {c: sum(1 for p in POSTS if p["cat"][0] == c) for c, _ in CATEGORIES}
    cats = "".join(f'<li class="cat-item"><a href="~/blog/categorie/{c}/">{n}</a> <span class="count">({counts[c]})</span></li>' for c, n in CATEGORIES if counts[c])
    recent = "".join(f'<li><a href="~/blog/{p["slug"]}/">{p["title"]}</a><span class="post-date">{fdate(p["date"])}</span></li>' for p in POSTS[:5] if p["slug"] != current)
    tags = sorted({t for p in POSTS for t in p["tags"]})
    tagc = "".join(f'<a href="~/recherche/?s={t.replace(" ", "+")}" class="tag-cloud-link">{t}</a>' for t in tags)
    return f'''<aside id="secondary" class="widget-area" aria-label="Barre latérale">
<section class="widget widget_search"><h2 class="widget-title">Rechercher</h2>
<form role="search" method="get" class="search-form" action="~/recherche/"><label><span class="screen-reader-text">Rechercher :</span><input type="search" class="search-field" placeholder="Rechercher…" name="s"></label><button type="submit" class="search-submit button" aria-label="Rechercher">{icon("search")}</button></form></section>
<section class="widget widget_categories"><h2 class="widget-title">Catégories</h2><ul>{cats}</ul></section>
<section class="widget widget_recent_entries"><h2 class="widget-title">Articles récents</h2><ul>{recent}</ul></section>
<section class="widget widget_cta"><h3>Document Health Check</h3><p>Évaluez la maturité documentaire de votre organisation en 20 questions.</p>{btn("Faire le test", "~/ressources/document-health-check/", "white", small=True)}</section>
<section class="widget widget_tag_cloud"><h2 class="widget-title">Étiquettes</h2><div class="tagcloud">{tagc}</div></section>
</aside>'''


GLOSSARY = [
    ("Accès (droits d')", "", "Autorisations accordées à un utilisateur ou un rôle pour consulter, modifier, partager ou archiver un document."),
    ("Archivage électronique", "", "Ensemble des moyens qui permettent de conserver des documents numériques dans des conditions garantissant leur intégrité, leur traçabilité et leur lisibilité pendant la durée requise."),
    ("Archives", "", "Ensemble des documents produits ou reçus par une personne ou une organisation dans l'exercice de son activité, quels que soient leur date, leur forme et leur support."),
    ("Archives hybrides", "", "Dossier dont une partie existe sur papier et une autre sous forme numérique. Cas extrêmement courant."),
    ("Audit trail", "Journal d'audit", "Enregistrement chronologique et inaltérable de toutes les opérations : qui, quoi, quand, depuis où, quelle action."),
    ("Blockchain", "Registre distribué", "Registre partagé et inviolable. En archivage, il sert à ancrer l'empreinte d'un document pour prouver son existence et son intégrité, pas à stocker le document."),
    ("Checksum", "Empreinte", "Voir Empreinte numérique."),
    ("Chiffrement", "", "Transformation des données pour qu'elles ne soient lisibles qu'avec une clé. S'applique au repos (stockage) et en transit (réseau)."),
    ("Communicabilité", "", "Possibilité, selon les règles applicables, de communiquer un document au public ou à un demandeur."),
    ("Coffre-fort numérique", "Vault", "Espace de conservation à sécurité renforcée pour les documents hautement sensibles."),
    ("Cycle de vie", "", "Étapes successives d'un document : création, usage actif, semi-actif, archivage, conservation longue durée, sort final."),
    ("Disaster recovery", "Plan de reprise d'activité", "Ensemble des mesures qui permettent de restaurer les systèmes et les données après un sinistre."),
    ("Durée de conservation", "Durée d'utilité administrative", "Période pendant laquelle un document doit être conservé, fixée selon les règles de l'organisation et le cadre juridique."),
    ("Empreinte numérique", "Hash, SHA-256", "Suite de caractères calculée à partir du contenu d'un fichier. Toute modification du fichier change l'empreinte."),
    ("Événement déclencheur", "", "Événement à partir duquel court la durée de conservation : fin de contrat, départ d'un salarié, clôture d'exercice."),
    ("Gel juridique", "Legal hold", "Suspension de toute destruction de documents liés à un contentieux, un audit ou une enquête."),
    ("GED", "Gestion électronique des documents", "Outils pour créer, capturer, classer, partager, rechercher et travailler sur les documents au quotidien."),
    ("GEC", "Gestion électronique du courrier", "Gestion du courrier entrant, sortant et interne : enregistrement, affectation, traitement, réponse, archivage."),
    ("Horodatage", "", "Attribution d'une date et d'une heure certaines à un document ou une opération, idéalement par un tiers de confiance."),
    ("IDP", "Intelligent Document Processing", "Traitement intelligent des documents : classification automatique et extraction des données par l'IA."),
    ("Indexation", "", "Attribution de métadonnées ou de mots-clés à un document pour permettre de le retrouver."),
    ("Intégrité", "", "Garantie qu'un document n'a pas été modifié depuis sa création ou son archivage."),
    ("ISO 14721", "OAIS", "Norme décrivant le modèle de référence d'un système ouvert d'archivage pour la préservation à long terme."),
    ("ISO 15489", "", "Norme internationale de référence pour le records management."),
    ("ISO 16363", "", "Norme d'audit et de certification des dépôts numériques fiables."),
    ("ISO 19005", "PDF/A", "Format PDF destiné à la conservation à long terme."),
    ("ISO 23081", "", "Norme relative aux métadonnées pour les documents d'activité."),
    ("ISO 27001", "", "Norme de système de management de la sécurité de l'information."),
    ("Métadonnées", "", "Informations qui décrivent un document : titre, auteur, dates, type, service, confidentialité, durée de conservation, empreinte…"),
    ("MFA", "Authentification multifacteur", "Connexion qui exige au moins deux preuves d'identité, par exemple un mot de passe et un code reçu sur un téléphone."),
    ("Migration", "", "Transfert de documents d'un système, d'un support ou d'un format vers un autre, sans perte d'information ni d'intégrité."),
    ("Multi-tenant", "", "Architecture où plusieurs organisations utilisent la même plateforme, chacune dans un espace strictement isolé."),
    ("Numérisation", "", "Transformation d'un document papier en fichier numérique par scan ou photographie."),
    ("OCR", "Reconnaissance optique de caractères", "Technologie qui transforme l'image d'un texte en texte exploitable par l'ordinateur."),
    ("On-premise", "Sur site", "Installation d'un logiciel dans l'infrastructure informatique du client."),
    ("Plan de classement", "", "Structure hiérarchique (fonctions, séries, sous-séries, types de documents) qui organise les documents d'une organisation."),
    ("Préservation numérique", "", "Ensemble des actions qui maintiennent l'accès à l'information dans la durée, malgré l'évolution des formats, logiciels et supports."),
    ("QR code", "", "Code-barres en deux dimensions. Apposé sur une boîte ou un dossier, il permet d'ouvrir sa fiche d'un simple scan."),
    ("RBAC", "Contrôle d'accès basé sur les rôles", "Attribution des droits selon le rôle de l'utilisateur : archiviste, auditeur, direction, employé…"),
    ("Records management", "Gestion des documents d'activité", "Gestion des documents selon leur contexte, leurs responsables, leurs métadonnées, leurs règles et leur cycle de vie."),
    ("Règle 3-2-1", "", "Trois copies des données, sur deux supports différents, dont une hors site."),
    ("SAE", "Système d'archivage électronique", "Système qui conserve les documents selon des règles définies, avec traçabilité, intégrité et contrôle du cycle de vie."),
    ("SaaS", "Software as a Service", "Logiciel utilisé en ligne, sur abonnement, sans installation chez le client."),
    ("Signature électronique", "", "Procédé qui permet d'identifier le signataire et de garantir son consentement sur un document électronique."),
    ("Sort final", "", "Devenir d'un document à la fin de sa durée de conservation : destruction, versement aux archives historiques ou conservation permanente."),
    ("SSO", "Authentification unique", "Connexion unique qui donne accès à plusieurs applications avec les mêmes identifiants."),
    ("Versement", "", "Transfert de documents d'un service producteur vers le service d'archives."),
    ("Workflow", "Circuit de validation", "Enchaînement d'étapes (contrôle, validation, signature, archivage) par lesquelles passe un document."),
]

HC = [
    ("Localisation et volumes", [
        ("Savez-vous où se trouvent toutes vos archives papier ?", "Locaux, caves, bureaux, sites distants…"),
        ("Connaissez-vous le volume de vos archives (mètres linéaires, pages, fichiers) ?", ""),
        ("Vos fichiers numériques sont-ils centralisés ?", "Plutôt que répartis entre ordinateurs, clés USB, e-mails et WhatsApp."),
        ("Vos archives papier sont-elles conservées dans des locaux adaptés ?", "À l'abri de l'humidité, du feu et des nuisibles."),
    ]),
    ("Organisation", [
        ("Existe-t-il un plan de classement commun à toute l'organisation ?", ""),
        ("Pouvez-vous retrouver un contrat signé il y a 5 ans en moins de 10 minutes ?", ""),
        ("Les documents sont-ils nommés et décrits selon des règles communes ?", "Métadonnées, conventions de nommage."),
        ("Les doublons sont-ils identifiés et maîtrisés ?", ""),
    ]),
    ("Accès et sécurité", [
        ("Savez-vous qui a accès à vos documents confidentiels ?", ""),
        ("Les droits d'accès sont-ils revus quand un salarié change de poste ou part ?", ""),
        ("Les consultations et modifications de documents sensibles sont-elles tracées ?", ""),
        ("L'accès à vos systèmes documentaires est-il protégé par une authentification forte ?", "Mot de passe robuste et second facteur."),
    ]),
    ("Sauvegarde et risques", [
        ("Vos données sont-elles sauvegardées automatiquement ?", ""),
        ("Existe-t-il une copie de sauvegarde hors de vos locaux ?", ""),
        ("Que se passerait-il en cas d'incendie de vos locaux d'archives ?", "Les documents essentiels existent-ils ailleurs ?"),
        ("Pourriez-vous reprendre votre activité après une attaque par rançongiciel ?", "Sauvegardes isolées, restauration testée."),
    ]),
    ("Conservation et conformité", [
        ("Existe-t-il une politique de conservation (durées par type de document) ?", ""),
        ("Les destructions de documents sont-elles décidées, autorisées et tracées ?", ""),
        ("Vos documents numériques importants sont-ils dans des formats pérennes ?", "Par exemple PDF/A."),
        ("Connaissez-vous les obligations légales applicables à vos archives ?", "Transactions électroniques, archivage électronique, données personnelles."),
    ]),
]


def build():
    # ------------------------------------------------------------------ blog index
    cats_bar = '<div class="filter-bar" data-filter-target="#posts-grid" role="group" aria-label="Filtrer par catégorie"><button class="is-active" data-cat="all" aria-pressed="true">Tous</button>' + "".join(
        f'<button data-cat="{c}" aria-pressed="false">{n}</button>' for c, n in CATEGORIES) + "</div>"
    featured = POSTS[0]
    feat = (f'<article class="wp-block-media-text post-featured mb-l"><div class="wp-block-media-text__media"><a href="~/blog/{featured["slug"]}/">'
            f'<img width="1200" height="675" src="~/{SITE["uploads"]}{featured["cover"]}" alt="" style="border-radius:10px"></a></div>'
            f'<div class="wp-block-media-text__content"><span class="eyebrow">À la une · {featured["cat"][1]}</span><h2><a href="~/blog/{featured["slug"]}/" style="color:inherit">{featured["title"]}</a></h2>'
            f'<p class="lead">{featured["excerpt"]}</p><div class="entry-meta"><time datetime="{featured["date"]}">{fdate(featured["date"])}</time><span class="sep">·</span>{featured["read"]} min de lecture</div>'
            f'<a class="read-more" href="~/blog/{featured["slug"]}/">Lire l\'article {icon("arrow-right")}</a></div></article>')
    grid = '<div class="posts-grid" id="posts-grid">' + "".join(post_card(p, "h2") for p in POSTS[1:]) + "</div>"
    add(Page("blog", "Blog", "", description="Articles, analyses et guides d'ADA sur la gestion documentaire, l'archivage électronique, la numérisation et la préservation numérique en Afrique.",
             hero=page_hero("Blog", "Méthodes, cadre réglementaire, sécurité et innovation : nos analyses pour mieux gérer et préserver vos documents.", [("Blog", None)], "Ressources", light=True),
             body_class="blog archive", nav="blog"))
    from .core import PAGES
    PAGES[-1].body = (f'<div class="container"><div class="content-area-with-sidebar"><div class="posts-area">{feat}{cats_bar}{grid}'
                      f'<nav class="navigation pagination" aria-label="Pagination"><span class="has-muted-color has-small-font-size">Page 1 sur 1</span></nav></div>{sidebar()}</div></div>')

    for c, n in CATEGORIES:
        ps = [p for p in POSTS if p["cat"][0] == c]
        if not ps:
            continue
        add(Page(f"blog/categorie/{c}", f"Catégorie : {n}",
                 f'<div class="container"><div class="content-area-with-sidebar"><div class="posts-area"><div class="posts-grid">{"".join(post_card(p, "h2") for p in ps)}</div></div>{sidebar()}</div></div>',
                 description=f"Articles de la catégorie {n} du blog ADA.",
                 hero=page_hero(n, f"{len(ps)} article{'s' if len(ps) > 1 else ''} dans cette catégorie.", [("Blog", "blog/"), (n, None)], "Catégorie", light=True),
                 body_class="archive category", nav="blog", search=False))

    for i, p in enumerate(POSTS):
        prev_p = POSTS[i + 1] if i + 1 < len(POSTS) else None
        next_p = POSTS[i - 1] if i > 0 else None
        nav_html = '<nav class="navigation post-navigation" aria-label="Articles">'
        nav_html += (f'<div class="nav-previous"><a href="~/blog/{prev_p["slug"]}/" rel="prev"><span class="nav-subtitle">Article précédent</span><span class="nav-title">{prev_p["title"]}</span></a></div>' if prev_p else "<div></div>")
        nav_html += (f'<div class="nav-next"><a href="~/blog/{next_p["slug"]}/" rel="next"><span class="nav-subtitle">Article suivant</span><span class="nav-title">{next_p["title"]}</span></a></div>' if next_p else "<div></div>")
        nav_html += "</nav>"
        related = [q for q in POSTS if q is not p and (q["cat"][0] == p["cat"][0] or set(q["tags"]) & set(p["tags"]))][:3]
        if len(related) < 3:
            related += [q for q in POSTS if q is not p and q not in related][:3 - len(related)]
        tags = "".join(f'<a href="~/recherche/?s={t.replace(" ", "+")}" rel="tag">{t}</a>' for t in p["tags"])
        comments = f'''<div id="comments" class="comments-area"><div id="respond" class="comment-respond">
<h3 id="reply-title" class="comment-reply-title">Une question sur cet article ?</h3>
<form class="wpcf7-form comment-form" data-subject="Question sur l'article : {p["title"]}" novalidate>
<p class="comment-notes">Votre adresse e-mail ne sera pas publiée. Les champs obligatoires sont indiqués avec <span class="required">*</span></p>
<div class="form-row full"><span class="wpcf7-form-control-wrap"><label for="comment-{i}">Votre question <span class="required">*</span></label><textarea id="comment-{i}" name="question" data-label="Question" aria-required="true" rows="5"></textarea></span></div>
<div class="form-row"><span class="wpcf7-form-control-wrap"><label for="author-{i}">Nom <span class="required">*</span></label><input id="author-{i}" name="nom" data-label="Nom" type="text" aria-required="true" autocomplete="name"></span>
<span class="wpcf7-form-control-wrap"><label for="email-{i}">E-mail <span class="required">*</span></label><input id="email-{i}" name="email" data-label="E-mail" type="email" aria-required="true" autocomplete="email"></span></div>
<p class="form-submit"><input type="submit" class="submit" value="Envoyer"></p><div class="wpcf7-response-output" aria-hidden="true"></div></form></div></div>'''
        body = f'''<div class="container"><div class="content-area-with-sidebar"><article id="post-{i+100}" class="post type-post status-publish format-standard has-post-thumbnail hentry category-{p["cat"][0]}">
<div class="entry-content">{p["body"]}</div>
<footer class="entry-footer" style="max-width:760px;margin-top:32px"><span class="tags-links tagcloud">{tags}</span></footer>
<div class="share-links">Partager : <a href="https://www.linkedin.com/sharing/share-offsite/?url={SITE["base_url"]}blog/{p["slug"]}/" aria-label="Partager sur LinkedIn" target="_blank" rel="noopener">{icon("linkedin")}</a><a href="https://www.facebook.com/sharer/sharer.php?u={SITE["base_url"]}blog/{p["slug"]}/" aria-label="Partager sur Facebook" target="_blank" rel="noopener">{icon("facebook")}</a><a href="https://wa.me/?text={SITE["base_url"]}blog/{p["slug"]}/" aria-label="Partager sur WhatsApp" target="_blank" rel="noopener">{icon("whatsapp")}</a><button type="button" data-copy-link aria-label="Copier le lien">{icon("link")}</button></div>
<div class="author-box"><div class="author-box__avatar">ADA</div><div><h4>Rédaction ADA</h4><p>Les articles du blog sont rédigés par l'équipe d'African Digital Archives : archivistes, consultants et spécialistes de la numérisation et de la sécurité.</p></div></div>
{nav_html}{comments}</article>{sidebar(p["slug"])}</div></div>
{section(intro("À lire aussi", "", "Articles liés") + '<div class="posts-grid cols-3">' + "".join(post_card(q) for q in related) + "</div>", "mist", "is-compact")}'''
        hero = f'''<header class="page-hero is-light single-post-hero"><div class="container">
<nav class="yoast-breadcrumbs" aria-label="Fil d'Ariane"><span><span><a href="~/">Accueil</a></span> <span class="sep">›</span> <span><a href="~/blog/">Blog</a></span> <span class="sep">›</span> <span><a href="~/blog/categorie/{p["cat"][0]}/">{p["cat"][1]}</a></span> <span class="sep">›</span> <span class="breadcrumb_last" aria-current="page">{p["title"]}</span></span></nav>
<div class="entry-meta"><span class="cat-links"><a href="~/blog/categorie/{p["cat"][0]}/">{p["cat"][1]}</a></span><span class="sep">·</span><time class="entry-date published" datetime="{p["date"]}">{fdate(p["date"])}</time><span class="sep">·</span><span class="byline">Par Rédaction ADA</span><span class="sep">·</span><span>{p["read"]} min de lecture</span></div>
<h1 class="entry-title">{p["title"]}</h1><p class="page-hero__lead">{p["excerpt"]}</p>
<div class="post-thumbnail" style="margin-top:36px"><img width="1200" height="675" src="~/{SITE["uploads"]}{p["cover"]}" alt="" style="border-radius:10px;width:100%" fetchpriority="high"></div></div></header>'''
        pg = add(Page(f"blog/{p['slug']}", p["title"], body, description=p["excerpt"], hero=hero,
                      body_class="post-template-default single single-post single-format-standard", kind="post", nav="blog", date=p["date"],
                      seo_title=f"{p['title']} | Blog ADA"))
        REG.append(pg)

    # ------------------------------------------------------------------ ressources hub
    guides = [p for p in POSTS if p["cat"][0] == "guides"]
    add(Page("ressources", "Ressources",
             description="Blog, guides, livres blancs, webinars, glossaire et Document Health Check : les ressources d'ADA sur l'archivage et la gestion documentaire.",
             hero=page_hero("Ressources", "Tout ce qu'il faut pour comprendre l'archivage, préparer votre projet et convaincre en interne.", [("Ressources", None)], "Ressources"),
             body=section(cols(*[card(t, d, ic, f"~/{u}", l) for t, d, ic, u, l in [
                 ("Blog", "Analyses, méthodes et actualités de la gestion documentaire en Afrique.", "file", "blog/", "Lire le blog"),
                 ("Guides", "Des méthodes pas à pas : plan de classement, métadonnées, GED et SAE.", "book", "ressources/guides/", "Voir les guides"),
                 ("Livres blancs", "Des dossiers approfondis pour préparer votre projet.", "download", "ressources/livres-blancs/", "Voir les livres blancs"),
                 ("Webinars", "Des sessions en ligne avec nos archivistes et consultants.", "play", "ressources/webinars/", "Voir le programme"),
                 ("Glossaire", "Le vocabulaire de l'archivage expliqué simplement.", "library", "ressources/glossaire/", "Consulter le glossaire"),
                 ("Document Health Check", "Évaluez la maturité documentaire de votre organisation en 20 questions.", "target", "ressources/document-health-check/", "Faire le test")]], n=3))
             + section(intro("Derniers articles", "", "Blog") + '<div class="posts-grid cols-3">' + "".join(post_card(p) for p in POSTS[:3]) + "</div>", "mist"),
             nav="ressources"))

    add(Page("ressources/guides", "Guides",
             description="Guides pratiques ADA : construire un plan de classement, choisir les métadonnées, distinguer GED et SAE.",
             hero=page_hero("Guides pratiques", "Des méthodes concrètes pour avancer dès aujourd'hui, même sans logiciel.", [("Ressources", "ressources/"), ("Guides", None)], "Ressources", light=True),
             body=section('<div class="posts-grid cols-3">' + "".join(post_card(p) for p in guides) + "</div>"),
             nav="ressources"))

    wps = [("Archiver en Côte d'Ivoire", "Cadre juridique, bonnes pratiques et points de vigilance pour l'archivage électronique.", "scale"),
           ("De la GED à la préservation", "Construire une stratégie documentaire complète, étape par étape.", "layers"),
           ("Numériser un fonds d'archives", "Préparer, chiffrer et piloter un projet de numérisation de masse.", "scan")]
    add(Page("ressources/livres-blancs", "Livres blancs",
             description="Livres blancs ADA sur l'archivage électronique en Côte d'Ivoire, la stratégie documentaire et la numérisation de masse.",
             hero=page_hero("Livres blancs", "Des dossiers approfondis, rédigés par nos archivistes et consultants.", [("Ressources", "ressources/"), ("Livres blancs", None)], "Ressources", light=True),
             body=section(cols(*[f'<div class="resource-card"><div class="resource-card__type">LIVRE BLANC</div><div><span class="badge is-v3">À paraître</span><h3 class="mt-m">{t}</h3><p>{d}</p><a class="more-link" href="~/contact/?sujet=livre-blanc">Être prévenu de la parution {icon("arrow-right")}</a></div></div>' for t, d, _ in wps], n=3))
             + section(notice("Nos livres blancs sont en cours de rédaction. Inscrivez-vous à la lettre d'information en bas de page pour les recevoir dès leur parution."), "white", "is-compact"),
             nav="ressources"))

    webs = [("Introduction à l'archivage pour les dirigeants", "Pourquoi l'archivage est un sujet de direction, et par où commencer.", "45 min"),
            ("GED ou SAE : bien choisir", "Comprendre les différences et construire le bon cahier des charges.", "45 min"),
            ("Préparer un projet de numérisation", "Volumes, priorités, budget, qualité : les questions à se poser.", "60 min"),
            ("Le cadre ivoirien de l'archivage électronique", "Les textes de référence et leurs conséquences pratiques.", "60 min"),
            ("Démonstration ARCHIVA360", "Capture, recherche, conservation et audit en conditions réelles.", "45 min"),
            ("Protéger ses archives contre le ransomware", "Sauvegarde 3-2-1, droits d'accès, reprise d'activité.", "45 min")]
    add(Page("ressources/webinars", "Webinars",
             description="Programme des webinars ADA : archivage, GED, SAE, numérisation, cadre ivoirien, démonstrations ARCHIVA360.",
             hero=page_hero("Webinars", "Des sessions en ligne, gratuites, avec nos archivistes et consultants.", [("Ressources", "ressources/"), ("Webinars", None)], "Ressources", light=True),
             body=section(intro("Programme 2026 – 2027", "Les dates seront annoncées dans notre lettre d'information et sur LinkedIn.", "Programme")
                          + cols(*[card(t, d, "play", f"~/contact/?sujet=webinar", "Être informé", tag=dur) for t, d, dur in webs], n=3)),
             nav="ressources"))

    # ------------------------------------------------------------------ glossary
    letters = {}
    for term in sorted(GLOSSARY, key=lambda x: x[0].lower().replace("é", "e")):
        letters.setdefault(term[0][0].upper().replace("É", "E"), []).append(term)
    idx = "".join(f'<a href="#lettre-{l}">{l}</a>' if l in letters else f"<span>{l}</span>" for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    secs = "".join(
        f'<section class="glossary-section" aria-labelledby="lettre-{l}"><h2 class="glossary-letter" id="lettre-{l}">{l}</h2>'
        + "".join(f'<dl class="glossary-term"><dt>{t}{f"<small>{a}</small>" if a else ""}</dt><dd>{d}</dd></dl>' for t, a, d in terms)
        + "</section>" for l, terms in letters.items())
    add(Page("ressources/glossaire", "Glossaire de l'archivage",
             description="Glossaire de l'archivage et de la gestion documentaire : GED, SAE, records management, OCR, métadonnées, OAIS, plan de classement, sort final…",
             hero=page_hero("Glossaire de l'archivage", f"{len(GLOSSARY)} termes essentiels, expliqués simplement, pour parler le même langage que vos archivistes.", [("Ressources", "ressources/"), ("Glossaire", None)], "Ressources", light=True),
             body=section(f'<div class="container is-narrow" style="padding:0"><div class="glossary-search"><label for="glossary-filter">Filtrer les termes</label><input type="search" id="glossary-filter" placeholder="Ex. : OCR, conservation, intégrité…"></div>'
                          f'<nav class="glossary-index" aria-label="Index alphabétique">{idx}</nav>{secs}<p id="glossary-empty" class="is-hidden">Aucun terme ne correspond à votre recherche.</p></div>'),
             nav="ressources"))

    # ------------------------------------------------------------------ health check
    qn = 0
    qhtml = ""
    for group, qs in HC:
        qhtml += f'<h2 class="hc-group-title">{group}</h2>'
        for q, help_ in qs:
            qn += 1
            h = f'<p class="hc-help">{help_}</p>' if help_ else ""
            qhtml += (f'<div class="hc-question"><fieldset><legend><span>{qn:02d}</span>{q}</legend>{h}<div class="hc-options">'
                      f'<label><input type="radio" name="q{qn}" value="1"> Oui</label>'
                      f'<label><input type="radio" name="q{qn}" value="0.5"> Partiellement</label>'
                      f'<label><input type="radio" name="q{qn}" value="0"> Non / je ne sais pas</label></div></fieldset></div>')
    result = f'''<aside class="hc-result" aria-live="polite"><h3>Votre score</h3>
<div class="hc-gauge"><svg viewBox="0 0 180 180"><circle cx="90" cy="90" r="78" fill="none" stroke="rgba(255,255,255,.1)" stroke-width="14"/><circle id="hc-ring" cx="90" cy="90" r="78" fill="none" stroke="#6FB1FF" stroke-width="14" stroke-linecap="round" style="transition:stroke-dashoffset .5s,stroke .3s"/></svg>
<div class="hc-gauge__value"><div><b id="hc-score">–</b><small>sur 100</small></div></div></div>
<div class="hc-level" id="hc-level">Répondez aux questions</div><div class="hc-progress" id="hc-progress">0 / {qn} questions répondues</div>
<div class="hc-advice" id="hc-advice"></div>
<a class="wp-block-button__link" id="hc-cta" data-base="~/contact/" href="~/contact/">Discuter de mes résultats</a>
<p class="hc-disclaimer">0–30 : organisation faible · 31–60 : intermédiaire · 61–80 : bonne maturité · 81–100 : maturité avancée. Ce score est un outil d'orientation, pas une certification juridique.</p></aside>'''
    add(Page("ressources/document-health-check", "Document Health Check",
             description="Évaluez gratuitement la maturité documentaire de votre organisation en 20 questions : localisation, organisation, accès, sauvegarde, conservation.",
             hero=page_hero("Document Health Check", "20 questions, 5 minutes : évaluez la maturité documentaire de votre organisation et recevez trois priorités d'action. Vos réponses restent dans votre navigateur.",
                            [("Ressources", "ressources/"), ("Document Health Check", None)], "Outil gratuit"),
             body=section(f'<form id="healthcheck-form" class="healthcheck" onsubmit="return false"><div>{qhtml}</div>{result}</form>', "mist"),
             nav="ressources"))

    # ------------------------------------------------------------------ academy
    levels = [("Introduction à l'archivage", "Vocabulaire, types d'archives (papier, numériques, hybrides), enjeux pour l'organisation.", "Tous publics"),
              ("Gestion documentaire", "GED, GEC, classement, nommage, versions, partage.", "Utilisateurs, assistants"),
              ("Records management", "Plan de classement, métadonnées, cycle de vie, règles de conservation.", "Archivistes, référents"),
              ("Archivage électronique", "SAE, intégrité, traçabilité, horodatage, signature, cadre ivoirien.", "Archivistes, juristes, IT"),
              ("Préservation numérique", "OAIS, formats pérennes, migration, contrôle d'intégrité.", "Archivistes, IT"),
              ("Administration ARCHIVA360", "Paramétrage, rôles, règles, workflows, sécurité, sauvegardes.", "Administrateurs")]
    lv = "".join(f'<div class="academy-level"><span class="academy-level__num">{i:02d}</span><div><h3>Niveau {i} — {t}</h3><p>{d}</p></div><span class="badge">{w}</span></div>' for i, (t, d, w) in enumerate(levels, 1))
    weeks = ["Vocabulaire archivistique", "GED / GEC / SAE", "Records management", "Métadonnées", "Cycle de vie documentaire", "Numérisation / OCR",
             "Préservation numérique / OAIS", "Sécurité", "Cadre ivoirien", "Modèle économique", "Architecture logicielle", "Vente aux entreprises"]
    add(Page("academy", "ARCHIVA Academy",
             description="ARCHIVA Academy : six niveaux de formation à l'archivage, du vocabulaire de base à l'administration d'ARCHIVA360, avec certificats internes.",
             hero=page_hero("ARCHIVA Academy", "Former les archivistes, documentalistes, équipes informatiques et utilisateurs dont l'Afrique a besoin pour préserver sa mémoire documentaire.",
                            [("ARCHIVA Academy", None)], "Formation", buttons(btn("Demander le programme", "~/contact/?sujet=formation", "white"))),
             body=section(intro("Six niveaux progressifs", "Chaque niveau se conclut par une évaluation et un certificat interne ARCHIVA Academy.", "Parcours", split=True) + lv)
             + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                       + intro("Parcours dirigeant : 12 semaines", "Pour les dirigeants qui débutent dans l'archivage. Vous n'avez pas besoin de devenir archiviste : vous devez comprendre suffisamment le domaine pour prendre les bonnes décisions.", "Programme")
                       + '</div><div class="wp-block-column"><ol class="wp-block-list is-style-columns" style="padding-left:1.4em">' + "".join(f"<li><strong>Semaine {i}</strong> — {w}</li>" for i, w in enumerate(weeks, 1)) + "</ol></div></div>", "mist")
             + section(intro("Formats", "", "Modalités") + cols(*[feature(t, d, ic) for t, d, ic in [
                 ("En présentiel à Abidjan", "Sessions interentreprises ou dans vos locaux.", "users"),
                 ("À distance", "Classes virtuelles pour les équipes réparties dans plusieurs pays.", "globe"),
                 ("Sur mesure", "Programme adapté à votre organisation et à ARCHIVA360.", "compass")]], n=3))
             + section(cta_band("ARCHIVA Certified Partner", "À terme, nous certifierons des intégrateurs partenaires au Sénégal, au Bénin, au Togo, au Cameroun, au Burkina Faso, au Ghana, au Kenya, au Maroc et ailleurs.",
                                btn("Devenir partenaire", "~/contact/?sujet=partenariat", "white"))),
             nav="academy"))
