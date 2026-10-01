"""ARCHIVA Academy — Parcours dirigeant (12 semaines), semaines 7 à 12, examen et assemblage."""
from .academy_n1_n2 import Q, VF
from .academy_dirigeant import WEEKS_1_6, case, ask, key, deliverable, further

W7 = {
    "title": "Préserver à long terme : le modèle OAIS pour décideurs", "minutes": 60,
    "html": """
<p class="lead">Le papier se dégrade lentement et de manière visible. Le numérique, lui, peut devenir illisible d'un coup, et en silence : un format abandonné, un support défaillant, une clé de chiffrement perdue. Préserver l'information numérique sur trente ans ou plus est un engagement d'organisation, pas une fonctionnalité logicielle.</p>
<h3>1. Les trois menaces du numérique</h3>
<ul><li><b>Le support</b> : disques, bandes et serveurs ont une durée de vie limitée ; sans copies et sans contrôles réguliers, une panne efface l'information.</li>
<li><b>Le format</b> : un fichier n'est lisible qu'avec un logiciel capable de l'interpréter ; les formats propriétaires et non documentés vieillissent mal.</li>
<li><b>Le contexte</b> : un fichier sans métadonnées, sans lien avec son dossier ni avec l'activité qui l'a produit, devient incompréhensible même s'il reste techniquement lisible.</li></ul>
<h3>2. OAIS : un modèle de référence, pas un logiciel</h3>
<p>Le modèle OAIS (<em>Open Archival Information System</em>, norme ISO 14721) décrit ce qu'une organisation doit faire pour préserver une information et la rendre compréhensible à une <strong>communauté d'utilisateurs cible</strong>. Il distingue trois paquets d'information :</p>
<table><thead><tr><th>Paquet</th><th>Rôle</th></tr></thead><tbody>
<tr><td><b>SIP</b> — paquet de versement</td><td>Ce que le producteur transmet : documents et métadonnées</td></tr>
<tr><td><b>AIP</b> — paquet d'archives</td><td>Ce que l'archive conserve : documents, métadonnées de description, de contexte, de provenance et d'intégrité</td></tr>
<tr><td><b>DIP</b> — paquet de diffusion</td><td>Ce que l'utilisateur reçoit en réponse à sa demande</td></tr></tbody></table>
<p>Et six fonctions : entrées, stockage, gestion des données, administration, planification de la préservation, accès. Pour un dirigeant, la leçon est la suivante : <strong>la préservation est une fonction permanente, dotée de responsables, de procédures et d'une veille</strong>, et non un achat ponctuel.</p>
<h3>3. Les décisions qui vous reviennent</h3>
<ol><li><b>Les formats acceptés</b> : privilégier des formats ouverts et documentés (PDF/A pour les documents, TIFF ou PNG pour les images, CSV ou XML pour les données) ; refuser ou convertir les autres au versement.</li>
<li><b>Le nombre et la localisation des copies</b> : la règle de prudence est au moins trois copies, sur deux types de supports, dont une hors site.</li>
<li><b>Le contrôle d'intégrité</b> : vérification périodique des empreintes de chaque document, avec rapport.</li>
<li><b>La veille et la migration</b> : surveiller l'obsolescence et migrer les formats à risque avant qu'il ne soit trop tard, en conservant la trace de chaque transformation.</li>
<li><b>La réversibilité</b> : pouvoir récupérer l'intégralité des documents et de leurs métadonnées dans des formats standards, si vous changez de prestataire.</li></ol>
""" + case("les rapports illisibles", """
<p>Un institut de recherche découvre que vingt ans de rapports d'études ont été produits avec un logiciel de traitement de texte disparu. Les fichiers sont intacts, mais aucun outil courant ne les ouvre correctement ; la conversion coûte des mois de travail et une partie des mises en forme, tableaux et formules est perdue.</p>
<p><em>Analyse.</em> Une politique de formats appliquée au versement (conversion en PDF/A, conservation du fichier d'origine à titre de référence) aurait coûté quelques minutes par document.</p>""") + ask([
        "Quels formats acceptons-nous dans notre système d'archivage ? Lesquels convertissons-nous ?",
        "Combien de copies de nos archives existent, sur quels supports, et dans quels lieux ?",
        "Quand l'intégrité de nos archives a-t-elle été vérifiée pour la dernière fois ? Où est le rapport ?",
        "Si nous changions de prestataire demain, comment récupérerions-nous nos documents et leurs métadonnées ?",
    ]) + key([
        "Trois menaces : le support, le format, le contexte.",
        "OAIS (ISO 14721) : un modèle de référence ; SIP au versement, AIP en conservation, DIP en diffusion.",
        "La préservation est une fonction permanente : formats, copies, contrôles, veille, réversibilité.",
    ]) + deliverable("<p>Rédigez une politique de formats d'une page : formats acceptés, formats convertis au versement, formats refusés, et la règle de copies (combien, où, contrôlées à quelle fréquence).</p>") + further([
        "ISO 14721:2012 — Modèle de référence OAIS.",
        "ARCHIVA Academy, niveau 5 : « Préservation numérique ».",
        "Livre blanc ADA : « De la GED à la préservation ».",
    ]),
    "quiz": [
        Q("Quelles sont les trois menaces qui pèsent sur l'information numérique selon la leçon ?",
          ["Le support", "Le format", "Le contexte", "La couleur de l'écran"], [0, 1, 2],
          "Un support défaillant, un format obsolète ou une perte de contexte suffisent à rendre l'information inutilisable."),
        Q("Dans le modèle OAIS, quel paquet l'archive conserve-t-elle ?",
          ["Le SIP", "L'AIP", "Le DIP", "Le PDF"], 1,
          "L'AIP (Archival Information Package) est le paquet conservé : documents et métadonnées de préservation."),
        Q("Le modèle OAIS est un logiciel que l'on peut acheter et installer.", VF, 1,
          "C'est un modèle de référence (ISO 14721) qui décrit des fonctions et des responsabilités."),
        Q("Quelle règle de prudence la leçon recommande-t-elle pour les copies ?",
          ["Au moins trois copies, sur deux types de supports, dont une hors site", "Une copie unique sur le serveur principal", "Deux copies dans le même bureau", "Une copie imprimée de chaque fichier"], 0,
          "C'est la règle dite « 3-2-1 », reprise dans la semaine consacrée à la sécurité."),
    ],
}

W8 = {
    "title": "Sécurité, continuité et cyber-risque", "minutes": 60,
    "html": """
<p class="lead">Les archives concentrent ce qu'une organisation a de plus sensible : données personnelles, secrets d'affaires, preuves, patrimoine. Elles sont aussi la cible privilégiée des rançongiciels, qui chiffrent les données et menacent de les publier. La sécurité documentaire n'est pas un sujet informatique délégué : c'est un arbitrage de direction sur le niveau de risque acceptable.</p>
<h3>1. La triade, appliquée aux archives</h3>
<table><thead><tr><th>Critère</th><th>Question</th><th>Mesures typiques</th></tr></thead><tbody>
<tr><td><b>Confidentialité</b></td><td>Seules les personnes autorisées accèdent-elles aux documents ?</td><td>Niveaux de confidentialité, droits par rôle, chiffrement, double authentification</td></tr>
<tr><td><b>Intégrité</b></td><td>Peut-on prouver qu'un document n'a pas été modifié ?</td><td>Empreintes, journal d'audit chaîné, versions</td></tr>
<tr><td><b>Disponibilité</b></td><td>Les documents restent-ils accessibles en cas d'incident ?</td><td>Sauvegardes, plan de continuité, plan de reprise</td></tr></tbody></table>
<p>Pour les archives, on ajoute souvent la <strong>traçabilité</strong> : savoir qui a fait quoi, et quand. C'est la condition de l'imputabilité et de la preuve.</p>
<h3>2. Le principe du moindre privilège</h3>
<p>Chaque utilisateur ne doit accéder qu'aux documents dont il a besoin pour son travail. En pratique, les droits s'accumulent : un agent change de poste et conserve ses anciens accès, un prestataire garde un compte après la fin de sa mission. Une <strong>revue des accès</strong> semestrielle, signée par chaque responsable de direction, est l'une des mesures les plus efficaces et les moins coûteuses.</p>
<h3>3. Sauvegarder n'est pas archiver, mais il faut les deux</h3>
<p>La sauvegarde protège contre la perte ; l'archivage garantit la preuve et la durée. La règle <strong>3-2-1</strong> fait référence : trois copies des données, sur deux supports différents, dont une hors site. Face aux rançongiciels, on y ajoute une copie <strong>hors ligne ou immuable</strong>, que l'attaquant ne peut ni chiffrer ni effacer. Une sauvegarde qui n'a jamais été restaurée lors d'un test n'est qu'une hypothèse.</p>
<h3>4. Continuité et reprise : deux chiffres à décider</h3>
<ul><li><b>RTO</b> (durée maximale d'interruption admissible) : combien de temps l'organisation peut-elle fonctionner sans accès à ses documents ?</li>
<li><b>RPO</b> (perte de données maximale admissible) : combien d'heures ou de jours de documents l'organisation accepte-t-elle de perdre ?</li></ul>
<p>Ces deux chiffres sont des <strong>décisions de direction</strong> : plus ils sont faibles, plus la solution est coûteuse. Les fixer, c'est choisir son niveau de risque en connaissance de cause.</p>
<h3>5. Le cadre ivoirien</h3>
<p>En Côte d'Ivoire, le référentiel général de sécurité des systèmes d'information (RGSSI, décret n°2021-916) fixe des exigences de sécurité, et la loi n°2013-451 réprime la cybercriminalité. La protection des données personnelles impose par ailleurs des mesures de sécurité adaptées aux risques.</p>
""" + case("le vendredi soir", """
<p>Un vendredi soir, une clinique privée voit ses serveurs chiffrés par un rançongiciel. Les sauvegardes étaient réalisées chaque nuit… sur un disque connecté en permanence au réseau, chiffré lui aussi. Les dossiers patients des cinq dernières années sont inaccessibles. La clinique fonctionne sur papier pendant trois semaines.</p>
<p><em>Analyse.</em> Une copie hors ligne ou immuable, un test de restauration trimestriel et une décision explicite sur le RTO auraient transformé une crise majeure en incident maîtrisé.</p>""") + ask([
        "Avons-nous une copie de nos archives hors ligne ou immuable, à l'abri d'un rançongiciel ?",
        "Quand avons-nous restauré une sauvegarde pour la dernière fois, en conditions réelles ?",
        "Quels sont nos RTO et RPO pour les documents ? Qui les a décidés ?",
        "Quand les droits d'accès ont-ils été revus pour la dernière fois, et par qui ?",
    ]) + key([
        "Confidentialité, intégrité, disponibilité, et traçabilité pour les archives.",
        "Moindre privilège et revue semestrielle des accès.",
        "Règle 3-2-1, plus une copie hors ligne ou immuable ; une sauvegarde non testée n'est qu'une hypothèse.",
        "RTO et RPO sont des décisions de direction, à prendre en connaissance de coût.",
    ]) + deliverable("<p>Fixez, pour trois catégories de documents (opérationnels, financiers, patrimoniaux), un RTO et un RPO cibles. Demandez à votre DSI le coût d'atteinte de ces cibles et le niveau actuel réel. L'écart entre les deux est votre plan d'action sécurité.</p>") + further([
        "ISO/IEC 27001:2022 — Systèmes de management de la sécurité de l'information.",
        "Décret n°2021-916 portant référentiel général de sécurité des systèmes d'information (Côte d'Ivoire).",
        "ARCHIVA Academy, niveau 6, module 3 : « Sécurité, sauvegarde et reprise ».",
        "Blog ADA : « La règle 3-2-1 de sauvegarde des archives ».",
    ]),
    "quiz": [
        Q("Que désigne le RTO ?",
          ["La durée maximale d'interruption admissible", "La perte de données maximale admissible", "Un format de fichier", "Le registre des traitements"], 0,
          "Le RTO fixe combien de temps l'organisation peut fonctionner sans accès ; le RPO, combien de données elle accepte de perdre."),
        Q("Face aux rançongiciels, quelle mesure complète utilement la règle 3-2-1 ?",
          ["Une copie hors ligne ou immuable", "Un mot de passe plus long sur le serveur de sauvegarde uniquement", "La suppression des archives anciennes", "Un antivirus sur les imprimantes"], 0,
          "Une copie que l'attaquant ne peut ni chiffrer ni effacer garantit la possibilité de reprise."),
        Q("Une sauvegarde réalisée chaque nuit suffit, même si elle n'a jamais été restaurée.", VF, 1,
          "Seul un test de restauration prouve qu'une sauvegarde est exploitable."),
        Q("Le choix des RTO et RPO est une décision purement technique qui revient à la DSI.", VF, 1,
          "Ce sont des décisions de direction : elles expriment le niveau de risque accepté et déterminent le coût de la solution."),
    ],
}

W9 = {
    "title": "Le cadre juridique : Côte d'Ivoire, OHADA et sous-région", "minutes": 60,
    "html": """
<p class="lead">Le droit ne dit pas seulement ce qu'il faut conserver. Il dit aussi à quelles conditions un document électronique fait preuve, comment protéger les personnes dont les données figurent dans les archives, et quelles autorités contrôlent. Un dirigeant n'a pas à devenir juriste, mais il doit connaître la carte des textes et savoir quelles questions poser à ses conseils. <em>Ce module présente des repères ; il ne remplace pas un avis juridique.</em></p>
<h3>1. Trois niveaux de normes</h3>
<ol><li><b>Le niveau national</b>. En Côte d'Ivoire : la loi n°2013-546 relative aux transactions électroniques, qui reconnaît l'écrit et la signature électroniques ; la loi n°2013-450 relative à la protection des données à caractère personnel ; la loi n°2013-451 relative à la lutte contre la cybercriminalité ; le décret n°2014-106 sur l'écrit et la signature électroniques ; le décret n°2016-851 sur l'archivage électronique ; le décret n°2021-916 portant RGSSI.</li>
<li><b>Le niveau régional et communautaire</b>. Le droit OHADA, notamment l'Acte uniforme relatif au droit comptable et à l'information financière pour la conservation des documents comptables ; les textes de la CEDEAO et de l'UEMOA sur les transactions électroniques et la protection des données ; la Convention de l'Union africaine sur la cybersécurité et la protection des données à caractère personnel (Convention de Malabo, 2014).</li>
<li><b>Le niveau sectoriel</b>. Banques et établissements financiers (réglementation bancaire de l'UMOA, instructions de la BCEAO), assurances (Code CIMA), santé, éducation, marchés publics : chaque secteur ajoute ses obligations de conservation et de communication.</li></ol>
<h3>2. Quand un document électronique fait-il preuve ?</h3>
<p>La loi ivoirienne sur les transactions électroniques, comme la plupart des législations inspirées de la loi type de la CNUDCI sur le commerce électronique, retient une logique d'<strong>équivalence fonctionnelle</strong> : l'écrit électronique a la même force probante que l'écrit papier, à condition que l'on puisse <strong>identifier la personne dont il émane</strong> et qu'il soit <strong>établi et conservé dans des conditions de nature à en garantir l'intégrité</strong>. C'est précisément ce qu'apportent un SAE, ses empreintes et son journal d'audit : la technique au service d'une condition juridique.</p>
<h3>3. Archives et données personnelles</h3>
<p>Les archives sont pleines de données personnelles : dossiers des agents, des clients, des patients, des élèves. La loi n°2013-450 impose notamment une <strong>finalité déterminée</strong>, une <strong>durée de conservation limitée</strong> à ce qui est nécessaire, des <strong>mesures de sécurité</strong> et le respect des <strong>droits des personnes</strong>. L'ARTCI est l'autorité de protection ; certains traitements doivent lui être déclarés ou autorisés. L'archivage à des fins historiques peut justifier une conservation prolongée, dans les conditions prévues par les textes.</p>
<h3>4. Les points de vigilance du dirigeant</h3>
<ul><li><b>La substitution</b> : avant d'éliminer des originaux papier numérisés, obtenir un avis juridique écrit, type de document par type de document.</li>
<li><b>L'hébergement</b> : vérifier les conditions applicables au transfert de données personnelles hors du territoire et aux données sensibles (santé notamment).</li>
<li><b>Les archives publiques</b> : elles obéissent à un régime propre (inaliénabilité, visa des éliminations par l'administration des archives, délais de communicabilité).</li>
<li><b>Le contrat avec le prestataire</b> : localisation des données, sécurité, réversibilité, sort des données en fin de contrat, accès des autorités.</li></ul>
""" + case("la substitution trop rapide", """
<p>Une entreprise numérise ses contrats commerciaux et détruit les originaux pour libérer des bureaux. Lors d'un litige, la partie adverse conteste l'intégrité des copies : elles ont été produites sans procédure documentée, sans empreinte, sans journal. Le juge apprécie souverainement leur valeur probante, avec une incertitude que l'entreprise aurait pu éviter.</p>
<p><em>Analyse.</em> La numérisation était une bonne décision ; la destruction des originaux sans procédure de copie fiable et sans validation juridique ne l'était pas.</p>""") + ask([
        "Disposons-nous d'une cartographie écrite des textes qui s'appliquent à nos archives, y compris sectoriels ?",
        "Nos traitements de données personnelles liés aux archives sont-ils documentés et, si nécessaire, déclarés à l'ARTCI ?",
        "Où sont hébergées nos données, et notre contrat d'hébergement couvre-t-il réversibilité et sécurité ?",
        "Avons-nous un avis juridique écrit avant toute élimination d'originaux numérisés ?",
    ]) + key([
        "Trois niveaux : national, régional et communautaire (OHADA, CEDEAO, UEMOA, Union africaine), sectoriel.",
        "L'écrit électronique fait preuve s'il identifie son auteur et si son intégrité est garantie.",
        "Données personnelles : finalité, durée limitée, sécurité, droits des personnes ; l'ARTCI contrôle.",
        "Substitution, hébergement, archives publiques, contrats : quatre points de vigilance.",
    ]) + deliverable("<p>Avec votre juriste, établissez la carte des textes applicables à votre organisation : un tableau à trois colonnes (texte, obligation pour nos archives, responsable interne). Identifiez les trois obligations aujourd'hui les moins bien respectées.</p>") + further([
        "Loi n°2013-546 relative aux transactions électroniques ; loi n°2013-450 relative à la protection des données à caractère personnel (Côte d'Ivoire).",
        "Convention de l'Union africaine sur la cybersécurité et la protection des données à caractère personnel (Malabo, 2014).",
        "Loi type de la CNUDCI sur le commerce électronique (1996).",
        "ARCHIVA Academy, niveau 4, module 4 : « Le cadre ivoirien et la protection des données ».",
        "Livre blanc ADA : « Archiver en Côte d'Ivoire ».",
    ]),
    "quiz": [
        Q("À quelles conditions l'écrit électronique a-t-il la même force probante que l'écrit papier ?",
          ["On peut identifier la personne dont il émane", "Il est établi et conservé dans des conditions garantissant son intégrité", "Il est imprimé en couleur", "Il a moins de cinq ans"], [0, 1],
          "Identification de l'auteur et garantie d'intégrité : c'est la logique d'équivalence fonctionnelle."),
        Q("Quelle loi ivoirienne porte sur la protection des données à caractère personnel ?",
          ["Loi n°2013-450", "Loi n°2013-546", "Loi n°2013-451", "Décret n°2016-851"], 0,
          "La loi n°2013-450 porte sur les données personnelles ; la 2013-546 sur les transactions électroniques ; la 2013-451 sur la cybercriminalité."),
        Q("Une fois des contrats numérisés, on peut toujours détruire les originaux papier sans autre formalité.", VF, 1,
          "La substitution suppose une procédure de copie fiable et une validation juridique, type de document par type de document."),
        Q("Quel texte de l'Union africaine traite de la cybersécurité et de la protection des données personnelles ?",
          ["La Convention de Malabo", "Le Code CIMA", "L'AUDCIF", "La loi type de la CNUDCI"], 0,
          "La Convention de l'Union africaine adoptée à Malabo en 2014."),
    ],
}

W10 = {
    "title": "Le modèle économique : coût complet et dossier d'investissement", "minutes": 60,
    "html": """
<p class="lead">Un projet documentaire se décide comme tout investissement : sur un coût complet, des bénéfices mesurables et des risques évités. Cette semaine, vous apprenez à construire le dossier que vous présenterez à votre conseil, ou à challenger celui que l'on vous présente.</p>
<h3>1. Le coût de la situation actuelle, d'abord</h3>
<p>Le point de comparaison n'est pas zéro. Ne rien faire coûte, mais ce coût est dispersé et invisible. Rendez-le visible avec cinq postes :</p>
<ol><li><b>Le temps de recherche</b> : mesurez-le sur un échantillon d'agents pendant deux semaines (nombre de recherches, durée, échecs). Multipliez par le coût horaire chargé.</li>
<li><b>L'espace</b> : mètres linéaires occupés, loyers, mobilier, stockage externe.</li>
<li><b>Les impressions, copies et envois</b>.</li>
<li><b>Les incidents</b> : pénalités, redressements, contentieux perdus faute de preuve, doublons de paiement, sur les trois dernières années.</li>
<li><b>Le risque</b> : probabilité et impact d'un sinistre (incendie, inondation, rançongiciel) sur des archives uniques.</li></ol>
<h3>2. Le coût complet du projet</h3>
<table><thead><tr><th>Poste</th><th>Nature</th><th>Souvent oublié ?</th></tr></thead><tbody>
<tr><td>Abonnement ou licences, hébergement</td><td>Récurrent</td><td>Non</td></tr>
<tr><td>Paramétrage, intégration aux logiciels existants</td><td>Ponctuel</td><td>Parfois</td></tr>
<tr><td>Plan de classement, référentiel, procédures</td><td>Ponctuel puis maintenance</td><td><b>Oui</b></td></tr>
<tr><td>Reprise de l'existant et numérisation</td><td>Ponctuel, souvent le premier poste</td><td><b>Oui</b></td></tr>
<tr><td>Formation et accompagnement du changement</td><td>Ponctuel puis continu</td><td><b>Oui</b></td></tr>
<tr><td>Temps interne : chef de projet, records manager, référents</td><td>Continu</td><td><b>Oui</b></td></tr>
<tr><td>Réversibilité et sortie</td><td>Éventuel</td><td><b>Oui</b></td></tr></tbody></table>
<p>Raisonnez sur <strong>cinq ans</strong> : c'est l'horizon pertinent pour comparer un abonnement (dépense de fonctionnement) et une acquisition avec infrastructure propre (dépense d'investissement puis de maintenance).</p>
<h3>3. Les bénéfices : trois catégories, trois niveaux de preuve</h3>
<ul><li><b>Bénéfices monétaires directs</b> : espace libéré, stockage externe résilié, impressions réduites. Faciles à chiffrer, ils suffisent rarement à justifier le projet.</li>
<li><b>Gains de productivité</b> : temps de recherche réduit, délais de traitement raccourcis. Réels, mais ils ne deviennent des économies que si le temps libéré est réaffecté. Soyez honnête sur ce point devant votre conseil.</li>
<li><b>Risques évités</b> : contentieux, sanctions, perte de données. On les estime en valeur espérée (probabilité × impact). Ce sont souvent eux qui justifient la décision.</li></ul>
<h3>4. Le dossier d'investissement en une page</h3>
<p>Problème (chiffré) ; solution retenue et alternatives écartées ; coût complet sur cinq ans ; bénéfices par catégorie ; risques du projet et parades ; indicateurs de succès ; calendrier ; demande précise au conseil. Une page, des annexes ensuite : un dirigeant doit pouvoir décider en dix minutes.</p>
""" + case("le chiffre qui a convaincu", """
<p>Le directeur général d'une société de distribution présente un projet de GED à son conseil. Les gains de productivité laissent les administrateurs sceptiques. Ce qui emporte la décision est une ligne de l'annexe : sur trois ans, l'entreprise a payé deux fois les mêmes factures fournisseurs pour un montant supérieur au coût annuel de la solution, faute de pouvoir rapprocher les pièces rapidement.</p>
<p><em>Analyse.</em> Les bénéfices les plus convaincants sont ceux que l'organisation a déjà perdus, documentés par ses propres chiffres.</p>""") + ask([
        "Combien de temps nos agents passent-ils réellement à chercher des documents ? L'avons-nous mesuré ?",
        "Quels incidents documentaires nous ont coûté de l'argent ces trois dernières années ?",
        "Le coût sur cinq ans inclut-il la reprise de l'existant, la formation et notre temps interne ?",
        "Quels gains de productivité seront réellement convertis en économies, et comment ?",
    ]) + key([
        "On compare le projet au coût de la situation actuelle, pas à zéro.",
        "Coût complet sur cinq ans : reprise, formation, temps interne et réversibilité compris.",
        "Trois catégories de bénéfices : monétaires directs, productivité, risques évités.",
        "Un dossier d'investissement tient en une page.",
    ]) + deliverable("<p>Construisez le dossier d'investissement d'une page de votre projet documentaire, en utilisant vos propres données. Faites-le relire par votre directeur financier et intégrez ses objections.</p>") + further([
        "ARCHIVA360 : « Offres et tarifs », pour un ordre de grandeur des abonnements.",
        "Ressources ADA : « Document Health Check », pour un premier diagnostic chiffré.",
    ]),
    "quiz": [
        Q("Quel est le bon point de comparaison pour évaluer un projet documentaire ?",
          ["Le coût de la situation actuelle", "Zéro", "Le budget de l'année précédente", "Le prix du concurrent le moins cher"], 0,
          "Ne rien faire coûte : temps de recherche, espace, incidents, risques."),
        Q("Quels postes sont souvent oubliés dans le coût complet ?",
          ["La reprise de l'existant", "La formation et l'accompagnement", "Le temps interne", "L'abonnement"], [0, 1, 2],
          "L'abonnement est rarement oublié ; la reprise, la formation et le temps interne le sont souvent."),
        Q("Les gains de productivité se transforment automatiquement en économies budgétaires.", VF, 1,
          "Ils ne deviennent des économies que si le temps libéré est réaffecté ; il faut le dire honnêtement."),
        Q("Comment estime-t-on la valeur d'un risque évité ?",
          ["Probabilité × impact", "Nombre de pages × prix du papier", "Nombre d'utilisateurs × prix de l'abonnement", "On ne peut pas l'estimer"], 0,
          "La valeur espérée d'un risque se calcule en multipliant sa probabilité par son impact."),
    ],
}

W11 = {
    "title": "Architecture et choix de solution : souveraineté et réversibilité", "minutes": 60,
    "html": """
<p class="lead">Choisir une solution documentaire engage l'organisation pour une décennie et ses archives pour bien plus longtemps. La décision ne se joue pas sur l'ergonomie d'une démonstration, mais sur quatre questions structurantes : où sont les données, qui les contrôle, comment l'outil s'intègre au reste du système d'information, et comment on en sort.</p>
<h3>1. Les modèles d'hébergement</h3>
<table><thead><tr><th>Modèle</th><th>Avantages</th><th>Points d'attention</th></tr></thead><tbody>
<tr><td><b>Cloud public mutualisé (SaaS)</b></td><td>Mise en service rapide, coûts prévisibles, mises à jour incluses</td><td>Localisation des données, dépendance à l'éditeur, conditions de réversibilité</td></tr>
<tr><td><b>Cloud privé ou dédié</b></td><td>Isolement, maîtrise de la localisation, personnalisation</td><td>Coût plus élevé, compétences du prestataire</td></tr>
<tr><td><b>Sur site</b></td><td>Contrôle total, exigences de souveraineté</td><td>Investissement, compétences internes, sécurité physique, énergie, sauvegardes hors site à organiser</td></tr>
<tr><td><b>Hybride</b></td><td>Données sensibles sur site, reste dans le cloud</td><td>Complexité d'architecture et de gouvernance</td></tr></tbody></table>
<p>Il n'y a pas de bonne réponse universelle. Une administration régalienne, une banque et une PME n'ont ni les mêmes contraintes réglementaires ni les mêmes moyens. La question à poser est : <strong>quel modèle répond à nos obligations et à notre appétence au risque, au meilleur coût complet ?</strong></p>
<h3>2. La souveraineté, concrètement</h3>
<p>Le mot est souvent employé de manière vague. Décomposez-le en questions vérifiables : dans quel pays les données sont-elles physiquement stockées ? Quel droit s'applique au prestataire, et des autorités étrangères peuvent-elles exiger l'accès aux données ? Qui détient les clés de chiffrement ? Les compétences d'exploitation existent-elles localement ? Le contrat est-il soumis au droit et aux juridictions de votre pays ?</p>
<h3>3. L'intégration au système d'information</h3>
<p>Un système documentaire isolé devient une île que les agents contournent. Il doit s'intégrer aux applications qui produisent les documents (comptabilité, paie, gestion commerciale, logiciels métiers), à l'annuaire de l'organisation pour les comptes et les droits, et, le cas échéant, à la signature électronique. Exigez des <strong>interfaces de programmation (API) documentées</strong> et des références d'intégration comparables à votre contexte.</p>
<h3>4. La réversibilité, clause la plus importante du contrat</h3>
<p>Vos archives vous survivront, ainsi qu'à votre prestataire. Le contrat doit garantir la restitution, à tout moment et à coût connu, de <strong>l'intégralité des documents, de leurs métadonnées, de leurs empreintes et des journaux d'audit</strong>, dans des formats ouverts et documentés. Demandez une démonstration de l'export complet avant de signer, et testez-le une fois par an.</p>
<h3>5. La grille de choix</h3>
<p>Pondérez vos critères <strong>avant</strong> de voir les démonstrations, pour ne pas être influencé : conformité fonctionnelle (records management, SAE), sécurité, hébergement et souveraineté, intégration, réversibilité, ergonomie, capacité d'accompagnement local, coût complet sur cinq ans, solidité du prestataire. Faites tester les deux finalistes par de vrais utilisateurs, sur vos propres documents.</p>
""" + case("la sortie impossible", """
<p>Une collectivité veut changer de solution après huit ans. Le contrat prévoit un export, mais seulement des fichiers, sans métadonnées ni journaux, et facturé au volume. Les huit années de classement, de règles de conservation et de traçabilité sont perdues ; la collectivité doit reprendre une partie de l'indexation à la main.</p>
<p><em>Analyse.</em> La clause de réversibilité se négocie avant la signature, quand l'organisation a encore du pouvoir de négociation, et se teste pendant toute la durée du contrat.</p>""") + ask([
        "Dans quel pays nos données seront-elles stockées, sous quel droit, et qui détient les clés de chiffrement ?",
        "La solution s'intègre-t-elle à nos logiciels de comptabilité, de paie et à notre annuaire ? Par quelles API ?",
        "Que contient exactement l'export de réversibilité ? L'avons-nous vu fonctionner ?",
        "Notre grille de choix a-t-elle été pondérée avant les démonstrations ?",
    ]) + key([
        "SaaS, cloud privé, sur site, hybride : choisir selon ses obligations et son appétence au risque.",
        "La souveraineté se décompose en questions vérifiables : localisation, droit applicable, clés, compétences.",
        "Un outil non intégré au système d'information sera contourné.",
        "La réversibilité porte sur les documents, les métadonnées, les empreintes et les journaux ; elle se teste.",
    ]) + deliverable("<p>Construisez votre grille de choix : huit à dix critères pondérés (total de 100), avec pour chacun la preuve attendue du prestataire (démonstration, document, référence). Gardez-la confidentielle jusqu'à l'ouverture des offres.</p>") + further([
        "ARCHIVA Academy, niveau 6, module 1 : « Organisation, utilisateurs et rôles ».",
        "ARCHIVA360 : page « Hébergement » des services ADA.",
    ]),
    "quiz": [
        Q("Quels éléments la réversibilité doit-elle couvrir ?",
          ["Les documents", "Les métadonnées", "Les empreintes et journaux d'audit", "Uniquement les fichiers récents"], [0, 1, 2],
          "Sans métadonnées, empreintes et journaux, on récupère des fichiers mais on perd le classement, les règles et la preuve."),
        Q("Pourquoi pondérer les critères de choix avant les démonstrations ?",
          ["Pour ne pas être influencé par la qualité de la présentation", "Parce que la loi l'interdit après", "Pour réduire le nombre de critères", "Pour favoriser le moins cher"], 0,
          "Une grille fixée à l'avance protège contre l'effet de séduction d'une démonstration."),
        Q("La souveraineté des données se résume au pays où se trouve le siège du prestataire.", VF, 1,
          "Elle se décompose en plusieurs questions : localisation physique, droit applicable, détention des clés, compétences locales, juridiction du contrat."),
        Q("Le modèle d'hébergement sur site est toujours le meilleur choix pour une organisation africaine.", VF, 1,
          "Il n'y a pas de réponse universelle : le choix dépend des obligations, des moyens et de l'appétence au risque."),
    ],
}

W12 = {
    "title": "Conduire le changement et piloter le programme", "minutes": 60,
    "html": """
<p class="lead">La plupart des projets documentaires n'échouent pas pour des raisons techniques, mais parce que les comportements n'ont pas changé : documents gardés sur les postes, échanges par messagerie personnelle, outil contourné. Cette dernière semaine assemble tout le parcours en un programme piloté, et vous donne les leviers pour le faire adopter.</p>
<h3>1. Le programme en trois horizons</h3>
<table><thead><tr><th>Horizon</th><th>Objectif</th><th>Réalisations typiques</th></tr></thead><tbody>
<tr><td><b>0 à 6 mois</b> — fondations</td><td>Gouverner et prouver la valeur</td><td>Politique signée, records manager nommé, plan de classement, référentiel validé pour deux processus pilotes, arrêt du flux papier entrant sur ces processus</td></tr>
<tr><td><b>6 à 18 mois</b> — déploiement</td><td>Étendre et industrialiser</td><td>Généralisation par vagues de directions, versement au SAE, reprise prioritaire de l'existant, premières éliminations réglementaires</td></tr>
<tr><td><b>18 mois et plus</b> — maturité</td><td>Optimiser et pérenniser</td><td>Intégrations, automatisation, audits annuels, préservation à long terme, éventuelle certification ISO 30301</td></tr></tbody></table>
<h3>2. Les leviers de l'adoption</h3>
<ul><li><b>L'exemplarité</b> : si le comité de direction continue à échanger ses documents par messagerie, personne ne changera. Les décisions du comité doivent elles-mêmes passer par l'outil.</li>
<li><b>Le bénéfice immédiat pour l'utilisateur</b> : commencer par ce qui simplifie la vie (retrouver un document en dix secondes, valider un circuit depuis son téléphone) plutôt que par les contraintes.</li>
<li><b>Les référents</b> : un correspondant formé dans chaque direction, relais de proximité du records manager.</li>
<li><b>La formation par rôle</b> : un dirigeant, un archiviste et un agent n'ont pas besoin des mêmes compétences ; ARCHIVA Academy propose un parcours pour chacun.</li>
<li><b>La fermeture des alternatives</b> : à une date annoncée, le serveur partagé passe en lecture seule. Sans cette étape, les anciennes habitudes perdurent.</li></ul>
<h3>3. Le tableau de bord du comité de direction</h3>
<p>Six indicateurs suffisent, suivis chaque trimestre :</p>
<ol><li>taux de documents engageants capturés dans le système, pour les processus déployés ;</li>
<li>délai moyen pour produire un dossier complet en cas de demande ou de contrôle ;</li>
<li>volume éliminé réglementairement, avec certificats, et mètres linéaires libérés ;</li>
<li>résultat du dernier contrôle d'intégrité et du dernier test de restauration ;</li>
<li>taux de revue des accès réalisée dans les délais ;</li>
<li>nombre d'agents formés et certifiés par rôle.</li></ol>
<h3>4. Porter le projet : convaincre et acheter</h3>
<p>Le dirigeant est le premier « vendeur » du programme : auprès du conseil, avec le dossier d'investissement (semaine 10) ; auprès des directions, en reliant le projet à leurs propres irritants ; auprès des agents, en expliquant ce qui change pour eux et pourquoi. Côté achats, structurez la consultation autour de vos exigences (semaines 2, 7, 8 et 11), de votre grille pondérée et d'un pilote payant sur un périmètre réel avant tout engagement global.</p>
""" + case("deux lancements", """
<p>Deux directions d'un même groupe lancent la même solution. La première organise une formation générale d'une journée et laisse l'ancien serveur ouvert. La seconde nomme un référent par service, forme chaque profil en deux heures sur ses propres documents, publie les indicateurs chaque mois et passe le serveur en lecture seule après huit semaines. Six mois plus tard, la première utilise l'outil pour 20 % de ses documents ; la seconde pour plus de 90 %.</p>
<p><em>Analyse.</em> L'outil était identique ; la conduite du changement a fait toute la différence.</p>""") + ask([
        "Quels sont nos deux processus pilotes, et pourquoi ceux-là ?",
        "Le comité de direction utilise-t-il lui-même l'outil pour ses propres documents ?",
        "Quelle est la date de passage en lecture seule de nos anciens espaces de stockage ?",
        "Quels six indicateurs suivrons-nous chaque trimestre, et qui les produit ?",
    ]) + key([
        "Trois horizons : fondations, déploiement, maturité.",
        "Exemplarité, bénéfice immédiat, référents, formation par rôle, fermeture des alternatives.",
        "Six indicateurs trimestriels pour piloter le programme en comité de direction.",
        "Le dirigeant porte le projet : conseil, directions, agents, achats.",
    ]) + deliverable("<p><strong>Livrable final du parcours.</strong> Assemblez vos livrables des onze semaines précédentes en une <em>feuille de route documentaire</em> de cinq à huit pages : diagnostic des risques, politique, gouvernance, plan de classement et référentiel (extraits), priorités de numérisation, politique de formats et de sécurité, cadre juridique applicable, dossier d'investissement, critères de choix, programme sur trois horizons et tableau de bord. Présentez-la à votre comité de direction.</p>") + further([
        "ISO 30301:2019, chapitres sur l'évaluation des performances et l'amélioration.",
        "ARCHIVA Academy, niveau 6, module 4 : « Exploiter et piloter la plateforme ».",
        "Services ADA : audit documentaire et conseil, pour un accompagnement de votre feuille de route.",
    ]),
    "quiz": [
        Q("Quel levier la leçon place-t-elle en premier pour l'adoption ?",
          ["L'exemplarité du comité de direction", "L'achat d'un scanner plus rapide", "La réduction du nombre d'utilisateurs", "L'interdiction de l'impression"], 0,
          "Si la direction n'utilise pas l'outil pour ses propres documents, personne ne le fera."),
        Q("Pourquoi passer l'ancien serveur partagé en lecture seule à une date annoncée ?",
          ["Pour fermer l'alternative et ancrer les nouvelles habitudes", "Pour économiser de l'électricité", "Parce que la loi l'impose", "Pour supprimer les documents anciens"], 0,
          "Tant que l'ancienne solution reste ouverte, les anciennes habitudes perdurent."),
        Q("Que contient l'horizon « fondations » (0 à 6 mois) ?",
          ["Politique signée et records manager nommé", "Plan de classement et référentiel pour des processus pilotes", "Certification ISO 30301 obtenue", "Arrêt du flux papier entrant sur les processus pilotes"], [0, 1, 3],
          "La certification relève de l'horizon de maturité."),
        Q("Un pilote payant sur un périmètre réel avant tout engagement global est déconseillé.", VF, 1,
          "Au contraire, il permet de vérifier la solution et le prestataire sur vos propres documents avant de vous engager."),
    ],
}

EXAM_EXTRA = [
    Q("Cas : votre DSI propose de « tout garder indéfiniment, puisque le stockage ne coûte presque rien ». Quelle est la meilleure réponse ?",
      ["Refuser : conserver sans justification crée des risques juridiques et de sécurité, et rend la recherche plus difficile", "Accepter, le stockage étant bon marché", "Accepter, mais seulement pour les données personnelles", "Tout supprimer au bout d'un an"], 0,
      "Le coût du stockage n'est pas le seul critère : données personnelles conservées sans justification, risques de fuite et de contentieux, bruit documentaire."),
    Q("Cas : un éditeur vous assure que sa GED « fait aussi l'archivage ». Que demandez-vous ?",
      ["Une démonstration du versement, du contrôle d'intégrité et du journal d'audit", "Le nombre de clients en Europe", "La couleur de l'interface", "Une remise sur les licences"], 0,
      "Les garanties d'un SAE se démontrent : versement, empreintes, journal, contrôle d'intégrité."),
    Q("Cas : un contentieux est annoncé avec un ancien fournisseur. Des documents le concernant arrivent au terme de leur durée de conservation. Que faites-vous ?",
      ["Les placer sous gel juridique jusqu'à la clôture de l'affaire", "Les éliminer comme prévu", "Les remettre au fournisseur", "Les numériser puis détruire les originaux"], 0,
      "Le gel juridique prime sur la durée de conservation."),
    Q("Cas : votre conseil demande le RTO et le RPO de vos archives. Qui doit les fixer ?",
      ["La direction, en arbitrant entre niveau de risque et coût", "Le prestataire d'hébergement", "Le stagiaire informatique", "Personne, ce sont des données techniques"], 0,
      "Ce sont des décisions de direction, éclairées par la DSI."),
    Q("Quelles mesures relèvent de la conduite du changement ?",
      ["Nommer des référents dans chaque direction", "Former par rôle", "Fermer à une date annoncée les anciens espaces de stockage", "Acheter davantage de licences que d'utilisateurs"], [0, 1, 2],
      "Référents, formation par rôle et fermeture des alternatives sont les leviers clés de l'adoption."),
    Q("Un plan de classement fonctionnel doit être entièrement refait à chaque réorganisation.", VF, 1,
      "C'est précisément l'avantage du classement par fonctions : il survit aux changements d'organigramme."),
    Q("Quel est le premier poste de coût souvent sous-estimé d'un projet documentaire ?",
      ["La reprise de l'existant et la numérisation", "Le mobilier de bureau", "Les frais de déplacement", "Les cartes de visite"], 0,
      "La reprise de l'existant est fréquemment le premier poste de coût réel."),
    Q("Dans un dossier d'investissement, quelle catégorie de bénéfices emporte souvent la décision ?",
      ["Les risques évités, documentés par les incidents passés", "La modernité de l'image", "Le nombre de fonctionnalités", "La rapidité du déploiement"], 0,
      "Les incidents déjà subis, chiffrés par l'organisation elle-même, sont l'argument le plus convaincant."),
]

DIR = {
    "num": 7, "slug": "parcours-dirigeant", "title": "Parcours dirigeant",
    "label": "Parcours dirigeant — 12 semaines",
    "unit": "Semaine",
    "audience": "Dirigeants, membres de comités de direction, secrétaires généraux",
    "duration": "12 semaines · 1 h par semaine",
    "intro": "Douze séances d'une heure pour gouverner l'information de votre organisation : comprendre, décider, investir et piloter, sans devenir archiviste.",
    "objectives": [
        "Lire l'archivage comme un enjeu de risque, de preuve et de performance, et le porter en comité de direction",
        "Distinguer les briques d'une solution (GEC, GED, records management, SAE) et rédiger des exigences justes",
        "Prendre les décisions qui reviennent à la direction : politique, responsabilités, durées de conservation, sécurité, hébergement",
        "Construire un dossier d'investissement sur un coût complet et des bénéfices démontrables",
        "Piloter un programme documentaire sur trois horizons avec six indicateurs, et en conduire l'adoption",
    ],
    "exam_size": 20,
    "modules": WEEKS_1_6 + [W7, W8, W9, W10, W11, W12],
    "exam_extra": EXAM_EXTRA,
}
