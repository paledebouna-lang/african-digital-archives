"""ARCHIVA Academy — contenus des niveaux 3 et 4."""
from .academy_n1_n2 import Q, VF

N3 = {
    "num": 3, "slug": "niveau-3", "title": "Records management",
    "audience": "Archivistes, référents documentaires", "duration": "4 h",
    "intro": "Gouverner les documents d'activité : principes de l'ISO 15489, plan de classement, métadonnées et règles de conservation.",
    "objectives": ["Citer les quatre caractéristiques d'un document d'activité selon l'ISO 15489",
                   "Construire un plan de classement fondé sur les activités",
                   "Choisir les métadonnées utiles à la gestion et à la preuve",
                   "Rédiger une règle de conservation complète et organiser une élimination tracée"],
    "modules": [
        {
            "title": "Les principes de l'ISO 15489", "minutes": 40,
            "html": """
<p>Le <strong>records management</strong> (gestion des documents d'activité) organise la création, la conservation, l'utilisation et le sort final des documents qui témoignent des activités d'une organisation. Sa norme de référence internationale est l'<strong>ISO 15489-1:2016</strong>.</p>
<h3>Le « record », un document qui engage</h3>
<p>Un <em>record</em> est un document produit ou reçu dans le cadre d'une activité et conservé comme preuve de cette activité. Tous les documents ne sont pas des records : un brouillon ou une copie de travail ne l'est généralement pas ; la version signée d'un contrat, si.</p>
<h3>Les quatre caractéristiques d'un document d'activité</h3>
<ul>
<li><strong>Authenticité</strong> : le document est bien ce qu'il prétend être, créé ou envoyé par la personne indiquée, au moment indiqué.</li>
<li><strong>Fiabilité</strong> : son contenu est une représentation exacte et complète de l'activité qu'il atteste.</li>
<li><strong>Intégrité</strong> : il est complet et n'a pas été altéré. Toute modification autorisée est tracée.</li>
<li><strong>Exploitabilité</strong> : on peut le retrouver, le présenter et l'interpréter, avec son contexte.</li>
</ul>
<h3>Un système, pas un logiciel</h3>
<p>Pour l'ISO 15489, le records management repose sur des <strong>politiques</strong> (qui est responsable de quoi), des <strong>processus</strong> (capture, classement, conservation, élimination), des <strong>outils</strong> (plan de classement, référentiel de conservation, règles d'accès) et des <strong>systèmes</strong> informatiques. Un logiciel seul n'en fait pas un dispositif de records management.</p>
<h3>Les responsabilités</h3>
<p>La direction porte la politique ; le records manager ou l'archiviste conçoit les outils et contrôle leur application ; chaque agent capture et classe correctement les documents qu'il produit ; l'informatique garantit la sécurité et la disponibilité des systèmes.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Authenticité, fiabilité, intégrité, exploitabilité.</li><li>Records management = politiques + processus + outils + systèmes.</li><li>La responsabilité est partagée, de la direction à chaque agent.</li></ul></div>""",
            "quiz": [
                Q("Quelles sont les quatre caractéristiques d'un document d'activité selon l'ISO 15489 ?",
                  ["Authenticité", "Fiabilité", "Intégrité", "Exploitabilité", "Rentabilité"], [0, 1, 2, 3],
                  "La rentabilité ne fait pas partie des caractéristiques définies par la norme."),
                Q("Un document « intègre » est un document…",
                  ["Complet et non altéré", "Écrit par un juriste", "Imprimé en couleur", "Classé dans le bon dossier"], 0,
                  "L'intégrité garantit que le document est complet et n'a pas été modifié sans trace."),
                Q("Installer un logiciel suffit à mettre en place un records management.", VF, 1,
                  "Il faut aussi des politiques, des processus et des outils comme le plan de classement."),
                Q("Quelle est la norme internationale de référence du records management ?",
                  ["ISO 15489", "ISO 27001", "ISO 9001", "ISO 14721"], 0,
                  "ISO 15489 pour le records management ; 27001 pour la sécurité ; 14721 pour la préservation (OAIS)."),
            ],
        },
        {
            "title": "Construire un plan de classement", "minutes": 45,
            "html": """
<p>Le <strong>plan de classement</strong> est la structure qui organise tous les documents de l'organisation. C'est l'outil le plus important du records management : il sert au rangement, à la recherche, aux droits d'accès et aux règles de conservation.</p>
<h3>Classer par fonctions et activités</h3>
<p>Un bon plan de classement suit les <strong>fonctions</strong> de l'organisation (ce qu'elle fait) plutôt que son organigramme (comment elle est organisée). Les organigrammes changent ; les fonctions restent.</p>
<table><thead><tr><th>Niveau</th><th>Exemple</th></tr></thead><tbody>
<tr><td>Fonction</td><td>Gestion financière</td></tr>
<tr><td>Activité / série</td><td>Comptabilité fournisseurs</td></tr>
<tr><td>Sous-série</td><td>Factures fournisseurs</td></tr>
<tr><td>Dossier</td><td>Factures 2026 — ABC SA</td></tr></tbody></table>
<h3>La méthode en six étapes</h3>
<ol><li><strong>Recenser les fonctions</strong> à partir des textes fondateurs, de l'organigramme et des entretiens.</li>
<li><strong>Détailler les activités</strong> de chaque fonction.</li>
<li><strong>Identifier les séries</strong> de documents produites par chaque activité.</li>
<li><strong>Codifier</strong> : donner un code à chaque niveau (par exemple FIN.02.03) pour un classement stable.</li>
<li><strong>Tester</strong> sur un échantillon réel de documents de chaque service.</li>
<li><strong>Valider et versionner</strong> : faire approuver le plan, le dater, le numéroter.</li></ol>
<h3>Les pièges</h3>
<ul><li>Trop de niveaux : au-delà de quatre ou cinq, personne ne s'y retrouve.</li>
<li>Des intitulés vagues (« Divers », « Autres », « À classer »).</li>
<li>Des doublons de séries d'un service à l'autre : un contrat ne se classe qu'à un seul endroit, les autres services y accèdent par les droits.</li></ul>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Classer selon les fonctions et activités, pas selon l'organigramme.</li><li>Fonction → activité → série → dossier, avec des codes stables.</li><li>Tester, valider, versionner.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Construisez le plan de classement de la fonction « Ressources humaines » de votre organisation sur trois niveaux. Testez-le avec dix documents réels.</p></div>""",
            "quiz": [
                Q("Sur quoi doit reposer de préférence un plan de classement ?",
                  ["L'organigramme", "Les fonctions et activités de l'organisation", "Les noms des agents", "L'ordre alphabétique"], 1,
                  "Les fonctions sont stables ; l'organigramme change avec les réorganisations."),
                Q("Pourquoi codifier les niveaux du plan de classement (ex. FIN.02.03) ?",
                  ["Pour un classement stable et non ambigu", "Pour masquer le contenu", "Pour faire joli", "Pour remplacer les métadonnées"], 0,
                  "Le code reste stable même si l'intitulé évolue légèrement."),
                Q("Un même contrat doit être classé dans chaque service qui l'utilise.", VF, 1,
                  "Un document se classe à un seul endroit ; les autres services y accèdent par les droits."),
                Q("Quelles étapes font partie de la méthode présentée ?",
                  ["Recenser les fonctions", "Tester sur un échantillon", "Valider et versionner", "Supprimer les anciens documents"], [0, 1, 2],
                  "La suppression ne fait pas partie de la construction du plan ; elle relève du sort final, encadré."),
            ],
        },
        {
            "title": "Les métadonnées", "minutes": 40,
            "html": """
<p>Les <strong>métadonnées</strong> sont les informations qui décrivent un document : son identité, son contexte, son contenu, sa gestion. Sans elles, un document archivé est introuvable et privé de son contexte. La norme <strong>ISO 23081</strong> leur est consacrée.</p>
<h3>Cinq familles de métadonnées</h3>
<table><thead><tr><th>Famille</th><th>Exemples</th></tr></thead><tbody>
<tr><td>Identification</td><td>Identifiant unique, titre, type de document, numéro, version</td></tr>
<tr><td>Contexte</td><td>Auteur, service producteur, dossier, client, projet</td></tr>
<tr><td>Dates</td><td>Création, réception, signature, archivage</td></tr>
<tr><td>Gestion</td><td>Code de classement, confidentialité, règle de conservation, échéance, statut</td></tr>
<tr><td>Technique et preuve</td><td>Format, taille, empreinte (SHA-256), signature, horodatage, localisation</td></tr></tbody></table>
<h3>Choisir les bonnes métadonnées</h3>
<p>Chaque type de document a ses métadonnées utiles : une facture demande un fournisseur, un numéro, une date et un montant ; un contrat demande des parties, une date de signature et une date d'échéance. Posez-vous une seule question : <em>comment les utilisateurs chercheront-ils ce document dans cinq ans ?</em></p>
<h3>Automatiser autant que possible</h3>
<p>Beaucoup de métadonnées peuvent être capturées automatiquement : dates techniques, format, taille, empreinte, auteur du dépôt. D'autres peuvent être proposées par l'OCR et l'intelligence artificielle (montant, numéro de facture) puis validées par l'utilisateur. Ce qui reste à saisir à la main doit être minimal.</p>
<h3>La qualité avant la quantité</h3>
<p>Dix champs obligatoires mal remplis valent moins que trois champs toujours justes. Utilisez des listes de valeurs (types, services, niveaux de confidentialité) plutôt que du texte libre, pour éviter « Compta », « comptabilité » et « Service comptable » pour la même chose.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Identification, contexte, dates, gestion, technique et preuve.</li><li>Choisir selon la façon dont on cherchera le document.</li><li>Automatiser, utiliser des listes de valeurs, viser la qualité.</li></ul></div>""",
            "quiz": [
                Q("Quelle norme est consacrée aux métadonnées des documents d'activité ?",
                  ["ISO 23081", "ISO 19005", "ISO 22301", "ISO 16363"], 0,
                  "ISO 23081 traite des métadonnées pour les records."),
                Q("Dans quelle famille range-t-on l'empreinte SHA-256 d'un document ?",
                  ["Identification", "Contexte", "Technique et preuve", "Dates"], 2,
                  "L'empreinte sert à prouver l'intégrité : famille technique et preuve."),
                Q("Pourquoi préférer des listes de valeurs au texte libre ?",
                  ["Pour éviter les variantes d'une même valeur", "Pour fiabiliser la recherche", "Pour ralentir la saisie", "Pour faciliter les statistiques"], [0, 1, 3],
                  "Les listes fiabilisent la recherche et les statistiques en supprimant les variantes."),
                Q("Plus il y a de métadonnées obligatoires, meilleure est la gestion.", VF, 1,
                  "Trop de champs obligatoires dégradent leur qualité ; mieux vaut peu de champs toujours justes."),
            ],
        },
        {
            "title": "Conservation et sort final", "minutes": 45,
            "html": """
<p>Le <strong>référentiel de conservation</strong> (ou tableau de gestion) fixe, pour chaque série de documents, combien de temps la conserver et ce qu'elle devient ensuite.</p>
<h3>Les éléments d'une règle de conservation</h3>
<table><thead><tr><th>Élément</th><th>Exemple : factures fournisseurs</th></tr></thead><tbody>
<tr><td>Série</td><td>FIN.02.03 — Factures fournisseurs</td></tr>
<tr><td>Durée</td><td>10 ans (à valider par le juriste)</td></tr>
<tr><td>Événement déclencheur</td><td>Clôture de l'exercice comptable</td></tr>
<tr><td>Sort final</td><td>Destruction après examen</td></tr>
<tr><td>Fondement</td><td>Texte applicable ou décision interne</td></tr>
<tr><td>Responsable</td><td>Chef comptable</td></tr></tbody></table>
<p><strong>Règle d'or :</strong> la durée n'est jamais inventée. Elle s'appuie sur la réglementation applicable, les besoins de preuve et les besoins métier, et elle est validée par un juriste. Un logiciel applique les règles ; il ne les décide pas.</p>
<h3>Les trois sorts finaux</h3>
<ul><li><strong>Destruction</strong> (élimination) : le document n'a plus d'utilité ni d'intérêt historique.</li>
<li><strong>Conservation définitive</strong> : le document a une valeur historique ou patrimoniale.</li>
<li><strong>Tri</strong> : on conserve un échantillon représentatif et on élimine le reste (par exemple une année sur dix).</li></ul>
<h3>Une élimination tracée</h3>
<p>Détruire n'est jamais un geste anodin. Le processus : liste des documents arrivés à échéance → vérification qu'aucun gel juridique ne s'applique → validation par le responsable habilité → destruction sécurisée (broyage, effacement sécurisé) → <strong>certificat ou bordereau d'élimination</strong> conservé définitivement.</p>
<h3>Le gel juridique</h3>
<p>Quand un contentieux, un audit ou une enquête est en cours ou prévisible, toute destruction des documents concernés est suspendue, même si leur durée est écoulée. C'est le <strong>gel juridique</strong> (<em>legal hold</em>).</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Série, durée, événement déclencheur, sort final, fondement, responsable.</li><li>Les durées se valident avec un juriste ; elles ne s'inventent pas.</li><li>Élimination validée, sécurisée, documentée ; gel juridique prioritaire.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Rédigez la règle de conservation complète de trois séries de votre organisation. Notez pour chacune le texte ou la décision qui justifie la durée.</p></div>""",
            "quiz": [
                Q("Que se passe-t-il pour un document arrivé à échéance mais concerné par un contentieux en cours ?",
                  ["Il est détruit immédiatement", "Sa destruction est suspendue (gel juridique)", "Il est transféré au client", "Il est anonymisé"], 1,
                  "Le gel juridique prime sur l'échéance : aucune destruction tant que le contentieux dure."),
                Q("Qui doit valider les durées de conservation ?",
                  ["Le logiciel automatiquement", "Un juriste, avec l'archiviste et les métiers", "Le stagiaire", "Le fournisseur informatique"], 1,
                  "Les durées s'appuient sur le droit applicable : un juriste les valide."),
                Q("Quels éléments composent une règle de conservation ?",
                  ["Une durée", "Un événement déclencheur", "Un sort final", "La couleur du classeur"], [0, 1, 2],
                  "Durée, déclencheur et sort final (plus fondement et responsable)."),
                Q("Le certificat d'élimination peut être détruit avec les documents qu'il liste.", VF, 1,
                  "Non : il prouve que l'élimination a été régulière, il se conserve définitivement."),
            ],
        },
    ],
    "exam_extra": [
        Q("Un brouillon de travail est en général un document d'activité (record).", VF, 1,
          "Le record est la version qui atteste l'activité, par exemple le contrat signé."),
        Q("Le tri, comme sort final, consiste à…",
          ["Tout détruire", "Tout garder", "Conserver un échantillon et éliminer le reste", "Numériser puis détruire"], 2,
          "Le tri conserve un échantillon représentatif."),
        Q("Qui garantit la sécurité et la disponibilité des systèmes d'archivage ?",
          ["L'informatique", "Le service commercial", "Les clients", "Personne"], 0,
          "Dans la répartition des responsabilités, c'est le rôle de l'informatique."),
        Q("Quelle question aide à choisir les métadonnées d'un type de document ?",
          ["Comment le cherchera-t-on dans cinq ans ?", "Combien pèse le fichier ?", "Qui l'a imprimé ?", "Quelle police est utilisée ?"], 0,
          "Les métadonnées servent d'abord à retrouver et comprendre le document plus tard."),
    ],
}

N4 = {
    "num": 4, "slug": "niveau-4", "title": "Archivage électronique",
    "audience": "Archivistes, juristes, équipes informatiques", "duration": "4 h",
    "intro": "Conserver des documents numériques avec valeur de preuve : exigences d'un SAE, intégrité, horodatage, signature et cadre ivoirien.",
    "objectives": ["Distinguer GED et système d'archivage électronique (SAE)",
                   "Expliquer le fonctionnement d'une empreinte cryptographique et de l'horodatage",
                   "Situer la signature électronique dans la chaîne de preuve",
                   "Citer les textes ivoiriens applicables à l'archivage électronique"],
    "modules": [
        {
            "title": "Du document vivant à l'archive : le SAE", "minutes": 40,
            "html": """
<p>Un <strong>système d'archivage électronique</strong> (SAE) conserve des documents numériques dans des conditions qui garantissent leur valeur dans le temps. Là où la GED gère des documents qu'on modifie, le SAE conserve des documents <strong>figés</strong>.</p>
<h3>GED et SAE : deux rôles complémentaires</h3>
<table><thead><tr><th></th><th>GED</th><th>SAE</th></tr></thead><tbody>
<tr><td>Objet</td><td>Documents vivants</td><td>Documents figés</td></tr>
<tr><td>Modification</td><td>Autorisée, versionnée</td><td>Interdite</td></tr>
<tr><td>Suppression</td><td>Par l'utilisateur, selon ses droits</td><td>Uniquement à l'échéance, par procédure</td></tr>
<tr><td>Objectif</td><td>Travailler ensemble</td><td>Prouver et conserver</td></tr></tbody></table>
<h3>Les exigences d'un SAE</h3>
<ul><li><strong>Intégrité</strong> : un document archivé ne peut plus être modifié, et toute altération est détectable.</li>
<li><strong>Traçabilité</strong> : chaque opération (versement, consultation, communication, élimination) est inscrite dans un journal.</li>
<li><strong>Pérennité</strong> : le document reste lisible pendant toute sa durée de conservation.</li>
<li><strong>Confidentialité</strong> : seules les personnes autorisées y accèdent.</li>
<li><strong>Disponibilité</strong> : le document peut être retrouvé et restitué quand on en a besoin.</li></ul>
<h3>Le versement</h3>
<p>Le passage d'un document de la GED vers le SAE s'appelle le <strong>versement</strong>. Il intervient à un moment défini : signature d'un contrat, clôture d'un dossier, fin d'un exercice. Au versement, le SAE vérifie le format, enregistre les métadonnées, calcule l'empreinte et applique la règle de conservation.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>GED pour travailler, SAE pour prouver et conserver.</li><li>Intégrité, traçabilité, pérennité, confidentialité, disponibilité.</li><li>Le versement fige le document et déclenche sa règle de conservation.</li></ul></div>""",
            "quiz": [
                Q("Dans un SAE, un document archivé peut être modifié par son auteur.", VF, 1,
                  "Le SAE conserve des documents figés : toute modification est interdite."),
                Q("Comment s'appelle le passage d'un document de la GED vers le SAE ?",
                  ["Le versement", "Le téléchargement", "La compression", "Le partage"], 0,
                  "Le versement fige le document et applique sa règle de conservation."),
                Q("Quelles exigences un SAE doit-il garantir ?",
                  ["Intégrité", "Traçabilité", "Pérennité", "Modification libre"], [0, 1, 2],
                  "La modification libre est justement exclue du SAE."),
                Q("Dans un SAE, la suppression d'un document intervient…",
                  ["Quand l'utilisateur le décide", "Uniquement à l'échéance, selon une procédure", "Tous les ans automatiquement", "Jamais, dans aucun cas"], 1,
                  "L'élimination suit la règle de conservation et une procédure validée et tracée."),
            ],
        },
        {
            "title": "Intégrité et preuve : empreinte, horodatage, journal", "minutes": 45,
            "html": """
<p>Comment prouver qu'un fichier n'a pas été modifié depuis son archivage ? En combinant trois outils : l'empreinte cryptographique, l'horodatage et le journal.</p>
<h3>L'empreinte cryptographique</h3>
<p>Une <strong>fonction de hachage</strong> comme <strong>SHA-256</strong> calcule, à partir du contenu d'un fichier, une empreinte de 256 bits, écrite sous la forme de 64 caractères hexadécimaux. Ses propriétés :</p>
<ul><li>le même fichier donne toujours la même empreinte ;</li>
<li>la moindre modification (une virgule, un pixel) donne une empreinte totalement différente ;</li>
<li>il est impossible en pratique de retrouver le fichier à partir de l'empreinte, ou de fabriquer un autre fichier ayant la même.</li></ul>
<p>Au versement, le SAE calcule et enregistre l'empreinte. Pour vérifier l'intégrité, il la recalcule et compare : identique, le document est intact ; différente, il a été altéré. Vous pouvez l'essayer sur la page <a href="~/archiva360/modules/">Modules d'ARCHIVA360</a>.</p>
<h3>L'horodatage</h3>
<p>L'empreinte prouve que le document n'a pas changé, mais pas <em>depuis quand</em>. L'<strong>horodatage</strong> associe une date et une heure certaines à l'empreinte. Pour qu'il soit opposable, il est délivré par un tiers de confiance (autorité d'horodatage) qui signe le couple empreinte + date.</p>
<h3>Le journal</h3>
<p>Le <strong>journal</strong> (audit trail) enregistre chaque opération : qui, quoi, quand, depuis où, quelle action. Pour être fiable, il doit lui-même être protégé contre la modification, par exemple en chaînant les empreintes de ses entrées : chaque entrée inclut l'empreinte de la précédente, si bien qu'une modification casse la chaîne.</p>
<h3>Et la blockchain ?</h3>
<p>Une blockchain peut servir de registre public d'empreintes. On n'y inscrit jamais le document lui-même (coût, confidentialité, impossibilité d'effacer), seulement son empreinte. C'est une option de preuve complémentaire, pas une obligation.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>SHA-256 : 64 caractères hexadécimaux, change totalement à la moindre modification.</li><li>Horodatage = date certaine délivrée par un tiers de confiance.</li><li>Journal protégé, par exemple par chaînage des empreintes.</li></ul></div>""",
            "quiz": [
                Q("Combien de caractères hexadécimaux compte une empreinte SHA-256 ?",
                  ["16", "32", "64", "256"], 2,
                  "256 bits = 64 caractères hexadécimaux (4 bits par caractère)."),
                Q("Si on ajoute une seule virgule dans un document, son empreinte SHA-256…",
                  ["Reste identique", "Change d'un seul caractère", "Change complètement", "Disparaît"], 2,
                  "La moindre modification produit une empreinte totalement différente."),
                Q("Que prouve l'horodatage délivré par un tiers de confiance ?",
                  ["Que le document existait sous cette forme à une date donnée", "Que le document est vrai", "Que l'auteur est honnête", "Que le fichier est léger"], 0,
                  "Associé à l'empreinte, il date de façon certaine l'état du document."),
                Q("Il est recommandé d'inscrire le document complet sur une blockchain.", VF, 1,
                  "On n'inscrit que l'empreinte : le document reste dans l'archive sécurisée."),
            ],
        },
        {
            "title": "Signature électronique", "minutes": 35,
            "html": """
<p>La <strong>signature électronique</strong> permet d'identifier le signataire et de manifester son consentement au contenu d'un document électronique. Elle garantit aussi que le document n'a pas été modifié après signature.</p>
<h3>Comment ça marche</h3>
<p>La signature électronique avancée repose sur la cryptographie à clé publique. Le signataire dispose d'une <strong>clé privée</strong>, qu'il est seul à contrôler, et d'un <strong>certificat</strong> délivré par une autorité de certification, qui associe sa clé publique à son identité. Signer, c'est chiffrer l'empreinte du document avec la clé privée ; vérifier, c'est la déchiffrer avec la clé publique et la comparer à l'empreinte recalculée.</p>
<h3>Les niveaux de signature</h3>
<p>On distingue généralement plusieurs niveaux de fiabilité : une signature simple (une case cochée, une image de signature), une signature avancée (liée de façon unique au signataire, avec détection des modifications) et une signature qualifiée (avec un dispositif sécurisé et un certificat qualifié). Plus l'enjeu juridique est fort, plus le niveau requis est élevé.</p>
<h3>Le cadre ivoirien</h3>
<p>En Côte d'Ivoire, la loi n°2013-546 relative aux transactions électroniques reconnaît l'écrit électronique, et le <strong>décret n°2014-106</strong> précise les conditions de l'écrit et de la signature électroniques. L'ANSSI Côte d'Ivoire recense ces textes.</p>
<h3>Signer puis archiver</h3>
<p>Une signature électronique doit pouvoir être vérifiée des années plus tard, alors que les certificats expirent. D'où l'importance d'archiver le document signé <strong>avec ses éléments de preuve</strong> : certificat, jeton d'horodatage, dossier de preuve du prestataire. ARCHIVA360 s'appuie sur des prestataires de signature de confiance et archive ces éléments avec le document.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Clé privée + certificat : identité du signataire et intégrité du document.</li><li>Niveau de signature proportionné à l'enjeu.</li><li>Archiver le document signé avec toutes ses preuves.</li></ul></div>""",
            "quiz": [
                Q("Que garantit une signature électronique avancée ?",
                  ["L'identification du signataire", "La détection d'une modification après signature", "La traduction automatique", "Le consentement du signataire"], [0, 1, 3],
                  "Identification, consentement et intégrité ; la traduction n'a rien à voir."),
                Q("Quel élément associe la clé publique d'un signataire à son identité ?",
                  ["Le certificat", "Le mot de passe", "Le nom du fichier", "L'adresse IP"], 0,
                  "Le certificat, délivré par une autorité de certification, fait ce lien."),
                Q("Pourquoi archiver le jeton d'horodatage et le certificat avec le document signé ?",
                  ["Pour pouvoir vérifier la signature même après l'expiration du certificat", "Pour alourdir le dossier", "Parce que c'est plus joli", "Pour supprimer la signature"], 0,
                  "Les preuves conservées permettent de vérifier la signature des années plus tard."),
                Q("En Côte d'Ivoire, la loi n°2013-546 porte sur…",
                  ["Les transactions électroniques", "Le code du travail", "La fiscalité locale", "Les marchés publics"], 0,
                  "La loi n°2013-546 est relative aux transactions électroniques."),
            ],
        },
        {
            "title": "Le cadre ivoirien et la protection des données", "minutes": 40,
            "html": """
<p>ADA démarre en Côte d'Ivoire notamment parce que le pays dispose d'un cadre identifié pour l'écrit électronique et l'archivage. Ce module présente les repères essentiels. Il ne remplace pas l'avis d'un juriste.</p>
<h3>Les textes de référence</h3>
<table><thead><tr><th>Texte</th><th>Objet</th></tr></thead><tbody>
<tr><td>Loi n°2013-546</td><td>Transactions électroniques ; définit notamment l'archivage électronique sécurisé</td></tr>
<tr><td>Loi n°2013-450</td><td>Protection des données à caractère personnel</td></tr>
<tr><td>Décret n°2014-106</td><td>Écrit et signature électroniques</td></tr>
<tr><td>Décret n°2016-851 du 19 octobre 2016</td><td>Modalités de mise en œuvre de l'archivage électronique</td></tr>
<tr><td>Décret n°2021-916</td><td>Référentiel général de sécurité des systèmes d'information (RGSSI)</td></tr></tbody></table>
<h3>Les autorités</h3>
<p>L'<strong>ARTCI</strong> (Autorité de régulation des télécommunications/TIC de Côte d'Ivoire) est l'autorité de protection des données personnelles. L'<strong>ANSSI Côte d'Ivoire</strong> recense les textes relatifs à la sécurité des systèmes d'information et à la confiance numérique.</p>
<h3>Archives et données personnelles</h3>
<p>Les archives regorgent de données personnelles : dossiers du personnel, dossiers clients, dossiers patients, pièces d'identité. La protection des données s'applique donc pleinement à l'archivage :</p>
<ul><li><strong>finalité</strong> : on conserve pour une raison définie ;</li>
<li><strong>durée limitée</strong> : on ne garde pas indéfiniment des données personnelles sans justification ;</li>
<li><strong>sécurité</strong> : accès restreint, journalisation, chiffrement ;</li>
<li><strong>droits des personnes</strong> : accès, rectification, opposition, selon les conditions prévues par la loi.</li></ul>
<h3>La posture professionnelle</h3>
<p>Travailler avec un archiviste, un juriste, un expert en cybersécurité et un spécialiste de la protection des données. Documenter les choix. Et ne jamais présenter un dispositif comme « conforme à tout » sans validation juridique et technique indépendante.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>2013-546, 2013-450, 2014-106, 2016-851, 2021-916.</li><li>ARTCI pour les données personnelles ; ANSSI pour la sécurité.</li><li>Finalité, durée limitée, sécurité, droits des personnes.</li></ul></div>""",
            "quiz": [
                Q("Quel texte porte sur les modalités de mise en œuvre de l'archivage électronique en Côte d'Ivoire ?",
                  ["Décret n°2016-851", "Loi n°2013-450", "Décret n°2014-106", "Décret n°2021-916"], 0,
                  "Le décret n°2016-851 du 19 octobre 2016 porte sur l'archivage électronique."),
                Q("Quelle autorité est chargée de la protection des données personnelles en Côte d'Ivoire ?",
                  ["L'ARTCI", "La BCEAO", "L'ANSSI", "La CNPS"], 0,
                  "L'ARTCI est l'autorité de protection des données à caractère personnel."),
                Q("Les règles de protection des données personnelles ne s'appliquent pas aux archives.", VF, 1,
                  "Elles s'appliquent pleinement : finalité, durée limitée, sécurité, droits des personnes."),
                Q("Que désigne le RGSSI ?",
                  ["Le référentiel général de sécurité des systèmes d'information", "Un logiciel de GED", "Une norme de numérisation", "Un registre de courrier"], 0,
                  "Le RGSSI, adopté par le décret n°2021-916, fixe des exigences de sécurité."),
            ],
        },
    ],
    "exam_extra": [
        Q("Le chaînage des empreintes dans un journal sert à…",
          ["Rendre toute modification du journal détectable", "Accélérer les recherches", "Compresser le journal", "Traduire le journal"], 0,
          "Chaque entrée dépendant de la précédente, une modification casse la chaîne."),
        Q("Le décret n°2014-106 porte sur l'écrit et la signature électroniques.", VF, 0,
          "C'est bien son objet."),
        Q("Une image de signature collée dans un document constitue une signature qualifiée.", VF, 1,
          "C'est au mieux une signature simple, sans garantie d'identité ni d'intégrité."),
        Q("Au versement dans le SAE, quelles opérations sont réalisées ?",
          ["Vérification du format", "Calcul de l'empreinte", "Application de la règle de conservation", "Envoi du document par WhatsApp"], [0, 1, 2],
          "Format, empreinte et règle de conservation : le document est figé et pris en charge."),
    ],
}
