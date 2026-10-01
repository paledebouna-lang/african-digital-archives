"""ARCHIVA Academy — contenus des niveaux 5 et 6."""
from .academy_n1_n2 import Q, VF

N5 = {
    "num": 5, "slug": "niveau-5", "title": "Préservation numérique",
    "audience": "Archivistes, équipes informatiques", "duration": "4 h",
    "intro": "Garder l'information numérique lisible, intègre et compréhensible pendant des décennies : risques, modèle OAIS, formats et stratégies.",
    "objectives": ["Identifier les menaces qui pèsent sur l'information numérique à long terme",
                   "Décrire le modèle OAIS : ses paquets et ses fonctions",
                   "Choisir des formats de conservation adaptés",
                   "Mettre en place une stratégie de préservation : migration, contrôles, copies"],
    "modules": [
        {
            "title": "Pourquoi le numérique est fragile", "minutes": 35,
            "html": """
<p>On croit souvent qu'un fichier numérique est éternel, puisqu'il se copie sans perte. C'est l'inverse : sans action, l'information numérique disparaît plus vite que le papier.</p>
<h3>Quatre menaces</h3>
<ul><li><strong>La dégradation des supports</strong> : disques durs, clés USB, CD et bandes ont une durée de vie limitée, parfois quelques années. Des bits peuvent s'altérer silencieusement.</li>
<li><strong>L'obsolescence matérielle</strong> : qui peut encore lire une disquette de 3,5 pouces ?</li>
<li><strong>L'obsolescence logicielle</strong> : un fichier n'est lisible qu'avec un logiciel capable de l'interpréter. Des formats propriétaires des années 1990 sont aujourd'hui difficiles à ouvrir.</li>
<li><strong>La perte de contexte</strong> : un fichier « scan_0012.tif » sans métadonnées est une image dont plus personne ne sait ce qu'elle représente, ni pourquoi elle a été conservée.</li></ul>
<h3>Préserver, c'est agir en continu</h3>
<p>La préservation numérique est l'ensemble des actions qui maintiennent l'accès à l'information dans la durée malgré l'évolution des formats, des logiciels et des supports. Ce n'est pas un stockage passif : c'est une surveillance et des interventions régulières, documentées, pendant toute la durée de conservation.</p>
<h3>Qui est concerné ?</h3>
<p>Toute organisation qui conserve des documents numériques au-delà de dix ans : administrations, universités, banques, institutions patrimoniales, mais aussi entreprises pour leurs actes, plans et titres. Pour un fonds historique, c'est ce qui distingue une archive d'un simple disque de sauvegarde.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Supports, matériels, logiciels, contexte : quatre menaces.</li><li>La préservation est une action continue, pas un stockage passif.</li><li>Elle concerne tout document conservé au-delà de dix ans.</li></ul></div>""",
            "quiz": [
                Q("Quelles sont les menaces pesant sur l'information numérique à long terme ?",
                  ["Dégradation des supports", "Obsolescence logicielle", "Perte de contexte", "Excès de lumière sur l'écran"], [0, 1, 2],
                  "Supports, obsolescence matérielle et logicielle, perte de contexte."),
                Q("Un fichier numérique copié régulièrement est automatiquement préservé pour toujours.", VF, 1,
                  "Une copie ne protège ni de l'obsolescence des formats ni de la perte de contexte."),
                Q("Pourquoi un fichier « scan_0012.tif » sans métadonnées pose-t-il problème ?",
                  ["On ne sait plus ce qu'il représente ni pourquoi il est conservé", "Il est trop lourd", "Le TIFF est interdit", "Il n'a pas d'empreinte"], 0,
                  "Sans contexte, l'information perd son sens : c'est la perte de contexte."),
                Q("La préservation numérique est surtout…",
                  ["Un stockage passif sur disque", "Une action continue de surveillance et d'intervention", "Une impression sur papier", "Une compression des fichiers"], 1,
                  "Elle suppose des contrôles et des actions documentées pendant toute la conservation."),
            ],
        },
        {
            "title": "Le modèle OAIS", "minutes": 45,
            "html": """
<p>Le modèle <strong>OAIS</strong> (<em>Open Archival Information System</em>, système ouvert d'archivage d'information), normalisé sous la référence <strong>ISO 14721</strong>, est le cadre de référence mondial de la préservation à long terme. Il décrit ce que doit faire une archive, quelle que soit la technologie utilisée.</p>
<h3>Trois types de paquets</h3>
<ul><li><strong>SIP</strong> (paquet d'information à verser) : ce que le producteur transmet à l'archive.</li>
<li><strong>AIP</strong> (paquet d'information archivé) : ce que l'archive conserve, enrichi de toutes les informations nécessaires à la préservation.</li>
<li><strong>DIP</strong> (paquet d'information diffusé) : ce que l'archive remet à l'utilisateur qui le demande.</li></ul>
<p>Un paquet contient le contenu (les fichiers) et l'<strong>information de pérennisation</strong> : provenance, contexte, identifiants, intégrité (empreintes), droits d'accès, ainsi que l'information de représentation qui permet d'interpréter les fichiers.</p>
<h3>Six fonctions</h3>
<table><thead><tr><th>Fonction</th><th>Rôle</th></tr></thead><tbody>
<tr><td>Entrées</td><td>Recevoir les SIP, les contrôler, produire les AIP</td></tr>
<tr><td>Stockage archivistique</td><td>Conserver les AIP, gérer les copies et les supports, vérifier l'intégrité</td></tr>
<tr><td>Gestion des données</td><td>Gérer les métadonnées descriptives et les bases de recherche</td></tr>
<tr><td>Administration</td><td>Piloter l'archive au quotidien, les accords avec les producteurs, les politiques</td></tr>
<tr><td>Planification de la préservation</td><td>Surveiller les technologies et décider des migrations</td></tr>
<tr><td>Accès</td><td>Rechercher et produire les DIP pour les utilisateurs</td></tr></tbody></table>
<h3>La communauté d'utilisateurs cible</h3>
<p>Notion clé de l'OAIS : l'archive doit s'assurer que l'information reste <strong>compréhensible par sa communauté d'utilisateurs cible</strong>. Des archives municipales destinées aux citoyens n'ont pas les mêmes besoins d'explication que des données scientifiques destinées à des chercheurs.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>OAIS = ISO 14721, modèle de référence de la préservation.</li><li>SIP → AIP → DIP.</li><li>Six fonctions : entrées, stockage, gestion des données, administration, planification, accès.</li></ul></div>""",
            "quiz": [
                Q("Quel paquet l'archive conserve-t-elle dans le modèle OAIS ?",
                  ["SIP", "AIP", "DIP", "PDF"], 1,
                  "L'AIP (paquet d'information archivé) est l'objet de la conservation."),
                Q("Quel paquet est remis à l'utilisateur qui fait une demande ?",
                  ["SIP", "AIP", "DIP", "ZIP"], 2,
                  "Le DIP (paquet d'information diffusé) est produit par la fonction Accès."),
                Q("Quelle fonction OAIS surveille les technologies et décide des migrations ?",
                  ["Planification de la préservation", "Entrées", "Accès", "Administration"], 0,
                  "La planification de la préservation assure la veille et décide des actions."),
                Q("Le modèle OAIS impose l'utilisation d'un logiciel précis.", VF, 1,
                  "OAIS est un modèle conceptuel, indépendant de toute technologie."),
            ],
        },
        {
            "title": "Choisir des formats de conservation", "minutes": 40,
            "html": """
<p>Le format d'un fichier conditionne sa lisibilité future. Pour la conservation longue, on privilégie des <strong>formats pérennes</strong>.</p>
<h3>Les critères d'un format pérenne</h3>
<ul><li><strong>Ouvert et documenté</strong> : sa spécification est publique, n'importe qui peut écrire un logiciel pour le lire.</li>
<li><strong>Largement utilisé</strong> : plus un format est répandu, plus il sera soutenu longtemps.</li>
<li><strong>Autonome</strong> : il ne dépend pas de ressources externes (polices non intégrées, liens vers des fichiers tiers).</li>
<li><strong>Sans chiffrement ni protection</strong> qui empêcherait sa lecture future.</li>
<li><strong>Normalisé</strong> si possible.</li></ul>
<h3>Quelques formats recommandés</h3>
<table><thead><tr><th>Type de contenu</th><th>Formats de conservation courants</th></tr></thead><tbody>
<tr><td>Documents textuels mis en page</td><td>PDF/A (ISO 19005)</td></tr>
<tr><td>Textes structurés, données</td><td>XML, CSV, ODF (ISO/IEC 26300)</td></tr>
<tr><td>Images numérisées</td><td>TIFF non compressé ou sans perte, JPEG 2000, PNG</td></tr>
<tr><td>Audio</td><td>WAV, FLAC</td></tr>
<tr><td>Vidéo</td><td>Formats ouverts et documentés selon les usages (par exemple FFV1 dans un conteneur Matroska pour la préservation)</td></tr></tbody></table>
<h3>Le PDF/A</h3>
<p>Le PDF/A est un profil du PDF conçu pour l'archivage : polices intégrées, pas de contenu dynamique, pas de chiffrement, métadonnées intégrées. Plusieurs versions coexistent (PDF/A-1, -2, -3, -4). Un PDF ordinaire n'est pas un PDF/A : il faut le convertir, puis <strong>valider</strong> la conformité avec un outil dédié.</p>
<h3>Identifier et valider</h3>
<p>À l'entrée dans l'archive, chaque fichier est <strong>identifié</strong> (quel format exactement, quelle version ?) puis <strong>validé</strong> (le fichier respecte-t-il réellement la spécification ?). Des outils comme DROID, Siegfried ou JHOVE servent à ces opérations et s'appuient sur des registres de formats comme PRONOM.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Ouvert, documenté, répandu, autonome, sans chiffrement.</li><li>PDF/A pour les documents, TIFF ou JPEG 2000 pour les images, CSV ou XML pour les données.</li><li>Identifier et valider chaque fichier à l'entrée.</li></ul></div>""",
            "quiz": [
                Q("Quels critères caractérisent un format pérenne ?",
                  ["Ouvert et documenté", "Largement utilisé", "Chiffré par mot de passe", "Autonome"], [0, 1, 3],
                  "Le chiffrement empêcherait la lecture future : il est à proscrire pour la conservation."),
                Q("Quelle norme définit le format PDF/A ?",
                  ["ISO 19005", "ISO 15489", "ISO 27001", "ISO 8601"], 0,
                  "ISO 19005 définit le PDF/A ; ISO 8601 concerne les dates."),
                Q("Un PDF ordinaire est automatiquement un PDF/A.", VF, 1,
                  "Il faut le convertir puis valider sa conformité."),
                Q("À quoi sert un outil comme DROID ou Siegfried ?",
                  ["Identifier précisément le format d'un fichier", "Numériser du papier", "Signer un document", "Envoyer des courriels"], 0,
                  "Ces outils identifient les formats en s'appuyant sur des registres comme PRONOM."),
            ],
        },
        {
            "title": "Stratégies de préservation", "minutes": 40,
            "html": """
<p>Une fois les fichiers dans de bons formats, il faut les maintenir dans la durée. Voici les stratégies principales.</p>
<h3>Copies multiples : la règle 3-2-1</h3>
<p>Trois copies, sur deux supports différents, dont une hors site. Pour la préservation, on ajoute souvent une copie isolée ou immuable, protégée des rançongiciels.</p>
<h3>Contrôle d'intégrité périodique</h3>
<p>Les empreintes calculées au versement sont recalculées à intervalles réguliers sur toutes les copies. Une différence révèle une corruption : on restaure alors à partir d'une copie saine. Sans ce contrôle, une copie corrompue peut être recopiée pendant des années sans que personne ne s'en aperçoive.</p>
<h3>Migration</h3>
<p>Quand un format devient obsolète, on <strong>migre</strong> les fichiers vers un format actuel. Chaque migration est documentée : format d'origine, format cible, outil, date, contrôles réalisés. On garde en général le fichier d'origine à côté du fichier migré. La norme <strong>ISO 13008</strong> traite de la migration et de la conversion des documents numériques.</p>
<h3>Émulation</h3>
<p>Plutôt que de convertir le fichier, on recrée l'environnement d'origine (système, logiciel) sur une machine moderne. Utile pour des contenus complexes : bases de données anciennes, logiciels, contenus interactifs.</p>
<h3>Rafraîchissement des supports</h3>
<p>Copier régulièrement les données sur des supports neufs, avant que les anciens ne se dégradent.</p>
<h3>Évaluer son dispositif</h3>
<p>La norme <strong>ISO 16363</strong> permet d'auditer et de certifier un dépôt numérique fiable. Des grilles plus légères, comme les niveaux de préservation NDSA, aident à mesurer sa progression : savoir où sont ses données, combien de copies existent, si l'intégrité est vérifiée, qui a accès, quelles métadonnées existent.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>3-2-1, contrôle d'intégrité périodique, rafraîchissement des supports.</li><li>Migration documentée (ISO 13008) ou émulation selon les contenus.</li><li>ISO 16363 pour l'audit d'un dépôt fiable.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Pour un fonds numérique de votre organisation, répondez : combien de copies ? Où ? Quand l'intégrité a-t-elle été vérifiée pour la dernière fois ? Quels formats sont menacés ?</p></div>""",
            "quiz": [
                Q("Que signifie la règle 3-2-1 ?",
                  ["3 copies, 2 supports différents, 1 copie hors site", "3 serveurs, 2 logiciels, 1 archiviste", "3 ans, 2 contrôles, 1 migration", "3 formats, 2 langues, 1 pays"], 0,
                  "Trois copies, deux supports, une hors site."),
                Q("Pourquoi recalculer périodiquement les empreintes de toutes les copies ?",
                  ["Pour détecter une corruption silencieuse et restaurer à partir d'une copie saine", "Pour réduire la taille des fichiers", "Pour changer de format", "Pour supprimer les doublons"], 0,
                  "Sans contrôle, une copie corrompue peut se propager sans que personne ne le sache."),
                Q("Quelle norme traite de la migration et de la conversion des documents numériques ?",
                  ["ISO 13008", "ISO 9001", "ISO 15489", "ISO 22301"], 0,
                  "ISO 13008 est consacrée à la migration et à la conversion."),
                Q("L'émulation consiste à…",
                  ["Recréer l'environnement d'origine sur une machine moderne", "Imprimer les fichiers", "Compresser les archives", "Supprimer les anciens formats"], 0,
                  "On fait tourner l'ancien logiciel dans un environnement recréé."),
            ],
        },
    ],
    "exam_extra": [
        Q("Dans le modèle OAIS, le producteur transmet à l'archive un…", ["SIP", "AIP", "DIP", "CSV"], 0,
          "Le SIP est le paquet à verser."),
        Q("Une migration de format doit être documentée (format d'origine, cible, outil, date, contrôles).", VF, 0,
          "La documentation garde la preuve de l'authenticité après transformation."),
        Q("Quelle norme permet d'auditer et certifier un dépôt numérique fiable ?", ["ISO 16363", "ISO 14001", "ISO 19005", "ISO 23081"], 0,
          "ISO 16363 est la norme d'audit des dépôts numériques fiables."),
        Q("Quels formats sont adaptés à la conservation d'images numérisées ?", ["TIFF", "JPEG 2000", "PNG", "Un fichier Word"], [0, 1, 2],
          "TIFF, JPEG 2000 et PNG sont courants ; Word n'est pas un format d'image."),
    ],
}

N6 = {
    "num": 6, "slug": "niveau-6", "title": "Administration ARCHIVA360",
    "audience": "Administrateurs de la plateforme", "duration": "4 h",
    "intro": "Paramétrer et exploiter ARCHIVA360 : organisation, rôles, plan de classement, règles, sécurité, sauvegarde et pilotage. Avec des exercices dans la démo interactive.",
    "objectives": ["Organiser les utilisateurs et les rôles selon le principe du moindre privilège",
                   "Paramétrer le plan de classement, les types de documents et les règles de conservation",
                   "Mettre en place la sécurité, la sauvegarde et la reprise d'activité",
                   "Piloter la plateforme avec le tableau de bord, le Retention Center et l'audit trail"],
    "modules": [
        {
            "title": "Organisation, utilisateurs et rôles", "minutes": 40,
            "html": """
<p>ARCHIVA360 est une plateforme <strong>multi-organisations</strong> : chaque organisation dispose d'un espace strictement isolé. L'administrateur de l'organisation y gère les utilisateurs et leurs droits.</p>
<h3>Les rôles</h3>
<table><thead><tr><th>Rôle</th><th>Périmètre</th></tr></thead><tbody>
<tr><td>Super Admin</td><td>Gère toute la plateforme (équipe ADA)</td></tr>
<tr><td>Organisation Admin</td><td>Gère son organisation : utilisateurs, paramétrage</td></tr>
<tr><td>Archiviste</td><td>Gère les archives, les versements, le sort final</td></tr>
<tr><td>Records Manager</td><td>Gère le plan de classement et les règles de conservation</td></tr>
<tr><td>Document Manager</td><td>Gère les documents d'un périmètre</td></tr>
<tr><td>Direction</td><td>Valide et consulte</td></tr>
<tr><td>Employé</td><td>Accès métier à son périmètre</td></tr>
<tr><td>Auditeur</td><td>Lecture contrôlée, accès au journal</td></tr>
<tr><td>Utilisateur externe</td><td>Accès limité et temporaire</td></tr></tbody></table>
<h3>Le principe du moindre privilège</h3>
<p>Chaque personne reçoit <strong>les droits strictement nécessaires</strong> à sa mission, et pas davantage. Un comptable n'a pas besoin des dossiers RH ; un auditeur n'a pas besoin de modifier. Les droits se combinent : rôle + périmètre (dossiers, séries) + niveau de confidentialité.</p>
<h3>Le cycle de vie des comptes</h3>
<ul><li><strong>Arrivée</strong> : création du compte avec le rôle adapté, activation de l'authentification multifacteur.</li>
<li><strong>Changement de poste</strong> : révision des droits (les anciens droits ne s'additionnent pas aux nouveaux).</li>
<li><strong>Départ</strong> : désactivation immédiate ; les documents restent dans l'organisation.</li>
<li><strong>Revue périodique</strong> : au moins une fois par an, chaque responsable confirme les droits de son équipe.</li></ul>
<div class="lesson-practice"><p><strong>Exercice dans la démo</strong></p><p>Ouvrez la <a href="~/archiva360/demo-interactive/">démo interactive ARCHIVA360</a>. Changez de rôle (menu en haut à droite) entre « Archiviste » et « Employé » : observez quelles actions disparaissent. Puis ouvrez l'Audit trail pour voir vos changements de rôle tracés.</p></div>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Rôle + périmètre + confidentialité.</li><li>Moindre privilège, MFA à l'arrivée, désactivation immédiate au départ.</li><li>Revue des droits au moins annuelle.</li></ul></div>""",
            "quiz": [
                Q("Selon le principe du moindre privilège, un utilisateur reçoit…",
                  ["Tous les droits pour ne pas être bloqué", "Les droits strictement nécessaires à sa mission", "Les droits de son responsable", "Aucun droit"], 1,
                  "Juste ce qu'il faut, pas davantage."),
                Q("Quel rôle gère le plan de classement et les règles de conservation ?",
                  ["Records Manager", "Employé", "Utilisateur externe", "Auditeur"], 0,
                  "Le Records Manager porte les outils du records management."),
                Q("Lors d'un changement de poste, les nouveaux droits s'ajoutent aux anciens.", VF, 1,
                  "Les droits sont révisés : sinon l'utilisateur accumule des accès excessifs."),
                Q("Que faire au départ d'un salarié ?",
                  ["Désactiver son compte immédiatement", "Supprimer tous ses documents", "Laisser le compte actif un an", "Donner son mot de passe à un collègue"], 0,
                  "Désactivation immédiate ; les documents restent la propriété de l'organisation."),
            ],
        },
        {
            "title": "Paramétrer le classement et les règles", "minutes": 45,
            "html": """
<p>Le paramétrage traduit dans ARCHIVA360 les outils conçus avec l'archiviste : plan de classement, types de documents, métadonnées et règles de conservation.</p>
<h3>L'ordre de paramétrage</h3>
<ol><li><strong>Plan de classement</strong> : saisir les fonctions, activités et séries avec leurs codes.</li>
<li><strong>Types de documents</strong> : facture, contrat, procès-verbal… avec, pour chacun, la série par défaut.</li>
<li><strong>Métadonnées</strong> : pour chaque type, les champs obligatoires et facultatifs, avec des listes de valeurs.</li>
<li><strong>Règles de conservation</strong> : durée, événement déclencheur, sort final, responsable, fondement.</li>
<li><strong>Droits</strong> : qui accède à quelle série, à quel niveau de confidentialité.</li>
<li><strong>Workflows</strong> : circuits de validation et versement automatique en fin de circuit.</li></ol>
<h3>Versionner le paramétrage</h3>
<p>Le plan de classement et le référentiel de conservation évoluent. Chaque modification est datée, motivée et validée. Une règle de conservation modifiée ne doit pas raccourcir silencieusement la durée de documents déjà archivés : ARCHIVA360 trace chaque changement et signale les documents concernés.</p>
<h3>Tester avant de déployer</h3>
<p>Avant l'ouverture aux utilisateurs, testez chaque type de document avec des fichiers réels : la bonne série est-elle proposée ? Les métadonnées obligatoires sont-elles pertinentes ? La date d'échéance calculée est-elle juste ?</p>
<div class="lesson-practice"><p><strong>Exercice dans la démo</strong></p><p>Dans la <a href="~/archiva360/demo-interactive/">démo interactive</a>, ouvrez « Règles de conservation » et modifiez la durée des factures. Retournez dans « Documents » : l'échéance des factures a été recalculée. Vérifiez la trace dans l'Audit trail.</p></div>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Classement → types → métadonnées → règles → droits → workflows.</li><li>Paramétrage versionné et tracé.</li><li>Tester avec des documents réels avant d'ouvrir.</li></ul></div>""",
            "quiz": [
                Q("Que faut-il paramétrer en premier ?",
                  ["Le plan de classement", "Les workflows", "Les couleurs de l'interface", "Les notifications"], 0,
                  "Tout le reste s'appuie sur le plan de classement."),
                Q("Une modification de règle de conservation peut raccourcir silencieusement la durée de documents déjà archivés.", VF, 1,
                  "Chaque changement est tracé et les documents concernés sont signalés."),
                Q("Quels éléments font partie d'une règle de conservation dans ARCHIVA360 ?",
                  ["Durée", "Événement déclencheur", "Sort final", "Taille maximale du fichier"], [0, 1, 2],
                  "Durée, déclencheur, sort final (et responsable, fondement)."),
                Q("Pourquoi tester avec des documents réels avant le déploiement ?",
                  ["Pour vérifier séries, métadonnées et échéances", "Pour remplir la base", "Pour former l'IA", "Ce n'est pas utile"], 0,
                  "Le test révèle les métadonnées inadaptées et les erreurs de calcul d'échéance."),
            ],
        },
        {
            "title": "Sécurité, sauvegarde et reprise", "minutes": 40,
            "html": """
<p>L'administrateur est le gardien de la sécurité de la plateforme au quotidien.</p>
<h3>Sécuriser les accès</h3>
<ul><li><strong>Authentification multifacteur (MFA)</strong> obligatoire, au minimum pour les administrateurs, archivistes et accès au coffre-fort.</li>
<li><strong>Authentification unique (SSO)</strong> avec l'annuaire de l'organisation quand c'est possible : un départ désactive tous les accès d'un coup.</li>
<li><strong>Politique de mots de passe</strong> et durée de session adaptées.</li>
<li><strong>Coffre-fort (Archive Vault)</strong> pour les documents les plus sensibles, avec accès nominatifs et justifiés.</li></ul>
<h3>Surveiller</h3>
<p>Le <strong>Security Center</strong> affiche connexions, échecs, sessions, appareils, téléchargements inhabituels et droits excessifs. Un pic d'échecs de connexion ou un téléchargement massif doit déclencher une vérification.</p>
<h3>Sauvegarder et restaurer</h3>
<p>Règle 3-2-1, copie hors site, copie isolée. Mais surtout : <strong>tester la restauration</strong>. Une sauvegarde jamais restaurée est une hypothèse, pas une garantie. Fixez deux objectifs :</p>
<ul><li><strong>RPO</strong> (perte de données maximale admissible) : jusqu'à quel point dans le passé doit-on pouvoir revenir ? Par exemple, la veille au soir.</li>
<li><strong>RTO</strong> (durée maximale d'interruption) : en combien de temps doit-on être de nouveau opérationnel ? Par exemple, 4 heures.</li></ul>
<h3>Le plan de reprise</h3>
<p>Qui fait quoi en cas d'incident ? Qui décide, qui restaure, qui communique ? Le plan est écrit, connu et exercé au moins une fois par an.</p>
<div class="lesson-practice"><p><strong>Exercice dans la démo</strong></p><p>Dans la <a href="~/archiva360/demo-interactive/">démo interactive</a>, ouvrez « Sauvegarde » et exportez une sauvegarde complète. Supprimez un document de démonstration, puis restaurez la sauvegarde : le document revient, avec son empreinte d'origine.</p></div>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>MFA, SSO, coffre-fort, surveillance des anomalies.</li><li>3-2-1 et tests de restauration réguliers.</li><li>RPO, RTO et plan de reprise écrit et exercé.</li></ul></div>""",
            "quiz": [
                Q("Que mesure le RTO ?",
                  ["La durée maximale d'interruption admissible", "La perte de données maximale admissible", "Le nombre d'utilisateurs", "Le volume de stockage"], 0,
                  "RTO = temps de reprise ; RPO = point de reprise (perte de données)."),
                Q("Une sauvegarde qui n'a jamais été restaurée est une garantie suffisante.", VF, 1,
                  "Seul un test de restauration prouve que la sauvegarde est exploitable."),
                Q("Quels signaux du Security Center doivent alerter ?",
                  ["Un pic d'échecs de connexion", "Un téléchargement massif inhabituel", "Des droits excessifs", "Une connexion réussie habituelle"], [0, 1, 2],
                  "Les anomalies sont à vérifier ; une connexion normale ne l'est pas."),
                Q("Quel avantage apporte le SSO lors du départ d'un salarié ?",
                  ["Un seul geste désactive tous ses accès", "Il garde ses accès un an", "Il transfère ses fichiers", "Aucun"], 0,
                  "Le compte central désactivé coupe tous les accès liés."),
            ],
        },
        {
            "title": "Exploiter et piloter la plateforme", "minutes": 40,
            "html": """
<p>Une plateforme d'archivage se pilote avec quelques indicateurs suivis régulièrement.</p>
<h3>Le tableau de bord</h3>
<p>Volume de documents, documents archivés, stockage utilisé, documents à échéance, workflows en attente, alertes de sécurité. L'administrateur le consulte chaque semaine et le présente à la direction chaque trimestre.</p>
<h3>Le Retention Center</h3>
<p>Il liste les documents qui arrivent à échéance. Le processus : filtrer par série → vérifier les gels juridiques → faire valider par le responsable → appliquer le sort final → générer le certificat d'élimination. <strong>Aucune élimination n'est automatique.</strong></p>
<h3>Le Compliance Center</h3>
<p>Il signale les écarts : documents sans métadonnées obligatoires, utilisateurs avec des droits excessifs, sauvegardes non vérifiées, contrôles d'intégrité en échec. Chaque écart devient une action avec un responsable et une date.</p>
<h3>L'audit trail</h3>
<p>Qui, quoi, quand, depuis où, quelle action : le journal sert aux enquêtes internes, aux audits externes et à la preuve. L'administrateur sait l'interroger (par utilisateur, par document, par période) et l'exporter pour un auditeur.</p>
<h3>Les indicateurs d'activité</h3>
<p>Pages numérisées, documents archivés, recherches effectuées, délai moyen des workflows, taux d'erreur OCR, disponibilité de la plateforme. Ce sont aussi les indicateurs qui démontrent la valeur du projet à la direction.</p>
<div class="lesson-practice"><p><strong>Exercice dans la démo</strong></p><p>Dans la <a href="~/archiva360/demo-interactive/">démo interactive</a>, ouvrez le Retention Center. Placez un document sous gel juridique, puis essayez de l'éliminer : la plateforme refuse. Levez le gel, éliminez-le en tant qu'Archiviste, et retrouvez le certificat d'élimination dans l'Audit trail.</p></div>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Tableau de bord hebdomadaire, bilan trimestriel à la direction.</li><li>Retention Center : jamais d'élimination automatique.</li><li>Compliance Center : chaque écart devient une action.</li></ul></div>""",
            "quiz": [
                Q("Dans le Retention Center, les documents arrivés à échéance sont éliminés automatiquement.", VF, 1,
                  "Aucune élimination n'est automatique : vérification, validation, puis action tracée."),
                Q("Que faut-il vérifier avant d'éliminer un document arrivé à échéance ?",
                  ["L'absence de gel juridique", "La validation du responsable habilité", "La couleur du dossier", "La taille du fichier"], [0, 1],
                  "Gel juridique et validation : deux conditions indispensables."),
                Q("Quel outil signale les documents sans métadonnées obligatoires ?",
                  ["Le Compliance Center", "Le moteur de recherche", "La messagerie", "Le scanner"], 0,
                  "Le Compliance Center centralise les écarts de conformité."),
                Q("À quoi sert l'export de l'audit trail ?",
                  ["À fournir des preuves à un auditeur", "À supprimer des documents", "À changer de rôle", "À numériser"], 0,
                  "Le journal exporté documente les opérations pour un audit."),
            ],
        },
    ],
    "exam_extra": [
        Q("Un auditeur a besoin de droits de modification sur les documents qu'il contrôle.", VF, 1,
          "Lecture contrôlée et accès au journal suffisent."),
        Q("Que signifie RPO ?",
          ["La perte de données maximale admissible", "Le temps de reprise", "Le nombre de rôles", "La politique de mots de passe"], 0,
          "Le RPO définit jusqu'où l'on doit pouvoir revenir dans le passé."),
        Q("Après la désactivation du compte d'un salarié parti, ses documents…",
          ["Restent dans l'organisation", "Sont supprimés", "Lui sont envoyés", "Deviennent publics"], 0,
          "Les documents appartiennent à l'organisation."),
        Q("Le plan de reprise d'activité doit être exercé au moins une fois par an.", VF, 0,
          "Un plan jamais exercé ne fonctionne pas le jour de l'incident."),
    ],
}
