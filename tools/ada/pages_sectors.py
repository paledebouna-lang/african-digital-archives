from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons,
                   faq, page_hero, notice, chips, tiles, MENU)
from .icons import icon

SECTORS = [
    {
        "slug": "gouvernement", "name": "Gouvernement et collectivités", "short": "Gouvernement", "icon": "landmark", "edition": "Government",
        "lead": "Ministères, mairies, préfectures, collectivités, établissements publics, tribunaux et agences : moderniser la gestion des archives publiques, dans le respect des règles d'accès et de communicabilité.",
        "challenges": ["Des décennies d'archives papier dans des locaux exposés à l'humidité, au feu et aux nuisibles", "Des actes administratifs et registres difficiles à retrouver", "Des exigences de souveraineté des données", "Des demandes d'accès des citoyens à traiter"],
        "docs": ["Actes administratifs", "Délibérations", "Registres d'état civil", "Arrêtés et décisions", "Marchés publics", "Courrier officiel", "Dossiers du personnel", "Plans et cadastre", "Archives historiques"],
        "features": [("Déploiement souverain", "Cloud souverain, infrastructure privée, installation sur site ou hybride : chaque administration dispose de son espace sécurisé.", "server"),
                     ("Gestion du courrier", "Enregistrement, affectation, traitement et archivage du courrier entrant et sortant.", "inbox"),
                     ("Portail citoyen", "Recherche, demande, autorisation, consultation : l'accès aux archives ouvertes, dans le respect des règles de communicabilité.", "globe"),
                     ("Archivage réglementaire", "Règles de conservation par type d'acte, sort final, versement aux archives historiques.", "archive")],
        "case": ("Exemple : une mairie et ses 3 millions de pages", "Audit, classement, inventaire, numérisation, OCR, indexation, contrôle qualité, import dans ARCHIVA360, création des règles de conservation, mise en ligne des archives autorisées. Résultat : un document retrouvé en quelques secondes au lieu d'heures de recherche dans les armoires.", "blog/numeriser-3-millions-de-pages-methode/"),
        "shot": "archiva360-archives-physiques.png",
    },
    {
        "slug": "banque", "name": "Banque et microfinance", "short": "Banque", "icon": "bank", "edition": "Enterprise",
        "lead": "Dossiers clients, crédits, garanties, conformité : des volumes considérables, des obligations de conservation strictes et une exigence absolue de confidentialité.",
        "challenges": ["Des dossiers de crédit dispersés entre agences et siège", "Des contrôles et audits qui exigent de retrouver vite une pièce", "Des pièces d'identité et données personnelles à protéger", "Des garanties dont les échéances doivent être suivies"],
        "docs": ["Dossiers d'ouverture de compte", "Pièces d'identité (KYC)", "Contrats de crédit", "Garanties et sûretés", "Relevés", "Correspondances", "Rapports d'audit", "Dossiers du personnel"],
        "features": [("Coffre-fort numérique", "Les contrats et garanties dans ARCHIVE VAULT : chiffrement, MFA, journalisation, horodatage.", "lock"),
                     ("Intégration SI", "API et connecteurs avec le système bancaire, l'ERP et l'annuaire (SSO).", "api"),
                     ("Alertes d'échéance", "Garanties, contrats et pièces arrivant à échéance signalés à l'avance.", "clock"),
                     ("Audit trail", "Qui a consulté quel dossier, quand, depuis où : prêt pour les contrôles.", "eye")],
        "case": ("La recherche au service de la conformité", "« Toutes les garanties expirant avant le 31/12 », « Dossiers de crédit supérieurs à 50 millions FCFA » : la recherche intelligente répond en quelques secondes, dans le respect des droits de chacun.", "solutions/ia-documentaire/"),
        "shot": "archiva360-security-center.png",
    },
    {
        "slug": "assurance", "name": "Assurance", "short": "Assurance", "icon": "umbrella", "edition": "Enterprise",
        "lead": "Polices, avenants, déclarations de sinistre, expertises, pièces justificatives : accélérer la gestion des dossiers tout en garantissant leur conservation.",
        "challenges": ["Des dossiers sinistres composés de dizaines de pièces hétérogènes", "Des délais de traitement qui dépendent de la recherche de documents", "Des durées de conservation longues après la fin des contrats", "Des échanges nombreux avec experts, courtiers et assurés"],
        "docs": ["Polices et avenants", "Déclarations de sinistre", "Rapports d'expertise", "Photos et vidéos", "Factures de réparation", "Correspondances", "Quittances"],
        "features": [("Dossier sinistre unique", "Toutes les pièces d'un sinistre réunies, liées à la police, visibles par les bons intervenants.", "folder"),
                     ("Extraction automatique", "L'IA lit les déclarations et factures et renseigne les métadonnées.", "sparkles"),
                     ("Workflows de validation", "Circuits d'indemnisation avec seuils, validations et signature.", "workflow"),
                     ("Documents audiovisuels", "Photos, vidéos et enregistrements gérés comme des documents, avec métadonnées.", "play")],
        "case": ("Des circuits adaptés aux montants", "Un workflow peut ajouter une étape de validation au-delà d'un certain montant d'indemnisation, puis archiver automatiquement le dossier clos avec sa règle de conservation.", "solutions/workflow-courrier/"),
        "shot": "archiva360-workflow.png",
    },
    {
        "slug": "sante", "name": "Santé", "short": "Santé", "icon": "heart-pulse", "edition": "Enterprise ou Government",
        "lead": "Hôpitaux, cliniques et laboratoires : des dossiers et comptes rendus sensibles, qui exigent un niveau de confidentialité et de protection des données particulièrement élevé.",
        "challenges": ["Des dossiers patients papier volumineux et difficiles à partager entre services", "Des données de santé soumises à une protection renforcée", "Des examens et images à conserver sur de longues durées", "Des documents administratifs et financiers à côté des dossiers médicaux"],
        "docs": ["Dossiers patients", "Comptes rendus", "Résultats d'examens", "Imagerie", "Prescriptions", "Consentements", "Documents administratifs", "Dossiers du personnel"],
        "features": [("Accès extrêmement contrôlé", "Droits par service et par rôle, accès d'urgence tracé, MFA obligatoire.", "lock"),
                     ("Protection des données", "Conception conforme à la loi ivoirienne n°2013-450 sur la protection des données personnelles.", "shield"),
                     ("Hébergement maîtrisé", "Installation sur site ou cloud privé pour les établissements qui le souhaitent.", "server"),
                     ("Traçabilité complète", "Chaque consultation de dossier est enregistrée et contrôlable.", "eye")],
        "case": ("HEALTH ARCHIVE, un module dédié", "Pour les établissements autorisés, le module HEALTH ARCHIVE organise dossiers, comptes rendus, examens, images, prescriptions et documents administratifs, avec des règles d'accès renforcées.", "solutions/securite/"),
        "shot": "archiva360-security-center.png",
        "note": "Les projets dans le secteur de la santé font systématiquement l'objet d'une étude préalable de protection des données, menée avec votre délégué à la protection des données et un juriste.",
    },
    {
        "slug": "education", "name": "Éducation et recherche", "short": "Éducation", "icon": "graduation", "edition": "Cloud, Enterprise ou Government",
        "lead": "Universités, grandes écoles, établissements scolaires et centres de formation : des dossiers étudiants et des diplômes à conserver parfois pour toujours.",
        "challenges": ["Des demandes d'attestations et de relevés qui mobilisent les services de scolarité", "Des diplômes et procès-verbaux à conserver à titre permanent", "Des mémoires et thèses à rendre consultables", "Des dossiers enseignants et administratifs dispersés"],
        "docs": ["Dossiers étudiants", "Diplômes", "Relevés de notes", "Inscriptions", "Procès-verbaux de délibération", "Mémoires et thèses", "Dossiers enseignants", "Archives administratives"],
        "features": [("EDU ARCHIVE", "Un module dédié aux dossiers étudiants, diplômes, relevés, inscriptions et procès-verbaux.", "graduation"),
                     ("Vérification des diplômes", "Empreinte et QR code pour vérifier l'authenticité d'un diplôme délivré.", "fingerprint"),
                     ("Bibliothèque numérique", "Mémoires et thèses consultables en plein texte, selon les droits de diffusion.", "library"),
                     ("Conservation permanente", "Préservation numérique des registres et procès-verbaux historiques.", "layers")],
        "case": ("Un diplôme vérifiable en quelques secondes", "Chaque diplôme numérisé ou émis peut recevoir une empreinte cryptographique. Un employeur vérifie qu'il correspond bien à l'original enregistré.", "blog/blockchain-archives-empreinte-pas-document/"),
        "shot": "archiva360-recherche-intelligente.png",
    },
    {
        "slug": "industrie", "name": "Industrie, énergie et BTP", "short": "Industrie", "icon": "factory", "edition": "Enterprise",
        "lead": "Construction, mines, pétrole, énergie, télécoms, industrie : des plans, études, permis, certificats et rapports d'inspection qui doivent suivre les installations pendant des décennies.",
        "challenges": ["Des plans grands formats et dessins techniques uniquement sur papier", "Des versions multiples d'un même plan", "Des rapports d'inspection et de maintenance à produire lors des contrôles", "Des chantiers éloignés avec une connexion limitée"],
        "docs": ["Plans et dessins techniques", "Études", "Rapports", "Permis", "Certificats", "Rapports d'inspection", "Dossiers de maintenance", "Contrats de marché"],
        "features": [("Numérisation grands formats", "Scanners de plans et grands formats dans notre centre d'Abidjan.", "scan"),
                     ("Gestion des versions", "Un seul plan de référence, l'historique complet des révisions.", "layers"),
                     ("Capture sur chantier", "ARCHIVA GO, y compris hors connexion, pour les équipes sur le terrain.", "smartphone"),
                     ("Documents liés", "Un équipement, ses plans, ses certificats et ses rapports de maintenance reliés.", "link")],
        "case": ("Un dossier par ouvrage", "Chaque ouvrage ou installation dispose d'un dossier structuré : études, plans, permis, réception, maintenance. Il se transmet sans perte d'un exploitant à l'autre.", "services/numerisation/"),
        "shot": "archiva360-plan-de-classement.png",
    },
    {
        "slug": "immobilier", "name": "Immobilier et foncier", "short": "Immobilier", "icon": "home", "edition": "Cloud ou Enterprise",
        "lead": "Promoteurs, agences, gestionnaires, notaires et services fonciers : des titres, actes, plans et permis dont la perte peut coûter très cher.",
        "challenges": ["Des titres de propriété et actes originaux uniques", "Des dossiers de vente composés de nombreuses pièces", "Des plans et permis à retrouver des années après", "Des litiges fonciers qui exigent la preuve des documents"],
        "docs": ["Titres fonciers", "Actes", "Contrats de vente et de bail", "Plans", "Permis de construire", "Dossiers techniques", "Photos", "Expertises"],
        "features": [("Originaux suivis", "Les originaux papier localisés et suivis dans le module Archives physiques.", "box"),
                     ("Preuve d'intégrité", "Empreinte et horodatage pour prouver l'état d'un document à une date donnée.", "fingerprint"),
                     ("Dossier par bien", "Toutes les pièces d'un bien réunies, du titre aux photos.", "home"),
                     ("Partage sécurisé", "Partage limité et temporaire avec acquéreurs, notaires et banques.", "link")],
        "case": ("Connecté à votre écosystème", "ARCHIVA360 peut se connecter à vos outils de gestion immobilière par API, pour que chaque bien dispose automatiquement de son dossier documentaire.", "solutions/ged/"),
        "shot": "archiva360-archives-physiques.png",
    },
    {
        "slug": "juridique", "name": "Juridique", "short": "Juridique", "icon": "scale", "edition": "Cloud ou Enterprise",
        "lead": "Cabinets d'avocats, notaires, directions juridiques : contrats, statuts, procès-verbaux, contentieux, décisions et propriété intellectuelle.",
        "challenges": ["Des contrats dont il faut suivre les échéances et obligations", "Des dossiers de contentieux volumineux", "Des documents confidentiels à protéger strictement", "Des versions de contrats difficiles à comparer"],
        "docs": ["Contrats", "Statuts", "Procès-verbaux", "Contentieux", "Actes", "Décisions", "Propriété intellectuelle", "Licences", "Conventions"],
        "features": [("LEGAL ARCHIVE", "Un espace dédié aux contrats, statuts, PV, contentieux et propriété intellectuelle.", "scale"),
                     ("Analyse de contrats", "« Trouve les obligations du fournisseur », « Compare ces deux versions ».", "sparkles"),
                     ("Gel juridique", "Suspension des destructions pour les dossiers en contentieux.", "lock"),
                     ("Signature électronique", "Circuits de validation et signature avec horodatage.", "pen")],
        "case": ("Chronologie d'un dossier", "ARCHIVA AI construit la chronologie d'un dossier de contentieux à partir de ses pièces, avec les références de chaque document. L'avocat vérifie et complète.", "solutions/ia-documentaire/"),
        "shot": "archiva360-archiva-ai.png",
    },
    {
        "slug": "ong", "name": "ONG et organismes internationaux", "short": "ONG", "icon": "hands", "edition": "Cloud ou Enterprise",
        "lead": "ONG, associations, agences de coopération et organismes internationaux : des dossiers de projets, de financement et d'audit à tenir à la disposition des bailleurs.",
        "challenges": ["Des pièces justificatives exigées par les bailleurs lors des audits", "Des équipes réparties dans plusieurs pays", "Des projets terminés dont il faut conserver la mémoire", "Des budgets contraints"],
        "docs": ["Conventions de financement", "Rapports d'activité", "Pièces justificatives", "Rapports d'audit", "Contrats", "Données de terrain", "Photos et vidéos"],
        "features": [("Multi-pays", "Un espace, plusieurs bureaux pays, des droits adaptés à chacun.", "globe"),
                     ("Prêt pour l'audit", "Pièces justificatives classées par projet, bailleur et ligne budgétaire.", "check-circle"),
                     ("Français et anglais", "Interface bilingue pour les équipes et les partenaires.", "users"),
                     ("Offre Cloud", "Démarrage rapide, sans infrastructure, avec un abonnement adapté.", "cloud")],
        "case": ("Un audit bailleur préparé en quelques heures", "Toutes les pièces d'un projet réunies, classées et exportables avec leur journal d'accès : l'auditeur reçoit un accès limité et temporaire.", "solutions/sae/"),
        "shot": "archiva360-audit-trail.png",
    },
    {
        "slug": "patrimoine", "name": "Patrimoine et culture", "short": "Patrimoine", "icon": "library", "edition": "Heritage",
        "lead": "Bibliothèques, musées, centres de documentation, archives historiques : numériser, préserver et rendre accessible la mémoire de l'Afrique.",
        "challenges": ["Des fonds anciens fragiles, menacés par le climat et le temps", "Des manuscrits, journaux, cartes et photographies uniques", "Un besoin de diffusion auprès des chercheurs et du public", "Des formats numériques à préserver sur des décennies"],
        "docs": ["Livres", "Journaux", "Manuscrits", "Photographies", "Cartes", "Archives historiques", "Thèses", "Enregistrements sonores", "Films"],
        "features": [("Numérisation patrimoniale", "Scanners de livres et grands formats, manipulation adaptée aux documents fragiles.", "scan"),
                     ("Préservation OAIS", "Formats pérennes, contrôle d'intégrité, migration planifiée.", "layers"),
                     ("DIGITAL LIBRARY", "Bibliothèque numérique avec recherche plein texte.", "library"),
                     ("Portail public", "Mise en ligne des fonds autorisés pour les chercheurs et le public.", "globe")],
        "case": ("ARCHIVA Heritage", "Une offre dédiée aux institutions patrimoniales : numérisation, description, préservation et diffusion. Pour que la mémoire documentaire africaine reste accessible aux générations futures.", "solutions/preservation-numerique/"),
        "shot": "archiva360-recherche-intelligente.png",
    },
]


def build():
    add(Page(
        "secteurs", "Secteurs",
        description="Administrations, banques, assurances, santé, éducation, industrie, immobilier, juridique, ONG, patrimoine : ADA adapte ARCHIVA360 aux documents et obligations de chaque secteur.",
        hero=page_hero("Pour les organisations qui ne peuvent pas perdre un document",
                       "Chaque secteur a ses documents, ses obligations et ses contraintes. Nous adaptons ARCHIVA360 et nos services à votre métier.",
                       [("Secteurs", None)], "Secteurs"),
        body=section(cols(*[card(s["name"], s["lead"], s["icon"], f"~/secteurs/{s['slug']}/", "Voir le secteur") for s in SECTORS], n=3))
        + section(intro("Nos marchés prioritaires", "Nous commençons par les organisations qui en ont le plus besoin, en Côte d'Ivoire, puis dans la sous-région.", "Priorités", center=True)
                  + '<div class="wp-block-columns cols-5 gap-sm" style="--cols:5">' + "".join(
                      f'<div class="wp-block-column"><div class="card is-flat"><span class="eyebrow">Priorité {i}</span><h3>{t}</h3><p>{d}</p></div></div>'
                      for i, (t, d) in enumerate([("Grandes entreprises", "Banques, assurances, télécoms, industries, immobilier, transport, énergie."),
                                                   ("Administrations", "Ministères, mairies, agences, établissements publics."),
                                                   ("Éducation", "Universités, écoles, centres de formation."),
                                                   ("Santé", "Cliniques, hôpitaux, laboratoires."),
                                                   ("Patrimoine", "Bibliothèques, musées, centres historiques, archives.")], 1)) + "</div>", "mist"),
        nav="secteurs"))

    for i, s in enumerate(SECTORS):
        others = [x for x in SECTORS if x is not s]
        note = section(notice(s["note"], "warning"), "white", "is-compact") if s.get("note") else ""
        body = (
            section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                    + intro("Vos enjeux", "", "Le constat") + ul(s["challenges"], "dash")
                    + '</div><div class="wp-block-column">' + intro("Les documents concernés", "", "Documents") + chips(s["docs"])
                    + f'<p class="has-muted-color">Édition recommandée : <strong>ARCHIVA360 {s["edition"]}</strong>. <a href="~/archiva360/offres-et-tarifs/">Voir les offres</a></p>'
                    + "</div></div>")
            + note
            + section(intro("Ce qu'ADA vous apporte", "", "Nos réponses") + cols(*[feature(t, d, ic) for t, d, ic in s["features"]], n=2, cls="gap-lg"), "mist")
            + section(media_text(img(s["shot"], f"ARCHIVA360 pour le secteur {s['short']}", frame=True),
                                 f'<span class="eyebrow">Cas d\'usage</span><h2>{s["case"][0]}</h2><p class="lead">{s["case"][1]}</p>'
                                 f'<a class="more-link" href="~/{s["case"][2]}">En savoir plus {icon("arrow-right")}</a>'))
            + section(cta_band(f"Un projet dans le secteur {s['short'].lower()} ?", "Commençons par un audit documentaire et un projet pilote sur un fonds représentatif.",
                               btn("Demander un audit", "~/contact/?sujet=audit", "white")))
            + section(intro("Autres secteurs", "", "Explorer") + tiles([(f"secteurs/{o['slug']}/", o["short"], o["icon"]) for o in others[:6]]), "mist", "is-compact")
        )
        add(Page(f"secteurs/{s['slug']}", s["name"], body, description=s["lead"],
                 hero=page_hero(s["name"], s["lead"], [("Secteurs", "secteurs/"), (s["short"], None)], "Secteur",
                                buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"), btn("Voir une démo", "~/archiva360/demo/", "outline"))),
                 nav="secteurs"))
