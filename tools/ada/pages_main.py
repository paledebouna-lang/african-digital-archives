from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons, faq,
                   page_hero, notice, steps, table, chips, stat, tiles, SITE, PAGES, MENU)
from .icons import icon
from .posts import POSTS

SUBJECTS = [("audit", "Demande d'audit documentaire"), ("demo", "Démonstration d'ARCHIVA360"), ("devis", "Devis ARCHIVA360"),
            ("numerisation", "Projet de numérisation"), ("migration", "Migration de documents"), ("conseil", "Conseil et conformité"),
            ("formation", "Formation / ARCHIVA Academy"), ("hebergement", "Hébergement et déploiement"), ("livre-blanc", "Livres blancs"),
            ("webinar", "Webinars"), ("partenariat", "Partenariat"), ("carriere", "Candidature"), ("question", "Autre question")]


def contact_form(default="audit"):
    opts = "".join(f'<option value="{v}"{" selected" if v == default else ""}>{t}</option>' for v, t in SUBJECTS)
    sectors = ["Administration publique", "Collectivité / mairie", "Banque / microfinance", "Assurance", "Entreprise privée", "Industrie / énergie / BTP",
               "Immobilier", "Juridique", "Santé", "Éducation / recherche", "ONG / organisme international", "Patrimoine / culture", "Autre"]
    countries = ["Côte d'Ivoire", "Sénégal", "Bénin", "Togo", "Burkina Faso", "Mali", "Niger", "Guinée", "Cameroun", "Gabon", "Congo", "RD Congo", "Ghana", "Nigeria", "Kenya", "Maroc", "Autre pays"]
    vols = ["Je ne sais pas encore", "Moins de 10 000 pages", "10 000 à 100 000 pages", "100 000 à 1 million de pages", "Plus d'un million de pages"]
    sel = lambda name, label, items, idn: (f'<span class="wpcf7-form-control-wrap"><label for="{idn}">{label}</label><select id="{idn}" name="{name}" data-label="{label}">'
                                            + "".join(f"<option>{x}</option>" for x in items) + "</select></span>")
    return f'''<div class="form-card"><div class="wpcf7 js" id="wpcf7-f214-o1" lang="fr-FR" dir="ltr">
<form class="wpcf7-form init" data-subject="Demande via le site ADA" novalidate>
<div class="form-row"><span class="wpcf7-form-control-wrap"><label for="cf7-name">Nom et prénom <span class="required">*</span></label><input id="cf7-name" name="nom" data-label="Nom" type="text" aria-required="true" autocomplete="name"></span>
<span class="wpcf7-form-control-wrap"><label for="cf7-org">Organisation <span class="required">*</span></label><input id="cf7-org" name="organisation" data-label="Organisation" type="text" aria-required="true" autocomplete="organization"></span></div>
<div class="form-row"><span class="wpcf7-form-control-wrap"><label for="cf7-email">E-mail professionnel <span class="required">*</span></label><input id="cf7-email" name="email" data-label="E-mail" type="email" aria-required="true" autocomplete="email"></span>
<span class="wpcf7-form-control-wrap"><label for="cf7-phone">Téléphone</label><input id="cf7-phone" name="telephone" data-label="Téléphone" type="tel" autocomplete="tel" placeholder="+225"></span></div>
<div class="form-row"><span class="wpcf7-form-control-wrap"><label for="cf7-role">Fonction</label><input id="cf7-role" name="fonction" data-label="Fonction" type="text" autocomplete="organization-title"></span>
{sel("pays", "Pays", countries, "cf7-country")}</div>
<div class="form-row">{sel("secteur", "Secteur", sectors, "cf7-sector")}
<span class="wpcf7-form-control-wrap"><label for="cf7-subject">Objet de la demande</label><select id="cf7-subject" name="objet" data-label="Objet">{opts}</select></span></div>
<div class="form-row full">{sel("volumes", "Volume approximatif de vos archives", vols, "cf7-volumes")}</div>
<div class="form-row full"><span class="wpcf7-form-control-wrap"><label for="cf7-message">Votre message</label><textarea id="cf7-message" name="message" data-label="Message" rows="6" placeholder="Types de documents, lieux de stockage, urgence, objectifs…"></textarea></span></div>
<div class="form-row full"><span class="wpcf7-form-control-wrap"><label class="wpcf7-acceptance"><input type="checkbox" name="consentement" value="oui" data-label="Consentement" aria-required="true"> <span>J'accepte que mes données soient utilisées pour répondre à ma demande, conformément à la <a href="~/politique-de-confidentialite/">politique de confidentialité</a>. <span class="required">*</span></span></label></span></div>
<input class="wpcf7-form-control wpcf7-submit has-spinner" type="submit" value="Envoyer la demande">
<div class="wpcf7-response-output" aria-live="polite"></div>
</form></div></div>'''


def build_home():
    from .pages_resources import post_card
    hero = f'''<section class="home-hero"><div class="container">
<div class="home-hero__copy"><span class="eyebrow">Gestion documentaire · Archivage · Préservation</span>
<h1>Préserver aujourd'hui. <em>Transmettre demain.</em></h1>
<p class="home-hero__lead">La plateforme africaine de gestion, d'archivage et de préservation documentaire. ADA transforme vos archives papier et numériques en un patrimoine organisé, sécurisé et durable.</p>
{buttons(btn("Demander un audit", "~/contact/?sujet=audit"), btn("Découvrir ARCHIVA360", "~/archiva360/", "outline"))}
<p class="home-hero__note">{icon("shield")}Hébergement en Côte d'Ivoire, en cloud privé ou dans vos locaux.</p></div>
<div class="home-hero__media">{img("archiva360-tableau-de-bord.png", "Tableau de bord de la plateforme ARCHIVA360", frame=True, lazy=False)}</div>
</div></section>
<div class="standards-strip"><div class="container"><p class="standards-strip__label">Une démarche fondée sur les références reconnues</p><ul>
<li><b>ISO 15489</b><span>Records management</span></li><li><b>ISO 14721</b><span>Préservation (OAIS)</span></li><li><b>ISO 23081</b><span>Métadonnées</span></li>
<li><b>PDF/A</b><span>ISO 19005</span></li><li><b>ISO 27001</b><span>Sécurité</span></li><li><b>Loi 2013-546</b><span>Côte d'Ivoire</span></li></ul></div></div>'''

    chaos = ["Dossiers papier", "Fichiers sur les ordinateurs", "Pièces jointes d'e-mails", "Fichiers WhatsApp", "Clés USB", "Disques externes", "Plusieurs serveurs", "Doublons", "Archives mal classées", "Durées de conservation inconnues", "Documents confidentiels trop exposés"]
    problem = section(
        '<div class="wp-block-columns cols-2 gap-lg is-vertically-aligned-center" style="--cols:2"><div class="wp-block-column">'
        + intro("Vos documents sont partout. Votre mémoire, nulle part.", "La plupart des organisations accumulent des tonnes de dossiers papier, des fichiers dispersés et des documents introuvables. Personne ne sait combien de temps les garder, ni qui peut les consulter.", "Le constat")
        + btn("Évaluer ma situation", "~/ressources/document-health-check/", "outline")
        + '</div><div class="wp-block-column"><div class="chaos-order" style="grid-template-columns:1fr">'
        + f'<div class="chaos-order__box is-chaos"><h3>Aujourd\'hui</h3>{chips(chaos)}</div>'
        + f'<div class="chaos-order__arrow" style="transform:rotate(90deg)">{icon("arrow-right")}</div>'
        + f'<div class="chaos-order__box is-order"><h3>Avec ADA : un patrimoine documentaire organisé</h3>{ul(["Chaque document classé selon un plan clair", "Retrouvé en quelques secondes", "Accessible aux seules bonnes personnes", "Conservé le temps qu’il faut, prouvé intact"])}</div>'
        + "</div></div></div>")

    chain = section(intro("Une seule chaîne, du carton à la préservation", "Au lieu de juxtaposer un scanner, un logiciel et un hébergeur, ADA prend en charge chaque étape de la vie de vos documents.", "Notre approche", center=True)
                    + '<ol class="chain">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in [
                        ("Archives papier", "Inventaire et préparation"), ("Numérisation", "Scan et contrôle qualité"), ("Organisation", "Plan de classement"),
                        ("GED", "Travail au quotidien"), ("Archivage électronique", "Règles et traçabilité"), ("Conservation", "Cycle de vie maîtrisé"),
                        ("Recherche", "Plein texte et métadonnées"), ("Preuve", "Empreinte et horodatage"), ("Préservation", "Lisible dans 30 ans")]) + "</ol>", "mist")

    poles = [
        ("consulting", "Consulting", "compass", "archiva360-plan-de-classement.png", "Comprendre vos fonds et fixer les règles",
         "Audit documentaire, plan de classement, politique d'archivage et conformité. Nos archivistes et juristes posent les règles avant de choisir l'outil.",
         ["Audit documentaire et cartographie des fonds", "Plan de classement et référentiel de conservation", "Politique d'archivage", "Accompagnement à la conformité"], "services/conseil/"),
        ("digitalisation", "Digitalisation", "scan", "archiva360-document-ocr.png", "Transformer le papier en information exploitable",
         "Notre centre de numérisation d'Abidjan prend en charge vos fonds : préparation, scan, OCR, indexation, contrôle qualité et import dans ARCHIVA360.",
         ["Scan A4, A3, livres, plans et grands formats", "OCR et indexation", "Contrôle qualité", "Migration de fonds existants"], "services/numerisation/"),
        ("software", "Software", "blocks", "archiva360-recherche-intelligente.png", "ARCHIVA360, la plateforme",
         "GED, archivage électronique, records management, archives physiques et IA documentaire dans un seul outil, en SaaS ou sur site.",
         ["20 modules, de la capture au portail public", "Recherche en langage naturel", "Workflows, courrier et signature", "Application mobile ARCHIVA GO"], "archiva360/"),
        ("trust", "Trust & Preservation", "shield", "archiva360-compliance-center.png", "Garantir l'intégrité dans la durée",
         "Coffre-fort numérique, empreinte et horodatage, sauvegarde 3-2-1, plan de reprise et préservation des formats selon le modèle OAIS.",
         ["Chiffrement, MFA, journal d'audit", "Empreinte SHA-256 et horodatage", "Sauvegarde 3-2-1 et reprise d'activité", "Préservation numérique OAIS"], "solutions/preservation-numerique/"),
    ]
    tabs_nav = "".join(f'<button role="tab" id="tab-{k}" aria-controls="panel-{k}" aria-selected="{"true" if i == 0 else "false"}" tabindex="{0 if i == 0 else -1}">{icon(ic)}{t}</button>' for i, (k, t, ic, *_ ) in enumerate(poles))
    panels = "".join(
        f'<div class="ada-tabs__panel" role="tabpanel" id="panel-{k}" aria-labelledby="tab-{k}"{"" if i == 0 else " hidden"}>'
        + media_text(img(shot, h, frame=True), f'<h3 style="font-size:1.7rem">{h}</h3><p class="lead">{p}</p>{ul(li)}<a class="more-link" href="~/{link}">En savoir plus {icon("arrow-right")}</a>')
        + "</div>" for i, (k, t, ic, shot, h, p, li, link) in enumerate(poles))
    poles_html = section(intro("Quatre métiers, un seul interlocuteur", "Nous ne vendons pas qu'un logiciel. Nous associons conseil archivistique, numérisation, technologie et préservation de confiance.", "Ce que nous faisons")
                         + f'<div class="ada-tabs"><div class="ada-tabs__nav" role="tablist" aria-label="Nos pôles">{tabs_nav}</div>{panels}</div>')

    product = section(
        '<div class="wp-block-columns cols-2 gap-lg is-vertically-aligned-center" style="--cols:2"><div class="wp-block-column">'
        + intro("ARCHIVA360 : capturer, gérer, archiver, préserver", "Un seul outil pensé pour les réalités africaines : archives physiques et numériques, plusieurs pays, français et anglais, cloud ou sur site.", "La plateforme")
        + cols(*[feature(t, d, ic, "h4") for t, d, ic in [
            ("Capture et OCR", "Scanner, importer, lire et extraire les données.", "scan"),
            ("Recherche intelligente", "« Factures supérieures à 5 millions FCFA ».", "search"),
            ("Records management", "Règles de conservation et échéances automatiques.", "hourglass"),
            ("Archives physiques", "Boîtes localisées et QR codes.", "qr")]], n=2, cls="gap-sm")
        + buttons(btn("Découvrir ARCHIVA360", "~/archiva360/", "white"), btn("Les 20 modules", "~/archiva360/modules/", "outline")).replace('class="wp-block-buttons', 'class="wp-block-buttons mt-l')
        + '</div><div class="wp-block-column">' + img("archiva360-archives-physiques.png", "Fiche d'une boîte d'archives dans ARCHIVA360", frame=True) + "</div></div>"
        + notice("<strong>Une règle non négociable :</strong> l'IA assiste, elle ne décide pas. Destruction, classement définitif et droits d'accès sont toujours validés par une personne habilitée, avec traçabilité.").replace('class="notice"', 'class="notice mt-l"'), "navy")

    sectors = section(intro("Pour les organisations qui ne peuvent pas perdre un document", "Administrations, banques, assurances, hôpitaux, universités, industries : chaque secteur a ses documents et ses obligations.", "Secteurs", split=True)
                      + tiles([(u, t, ic) for u, t, _, ic in MENU[2]["items"][:9]])
                      + f'<p class="mt-m"><a class="more-link" href="~/secteurs/">Tous les secteurs {icon("arrow-right")}</a></p>')

    method = section(
        '<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
        + intro("Commencer par un pilote", "Pas de grand projet à l'aveugle. Nous commençons par un audit et un fonds pilote pour que vous jugiez sur pièces.", "Méthode")
        + '<blockquote class="wp-block-quote"><p>« Nous analysons 10 000 dossiers de votre organisation, vous proposons un plan de classement et numérisons un fonds pilote de 1 000 dossiers. »</p><cite>Notre offre de démarrage : Audit + digitalisation pilote</cite></blockquote>'
        + card("Document Health Check", "Répondez à 20 questions et obtenez un premier score de maturité documentaire, avec trois priorités d'action.", "target", "~/ressources/document-health-check/", "Faire le test gratuit")
        + '</div><div class="wp-block-column">'
        + steps([("Diagnostic", "Un premier échange gratuit pour comprendre vos fonds et vos contraintes."), ("Audit documentaire", "Volumes, lieux de stockage, accès, risques et sauvegardes."),
                 ("Plan d'archivage", "Plan de classement et règles de conservation, définis avec un archiviste et un juriste."), ("Projet pilote", "Numérisation, OCR et indexation d'un premier fonds."),
                 ("Démonstration ARCHIVA360", "Vos propres documents, retrouvés en quelques secondes."), ("Déploiement et formation", "Mise en service, formation des équipes et accompagnement.")])
        + "</div></div>", "mist")

    stats = section('<div class="wp-block-columns cols-4" style="--cols:4">' + "".join(
        f'<div class="wp-block-column">{stat(v, l)}</div>' for v, l in [("9", "étapes de la chaîne documentaire couvertes"), ("20", "modules dans ARCHIVA360"), ("4", "modes de déploiement : SaaS, privé, sur site, hybride"), ("1", "interlocuteur, du carton à la préservation")]) + "</div>", "white", "is-compact")

    africa = section(
        '<div class="wp-block-columns cols-2 gap-lg is-vertically-aligned-center" style="--cols:2"><div class="wp-block-column">'
        + intro("Né en Côte d'Ivoire, pensé pour l'Afrique", "Un même cœur logiciel, adapté à chaque pays : règles, métadonnées, durées, langues et hébergement se configurent par pays.", "Expansion")
        + f'<a class="more-link" href="~/entreprise/afrique/">Notre feuille de route africaine {icon("arrow-right")}</a></div><div class="wp-block-column">'
        + '<div class="roadmap" style="grid-template-columns:repeat(2,1fr);border:0;gap:28px 24px">' + "".join(
            f'<div class="roadmap__step{" is-current" if i == 0 else ""}" style="border-top:2px solid rgba(255,255,255,.14)"><small>Étape {i+1}</small><h4>{t}</h4><p>{d}</p></div>'
            for i, (t, d) in enumerate([("Côte d'Ivoire", "Abidjan, premier centre de numérisation"), ("UEMOA", "Sénégal, Bénin, Togo, Burkina Faso"),
                                        ("Afrique centrale", "Cameroun, RDC, Gabon, Congo"), ("Afrique anglophone", "Ghana, Kenya, Nigeria")])) + "</div></div></div>", "navy")

    news = section(intro("Ressources et analyses", "", "Blog", split=True).replace("<div><p></p></div>", f'<div style="text-align:right"><a class="more-link" href="~/blog/">Tous les articles {icon("arrow-right")}</a></div>')
                   + '<div class="posts-grid cols-3">' + "".join(post_card(p) for p in POSTS[:3]) + "</div>")

    faqs = section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                   + intro("Questions fréquentes", "Les questions que nous posent le plus souvent les directions générales, les DSI et les archivistes.", "FAQ")
                   + btn("Nous contacter", "~/contact/", "outline") + '</div><div class="wp-block-column">'
                   + faq([("ADA est-il un éditeur de logiciel ou un prestataire de services ?", "Les deux. ADA commence comme une société de transformation documentaire (conseil, numérisation, migration) et édite la plateforme ARCHIVA360. Vous pouvez faire appel à nos services, à la plateforme, ou aux deux."),
                          ("Nos données restent-elles en Côte d'Ivoire ?", "Vous choisissez : hébergement par ADA, cloud privé, installation dans vos locaux ou architecture hybride. Pour les administrations, nous privilégions la souveraineté des données."),
                          ("Combien coûte un projet ?", "Cela dépend des volumes, du nombre d'utilisateurs et du niveau de sécurité. Les abonnements démarrent à partir de 25 000 FCFA par mois ; la numérisation est facturée à la page ou au projet. Un audit permet de chiffrer précisément."),
                          ("Faut-il tout numériser ?", "Non. L'audit identifie les fonds prioritaires : les documents les plus consultés, les plus précieux ou les plus menacés. Les autres peuvent rester sur papier, inventoriés et localisés grâce aux QR codes."),
                          ("La plateforme est-elle conforme à la réglementation ivoirienne ?", "ARCHIVA360 est conçue à partir du cadre ivoirien (transactions électroniques, archivage électronique, protection des données) et des normes internationales. Nous faisons valider chaque dispositif par un juriste et ne revendiquons aucune conformité sans validation indépendante.")])
                   + "</div></div>", "mist")

    p = add(Page("", "Accueil", problem + chain + poles_html + product + stats + sectors + method + africa + news + faqs,
                 seo_title="African Digital Archives (ADA) — Gestion documentaire, archivage et préservation en Afrique",
                 description="ADA accompagne les organisations africaines dans la transformation de leurs archives physiques et numériques : conseil, numérisation, plateforme ARCHIVA360, archivage électronique et préservation.",
                 hero=hero, body_class="home page-template-front-page", nav="home"))
    return p


def build_company():
    values = [("Confiance", "Nous préservons la mémoire des organisations : la confiance est notre premier produit.", "shield"),
              ("Rigueur", "Des méthodes archivistiques éprouvées, des normes reconnues, des résultats mesurés.", "check-circle"),
              ("Souveraineté", "Vos données restent sous votre contrôle, là où vous le décidez.", "server"),
              ("Transmission", "Former, documenter, rendre les équipes autonomes.", "graduation"),
              ("Ancrage africain", "Une solution pensée pour l'Afrique, pas une adaptation d'un logiciel étranger.", "globe"),
              ("Honnêteté", "Nous ne promettons pas une conformité que nous n'avons pas fait valider.", "scale")]
    diff = ["Pensée pour l'Afrique", "Multi-pays : Côte d'Ivoire, UEMOA, CEDEAO, Afrique", "Français et anglais, puis portugais et arabe", "Archives physiques et numériques",
            "IA documentaire", "Préservation longue durée, pas seulement du stockage", "Cloud et sur site", "Prix adaptés au marché africain", "Centre de numérisation", "Conseil et logiciel"]
    add(Page("entreprise", "Qui sommes-nous ?",
             description="African Digital Archives (ADA) : une infrastructure africaine de confiance documentaire, née à Abidjan. Vision, mission, valeurs et expertise.",
             hero=page_hero("Une infrastructure africaine de confiance documentaire", "ADA accompagne les organisations africaines dans la transformation de leurs archives physiques et numériques en un patrimoine documentaire sécurisé, organisé, accessible, traçable et durable.",
                            [("Entreprise", None)], "Qui sommes-nous ?"),
             body=section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                          + intro("Nous ne stockons pas vos documents. Nous préservons votre mémoire.", "", "Notre raison d'être")
                          + '</div><div class="wp-block-column"><p class="lead">Administrations, entreprises, universités, hôpitaux, institutions : partout en Afrique, des décennies de documents dorment dans des armoires, des caves, des disques externes et des messageries. Ils sont précieux, souvent uniques, et exposés au feu, à l\'eau, au temps et aux cyberattaques.</p>'
                          + "<p>ADA est née à Abidjan pour y répondre, avec une conviction : le problème n'est pas seulement technologique. Il faut à la fois des règles d'archivage, des bras pour numériser, une plateforme pour gérer et une garantie de conservation dans la durée. C'est pourquoi ADA réunit conseil, numérisation, logiciel et préservation.</p></div></div>")
             + section(cols(card("Vision", "Devenir l'infrastructure de confiance documentaire de l'Afrique : un réseau où chaque institution préserve et valorise son patrimoine documentaire.", "compass", dark=True),
                            card("Mission", "Transformer, organiser, sécuriser, conserver et valoriser les documents et archives des administrations, entreprises et institutions africaines.", "target", dark=True),
                            card("Ambition", "Construire à terme l'African Archive Network : des nœuds nationaux reliant institutions, entreprises, universités, bibliothèques et archives historiques, chacune gardant la maîtrise de ses accès.", "globe", dark=True), n=3), "navy")
             + section(intro("Nos valeurs", "", "Valeurs", center=True) + cols(*[feature(t, d, ic) for t, d, ic in values], n=3, cls="gap-lg"))
             + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                       + intro("Ce qui nous distingue", "Le marché de la GED existe déjà. Notre différence n'est pas de « faire de la GED », mais d'être la plateforme africaine intégrée de gouvernance, d'archivage et de préservation documentaire.", "Différenciation")
                       + '</div><div class="wp-block-column"><ol class="wp-block-list is-style-columns" style="padding-left:1.4em">' + "".join(f"<li>{d}</li>" for d in diff) + "</ol></div></div>", "mist")
             + section(cols(*[card(t, d, ic, f"~/{u}", l) for t, d, ic, u, l in [
                 ("Notre approche", "Commencer par un pilote, prouver sur pièces, puis déployer.", "target", "entreprise/notre-approche/", "Découvrir"),
                 ("Équipe et carrières", "Archivistes, ingénieurs, opérateurs : les métiers qui font ADA.", "users", "entreprise/equipe/", "Rencontrer l'équipe"),
                 ("Expansion africaine", "De la Côte d'Ivoire au continent, pays par pays.", "globe", "entreprise/afrique/", "Voir la feuille de route")]], n=3)),
             nav="entreprise"))

    add(Page("entreprise/notre-approche", "Notre approche",
             description="L'approche ADA : services d'abord, premiers clients, connaissance des problèmes, puis plateforme. Audit, pilote, déploiement.",
             hero=page_hero("Notre approche : prouver avant de déployer", "Nous ne vous demandons pas de parier sur un grand projet. Nous commençons petit, nous mesurons, puis nous déployons.",
                            [("Entreprise", "entreprise/"), ("Notre approche", None)], "Méthode"),
             body=section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                          + intro("Construit avec les métiers de l'archive", "La première erreur serait de créer un produit uniquement avec des développeurs. ARCHIVA360 est conçu avec des archivistes, des juristes, des experts en cybersécurité et des spécialistes de la numérisation.", "Principe")
                          + '</div><div class="wp-block-column">' + steps([
                              ("Services", "Nous commençons comme société de transformation documentaire : audit, numérisation, migration."),
                              ("Premiers clients", "Chaque projet nous confronte aux réalités du terrain."),
                              ("Connaissance des problèmes", "Nous capitalisons sur ce que nous observons."),
                              ("MVP puis ARCHIVA360", "La plateforme intègre d'abord l'essentiel, puis s'enrichit."),
                              ("SaaS, Enterprise, Government", "Des éditions adaptées à chaque type d'organisation."),
                              ("African Digital Archive Network", "Un réseau de confiance à l'échelle du continent.")]) + "</div></div>")
             + section(intro("Le processus commercial, en toute transparence", "", "Étapes", center=True)
                       + '<ol class="chain">' + "".join(f"<li><b>{s}</b></li>" for s in ["Prospection", "Diagnostic gratuit", "Audit documentaire", "Plan d'archivage", "Projet pilote", "Numérisation", "ARCHIVA360", "Formation", "Déploiement"]) + "</ol>"
                       + '<p class="has-text-align-center has-muted-color mt-m">… puis un abonnement annuel pour l\'hébergement, la maintenance, le support et l\'évolution.</p>', "mist")
             + section(intro("La feuille de route produit", "", "Versions") + cols(
                 card("MVP", "Authentification, organisations, utilisateurs, rôles, documents, dossiers, métadonnées, upload, OCR, recherche, prévisualisation, versions, audit trail, permissions, QR codes, conservation de base, tableau de bord, administration, sauvegarde.", "check-circle", tag="Lancement"),
                 card("Version 2", "Workflows, courrier, signature, API, IA avancée, archives physiques, application mobile, SSO, intégrations.", "layers", tag="Ensuite"),
                 card("Version 3", "Préservation OAIS, migration de formats, registre d'empreintes, archivage distribué, portail public, marketplace, Academy, réseau africain.", "globe", tag="À terme"), n=3)),
             nav="entreprise"))

    roles = [("Direction générale", "Pilote la stratégie, les partenariats et le développement.", "briefcase"),
             ("Direction archivistique", "Archiviste / records manager : garant des méthodes et des règles.", "library"),
             ("Direction technique (CTO)", "Architecture de la plateforme, sécurité, qualité.", "cpu"),
             ("Développeurs", "Construisent ARCHIVA360 : web, mobile, API.", "api"),
             ("DevOps et cybersécurité", "Hébergement, sauvegardes, supervision, sécurité.", "shield"),
             ("Expert IA / OCR", "Reconnaissance, classification, extraction.", "sparkles"),
             ("Chef de projet", "Conduit les projets clients de l'audit au déploiement.", "workflow"),
             ("Opérateurs de numérisation", "Préparent, numérisent et contrôlent les fonds.", "scan"),
             ("Commercial B2B", "Accompagne les organisations dans leur projet.", "users"),
             ("Juriste / DPO", "Conformité, protection des données, durées de conservation.", "scale")]
    team_html = '<div class="wp-block-columns cols-2 gap-sm" style="--cols:2">' + "".join(
        f'<div class="wp-block-column"><div class="team-role"><div class="team-role__avatar">{icon(ic)}</div><div><h4>{t}</h4><p>{d}</p></div></div></div>' for t, d, ic in roles) + "</div>"
    add(Page("entreprise/equipe", "Équipe et carrières",
             description="Les métiers d'ADA : archivistes, ingénieurs, experts IA et cybersécurité, opérateurs de numérisation, juristes. Rejoignez-nous à Abidjan.",
             hero=page_hero("Les métiers qui font ADA", "Un projet d'archivage réussi réunit des compétences rarement rassemblées : archivistique, droit, technologie, sécurité et numérisation.",
                            [("Entreprise", "entreprise/"), ("Équipe et carrières", None)], "Équipe"),
             body=section(intro("Une équipe pluridisciplinaire", "Notre organisation réunit technique, archivistique et commercial autour des opérations de numérisation.", "Organisation") + team_html)
             + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                       + intro("Rejoindre ADA", "Nous construisons l'équipe à Abidjan. Vous êtes archiviste, développeur, ingénieur DevOps, spécialiste de l'OCR, chef de projet, opérateur de numérisation ou commercial B2B ? Écrivez-nous.", "Carrières")
                       + btn("Envoyer une candidature spontanée", "~/contact/?sujet=carriere") + '</div><div class="wp-block-column">'
                       + ul(["Un projet qui a du sens : préserver la mémoire documentaire africaine", "Des métiers variés, de l'archive au cloud", "Une entreprise en construction où chaque personne compte", "Des formations internes via ARCHIVA Academy"])
                       + "</div></div>", "mist"),
             nav="entreprise"))

    add(Page("entreprise/afrique", "Expansion africaine",
             description="La feuille de route africaine d'ADA : Côte d'Ivoire, UEMOA, Afrique centrale, Afrique anglophone, puis Afrique du Nord. Packs pays et African Archive Network.",
             hero=page_hero("De la Côte d'Ivoire au continent", "Nous ne cherchons pas à couvrir 54 pays immédiatement. Nous avançons pays par pays, avec un produit conçu dès le départ pour s'adapter.",
                            [("Entreprise", "entreprise/"), ("Expansion africaine", None)], "Expansion"),
             body=section('<div class="roadmap">' + "".join(
                 f'<div class="roadmap__step{" is-current" if i == 0 else ""}"><small>Étape {i+1}</small><h4>{t}</h4><p>{d}</p></div>'
                 for i, (t, d) in enumerate([("Côte d'Ivoire", "Abidjan : siège, premier centre de numérisation, premiers clients."), ("UEMOA", "Sénégal, Bénin, Togo, Burkina Faso."),
                                             ("Afrique centrale", "Cameroun, RDC, Gabon, Congo."), ("Afrique anglophone", "Ghana, Kenya, Nigeria."), ("Afrique du Nord", "Et d'autres marchés.")])) + "</div>", "mist")
             + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                       + intro("Un cœur, des packs pays", "Les environnements réglementaires ne sont pas identiques. Le logiciel reste le même ; les règles, métadonnées, durées, connecteurs, langues, hébergement et exigences réglementaires se configurent par pays.", "Architecture")
                       + '</div><div class="wp-block-column">'
                       + chips(["ARCHIVA CORE", "Pack Côte d'Ivoire", "Pack Sénégal", "Pack Bénin", "Pack Togo", "Pack Cameroun", "Pack Ghana", "Pack Kenya"])
                       + "</div></div>")
             + section(intro("L'African Archive Network", "À terme, une infrastructure permettant aux institutions participantes de préserver leur patrimoine documentaire : un nœud national par pays, relié aux institutions publiques, entreprises, universités, bibliothèques et archives historiques. Les données ne sont jamais accessibles d'une organisation à l'autre sans autorisation : chaque institution garde la maîtrise de ses accès, dans le respect du cadre juridique applicable.", "Vision"), "navy")
             + section(cta_band("Vous êtes intégrateur hors de Côte d'Ivoire ?", "Le programme ARCHIVA Certified Partner permettra de certifier des partenaires dans chaque pays.", btn("Devenir partenaire", "~/contact/?sujet=partenariat", "white"))),
             nav="entreprise"))


def build_contact():
    add(Page("contact", "Contact",
             description="Contactez ADA : demande d'audit documentaire, démonstration ARCHIVA360, devis de numérisation, partenariat. Abidjan, Côte d'Ivoire.",
             hero=page_hero("Parlons de vos archives", "Diagnostic gratuit, audit documentaire, démonstration ou devis : décrivez votre besoin, un spécialiste vous répond sous deux jours ouvrés.",
                            [("Contact", None)], "Contact"),
             body=section('<div class="wp-block-columns gap-lg" style="--cols:2;grid-template-columns:1.5fr 1fr"><div class="wp-block-column">' + contact_form("audit")
                          + '</div><div class="wp-block-column"><ul class="contact-info">'
                          + f'<li><span class="feature__icon">{icon("map-pin")}</span><div><b>Siège</b><span>{SITE["city"]}</span></div></li>'
                          + f'<li><span class="feature__icon">{icon("mail")}</span><div><b>E-mail</b><span><a href="mailto:{SITE["email"]}">{SITE["email"]}</a></span></div></li>'
                          + f'<li><span class="feature__icon">{icon("clock")}</span><div><b>Horaires</b><span>Du lundi au vendredi, de 8 h à 17 h (GMT)</span></div></li>'
                          + f'<li><span class="feature__icon">{icon("scan")}</span><div><b>Centre de numérisation</b><span>ARCHIVA Digitalization Center — Abidjan. Visites sur rendez-vous.</span></div></li></ul>'
                          + '<div class="card is-flat mt-m"><h3>Avant d\'écrire</h3><p>Faites le Document Health Check : votre score nous aide à préparer le premier échange.</p>'
                          + f'<a class="more-link" href="~/ressources/document-health-check/">Faire le test {icon("arrow-right")}</a></div></div></div>'),
             nav="contact"))

    add(Page("espace-client", "Espace client",
             description="Espace client ARCHIVA360.",
             hero=page_hero("Espace client", "Accédez à votre espace ARCHIVA360 : archives, utilisateurs, workflows, demandes, statistiques, factures, politiques de conservation et audits.", [("Espace client", None)], "Connexion", light=True),
             body=section('<div class="container is-narrow" style="padding:0"><div class="wp-block-columns gap-lg" style="--cols:2"><div class="wp-block-column"><div class="form-card">'
                          + '<h2 style="font-size:1.4rem">Connexion</h2><form class="login-form" onsubmit="event.preventDefault();document.getElementById(\'login-msg\').hidden=false">'
                          + '<p><label for="user_login">Identifiant ou adresse e-mail</label><input type="text" id="user_login" autocomplete="username"></p>'
                          + '<p><label for="user_pass">Mot de passe</label><input type="password" id="user_pass" autocomplete="current-password"></p>'
                          + '<p class="wpcf7-acceptance" style="margin-bottom:18px"><input type="checkbox" id="rememberme"> <label for="rememberme" style="display:inline;font-weight:400">Se souvenir de moi</label></p>'
                          + '<input type="submit" class="button" value="Se connecter" style="width:100%">'
                          + '<p id="login-msg" class="notice is-warning mt-m" hidden>Le portail client ARCHIVA360 ouvrira avec les premiers déploiements : vos accès vous seront communiqués par votre chef de projet ADA. En attendant, essayez la <a href="~/archiva360/demo-interactive/">démo interactive</a>.</p></form></div></div>'
                          + '<div class="wp-block-column"><div class="notice is-success"><p><strong>Envie d\'essayer dès maintenant ?</strong> La démo interactive ARCHIVA360 fonctionne dans votre navigateur, avec un espace d\'exemple prêt à l\'emploi.</p></div>'
                          + btn("Ouvrir la démo interactive", "~/archiva360/demo-interactive/")
                          + '<h3 class="mt-l">Dans votre espace</h3>'
                          + ul(["Mes archives", "Mes utilisateurs", "Mes workflows", "Mes demandes", "Mes statistiques", "Mes factures", "Mes politiques de conservation", "Mes audits"])
                          + f'<p class="has-muted-color">Pas encore client ? <a href="~/contact/?sujet=demo">Demandez une démonstration</a>.</p></div></div></div>'),
             nav="", search=False))


def build_legal():
    add(Page("mentions-legales", "Mentions légales",
             description="Mentions légales du site African Digital Archives (ADA).",
             hero=page_hero("Mentions légales", "", [("Mentions légales", None)], light=True),
             body=section('<div class="legal-content entry-content">'
                          + "<h2>Éditeur du site</h2><p>African Digital Archives (ADA), société en cours de constitution, Abidjan, Côte d'Ivoire.<br>"
                          + f'E-mail : <a href="mailto:{SITE["email"]}">{SITE["email"]}</a></p>'
                          + "<p><em>Forme juridique, capital, numéro RCCM, compte contribuable et directeur de la publication : à compléter après l'immatriculation.</em></p>"
                          + "<h2>Hébergement</h2><p>GitHub Pages, GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>"
                          + "<h2>Propriété intellectuelle</h2><p>L'ensemble des contenus de ce site (textes, visuels, captures d'écran, logos, marques ADA, ARCHIVA360, ARCHIVA AI, ARCHIVA GO) est protégé. Toute reproduction sans autorisation écrite est interdite. Les noms de produits et de marques sont soumis à vérification de disponibilité et de dépôt.</p>"
                          + "<h2>Captures d'écran</h2><p>Les captures d'écran d'ARCHIVA360 présentées sur ce site illustrent l'interface de la plateforme avec des données fictives (organisation de démonstration, noms et montants d'exemple).</p>"
                          + "<h2>Responsabilité</h2><p>Les informations publiées, notamment sur le cadre juridique, ont une valeur informative et ne constituent pas un conseil juridique. Les tarifs affichés sont des tarifs de lancement indicatifs.</p>"
                          + "</div>"),
             nav="", search=False))
    add(Page("politique-de-confidentialite", "Politique de confidentialité",
             description="Politique de confidentialité et cookies du site ADA, conformément à la loi ivoirienne n°2013-450 relative à la protection des données à caractère personnel.",
             hero=page_hero("Politique de confidentialité", "Comment nous traitons les données que vous nous confiez sur ce site.", [("Politique de confidentialité", None)], light=True),
             body=section('<div class="legal-content entry-content">'
                          + "<p>ADA attache une importance particulière à la protection des données personnelles, conformément à la loi ivoirienne n°2013-450 du 19 juin 2013 relative à la protection des données à caractère personnel.</p>"
                          + "<h2>Données collectées</h2><p>Via les formulaires : nom, organisation, fonction, e-mail, téléphone, pays, secteur, volume d'archives et message. Via la lettre d'information : adresse e-mail.</p>"
                          + "<h2>Finalités</h2><ul><li>Répondre à vos demandes (audit, démonstration, devis, questions).</li><li>Vous adresser la lettre d'information si vous l'avez demandée.</li></ul>"
                          + "<h2>Mode de transmission</h2><p>Les formulaires de ce site ouvrent votre messagerie avec un message prérempli : aucune donnée n'est stockée par le site lui-même. Vos réponses au Document Health Check sont calculées dans votre navigateur et ne nous sont pas transmises, sauf si vous choisissez de nous écrire.</p>"
                          + "<h2>Durée de conservation</h2><p>Les échanges commerciaux sont conservés trois ans après le dernier contact, sauf obligation légale contraire.</p>"
                          + f'<h2>Vos droits</h2><p>Vous disposez d\'un droit d\'accès, de rectification, d\'opposition et de suppression. Écrivez-nous à <a href="mailto:{SITE["email"]}">{SITE["email"]}</a>. Vous pouvez également saisir l\'ARTCI, autorité de protection des données en Côte d\'Ivoire.</p>'
                          + '<h2 id="cookies">Cookies</h2><p>Ce site n\'utilise que le stockage local du navigateur pour mémoriser votre choix concernant les cookies. Aucun cookie publicitaire n\'est déposé. Si une mesure d\'audience est ajoutée, elle ne sera activée qu\'avec votre accord.</p>'
                          + "</div>"),
             nav="", search=False))


def build_utility():
    add(Page("recherche", "Recherche",
             '<div class="container is-narrow" style="padding-top:48px;padding-bottom:96px">'
             + '<form role="search" method="get" class="search-form" action="~/recherche/"><label style="flex:1"><span class="screen-reader-text">Rechercher :</span><input type="search" id="search-page-field" class="search-field" name="s" placeholder="Rechercher…"></label><button type="submit" class="search-submit button">Rechercher</button></form>'
             + '<div class="search-results-list" id="search-results"></div></div>',
             description="Rechercher sur le site ADA.",
             hero='<header class="page-hero is-light"><div class="container"><nav class="yoast-breadcrumbs" aria-label="Fil d\'Ariane"><span><span><a href="~/">Accueil</a></span> <span class="sep">›</span> <span class="breadcrumb_last">Recherche</span></span></nav><h1 class="page-title" id="search-title">Rechercher sur le site</h1></div></header>',
             body_class="search search-results", nav="", search=False,
             scripts=f'<script src="~/{SITE["theme"]}assets/js/search-index.js?ver={SITE["version"]}"></script>'))

    add(Page("404", "Page introuvable",
             '<section class="error-404 not-found"><div class="container"><div class="code">404</div><h1 class="page-title">Cette page est introuvable</h1>'
             + '<p class="lead has-muted-color">Elle a peut-être été déplacée, ou l\'adresse contient une erreur.</p>'
             + '<form role="search" method="get" class="search-form" action="~/recherche/"><label style="flex:1"><span class="screen-reader-text">Rechercher :</span><input type="search" class="search-field" name="s" placeholder="Rechercher sur le site…"></label><button type="submit" class="search-submit button">Rechercher</button></form>'
             + buttons(btn("Retour à l'accueil", "~/"), btn("Plan du site", "~/plan-du-site/", "outline"), center=True) + "</div></section>",
             description="Page introuvable.", body_class="error404", kind="404", nav="", search=False))


def build_sitemap():
    groups = {}
    labels = {"": "Accueil", "solutions": "Solutions", "archiva360": "ARCHIVA360", "secteurs": "Secteurs", "services": "Services",
              "ressources": "Ressources", "blog": "Blog", "entreprise": "Entreprise", "academy": "ARCHIVA Academy", "contact": "Contact"}
    for p in PAGES:
        if p.kind == "404" or p.path.startswith("blog/categorie") or p.path in ("recherche/",):
            continue
        key = p.path.split("/")[0]
        groups.setdefault(key if key in labels else "autres", []).append(p)
    html_ = '<ul class="sitemap-list wp-block-list">'
    for key, ps in groups.items():
        title = labels.get(key, "Informations")
        html_ += f'<li><strong>{title}</strong><ul>' + "".join(f'<li><a href="~/{p.path}">{p.title}</a></li>' for p in ps) + "</ul></li>"
    html_ += "</ul>"
    add(Page("plan-du-site", "Plan du site", section(html_), description="Plan du site African Digital Archives.",
             hero=page_hero("Plan du site", "", [("Plan du site", None)], light=True), nav="", search=False))
