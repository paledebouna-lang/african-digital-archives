from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons,
                   faq, page_hero, notice, steps, table, chips, stat)
from .icons import icon

MODULES = [
    ("Dashboard", "Vue générale : documents, dossiers, utilisateurs, stockage, workflows, demandes, alertes, conservation, activité, sécurité.", "mvp"),
    ("Documents", "Le cœur de la GED : importer, déposer, prévisualiser, classer, déplacer, partager, versionner, verrouiller, archiver.", "mvp"),
    ("Dossiers", "Arborescences par direction et service : Juridique, Finance, RH… avec héritage des droits.", "mvp"),
    ("Numérisation", "Scan, import massif, OCR, contrôle qualité, indexation, détection des pages, séparation automatique.", "mvp"),
    ("OCR + IA", "Lecture des documents et extraction des données : fournisseur, date, numéro, montant, TVA, devise.", "mvp"),
    ("Recherche intelligente", "Plein texte, métadonnées, OCR, tags, dates, utilisateurs, départements, montants, types.", "mvp"),
    ("Archive AI", "Assistant documentaire : résumer, comparer, trouver des obligations, détecter des doublons, construire une chronologie.", "v2"),
    ("Workflow", "Circuits de validation par glisser-déposer : contrôle, responsable, juridique, direction, signature, archivage.", "v2"),
    ("Courrier", "Courrier entrant, sortant et interne : enregistrement, affectation, traitement, réponse, archivage.", "v2"),
    ("Signature électronique", "Créer, valider, signer, horodater, archiver, avec un prestataire de confiance.", "v2"),
    ("Archive Vault", "Coffre-fort pour contrats, dossiers juridiques, données sensibles, décisions, propriété intellectuelle.", "v2"),
    ("Records management", "Types de documents, plan de classement, règles, événements déclencheurs, durées, sort final, gel juridique.", "mvp"),
    ("Retention Center", "Calcul automatique des échéances et décisions tracées : examiner, conserver, préserver, détruire.", "mvp"),
    ("Archives physiques", "ARCHIVA ID et localisation de chaque boîte : site, bâtiment, salle, rayon, étagère.", "v2"),
    ("QR code", "Chaque dossier, boîte, étagère ou archive a son QR code. L'archiviste scanne et obtient la fiche.", "mvp"),
    ("Audit trail", "Traçabilité complète : qui, quoi, quand, depuis où, quelle action.", "mvp"),
    ("Security Center", "Connexions, échecs, utilisateurs, permissions, téléchargements, anomalies, appareils, sessions.", "v2"),
    ("Backup & Disaster Recovery", "Sauvegardes automatiques, réplication, copie hors site, tests de restauration, plan de reprise.", "mvp"),
    ("Portail public", "Archives ouvertes : délibérations, archives historiques, documents autorisés à la consultation.", "v3"),
    ("Administration", "Organisation, utilisateurs, rôles, permissions, stockage, règles, workflows, métadonnées, API, facturation.", "mvp"),
]
BADGE = {"mvp": ('is-mvp', "Disponible au lancement"), "v2": ("is-v2", "Version 2"), "v3": ("is-v3", "Version 3")}


def build():
    arch = f'''<div class="archi">
<div class="archi__row">
<div class="archi__box"><h4>Capture</h4><ul><li>Scanner</li><li>OCR</li><li>E-mail</li><li>Mobile</li><li>API</li></ul></div>
<div class="archi__box"><h4>Gestion</h4><ul><li>GED</li><li>Dossiers</li><li>Workflow</li><li>Recherche</li><li>Partage</li><li>Courrier</li></ul></div>
<div class="archi__box"><h4>Archivage</h4><ul><li>SAE</li><li>Conservation</li><li>Cycle de vie</li><li>Preuve</li><li>Intégrité</li></ul></div></div>
<div class="archi__box is-ai"><h4>Archive AI</h4><ul><li>OCR</li><li>Classification</li><li>Extraction</li><li>Recherche en langage naturel</li><li>Résumés</li><li>Doublons</li><li>Transcription</li></ul></div>
<div class="archi__box is-vault"><h4>Archive Vault</h4><ul><li>Sécurité</li><li>Sauvegarde</li><li>Audit</li><li>Chiffrement</li><li>Réplication</li><li>Reprise d'activité</li></ul></div></div>'''

    features = [
        ("archiva360-document-ocr.png", "Capture", "Le papier devient une information exploitable", "Scannez, importez ou photographiez. ARCHIVA360 reconnaît le texte, identifie le type de document, extrait les données clés et propose un classement. Vous validez.", ["OCR en français et en anglais", "Extraction : dates, montants, parties, numéros", "Séparation automatique des lots", "Capture e-mail, mobile et API"], "solutions/capture-numerisation/"),
        ("archiva360-recherche-intelligente.png", "Recherche", "Retrouver un document en quelques secondes", "« Contrats de construction signés en 2024 », « Factures supérieures à 5 millions FCFA », « Tous les dossiers concernant le projet X ». La recherche comprend la question et ne montre que ce que vous avez le droit de voir.", ["Plein texte, OCR et métadonnées", "Filtres par service, période, montant, type", "Recherche dans les boîtes physiques", "Résultats en moins d'une seconde"], "solutions/ged/"),
        ("archiva360-retention-center.png", "Archivage", "Chaque document a une durée de vie maîtrisée", "Les règles de conservation définies avec votre archiviste s'appliquent automatiquement. Le Retention Center affiche les échéances ; les décisions restent humaines et tracées.", ["Plan de classement et règles de conservation", "Échéances calculées automatiquement", "Gel juridique", "Empreinte SHA-256 et horodatage"], "solutions/sae/"),
        ("archiva360-compliance-center.png", "Pilotage", "Savoir où vous en êtes, à tout moment", "Le Compliance Center signale les documents sans métadonnées, les droits excessifs, les échéances et les sauvegardes non vérifiées. Le Security Center surveille les connexions et les anomalies.", ["Score de conformité par organisation", "Alertes et plans d'action", "Rapports pour la direction et les auditeurs", "Journal d'audit exportable"], "solutions/securite/"),
    ]
    feat_html = ""
    for i, (shot, eb, h, p, li, link) in enumerate(features):
        feat_html += media_text(img(shot, h, frame=True),
                                f'<span class="eyebrow">{eb}</span><h2>{h}</h2><p class="lead">{p}</p>{ul(li)}<a class="more-link" href="~/{link}">En savoir plus {icon("arrow-right")}</a>',
                                right=i % 2 == 1)

    editions = cols(
        card("ARCHIVA360 Cloud", "Pour les PME, associations, cabinets, petites administrations et établissements scolaires. 100 % en ligne, prêt en quelques jours.", "cloud",
             extra=ul(["Abonnement mensuel", "Mises à jour incluses", "Hébergement et sauvegardes gérés par ADA"])),
        card("ARCHIVA360 Enterprise", "Pour les banques, assurances, grands groupes, industries et universités.", "briefcase",
             extra=ul(["API et SSO", "Intégration ERP, CRM, SAP, Microsoft 365", "Workflows complexes", "Stockage privé, haute disponibilité"])),
        card("ARCHIVA360 Government", "Pour les ministères, mairies, collectivités, établissements publics et agences.", "landmark",
             extra=ul(["Cloud souverain, privé, sur site ou hybride", "Sécurité renforcée", "Archivage réglementaire", "Portail citoyen"])), n=3)

    add(Page(
        "archiva360", "ARCHIVA360 — la plateforme",
        seo_title="ARCHIVA360 : plateforme de gestion documentaire et d'archivage | ADA",
        description="ARCHIVA360 réunit GED, archivage électronique, records management, archives physiques, IA documentaire et préservation dans une seule plateforme, en SaaS ou sur site.",
        hero=page_hero("ARCHIVA360, la plateforme documentaire pensée pour l'Afrique",
                       "Capturer, gérer, archiver et préserver vos documents papier et numériques dans un seul outil, en français et en anglais, dans le cloud ou dans votre propre infrastructure.",
                       [("ARCHIVA360", None)], "Plateforme",
                       buttons(btn("Essayer la démo interactive", "~/archiva360/demo-interactive/", "white"), btn("Offres et tarifs", "~/archiva360/offres-et-tarifs/", "outline")),
                       media=img("archiva360-tableau-de-bord.png", "Tableau de bord ARCHIVA360", frame=True, lazy=False)),
        body=section(feat_html)
        + section('<div class="wp-block-columns cols-2 gap-lg is-vertically-aligned-center" style="--cols:2"><div class="wp-block-column">'
                  + intro("Une architecture, cinq briques", "Capture, gestion et archivage s'appuient sur deux couches communes : l'intelligence artificielle, qui lit et classe, et le coffre-fort, qui sécurise et prouve.", "Architecture")
                  + ul(["Multi-organisations : chaque organisation dispose d'un espace strictement isolé", "Tenant dédié pour les clients les plus sensibles", "Français et anglais, puis portugais et arabe", "Packs pays : règles, métadonnées, durées et connecteurs adaptés"])
                  + f'</div><div class="wp-block-column">{arch}</div></div>', "navy")
        + section(intro("Trois éditions", "Le même cœur logiciel, trois façons de le déployer.", "Éditions", center=True) + editions
                  + buttons(btn("Comparer les offres", "~/archiva360/offres-et-tarifs/"), center=True).replace('class="wp-block-buttons', 'class="wp-block-buttons mt-l'), "mist")
        + section('<div class="wp-block-columns cols-4" style="--cols:4">'
                  + "".join(f'<div class="wp-block-column">{stat(v, l)}</div>' for v, l in [("20", "modules fonctionnels"), ("3", "éditions : Cloud, Enterprise, Government"), ("4", "modes de déploiement"), ("2", "langues au lancement : français, anglais")])
                  + "</div>", "white", "is-compact")
        + section(media_text(img("archiva-go-mobile.png", "Application ARCHIVA GO", 420, 860, cls="is-mobile"),
                             f'<span class="eyebrow">Mobile</span><h2>ARCHIVA GO, vos archives dans la poche</h2><p class="lead">Scanner un document, retrouver un contrat, valider une étape de workflow ou vérifier une boîte d\'archives avec son QR code, depuis Android ou iPhone, en l\'installant directement depuis le navigateur.</p>{ul(["Scanner et photographier avec OCR", "Consulter, approuver, signer via intégration", "Notifications et suivi des demandes d’accès", "Scan des QR codes des boîtes"])}<a class="more-link" href="~/archiva360/archiva-go/">Découvrir ARCHIVA GO {icon("arrow-right")}</a>'), "mist")
        + section(cta_band("Voyez ARCHIVA360 avec vos propres documents", "Nous préparons une démonstration sur un échantillon de vos documents : vous jugez sur pièces.",
                           btn("Demander une démonstration", "~/archiva360/demo/", "white"))),
        nav="archiva360"))

    # Modules
    mods = "".join(
        f'<div class="module" id="module-{i+1:02d}"><span class="module__num">MODULE {i+1:02d}</span><h3>{t}</h3><p>{d}</p><span class="badge {BADGE[v][0]}">{BADGE[v][1]}</span></div>'
        for i, (t, d, v) in enumerate(MODULES))
    roles = [("Super Admin", "Gère toute la plateforme."), ("Organisation Admin", "Gère son organisation."), ("Archiviste", "Gère les archives."),
             ("Records Manager", "Gère les règles de conservation."), ("Document Manager", "Gère les documents."), ("Direction", "Valide et consulte."),
             ("Employé", "Accès métier."), ("Auditeur", "Accès contrôlé, en lecture."), ("Utilisateur externe", "Accès limité et temporaire."), ("Public", "Accès aux archives ouvertes.")]
    meta = ["Document ID", "Organization ID", "Title", "Document Type", "Author", "Creation Date", "Capture Date", "Archive Date", "Department", "Owner",
            "Classification", "Security Level", "Retention Rule", "Retention Start", "Retention End", "Version", "File Format", "File Size", "Checksum",
            "OCR Status", "Digital Signature", "Timestamp", "Physical Location", "Digital Location", "Access Policy", "Created By", "Created At", "Updated At"]
    add(Page(
        "archiva360/modules", "Les 20 modules d'ARCHIVA360",
        description="Dashboard, documents, numérisation, OCR et IA, recherche, workflow, courrier, signature, coffre-fort, records management, archives physiques, audit, sécurité, portail public : les 20 modules d'ARCHIVA360.",
        hero=page_hero("Les 20 modules d'ARCHIVA360", "Une plateforme modulaire : commencez par l'essentiel, activez les modules avancés quand votre organisation est prête.",
                       [("ARCHIVA360", "archiva360/"), ("Modules", None)], "Fonctionnalités"),
        body=section(intro("Tous les modules", "Les modules marqués « Disponible au lancement » composent le socle livré en premier. Les autres arrivent avec les versions 2 et 3 de la plateforme.", split=True)
                     + f'<div class="module-grid">{mods}</div>')
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("Des rôles et des droits précis", "Chaque personne voit et fait uniquement ce que son rôle autorise. Les rôles se combinent avec des droits par dossier, par série et par niveau de confidentialité.", "Utilisateurs")
                  + '</div><div class="wp-block-column">'
                  + table(["Rôle", "Périmètre"], roles, "is-style-stripes") + "</div></div>", "mist")
        + section(intro("Les métadonnées de chaque document", "Au minimum, chaque document porte ces informations. Elles rendent la recherche fiable et la preuve possible.", "Données")
                  + chips(meta) + notice("Chaque document reçoit une empreinte cryptographique (par exemple SHA-256). Si le fichier est modifié, l'empreinte actuelle ne correspond plus à l'empreinte d'origine et la plateforme signale l'altération."))
        + section('<div class="wp-block-columns cols-2 gap-lg is-vertically-aligned-center" style="--cols:2"><div class="wp-block-column">'
                  + intro("Essayez : la preuve d'intégrité", "Modifiez le texte ci-contre, même d'une seule lettre : l'empreinte change entièrement. C'est ainsi qu'ARCHIVA360 détecte toute altération d'une archive.", "Démonstration")
                  + '</div><div class="wp-block-column"><div class="hash-demo"><label for="hash-input">Contenu du document</label>'
                  + '<textarea id="hash-input" rows="3">Contrat fournisseur 2026-0045 — montant : 4 500 000 FCFA — durée : 3 ans.</textarea>'
                  + '<label class="mt-m">Empreinte SHA-256</label><code aria-live="polite">…</code><p class="hash-status is-ok"><i></i><span>Intègre.</span></p></div></div></div>', "mist")
        + section(cta_band("Quel périmètre pour commencer ?", "Nous vous aidons à choisir les modules utiles dès le départ, sans payer pour ce dont vous n'avez pas besoin.",
                           btn("Parler à un expert", "~/contact/?sujet=demo", "white"))),
        nav="archiva360"))

    # ARCHIVA AI
    subs = [("AI OCR", "Lecture du texte", "file"), ("AI Classify", "Classement automatique", "folder"), ("AI Search", "Recherche en langage naturel", "search"),
            ("AI Extract", "Extraction de données", "database"), ("AI Summarize", "Résumés", "files"), ("AI Compare", "Comparaison de versions", "layers"),
            ("AI Assist", "Assistant conversationnel", "sparkles"), ("AI Duplicate", "Détection des doublons", "blocks"), ("AI Metadata", "Métadonnées suggérées", "workflow"),
            ("AI Transcribe", "Transcription audio et vidéo", "play")]
    add(Page(
        "archiva360/archiva-ai", "ARCHIVA AI — l'assistant documentaire",
        description="ARCHIVA AI lit, classe, extrait, résume et compare vos documents. L'IA assiste, elle ne décide pas : destruction, classement définitif et droits restent humains.",
        hero=page_hero("ARCHIVA AI : l'intelligence au service de l'archiviste", "Des heures de saisie et de recherche en moins, sans jamais perdre le contrôle de vos archives.",
                       [("ARCHIVA360", "archiva360/"), ("ARCHIVA AI", None)], "Intelligence artificielle",
                       buttons(btn("Voir une démonstration", "~/archiva360/demo/", "white")),
                       media=img("archiva360-archiva-ai.png", "Assistant ARCHIVA AI", frame=True, lazy=False)),
        body=section(intro("Dix fonctions, une seule identité", "ARCHIVA AI regroupe toutes les capacités d'intelligence artificielle de la plateforme.", "Sous-modules")
                     + cols(*[card(t, d, ic) for t, d, ic in subs], n=5, cls="gap-sm"))
        + section(media_text(img("archiva360-recherche-intelligente.png", "Recherche intelligente", frame=True),
                             f'<span class="eyebrow">Exemples</span><h2>Posez la question comme à un collègue</h2>{ul(["« Trouve-moi tous les contrats fournisseurs de 2022 »", "« Toutes les factures supérieures à 10 millions FCFA »", "« Tous les dossiers du personnel arrivant à échéance en 2027 »", "« Tous les documents concernant le projet autoroute Abidjan–Lagos »", "« Compare ces deux contrats » · « Trouve les doublons »"], "dash")}'), "mist")
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("Nos garde-fous", "Une IA utile dans l'archivage est une IA encadrée.", "Gouvernance")
                  + '</div><div class="wp-block-column">'
                  + ul(["<strong>L'IA assiste, elle ne décide pas</strong> : ni destruction, ni classement définitif, ni droits d'accès sans validation humaine.",
                        "<strong>Respect des droits</strong> : l'assistant ne voit que les documents accessibles à l'utilisateur qui l'interroge.",
                        "<strong>Sources citées</strong> : chaque réponse renvoie aux documents utilisés.",
                        "<strong>Traçabilité</strong> : les propositions de l'IA et leur validation sont inscrites dans l'audit trail.",
                        "<strong>Confidentialité</strong> : vos documents ne servent pas à entraîner des modèles partagés."])
                  + "</div></div>", "navy")
        + section(cta_band("Testez ARCHIVA AI sur vos documents", "Envoyez-nous un lot d'exemple : nous vous montrons ce que l'IA en extrait.", btn("Organiser un test", "~/contact/?sujet=demo", "white"))),
        nav="archiva360"))

    # ARCHIVA GO
    add(Page(
        "archiva360/archiva-go", "ARCHIVA GO — l'application mobile",
        description="ARCHIVA GO, l'application mobile d'ARCHIVA360 : installable dès aujourd'hui depuis le navigateur sur Android et iPhone, sans passer par un store.",
        hero=page_hero("ARCHIVA GO, l'archive dans votre poche", "L'application mobile d'ARCHIVA360 s'installe dès aujourd'hui depuis votre navigateur, sur Android comme sur iPhone : gratuite, sans store, toujours à jour.",
                       [("ARCHIVA360", "archiva360/"), ("ARCHIVA GO", None)], "Application mobile",
                       buttons(btn("Ouvrir et installer l'application", "~/archiva360/connexion/", "white"),
                               btn("Essayer la démo", "~/archiva360/demo-interactive/", "outline")),
                       media=img("archiva-go-mobile.png", "Application ARCHIVA GO", 420, 860, cls="is-mobile", lazy=False)),
        body=section(intro("Installer en 30 secondes", "Ouvrez la page de connexion ARCHIVA360 sur votre téléphone, puis ajoutez-la à votre écran d'accueil. L'icône ARCHIVA360 apparaît et l'application s'ouvre en plein écran.", "Installation")
                     + cols('<h3>Sur Android (Chrome)</h3>' + steps([
                                ("Ouvrez la page de connexion", "Rendez-vous sur la page « Connexion à ARCHIVA360 » depuis Chrome."),
                                ("Touchez « Installer l'application »", "Le bouton apparaît sous le formulaire. À défaut : menu ⋮, puis « Installer l'application » ou « Ajouter à l'écran d'accueil »."),
                                ("Confirmez", "ARCHIVA360 rejoint vos applications, avec son icône.")]),
                            '<h3>Sur iPhone et iPad (Safari)</h3>' + steps([
                                ("Ouvrez la page dans Safari", "L'installation sur iPhone passe obligatoirement par Safari."),
                                ("Touchez « Partager »", "Le carré avec une flèche vers le haut, en bas de l'écran."),
                                ("Choisissez « Sur l'écran d'accueil »", "Puis « Ajouter » : l'icône ARCHIVA360 apparaît sur votre écran d'accueil.")]), n=2, cls="gap-lg")
                     + buttons(btn("Ouvrir la page de connexion", "~/archiva360/connexion/")))
        + section(intro("Ce que vous pouvez faire", "", "Fonctions") + cols(*[feature(t, d, ic) for t, d, ic in [
            ("Se connecter et gérer son compte", "Connexion sécurisée, mot de passe oublié, profil. <b>Disponible.</b>", "key"),
            ("Gérer les utilisateurs et les rôles", "Inviter, attribuer un rôle, retirer un accès, depuis le téléphone. <b>Disponible.</b>", "users"),
            ("Scanner", "Photographier un document : OCR et métadonnées proposées. <b>Disponible dans la démo.</b>", "scan"),
            ("Rechercher et consulter", "La recherche en langage naturel d'ARCHIVA360. <b>Disponible dans la démo.</b>", "search"),
            ("Scanner un QR code", "Identifier une boîte ou un dossier physique et ouvrir sa fiche. <b>À venir.</b>", "qr"),
            ("Approuver", "Valider une étape de workflow en un geste. <b>À venir.</b>", "check-circle"),
            ("Signer", "Signature électronique via le prestataire intégré. <b>À venir.</b>", "pen"),
            ("Notifications", "Être prévenu des tâches, échéances et demandes. <b>À venir.</b>", "inbox"),
            ("Travail hors connexion", "Les écrans s'ouvrent sans réseau ; l'envoi reprend au retour de la connexion. <b>Disponible pour les écrans, à venir pour l'envoi.</b>", "cloud")]], n=3, cls="gap-lg"), "mist")
        + section(notice("Versions Google Play et App Store : en préparation. L'application installable depuis le navigateur offre déjà les mêmes écrans et se met à jour automatiquement, sans téléchargement.", ""), "white", "is-compact"),
        nav="archiva360"))

    # Offres et tarifs
    plans = [
        ("Start", "Petites structures", "25 000", "FCFA / mois", False, ["5 utilisateurs", "Stockage limité", "GED et recherche", "OCR", "Sauvegarde", "Support"]),
        ("Business", "PME", "75 000", "FCFA / mois", True, ["20 utilisateurs", "Workflows", "OCR avancé", "Audit trail", "API", "Règles de conservation", "Application mobile"]),
        ("Professional", "Organisations en croissance", "200 000", "FCFA / mois", False, ["Utilisateurs selon besoin", "Records management complet", "Archives physiques et QR", "Coffre-fort", "Formation incluse"]),
        ("Enterprise", "Grands groupes", "Sur devis", "", False, ["Utilisateurs illimités selon contrat", "SSO, API, ERP", "Workflows avancés", "Stockage dédié", "SLA", "Audit"]),
        ("Government", "Administrations", "Sur devis", "", False, ["Infrastructure dédiée", "Sur site ou cloud privé", "Sécurité renforcée", "Intégration SI", "Portail public"]),
    ]
    pt = [
        f'<div class="pricing-table{" is-featured" if f else ""}">{"<span class=pricing-table__badge>Le plus choisi</span>" if f else ""}<h3>ARCHIVA {n}</h3><p class="pricing-table__for">{w}</p>'
        f'<div class="pricing-table__price">{"<small>À partir de</small>" if u else "<small>&nbsp;</small>"}<b>{p}</b> <span>{u}</span></div>{ul(li)}'
        f'{btn("Demander un devis" if not u else "Démarrer", "~/contact/?sujet=devis", None if f else "outline", arrow=False)}</div>'
        for n, w, p, u, f, li in plans]
    pricing = ('<div class="wp-block-columns cols-3" style="--cols:3">'
               + "".join(f'<div class="wp-block-column">{x}</div>' for x in pt) + "</div>"
               + '<p class="has-small-font-size has-muted-color mt-m">Tarifs de lancement indicatifs, hors taxes. Le stockage, le nombre d’utilisateurs, les workflows et les exigences de sécurité peuvent faire varier fortement le prix.</p>')
    add(Page(
        "archiva360/offres-et-tarifs", "Offres et tarifs",
        description="ARCHIVA Start, Business, Professional, Enterprise, Government et Heritage : les offres ARCHIVA360 et les tarifs de lancement en FCFA.",
        hero=page_hero("Offres et tarifs", "Des prix pensés pour le marché africain, en FCFA. Le nombre d'utilisateurs, le volume de stockage, les workflows et les exigences de sécurité font varier le prix : chaque proposition est ajustée à votre situation.",
                       [("ARCHIVA360", "archiva360/"), ("Offres et tarifs", None)], "Tarifs"),
        body=section(pricing)
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + card("ARCHIVA Heritage", "Pour les bibliothèques, musées, archives historiques, universités et institutions du patrimoine culturel : numérisation patrimoniale, préservation OAIS, portail public de consultation.", "library", "~/secteurs/patrimoine/", "Découvrir l'offre Heritage")
                  + '</div><div class="wp-block-column">'
                  + card("Stockage et archivage longue durée", "Facturation selon le volume (10 Go, 100 Go, 1 To, 10 To…) et abonnement annuel pour la conservation longue durée. Hébergement privé pour les grands comptes.", "hard-drive", "~/services/hebergement/", "Voir l'hébergement")
                  + "</div></div>", "mist")
        + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                  + intro("Questions sur les tarifs", "", "FAQ") + '</div><div class="wp-block-column">'
                  + faq([("Les prix sont-ils définitifs ?", "Il s'agit d'une grille de lancement indicative. Chaque proposition commerciale est établie après un échange sur vos volumes, vos utilisateurs et vos exigences."),
                         ("La numérisation est-elle comprise ?", "Non. La numérisation est un service facturé à la page ou au projet (scan simple, scan + OCR, scan + OCR + indexation, traitements complexes). Voir le service Numérisation."),
                         ("Y a-t-il des frais d'installation ?", "Les éditions Cloud démarrent sans frais d'installation. Les projets Enterprise et Government comprennent une phase d'intégration chiffrée au devis."),
                         ("Peut-on payer annuellement ?", "Oui, l'abonnement annuel est proposé pour toutes les offres.")])
                  + "</div></div>"),
        nav="archiva360"))

    # Démo
    add(Page(
        "archiva360/demo", "Demander une démonstration d'ARCHIVA360",
        description="Demandez une démonstration d'ARCHIVA360 sur vos propres documents.",
        hero=page_hero("Demander une démonstration", "Une démonstration de 45 minutes, en visioconférence ou dans vos locaux à Abidjan, préparée avec un échantillon de vos documents.",
                       [("ARCHIVA360", "archiva360/"), ("Démonstration", None)], "Démonstration"),
        body=section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                     + intro("Comment se déroule la démonstration", "", "Déroulé")
                     + '<ol class="steps">' + "".join(f"<li><div><h3>{t}</h3><p>{d}</p></div></li>" for t, d in [
                         ("Un premier échange", "15 minutes pour comprendre vos documents et vos priorités."),
                         ("La préparation", "Vous nous confiez quelques documents anonymisés ; nous les chargeons dans un espace de démonstration."),
                         ("La démonstration", "Capture, recherche, classement, conservation et audit sur vos propres exemples."),
                         ("La proposition", "Une proposition de périmètre et de budget, sans engagement.")]) + "</ol>"
                     + '<div class="card is-flat mt-l"><h3>Pas le temps d\'attendre ?</h3><p>La démo interactive fonctionne tout de suite dans votre navigateur : import de documents, OCR, recherche, empreintes, conservation, archives physiques, audit trail.</p>' + btn("Ouvrir la démo interactive", "~/archiva360/demo-interactive/", small=True) + '</div>'
                     + '</div><div class="wp-block-column">' + _form("demo") + "</div></div>"),
        nav="archiva360"))


def _form(default):
    from .pages_main import contact_form
    return contact_form(default)
