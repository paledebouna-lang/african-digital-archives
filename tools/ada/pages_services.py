from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons,
                   faq, page_hero, notice, steps, table, chips)
from .icons import icon


def build():
    services = [
        ("audit-documentaire", "Audit documentaire", "Comprendre vos fonds, vos risques et vos priorités avant d'investir.", "eye"),
        ("numerisation", "Numérisation", "Notre centre de numérisation d'Abidjan traite vos fonds, du simple scan à la gestion externalisée.", "scan"),
        ("migration", "Migration", "Reprendre vos serveurs de fichiers, disques et anciens logiciels dans ARCHIVA360.", "refresh"),
        ("conseil", "Conseil", "Plan de classement, politique d'archivage, conformité : poser les règles avant l'outil.", "compass"),
        ("formation", "Formation", "Former archivistes, documentalistes, équipes IT, RH et utilisateurs.", "presentation"),
        ("hebergement", "Hébergement", "Cloud, cloud privé, sur site ou hybride : vos données restent sous votre contrôle.", "server"),
    ]
    add(Page(
        "services", "Services",
        description="Audit documentaire, numérisation, migration, conseil, formation et hébergement : les services d'ADA pour transformer vos archives.",
        hero=page_hero("Des services pour chaque étape de votre projet",
                       "ADA ne vend pas seulement un logiciel. Nous combinons conseil archivistique, numérisation, technologie et préservation pour mener votre projet de bout en bout.",
                       [("Services", None)], "Services",
                       buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"))),
        body=section(cols(*[card(t, d, ic, f"~/services/{s}/") for s, t, d, ic in services], n=3))
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("Quatre pôles, un seul interlocuteur", "Notre organisation reflète la chaîne documentaire complète.", "Organisation")
                  + '</div><div class="wp-block-column">'
                  + cols(card("Consulting", "Audit documentaire, plan de classement, politique d'archivage, conseil, conformité.", "compass", flat=True),
                         card("Digitalisation", "Numérisation, OCR, indexation, classement, migration.", "scan", flat=True),
                         card("Software", "La plateforme ARCHIVA360 et ses applications.", "blocks", flat=True),
                         card("Trust & Preservation", "Archivage électronique, conservation longue durée, sécurité, signature, horodatage, intégrité, sauvegarde, reprise d'activité.", "shield", flat=True), n=2, cls="gap-sm")
                  + "</div></div>", "mist"),
        nav="services"))

    # Audit
    add(Page(
        "services/audit-documentaire", "Audit documentaire",
        description="L'audit documentaire ADA : diagnostic de vos fonds papier et numériques, risques, plan de classement, projet pilote de numérisation.",
        hero=page_hero("Audit documentaire et projet pilote", "Avant d'acheter un logiciel, comprenez vos archives. Notre audit identifie vos fonds, vos risques et vos priorités, puis nous le prouvons sur un projet pilote.",
                       [("Services", "services/"), ("Audit documentaire", None)], "Service",
                       buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"), btn("Faire le Health Check", "~/ressources/document-health-check/", "outline"))),
        body=section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                     + intro("Ce que nous analysons", "", "Périmètre")
                     + ul(["Où sont vos archives, papier et numériques ?", "Combien : mètres linéaires, pages, fichiers, volumes", "Qui y accède, et avec quels droits ?", "Sont-elles sauvegardées ? Que se passe-t-il en cas d'incendie ou de ransomware ?",
                           "Pouvez-vous retrouver un contrat rapidement ?", "Existe-t-il un plan de classement et une politique de conservation ?", "Quels documents sont confidentiels ?", "Quelles obligations réglementaires s'appliquent ?"])
                     + '</div><div class="wp-block-column"><div class="card is-dark"><div class="card__icon">' + icon("target") + '</div><h3>Notre premier produit : Audit + digitalisation pilote</h3>'
                     + '<p>« Nous analysons 10 000 dossiers de votre organisation, vous proposons un plan de classement et numérisons un fonds pilote de 1 000 dossiers. »</p>'
                     + '<p>À la fin : un rapport, une démonstration d\'ARCHIVA360 avec vos documents et une proposition de déploiement.</p></div></div></div>')
        + section(intro("Notre processus", "Du premier contact à l'abonnement annuel, chaque étape produit un livrable concret.", "Démarche")
                  + '<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + steps([("Diagnostic gratuit", "Un échange pour comprendre votre situation."), ("Audit documentaire", "Visite des locaux, inventaire, entretiens avec les services."),
                           ("Plan d'archivage", "Plan de classement, règles de conservation, priorités de numérisation."), ("Projet pilote", "Numérisation et indexation d'un fonds représentatif.")])
                  + '</div><div class="wp-block-column">'
                  + steps([("Numérisation", "Traitement des fonds prioritaires."), ("ARCHIVA360", "Paramétrage et import dans la plateforme."), ("Formation", "Formation des référents et des utilisateurs."), ("Déploiement et abonnement", "Mise en service, support et évolution.")])
                  + "</div></div>", "mist")
        + section(intro("Les livrables de l'audit", "", "Livrables") + cols(*[card(t, d, ic) for t, d, ic in [
            ("Rapport d'audit", "État des lieux, volumes, risques, niveau de maturité et recommandations.", "file"),
            ("Cartographie des fonds", "Localisation et description de vos archives papier et numériques.", "map-pin"),
            ("Plan d'action chiffré", "Priorités, calendrier et budget du projet.", "chart")]], n=3))
        + section(cta_band("Commencez par évaluer votre maturité", "Le Document Health Check vous donne un premier score en 20 questions. Gratuit, 5 minutes.",
                           btn("Faire le test", "~/ressources/document-health-check/", "white"))),
        nav="services"))

    # Numérisation
    offers = [("Offre A", "Numérisation simple", "Scan haute qualité et contrôle visuel."),
              ("Offre B", "Numérisation + OCR", "Documents lisibles et interrogeables en plein texte."),
              ("Offre C", "Numérisation + OCR + indexation", "Métadonnées saisies ou extraites, prêtes pour la recherche."),
              ("Offre D", "Numérisation + classement + migration", "Import complet dans ARCHIVA360 selon votre plan de classement."),
              ("Offre E", "Gestion complète externalisée", "ADA prend en charge vos archives de bout en bout.")]
    add(Page(
        "services/numerisation", "Numérisation — Scan Center Abidjan",
        description="Le centre de numérisation ADA à Abidjan : scan, OCR, indexation, contrôle qualité, migration vers ARCHIVA360. Tarification à la page ou au projet.",
        hero=page_hero("Numérisation : du carton au document exploitable", "Nos équipes numérisent vos fonds dans notre centre d'Abidjan ou directement dans vos locaux, avec préparation, contrôle qualité et indexation.",
                       [("Services", "services/"), ("Numérisation", None)], "Service",
                       buttons(btn("Demander un devis", "~/contact/?sujet=numerisation", "white")),
                       media=img("archiva360-document-ocr.png", "Document numérisé et indexé", frame=True, lazy=False)),
        body=section(intro("Cinq niveaux de service", "Choisissez le niveau adapté à vos fonds et à votre budget.", "Offres")
                     + cols(*[f'<div class="card"><span class="eyebrow">{a}</span><h3>{b}</h3><p>{c}</p></div>' for a, b, c in offers], n=5, cls="gap-sm"))
        + section(intro("Notre chaîne de numérisation", "Dix étapes maîtrisées, du rayonnage à la conservation.", "Méthode", center=True)
                  + '<ol class="chain">' + "".join(f"<li><b>{s}</b></li>" for s in ["Préparation", "Classement", "Numérisation", "OCR", "Contrôle qualité", "Indexation", "Importation", "Archivage électronique", "Conservation"]) + "</ol>", "mist")
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("ARCHIVA Digitalization Center — Abidjan", "Notre premier centre de numérisation est équipé pour traiter tous les types de documents, dans un environnement sécurisé.", "Centre")
                  + ul(["Scanners A3/A4 haute vitesse", "Scanners de livres", "Scanners de plans et grands formats", "Postes de contrôle qualité et d'OCR", "Stockage temporaire et serveur sécurisés", "Matériel de sauvegarde", "Destruction sécurisée des supports, si elle est autorisée"])
                  + '</div><div class="wp-block-column">'
                  + intro("Comment nous fixons les prix", "Les tarifs sont calculés à partir du coût des équipements, de la main-d'œuvre, de la préparation, du contrôle qualité, du stockage, de l'OCR, du transport et de la marge.", "Tarification")
                  + table(["Prestation", "Mode de facturation"], [("Scan simple", "Prix par page"), ("Scan + OCR", "Prix par page"), ("Scan + OCR + indexation", "Prix par page"), ("Traitement complexe", "Prix par page ou forfait projet"), ("Migration d'un fonds documentaire", "Forfait projet")])
                  + "</div></div>")
        + section(intro("Un réseau de Scan Centers en Afrique", "Abidjan d'abord. À terme, des centres régionaux au plus près des fonds.", "Vision")
                  + chips(["Abidjan", "Dakar", "Accra", "Lagos", "Nairobi", "Casablanca", "Douala", "Cotonou", "Lomé", "Ouagadougou", "Conakry"])
                  + '<p class="has-muted-color">Aujourd\'hui, seul le centre d\'Abidjan est ouvert. Les autres implantations suivront notre développement dans la sous-région.</p>', "mist")
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">' + intro("Questions fréquentes", "", "FAQ") + '</div><div class="wp-block-column">'
                  + faq([("Mes documents quittent-ils mes locaux ?", "Vous choisissez : traitement dans notre centre d'Abidjan avec transport sécurisé et bordereaux, ou intervention de nos équipes sur site pour les fonds sensibles."),
                         ("Que deviennent les originaux ?", "Ils vous sont restitués, reconditionnés et étiquetés avec leur QR code. Leur éventuelle destruction ne se fait qu'avec votre accord écrit et dans le respect des règles applicables."),
                         ("Quelle qualité d'image ?", "Résolution et format définis selon l'usage : consultation, preuve ou préservation patrimoniale. Un contrôle qualité est réalisé sur chaque lot.")])
                  + "</div></div>"),
        nav="services"))

    # Migration
    add(Page(
        "services/migration", "Migration de fonds et de systèmes",
        description="Migration vers ARCHIVA360 : serveurs de fichiers, disques externes, messageries, anciens logiciels de GED, avec dédoublonnage, classement et contrôle d'intégrité.",
        hero=page_hero("Migration : reprendre l'existant sans rien perdre", "Serveurs de fichiers, disques externes, clés USB, messageries, fichiers WhatsApp, anciens logiciels : nous rassemblons vos documents dispersés dans ARCHIVA360.",
                       [("Services", "services/"), ("Migration", None)], "Service", buttons(btn("Planifier une migration", "~/contact/?sujet=migration", "white"))),
        body=section(intro("Les sources que nous reprenons", "", "Sources") + chips(["Serveurs de fichiers", "Disques externes", "Clés USB", "Messageries et e-mails", "Fichiers WhatsApp", "Anciens logiciels de GED", "Bases de données", "Fonds numérisés existants"])
                     + intro("Notre méthode", "", "Méthode").replace('class="section-intro"', 'class="section-intro mt-l"')
                     + '<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                     + steps([("Inventaire", "Volumes, formats, arborescences, doublons."), ("Correspondance", "Chaque dossier source est rattaché au plan de classement cible."), ("Nettoyage", "Dédoublonnage, identification des formats, conversion si nécessaire.")])
                     + '</div><div class="wp-block-column">'
                     + steps([("Import", "Import avec métadonnées et empreintes calculées dès l'entrée."), ("Contrôle", "Rapprochement des volumes source et cible, contrôle d'intégrité."), ("Bascule", "Mise en service et accompagnement des utilisateurs.")])
                     + "</div></div>")
        + section(notice("Chaque migration se termine par un rapport de contrôle : nombre de fichiers repris, rejetés et convertis, avec leurs empreintes. Vous gardez la preuve qu'aucun document n'a été perdu.", "success"), "mist", "is-compact"),
        nav="services"))

    # Conseil
    add(Page(
        "services/conseil", "Conseil en gouvernance documentaire",
        description="Conseil archivistique ADA : audit, plan de classement, référentiel de conservation, politique d'archivage, conformité au cadre ivoirien.",
        hero=page_hero("Conseil : poser les règles avant l'outil", "Un logiciel ne remplace pas une politique d'archivage. Nos archivistes et juristes vous aident à définir les règles qui feront fonctionner votre système.",
                       [("Services", "services/"), ("Conseil", None)], "Service", buttons(btn("Parler à un consultant", "~/contact/?sujet=conseil", "white"))),
        body=section(cols(*[card(t, d, ic) for t, d, ic in [
            ("Plan de classement", "Une structure commune, validée avec vos services, qui reflète vos activités réelles.", "workflow"),
            ("Référentiel de conservation", "Durées, événements déclencheurs et sort final par type de document, validés par un juriste.", "hourglass"),
            ("Politique d'archivage", "Rôles, responsabilités, règles d'accès, procédures de versement et d'élimination.", "file"),
            ("Conformité", "Mise en regard avec le cadre ivoirien : transactions électroniques, archivage électronique, protection des données.", "scale"),
            ("Gouvernance de l'information", "Comités, indicateurs et tableau de bord de conformité.", "chart"),
            ("Accompagnement au changement", "Communication interne, référents, formation des équipes.", "users")]], n=3))
        + section(notice("Nous travaillons toujours avec un archiviste, un juriste, un expert en cybersécurité et un spécialiste de la protection des données. Nous ne présentons jamais un dispositif comme « juridiquement conforme » sans validation juridique et technique indépendante.", "warning"), "mist", "is-compact"),
        nav="services"))

    # Formation
    add(Page(
        "services/formation", "Formation",
        description="Formations ADA et ARCHIVA Academy : archivage, gestion documentaire, records management, archivage électronique, préservation numérique, administration d'ARCHIVA360.",
        hero=page_hero("Formation : des équipes autonomes", "Un projet documentaire réussit quand les équipes s'en emparent. Nous formons chaque profil à ce dont il a besoin.",
                       [("Services", "services/"), ("Formation", None)], "Service", buttons(btn("Voir ARCHIVA Academy", "~/academy/", "white"))),
        body=section(intro("Les publics que nous formons", "", "Publics") + cols(*[feature(t, d, ic) for t, d, ic in [
            ("Archivistes et documentalistes", "Records management, archivage électronique, préservation.", "library"),
            ("Équipes IT", "Administration, sécurité, sauvegarde, intégrations.", "server"),
            ("Ressources humaines", "Gestion et confidentialité des dossiers du personnel.", "users"),
            ("Secrétariats et assistants", "Courrier, classement, recherche, workflows.", "inbox"),
            ("Administrateurs ARCHIVA360", "Paramétrage, rôles, règles, métadonnées.", "blocks"),
            ("Directions", "Gouvernance documentaire et pilotage de la conformité.", "briefcase")]], n=3, cls="gap-lg"))
        + section(cta_band("Six niveaux, du débutant à l'administrateur", "ARCHIVA Academy structure nos formations en parcours progressifs avec certificats internes.", btn("Découvrir l'Academy", "~/academy/", "white"))),
        nav="services"))

    # Hébergement
    add(Page(
        "services/hebergement", "Hébergement et déploiement",
        description="Hébergement d'ARCHIVA360 : SaaS, cloud privé, installation sur site ou hybride, multi-tenant isolé, sauvegarde 3-2-1, souveraineté des données.",
        hero=page_hero("Vos données restent sous votre contrôle", "Cloud ADA, cloud privé, installation dans vos locaux ou architecture hybride : nous choisissons avec vous le mode de déploiement adapté à la sensibilité de vos archives.",
                       [("Services", "services/"), ("Hébergement", None)], "Service", buttons(btn("Étudier mon projet", "~/contact/?sujet=hebergement", "white"))),
        body=section(cols(*[card(t, d, ic) for t, d, ic in [
            ("Cloud SaaS", "Le plus simple : ADA héberge, sauvegarde et met à jour. Idéal pour les PME et associations.", "cloud"),
            ("Cloud privé", "Une infrastructure dédiée pour les grands groupes.", "server"),
            ("Sur site", "Installation dans votre propre infrastructure, pour les administrations sensibles.", "landmark"),
            ("Hybride", "Une partie sur site, une partie dans le cloud. Particulièrement adapté aux administrations.", "layers")]], n=4))
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("Multi-organisations, strictement isolées", "ARCHIVA360 est une plateforme SaaS multi-organisations : un ministère, une banque, une université et une entreprise privée peuvent l'utiliser, chacun dans un environnement isolé. Pour les clients très sensibles, un tenant dédié est possible.", "Architecture")
                  + '</div><div class="wp-block-column">'
                  + ul(["Chiffrement au repos et en transit", "Sauvegarde 3-2-1 : 3 copies, 2 supports, 1 hors site", "Réplication et plan de reprise d'activité", "Supervision (Prometheus, Grafana) et journalisation", "Séparation des environnements et tests d'intrusion"])
                  + "</div></div>", "navy")
        + section(intro("Stockage", "Facturé selon le volume : 10 Go, 100 Go, 1 To, 10 To et plus. L'archivage longue durée fait l'objet d'un abonnement annuel.", "Volumes"), "mist", "is-compact"),
        nav="services"))
