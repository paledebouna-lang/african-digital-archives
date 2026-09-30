from .core import (Page, add, section, intro, cols, card, feature, ul, img, media_text, cta_band, btn, buttons,
                   faq, page_hero, notice, steps, table, chips, MENU)
from .icons import icon

SOLUTIONS = [
    {
        "slug": "ged", "title": "GED — Gestion électronique des documents", "short": "GED", "icon": "folder",
        "desc": "Créer, capturer, classer, partager et retrouver vos documents au quotidien, avec versions, droits d'accès et traçabilité.",
        "hero": "Vos équipes créent, reçoivent et modifient des documents toute la journée. La GED d'ARCHIVA360 les range au bon endroit, avec les bonnes métadonnées, et les rend retrouvables en quelques secondes.",
        "shot": ("archiva360-document-ocr.png", "Fiche document dans ARCHIVA360 avec métadonnées extraites"),
        "features": [
            ("Import et dépôt", "Glisser-déposer, import massif, capture depuis un scanner, un e-mail ou l'application mobile.", "download"),
            ("Classement structuré", "Arborescences par direction et service, plan de classement commun, métadonnées obligatoires par type.", "folder"),
            ("Versions et verrouillage", "Historique complet des versions, verrouillage pendant la modification, comparaison entre versions.", "layers"),
            ("Prévisualisation", "PDF, PDF/A, Word, Excel, PowerPoint, images, TIFF, audio, vidéo et ZIP, sans téléchargement.", "eye"),
            ("Partage maîtrisé", "Partage interne ou externe avec droits limités, date d'expiration et journalisation.", "link"),
            ("Recherche", "Plein texte, OCR, métadonnées, tags, dates, montants, services et types de documents.", "search"),
        ],
        "detail_h": "Un classement que tout le monde comprend",
        "detail": "<p>La plupart des organisations ne manquent pas de documents : elles manquent d'un classement commun. ARCHIVA360 part de votre organisation réelle (Direction générale, Finance, RH, Juridique, Technique…) et la traduit en dossiers, séries et types de documents.</p><p>Chaque type de document porte ses propres métadonnées obligatoires. Une facture demande un fournisseur, un numéro et un montant ; un contrat, des parties, une date de signature et une échéance. Le classement cesse de dépendre de la mémoire de chacun.</p>",
        "detail_list": ["Arborescence type : Direction générale › Juridique › Contrats, Contentieux, Conventions", "Métadonnées proposées automatiquement par l'OCR et l'IA, validées par l'utilisateur", "Doublons signalés à l'import", "Documents liés entre eux : un contrat, ses avenants, ses factures"],
        "detail_shot": ("archiva360-plan-de-classement.png", "Plan de classement dans ARCHIVA360"),
        "faq": [
            ("Quelle différence entre la GED et l'archivage électronique ?", "La GED sert à travailler sur des documents vivants : les créer, les modifier, les partager. L'archivage électronique (SAE) intervient quand un document doit être conservé selon des règles, avec intégrité, traçabilité et durée de conservation. ARCHIVA360 réunit les deux, et fait passer un document de l'un à l'autre au bon moment."),
            ("Peut-on reprendre nos fichiers existants ?", "Oui. Nos équipes reprennent vos serveurs de fichiers, disques externes, boîtes e-mail et anciens logiciels : dédoublonnage, classement, métadonnées, puis import. Voir notre service de migration."),
            ("Quels formats sont acceptés ?", "Tous les formats courants : PDF, PDF/A, Word, Excel, PowerPoint, JPG, PNG, TIFF, audio, vidéo, ZIP. Pour la conservation longue durée, nous recommandons des formats pérennes comme le PDF/A."),
        ],
    },
    {
        "slug": "sae", "title": "Archivage électronique (SAE)", "short": "SAE", "icon": "archive",
        "desc": "Conserver vos documents avec intégrité, traçabilité et durées de conservation maîtrisées, pour qu'ils gardent leur valeur de preuve.",
        "hero": "Un document archivé doit rester intègre, retrouvable et opposable pendant toute sa durée de conservation. Le système d'archivage électronique d'ARCHIVA360 le garantit, de l'archivage au sort final.",
        "shot": ("archiva360-retention-center.png", "Retention Center d'ARCHIVA360"),
        "features": [
            ("Versement contrôlé", "Le document entre dans le SAE avec ses métadonnées, son format vérifié et son empreinte cryptographique.", "archive"),
            ("Intégrité", "Empreinte SHA-256 calculée à l'archivage et vérifiée périodiquement. Toute altération est signalée.", "fingerprint"),
            ("Horodatage", "Date certaine de l'archivage, par intégration avec un prestataire de confiance.", "clock"),
            ("Durées de conservation", "Règles par type de document, événement déclencheur, calcul automatique des échéances.", "hourglass"),
            ("Gel juridique", "Suspension de toute destruction en cas de contentieux, d'audit ou d'enquête.", "lock"),
            ("Journal inaltérable", "Chaque consultation, communication ou décision est inscrite dans l'audit trail.", "eye"),
        ],
        "detail_h": "Du document actif au sort final, sans rupture",
        "detail": "<p>Un document suit un cycle de vie : il est créé, utilisé activement, consulté de temps en temps, archivé, puis conservé à long terme ou éliminé. Le SAE applique les règles définies pour chaque type de document et calcule les échéances à votre place.</p><p>Quand une échéance arrive, rien n'est supprimé automatiquement. Le responsable examine les documents et décide : conserver, transférer ou détruire selon la procédure autorisée. Chaque décision est tracée.</p>",
        "detail_list": ["Alerte : « 1 250 documents arrivent à échéance dans 90 jours »", "Actions possibles : conserver, transférer, détruire selon procédure", "Pas de bouton « supprimer définitivement » accessible à tous", "Certificat de destruction généré et archivé"],
        "detail_shot": ("archiva360-audit-trail.png", "Audit trail d'ARCHIVA360"),
        "extra": "cycle",
        "faq": [
            ("Un document archivé électroniquement a-t-il une valeur juridique en Côte d'Ivoire ?", "Le cadre ivoirien reconnaît l'archivage électronique sécurisé (loi n°2013-546 relative aux transactions électroniques, décret n°2016-851 sur les modalités de l'archivage électronique). La valeur probante dépend des conditions de conservation : intégrité, traçabilité, durée. Nous faisons valider chaque dispositif par un juriste avant de le présenter comme conforme."),
            ("Qui fixe les durées de conservation ?", "Votre organisation, avec un archiviste et un juriste, selon votre secteur et la réglementation applicable. La plateforme applique les règles ; elle n'invente jamais une durée légale."),
            ("Peut-on archiver des e-mails ?", "Oui. Les e-mails et leurs pièces jointes peuvent être capturés, classés et archivés comme n'importe quel document, avec leurs métadonnées d'origine."),
        ],
    },
    {
        "slug": "records-management", "title": "Records management", "short": "Records management", "icon": "hourglass",
        "desc": "Gérer vos documents d'activité selon leur contexte, leurs responsables, leurs métadonnées et leur cycle de vie, conformément à l'ISO 15489.",
        "hero": "Le records management est ce qui fait passer une GED à une véritable plateforme d'archivage : chaque document d'activité a un contexte, un responsable, des règles et une fin de vie prévue.",
        "shot": ("archiva360-plan-de-classement.png", "Plan de classement et règles de gestion"),
        "features": [
            ("Plan de classement", "Catégorie, sous-catégorie, série, sous-série, type de document : une structure validée par l'archiviste.", "workflow"),
            ("Types de documents", "Pour chaque type : métadonnées, confidentialité, propriétaire, service responsable.", "file"),
            ("Règles de conservation", "Durées de 5, 10, 20, 30 ans ou permanentes, selon les règles de l'organisation et le cadre juridique.", "hourglass"),
            ("Événements déclencheurs", "Fin de contrat, départ d'un salarié, clôture d'exercice : la durée court à partir du bon événement.", "calendar"),
            ("Sort final", "Destruction, versement aux archives historiques ou conservation permanente.", "archive"),
            ("Restrictions et gel", "Restrictions d'accès, gel juridique, responsables désignés pour chaque série.", "lock"),
        ],
        "detail_h": "Un plan de classement construit avec vous",
        "detail": "<p>Nous ne livrons pas un plan de classement générique. Notre archiviste le construit avec vos services, à partir de vos documents réels et de vos obligations. Il est ensuite paramétré dans ARCHIVA360, versionné et documenté.</p><p>Les métadonnées font partie des concepts fondamentaux du records management selon l'ISO 15489. Chaque série reçoit les siennes : titre, auteur, dates, service, numéro, client, projet, localisation, confidentialité, durée, statut, version, empreinte.</p>",
        "detail_list": ["Plan de classement versionné et validé", "Référentiel des durées de conservation", "Matrice des responsabilités par série", "Documentation remise à l'organisation"],
        "detail_shot": ("archiva360-retention-center.png", "Échéances de conservation"),
        "extra": "cycle",
        "faq": [
            ("Faut-il un archiviste dans notre organisation ?", "Ce n'est pas obligatoire au démarrage. ADA met à disposition un archiviste pour concevoir les règles, puis forme un référent interne. À terme, un responsable documentaire identifié reste une bonne pratique."),
            ("Le records management s'applique-t-il aussi au papier ?", "Oui. Les mêmes règles s'appliquent aux boîtes et dossiers physiques, suivis dans le module Archives physiques."),
        ],
    },
    {
        "slug": "capture-numerisation", "title": "Capture et numérisation", "short": "Capture et numérisation", "icon": "scan",
        "desc": "Scanner, importer, reconnaître le texte, contrôler la qualité et indexer automatiquement : le papier devient une information exploitable.",
        "hero": "Un document scanné sans OCR ni métadonnées n'est qu'une image. ARCHIVA360 transforme chaque page capturée en document lisible, classé et retrouvable.",
        "shot": ("archiva360-document-ocr.png", "Extraction automatique des données d'une facture"),
        "features": [
            ("Scan et import massif", "Scanners de production, multifonctions, import de lots, capture mobile avec ARCHIVA GO.", "scan"),
            ("OCR", "Reconnaissance du texte sur les documents imprimés, en français et en anglais.", "file"),
            ("Contrôle qualité", "Détection des pages blanches, pages manquantes, images floues ou mal orientées.", "check-circle"),
            ("Séparation automatique", "Détection des pages de garde et des codes-barres pour séparer les dossiers d'un même lot.", "layers"),
            ("Indexation", "Extraction des données clés et création automatique des métadonnées.", "database"),
            ("Capture e-mail et API", "Boîtes de réception dédiées, connecteurs et API pour vos applications métier.", "api"),
        ],
        "detail_h": "Exemple : 2 000 factures chargées d'un coup",
        "detail": "<p>Un utilisateur charge 2 000 factures scannées. ARCHIVA AI lit chaque document et extrait le fournisseur, la date, le numéro, le montant, la TVA, la devise, le client et le numéro de commande. Puis il propose un classement automatique.</p><p>L'utilisateur voit le niveau de confiance de chaque champ, corrige si besoin et valide. Les factures sont alors retrouvables par fournisseur, par montant ou par période.</p>",
        "detail_list": ["Facture_2023_0045.pdf → Société : ABC SA", "Date : 12/04/2023 · Montant : 4 500 000 FCFA", "Numéro : FAC-0045 · Département : Comptabilité", "Métadonnées créées automatiquement, validées par l'utilisateur"],
        "detail_shot": ("archiva360-recherche-intelligente.png", "Recherche sur les données extraites"),
        "chain": True,
        "faq": [
            ("Vous numérisez aussi pour nous ?", "Oui. Notre centre de numérisation d'Abidjan prend en charge vos fonds, ou nos équipes interviennent sur site. Voir le service Numérisation."),
            ("Et les documents manuscrits ?", "L'OCR donne d'excellents résultats sur les documents imprimés. Pour les manuscrits, nous combinons une indexation manuelle par nos opérateurs et, selon les fonds, des outils de reconnaissance d'écriture."),
        ],
    },
    {
        "slug": "archives-physiques", "title": "Archives physiques", "short": "Archives physiques", "icon": "box",
        "desc": "Localiser chaque boîte, dossier et original papier grâce à un identifiant unique et un QR code, et suivre tous ses mouvements.",
        "hero": "Beaucoup de dossiers sont hybrides : une partie papier, une partie numérique. ARCHIVA360 est aussi un système de gestion des archives physiques, pour ne plus jamais perdre la trace d'un original.",
        "shot": ("archiva360-archives-physiques.png", "Fiche d'une boîte d'archives physiques"),
        "features": [
            ("ARCHIVA ID", "Chaque boîte reçoit un identifiant unique, par exemple CI-ABJ-PLT-2026-000457.", "fingerprint"),
            ("Localisation précise", "Site, bâtiment, salle, rayon, étagère, boîte, dossier.", "map-pin"),
            ("QR code et code-barres", "L'archiviste scanne la boîte et voit immédiatement son contenu, son propriétaire et sa durée de conservation.", "qr"),
            ("Mouvements tracés", "Sorties, prêts, retours, transferts : chaque mouvement est enregistré.", "refresh"),
            ("Lien papier–numérique", "La fiche numérique indique où se trouve l'original, et inversement.", "link"),
            ("Demandes de communication", "Un utilisateur demande un dossier, l'archiviste le prépare, le retour est suivi.", "inbox"),
        ],
        "detail_h": "Le papier compte aussi",
        "detail": "<p>La plateforme ne se contente pas de dire « document numérique disponible ». Elle indique aussi : document original physique — entrepôt Abidjan, salle B, rayon 04, étagère 12, boîte 045, dossier 0087.</p><p>Les mêmes règles de conservation s'appliquent au papier et au numérique. Quand une boîte arrive à échéance, elle apparaît dans le Retention Center comme n'importe quel document.</p>",
        "detail_list": ["Étiquettes QR imprimables pour boîtes, dossiers et étagères", "Inventaire des fonds existants par nos équipes", "Scan du QR avec ARCHIVA GO", "Contenu, dates, propriétaire, emplacement, durée, statut"],
        "detail_shot": ("archiva-go-mobile.png", "Application ARCHIVA GO"),
        "faq": [
            ("Vous stockez nos archives papier ?", "Notre offre porte d'abord sur l'organisation, l'inventaire et le suivi de vos archives physiques, chez vous. Le stockage externalisé fait partie de notre offre de gestion complète, à étudier selon vos volumes."),
        ],
    },
    {
        "slug": "ia-documentaire", "title": "IA documentaire", "short": "IA documentaire", "icon": "sparkles",
        "desc": "OCR, classification, extraction, recherche en langage naturel, résumés, comparaisons et détection des doublons, sous contrôle humain.",
        "hero": "ARCHIVA AI lit, classe et analyse vos documents pour vous faire gagner des heures. Avec une règle simple : l'IA assiste, elle ne décide pas.",
        "shot": ("archiva360-archiva-ai.png", "L'assistant ARCHIVA AI"),
        "features": [
            ("AI OCR", "Lecture du texte des documents scannés et des images.", "file"),
            ("AI Classify", "Identification du type de document et proposition de classement.", "folder"),
            ("AI Extract", "Extraction des dates, montants, parties, numéros et départements.", "database"),
            ("AI Search", "« Tous les contrats fournisseurs de 2022 » : la recherche comprend votre question.", "search"),
            ("AI Summarize et Compare", "Résumé d'un contrat, comparaison de deux versions, chronologie d'un dossier.", "files"),
            ("AI Duplicate", "Détection des doublons et des quasi-doublons à l'import.", "layers"),
        ],
        "detail_h": "L'IA assiste. Elle ne décide pas.",
        "detail": "<p>ARCHIVA AI ne peut ni modifier ni supprimer arbitrairement une archive. Il respecte les droits de l'utilisateur qui l'interroge : il ne voit que les documents auxquels cette personne a accès.</p><p>La destruction, le classement définitif et les droits d'accès restent des décisions humaines, prises par une personne habilitée et inscrites dans le journal d'audit. L'IA propose, l'archiviste valide.</p>",
        "detail_list": ["« Résume ce contrat. »", "« Trouve les obligations du fournisseur. »", "« Quels documents arrivent bientôt à échéance ? »", "« Construis la chronologie de ce dossier. »"],
        "detail_shot": ("archiva360-recherche-intelligente.png", "Recherche en langage naturel"),
        "faq": [
            ("Nos documents servent-ils à entraîner un modèle d'IA ?", "Non. Vos documents restent dans votre espace et ne sont pas utilisés pour entraîner des modèles partagés avec d'autres organisations."),
            ("L'IA fonctionne-t-elle sur une installation sur site ?", "Oui, selon les fonctions. Pour les administrations sensibles, les traitements peuvent être déployés dans votre propre infrastructure."),
        ],
    },
    {
        "slug": "securite", "title": "Sécurité et coffre-fort numérique", "short": "Sécurité", "icon": "shield",
        "desc": "Chiffrement, authentification multifacteur, droits fins, journalisation, sauvegarde 3-2-1 et plan de reprise : vos archives survivent à l'imprévu.",
        "hero": "Incendie, dégât des eaux, ransomware, suppression accidentelle, panne électrique : vos archives doivent survivre à tout. La sécurité est intégrée à ARCHIVA360 dès la conception.",
        "shot": ("archiva360-security-center.png", "Security Center d'ARCHIVA360"),
        "features": [
            ("Chiffrement", "Au repos et en transit, pour tous les espaces.", "lock"),
            ("MFA et SSO", "Authentification multifacteur, connexion unique avec l'annuaire de l'entreprise.", "key"),
            ("Droits fins (RBAC)", "Super admin, archiviste, records manager, direction, employé, auditeur, externe, public.", "users"),
            ("ARCHIVE VAULT", "Coffre-fort pour les contrats stratégiques, dossiers RH, décisions et propriété intellectuelle.", "shield"),
            ("Sauvegarde 3-2-1", "3 copies, 2 supports différents, 1 copie hors site. Tests de restauration réguliers.", "hard-drive"),
            ("Détection d'anomalies", "Échecs de connexion, téléchargements inhabituels, droits excessifs : alertes en temps réel.", "alert"),
        ],
        "detail_h": "Digital disaster recovery",
        "detail": "<p>En Afrique comme ailleurs, les archives disparaissent rarement par manque de logiciel : elles disparaissent dans un incendie, une inondation ou une attaque par rançongiciel. ARCHIVA360 applique la règle 3-2-1 et un plan de reprise d'activité testé.</p><p>Le Security Center donne une vue en temps réel : connexions, échecs, sessions, appareils, permissions, téléchargements et anomalies.</p>",
        "detail_list": ["Sauvegardes automatiques et réplication", "Copie hors site chiffrée", "Tests de restauration planifiés", "Tests d'intrusion et séparation des environnements", "Politique de mots de passe et gestion des sessions"],
        "detail_shot": ("archiva360-compliance-center.png", "Compliance Center"),
        "faq": [
            ("Où sont hébergées nos données ?", "Selon votre choix : cloud ADA, cloud privé, installation sur site ou hybride. Pour les administrations, nous privilégions un hébergement souverain ou dans leur propre infrastructure."),
            ("Êtes-vous certifiés ISO 27001 ?", "ISO 27001 est notre référentiel de conception. Nous ne revendiquons pas de certification tant qu'elle n'a pas été obtenue auprès d'un organisme accrédité."),
        ],
    },
    {
        "slug": "preservation-numerique", "title": "Préservation numérique", "short": "Préservation numérique", "icon": "layers",
        "desc": "Maintenir l'accès à vos documents sur des décennies malgré l'évolution des logiciels, des formats et des supports, selon le modèle OAIS.",
        "hero": "Un fichier créé aujourd'hui peut devenir illisible dans 20 ans. La préservation numérique garantit qu'il restera lisible, intègre et compréhensible, quel que soit l'avenir des logiciels.",
        "shot": ("archiva360-compliance-center.png", "Contrôles d'intégrité"),
        "features": [
            ("Identification des formats", "Chaque fichier est identifié précisément à l'entrée dans l'archive.", "search"),
            ("Validation", "Vérification que le fichier respecte bien la norme de son format.", "check-circle"),
            ("Formats pérennes", "Conversion vers des formats de conservation comme le PDF/A (ISO 19005).", "file"),
            ("Migration", "Migration planifiée vers de nouveaux formats et supports (ISO 13008).", "refresh"),
            ("Contrôle d'intégrité", "Vérification périodique des empreintes de tous les fichiers.", "fingerprint"),
            ("Métadonnées de préservation", "Historique de chaque transformation, pour garder la preuve de l'authenticité.", "database"),
        ],
        "detail_h": "Le modèle OAIS, appliqué",
        "detail": "<p>Le modèle OAIS (ISO 14721:2025) est la référence internationale de la préservation à long terme. Il décrit l'entrée des documents dans l'archive, leur stockage, la gestion de leurs données, l'accès et la diffusion, ainsi que leur migration vers de nouveaux supports et formats.</p><p>ARCHIVA360 organise la préservation selon ces fonctions. Pour les fonds historiques et patrimoniaux, c'est ce qui distingue une archive d'un simple stockage.</p>",
        "detail_list": ["Entrée : paquets de versement contrôlés", "Stockage archivistique redondant", "Gestion des données descriptives", "Accès et diffusion, y compris portail public", "Planification de la préservation"],
        "detail_shot": ("archiva360-audit-trail.png", "Traçabilité des opérations"),
        "faq": [
            ("La préservation concerne-t-elle toutes les organisations ?", "Surtout celles qui conservent des documents plus de 10 ans : administrations, universités, banques, patrimoine. Pour les autres, un bon format de conservation et un contrôle d'intégrité suffisent souvent."),
        ],
    },
    {
        "slug": "workflow-courrier", "title": "Workflow, courrier et signature", "short": "Workflow et courrier", "icon": "workflow",
        "desc": "Des circuits de validation construits par glisser-déposer, la gestion du courrier entrant et sortant, et la signature électronique intégrée.",
        "hero": "Un contrat déposé par un employé passe par le juridique, la direction, la signature, puis rejoint automatiquement l'archive. Sans e-mail perdu, sans parapheur égaré.",
        "shot": ("archiva360-workflow.png", "Constructeur de workflow ARCHIVA360"),
        "features": [
            ("Constructeur visuel", "Dépôt → Contrôle → Validation → Signature → Archivage, par glisser-déposer.", "workflow"),
            ("Conditions et délais", "Étapes selon le montant ou le type, relances automatiques, délégations.", "clock"),
            ("Courrier", "Courrier entrant, sortant et interne : enregistrement, affectation, traitement, réponse, archivage.", "inbox"),
            ("Signature électronique", "Créer → Valider → Signer → Horodater → Archiver, avec un prestataire de confiance.", "pen"),
            ("Notifications", "Sur le web et sur ARCHIVA GO : validez un document depuis votre téléphone.", "smartphone"),
            ("Traçabilité", "Chaque décision, refus ou commentaire est inscrit dans l'audit trail.", "eye"),
        ],
        "detail_h": "Du dépôt à l'archive, automatiquement",
        "detail": "<p>Un employé dépose un contrat. Le responsable juridique le contrôle, la direction valide, le signataire signe électroniquement, le document est horodaté puis archivé avec sa règle de conservation. Chaque étape est tracée.</p><p>La Côte d'Ivoire dispose d'un cadre réglementaire pour l'écrit et la signature électroniques (décret n°2014-106). ARCHIVA360 s'intègre à des prestataires de signature de confiance plutôt que de réinventer la signature.</p>",
        "detail_list": ["Modèles de circuits prêts à l'emploi : contrats, factures, notes de service", "Registre du courrier avec numérotation chronologique", "Tableau de bord des délais de traitement", "Archivage automatique en fin de circuit"],
        "detail_shot": ("archiva-go-mobile.png", "Validation mobile avec ARCHIVA GO"),
        "faq": [
            ("Peut-on garder notre outil de signature actuel ?", "Si votre prestataire propose une API, nous pouvons l'intégrer. Sinon, nous vous proposons des prestataires reconnus."),
        ],
    },
]


def _cycle():
    return ('<h3 class="mt-l">Le cycle de vie d\'un document</h3><div class="retention-demo">'
            '<div>Créé</div><div>Actif</div><div>Semi-actif</div><div>Archivé</div><div>Conservation longue</div><div>Sort final</div></div>'
            '<p class="has-small-font-size has-muted-color">Durées possibles : 5, 10, 20, 30 ans ou permanent, selon les règles de l\'organisation et le cadre juridique applicable.</p>')


def _chain():
    stages = ["Archives physiques", "Préparation", "Classement", "Numérisation", "OCR", "Contrôle qualité", "Indexation", "Importation", "Archivage électronique"]
    return '<ol class="chain mt-l">' + "".join(f"<li><b>{s}</b></li>" for s in stages) + "</ol>"


def build():
    add(Page(
        "solutions", "Solutions",
        description="GED, archivage électronique, records management, numérisation, archives physiques, IA documentaire, sécurité et préservation numérique : les solutions ADA.",
        hero=page_hero("Une chaîne complète pour vos documents, du carton à la préservation",
                       "Archives papier, numérisation, organisation, GED, archivage électronique, conservation, recherche, preuve et préservation longue durée : ADA couvre chaque étape, avec une seule plateforme et un seul interlocuteur.",
                       [("Solutions", None)], "Solutions",
                       buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"), btn("Voir ARCHIVA360", "~/archiva360/", "outline")),
                       media=img("archiva360-tableau-de-bord.png", "Tableau de bord ARCHIVA360", frame=True, lazy=False)),
        body=section(intro("Ne pas confondre GED et archivage", "C'est essentiel. La GED sert à travailler sur les documents ; l'archivage électronique à les conserver avec valeur de preuve ; le records management à gérer leur cycle de vie ; la préservation numérique à les garder lisibles dans la durée. Une vraie plateforme combine les quatre.", "Nos solutions")
                     + cols(*[card(s["short"], s["desc"], s["icon"], f"~/solutions/{s['slug']}/") for s in SOLUTIONS], n=3))
        + section(intro("Pourquoi une seule chaîne ?", "Parce que la plupart des projets échouent aux coutures : entre le prestataire qui scanne, le logiciel qui stocke et l'hébergeur qui sauvegarde. ADA prend la responsabilité de toute la chaîne.", center=True)
                  + '<ol class="chain">' + "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in [
                      ("Archives papier", "Inventaire et préparation"), ("Numérisation", "Scan et contrôle qualité"), ("Organisation", "Plan de classement"),
                      ("GED", "Travail au quotidien"), ("Archivage électronique", "Règles et traçabilité"), ("Conservation", "Cycle de vie maîtrisé"),
                      ("Recherche", "Plein texte et métadonnées"), ("Preuve", "Empreinte et horodatage"), ("Préservation", "Lisible dans 30 ans")]) + "</ol>", "mist")
        + section(cta_band("Vous ne savez pas par où commencer ?", "Évaluez la maturité documentaire de votre organisation en 20 questions, puis parlons-en.",
                           btn("Faire le Document Health Check", "~/ressources/document-health-check/", "white"))),
        crumbs=None, nav="solutions"))

    for i, s in enumerate(SOLUTIONS):
        feats = cols(*[feature(t, d, ic) for t, d, ic in s["features"]], n=3, cls="gap-lg")
        extra = _cycle() if s.get("extra") == "cycle" else ""
        chain = _chain() if s.get("chain") else ""
        related = [x for x in SOLUTIONS if x["slug"] != s["slug"]]
        related = [related[(i + k) % len(related)] for k in range(3)]
        body = (
            section(intro(f"Ce que couvre la solution {s['short']}", s["desc"], "Fonctionnalités") + feats)
            + section(media_text(img(s["detail_shot"][0], s["detail_shot"][1], *( (420, 860) if "mobile" in s["detail_shot"][0] else (1600, 1000) ), frame="mobile" not in s["detail_shot"][0], cls="is-mobile" if "mobile" in s["detail_shot"][0] else ""),
                                 f'<span class="eyebrow">Dans ARCHIVA360</span><h2>{s["detail_h"]}</h2>{s["detail"]}{ul(s["detail_list"])}'
                                 + buttons(btn("Demander une démonstration", "~/archiva360/demo/"), btn("Voir les modules", "~/archiva360/modules/", "outline"))) + extra + chain, "mist")
            + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                      + intro("Questions fréquentes", "Vous ne trouvez pas votre réponse ? Écrivez-nous, un spécialiste vous répond.", "FAQ")
                      + btn("Poser une question", "~/contact/?sujet=question", "outline")
                      + f'</div><div class="wp-block-column">{faq(s["faq"])}</div></div>')
            + section(intro("Solutions associées", "", "Aller plus loin") + cols(*[card(r["short"], r["desc"], r["icon"], f"~/solutions/{r['slug']}/") for r in related], n=3), "mist", "is-compact")
        )
        add(Page(
            f"solutions/{s['slug']}", s["title"], body,
            description=s["desc"],
            hero=page_hero(s["title"], s["hero"], [("Solutions", "solutions/"), (s["short"], None)], "Solution",
                           buttons(btn("Demander un audit", "~/contact/?sujet=audit", "white"), btn("Voir une démo", "~/archiva360/demo/", "outline")),
                           media=img(s["shot"][0], s["shot"][1], frame=True, lazy=False)),
            nav="solutions"))
