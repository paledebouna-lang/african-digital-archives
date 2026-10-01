"""ARCHIVA Academy — Parcours dirigeant (12 semaines), semaines 1 à 6.

Chaque semaine suit la même architecture pédagogique :
enjeu pour la direction → notions → étude de cas → questions à poser à ses équipes →
à retenir → livrable de la semaine → pour aller plus loin.
"""
from .academy_n1_n2 import Q, VF


def case(title, body):
    return f'<div class="lesson-case"><p><strong>Étude de cas — {title}</strong></p>{body}</div>'


def ask(items):
    return ('<div class="lesson-questions"><p><strong>Les questions à poser à vos équipes</strong></p><ol>'
            + "".join(f"<li>{i}</li>" for i in items) + "</ol></div>")


def key(items):
    return '<div class="lesson-key"><p><strong>À retenir</strong></p><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"


def deliverable(text):
    return f'<div class="lesson-practice"><p><strong>Livrable de la semaine</strong></p>{text}</div>'


def further(items):
    return ('<div class="lesson-ref"><p><strong>Pour aller plus loin</strong></p><ul>'
            + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>")


W1 = {
    "title": "L'information, actif stratégique et preuve de l'organisation", "minutes": 60,
    "html": """
<p class="lead">Un dirigeant ne gère pas des documents : il gère des <strong>droits, des obligations et des décisions</strong>. Les archives en sont la trace. Cette première semaine installe la grille de lecture que nous utiliserons pendant tout le parcours : l'information d'activité est un actif, elle porte un risque, et elle se gouverne.</p>
<h3>1. Trois fonctions que rien d'autre ne remplit</h3>
<p>Les archivistes distinguent trois valeurs du document d'activité. Pour une direction, elles se traduisent en trois fonctions concrètes :</p>
<table><thead><tr><th>Valeur</th><th>Ce qu'elle permet à la direction</th><th>Exemple</th></tr></thead><tbody>
<tr><td><b>Preuve</b></td><td>Défendre un droit, s'acquitter d'une obligation, répondre à un contrôle</td><td>Produire en 48 heures le contrat signé et ses avenants face à un contentieux fournisseur</td></tr>
<tr><td><b>Gestion</b></td><td>Décider sur des faits plutôt que sur des souvenirs</td><td>Retrouver les conditions négociées il y a cinq ans avant de renouveler un marché</td></tr>
<tr><td><b>Mémoire</b></td><td>Transmettre, capitaliser, raconter l'histoire de l'institution</td><td>Les délibérations fondatrices d'une université, les plans d'origine d'un ouvrage</td></tr></tbody></table>
<p>Un même document cumule souvent ces valeurs, et elles évoluent dans le temps : une facture est d'abord un outil de gestion, puis une pièce de preuve pendant le délai légal, puis, sauf exception, elle n'a plus de valeur et doit être éliminée.</p>
<h3>2. Le document d'activité n'est pas une simple information</h3>
<p>La norme internationale ISO 15489 parle de <em>records</em>, traduit par « documents d'activité » : des informations créées, reçues et conservées <strong>comme preuve et comme actif</strong> par une organisation, dans l'exercice de ses obligations légales ou de ses activités. Quatre qualités les distinguent d'un simple fichier :</p>
<ul><li><strong>Authenticité</strong> : le document est bien ce qu'il prétend être, produit par qui il prétend l'avoir été, au moment indiqué ;</li>
<li><strong>Fiabilité</strong> : son contenu représente fidèlement l'opération qu'il atteste ;</li>
<li><strong>Intégrité</strong> : il est complet et n'a pas été altéré ;</li>
<li><strong>Exploitabilité</strong> : on peut le localiser, le lire et l'interpréter.</li></ul>
<p>Retenez cette idée-force : <strong>un document que l'on ne peut pas retrouver, ou dont on ne peut pas prouver qu'il n'a pas été modifié, a perdu l'essentiel de sa valeur</strong>, même s'il existe quelque part sur un serveur.</p>
<h3>3. Lire l'archivage comme un risque</h3>
<p>Le langage du conseil d'administration est celui du risque. Les défaillances documentaires se rangent en cinq familles :</p>
<ol><li><b>Risque juridique</b> : impossibilité de prouver, conservation trop courte (preuve perdue) ou trop longue (données personnelles conservées sans justification).</li>
<li><b>Risque financier</b> : redressement fiscal faute de pièces justificatives, pénalités, doublons de paiement.</li>
<li><b>Risque opérationnel</b> : temps perdu à chercher, décisions prises sur des versions périmées, dépendance à la mémoire de quelques personnes.</li>
<li><b>Risque de sécurité</b> : fuite de documents confidentiels, rançongiciel, perte d'un support unique.</li>
<li><b>Risque de réputation et de mémoire</b> : patrimoine détruit, incapacité à rendre compte aux citoyens, aux bailleurs ou aux actionnaires.</li></ol>
<p>Un dirigeant n'a pas besoin de maîtriser la technique de chacune de ces familles. Il doit savoir <strong>qui en est responsable, comment elles sont mesurées et quel niveau de risque il accepte</strong>.</p>
""" + case("le départ d'une directrice financière", """
<p>Dans un établissement public d'Abidjan, la directrice financière part à la retraite. Trois mois plus tard, un contrôle porte sur un financement reçu quatre ans auparavant. Les pièces existent : une partie dans des classeurs de son bureau, une partie dans sa messagerie, désactivée à son départ, une partie sur une clé USB introuvable. L'établissement met six semaines à reconstituer un dossier incomplet.</p>
<p><em>Analyse.</em> Aucun document n'a été « perdu » au sens strict. C'est l'organisation qui n'avait jamais décidé où les documents de preuve devaient vivre, ni sous la responsabilité de qui. Le problème n'était pas technique : il relevait de la gouvernance.</p>""") + ask([
        "Quels sont nos dix documents les plus critiques (preuve de propriété, contrats majeurs, autorisations, statuts) et où sont leurs originaux ?",
        "Combien de temps nous faut-il pour produire un dossier complet en cas de contrôle ou de contentieux ?",
        "Que se passe-t-il pour les documents d'un collaborateur qui quitte l'organisation ?",
        "Qui, aujourd'hui, est responsable de nos archives ? Cette responsabilité est-elle écrite ?",
    ]) + key([
        "Une archive se définit par son lien avec une activité, non par son âge ou son support.",
        "Authenticité, fiabilité, intégrité, exploitabilité : sans elles, le document perd sa valeur de preuve.",
        "Pour la direction, l'archivage se pilote comme un risque : juridique, financier, opérationnel, sécurité, réputation.",
    ]) + deliverable("<p>Rédigez une note d'une page : « Nos cinq risques documentaires majeurs ». Pour chacun : un exemple vécu ou plausible, l'impact estimé, et la personne qui devrait en être responsable.</p>") + further([
        "ISO 15489-1:2016 — Information et documentation, gestion des documents d'activité : concepts et principes.",
        "ARCHIVA Academy, niveau 1, module 1 : « Qu'est-ce qu'une archive ? ».",
    ]),
    "quiz": [
        Q("Selon l'ISO 15489, qu'est-ce qui distingue un document d'activité d'un simple fichier ?",
          ["Son ancienneté", "Il est conservé comme preuve et comme actif de l'organisation", "Il est imprimé sur papier", "Il est stocké sur un serveur"], 1,
          "Le document d'activité est créé, reçu et conservé comme preuve et comme actif, dans l'exercice des activités de l'organisation."),
        Q("Quelles sont les quatre qualités d'un document d'activité ?",
          ["Authenticité", "Fiabilité", "Intégrité", "Exploitabilité", "Ancienneté"], [0, 1, 2, 3],
          "Authenticité, fiabilité, intégrité et exploitabilité. L'ancienneté n'en fait pas partie."),
        Q("Dans l'étude de cas, la cause principale de la crise était technique.", VF, 1,
          "Non : les documents existaient. Personne n'avait décidé où ils devaient être conservés ni sous quelle responsabilité. C'est une défaillance de gouvernance."),
        Q("Conserver des documents trop longtemps ne présente aucun risque.", VF, 1,
          "Faux : conserver des données personnelles au-delà de ce qui est justifié est un risque juridique, et tout ce qui est conservé peut être exigé lors d'un contentieux."),
    ],
}

W2 = {
    "title": "GED, GEC, SAE : comprendre ce que l'on achète", "minutes": 60,
    "html": """
<p class="lead">Les éditeurs utilisent un vocabulaire foisonnant, souvent à dessein. Un dirigeant qui confond GED et SAE risque d'acheter un outil de partage de fichiers en croyant acquérir un système de preuve. Cette semaine, vous apprenez à reconnaître chaque brique et la question à laquelle elle répond.</p>
<h3>1. Quatre briques, quatre questions</h3>
<table><thead><tr><th>Brique</th><th>Question à laquelle elle répond</th><th>Fonctions caractéristiques</th></tr></thead><tbody>
<tr><td><b>GEC</b> — gestion électronique du courrier</td><td>Qui a reçu quoi, quand, et qui doit répondre ?</td><td>Enregistrement à l'arrivée, numérisation, attribution, relances, suivi des délais de réponse</td></tr>
<tr><td><b>GED</b> — gestion électronique des documents</td><td>Comment travaillons-nous ensemble sur nos documents vivants ?</td><td>Stockage, versions, recherche, droits d'accès, circuits de validation</td></tr>
<tr><td><b>Records management</b></td><td>Quels documents ont valeur de preuve, combien de temps les garder, et que faire ensuite ?</td><td>Plan de classement, référentiel de conservation, gel juridique, sort final</td></tr>
<tr><td><b>SAE</b> — système d'archivage électronique</td><td>Comment garantir qu'un document figé restera intègre, lisible et prouvable pendant des décennies ?</td><td>Versement, empreintes, horodatage, journal d'audit, contrôle d'intégrité, préservation des formats</td></tr></tbody></table>
<h3>2. La distinction décisive : document vivant, document figé</h3>
<p>La GED gère des documents <strong>qui évoluent</strong> : on les modifie, on les commente, on en crée des versions. Le SAE gère des documents <strong>qui ne doivent plus évoluer</strong> : un contrat signé, une délibération adoptée, une paie clôturée. Le passage de l'un à l'autre s'appelle le <em>versement</em>. Au versement, le document est figé, son empreinte numérique est calculée, sa durée de conservation lui est appliquée, et toute action ultérieure est tracée.</p>
<p>Une GED, même excellente, n'apporte pas ces garanties par défaut : un administrateur peut y modifier ou supprimer un document sans laisser de trace exploitable. C'est pourquoi la question « votre solution est-elle un SAE ? » doit toujours être suivie de : « montrez-moi le journal d'audit et le contrôle d'intégrité ».</p>
<h3>3. Les fausses équivalences fréquentes</h3>
<ul><li><b>« Nous avons un serveur partagé, donc une GED. »</b> Un serveur de fichiers n'a ni métadonnées, ni versions maîtrisées, ni recherche plein texte, ni traçabilité.</li>
<li><b>« Tout est dans le cloud, donc archivé. »</b> Un service de stockage en ligne sauvegarde des fichiers ; il ne gère ni la durée de conservation, ni la preuve, ni la pérennité des formats.</li>
<li><b>« Nous avons numérisé, donc nous avons archivé. »</b> La numérisation produit des images ; sans classement, métadonnées et règles, elle produit surtout un désordre numérique.</li>
<li><b>« Le PDF est un format d'archivage. »</b> Seul le PDF/A, profil normalisé (ISO 19005), est conçu pour la conservation à long terme.</li></ul>
<h3>4. L'architecture cible, en une phrase</h3>
<p>Le courrier entre par la GEC, le travail collaboratif se fait dans la GED, les règles de records management décident de ce qui a valeur de preuve, et le SAE garantit cette preuve dans la durée. ARCHIVA360 réunit ces briques dans une même plateforme, mais la distinction conceptuelle demeure : elle structure votre cahier des charges et vos responsabilités.</p>
""" + case("le marché mal qualifié", """
<p>Une société d'assurance publie un appel d'offres pour « une solution d'archivage électronique ». Elle retient l'offre la moins chère : un outil de partage documentaire, très ergonomique. Deux ans plus tard, un litige oppose la société à un assuré qui conteste la date d'un avenant. Le fichier existe, mais il a été ouvert et réenregistré plusieurs fois ; aucune empreinte, aucun journal ne permet de démontrer qu'il n'a pas été modifié.</p>
<p><em>Analyse.</em> Le besoin exprimé était un SAE ; le cahier des charges n'en décrivait pas les exigences (versement, intégrité, journal, conservation). Le marché a été attribué sur le prix d'un produit qui ne répondait pas au risque.</p>""") + ask([
        "Pour chacun de nos outils actuels, est-ce une GEC, une GED, un SAE ou rien de tout cela ?",
        "Nos documents engageants (contrats, délibérations, paies) sont-ils figés quelque part, avec une empreinte et un journal ?",
        "Un administrateur informatique peut-il supprimer un document sans laisser de trace ?",
        "Notre cahier des charges distingue-t-il les exigences de GED et celles de SAE ?",
    ]) + key([
        "GEC : le courrier. GED : les documents vivants. Records management : les règles. SAE : la preuve dans la durée.",
        "Le versement fige le document : empreinte, règle de conservation, traçabilité.",
        "Serveur partagé, cloud et numérisation ne sont pas de l'archivage.",
    ]) + deliverable("<p>Dressez la cartographie de vos outils documentaires actuels (messagerie, serveurs, logiciels métiers, cloud, armoires) et classez chacun dans l'une des quatre briques, ou dans « aucune ». Les cases vides de la cartographie dessinent votre besoin.</p>") + further([
        "ISO 14641:2018 — Archivage électronique : conception et exploitation d'un système d'information pour la conservation de documents électroniques.",
        "ISO 19005 — PDF/A, format de fichier pour la conservation à long terme.",
        "ARCHIVA Academy, niveau 2 (Gestion documentaire) et niveau 4, module 1 (« Du document vivant à l'archive : le SAE »).",
    ]),
    "quiz": [
        Q("Quelle brique garantit qu'un document figé restera intègre et prouvable pendant des décennies ?",
          ["La GEC", "La GED", "Le SAE", "Le serveur de fichiers"], 2,
          "Le SAE assure la conservation probante : empreintes, journal d'audit, contrôle d'intégrité, préservation."),
        Q("Que se passe-t-il au moment du versement d'un document dans le SAE ?",
          ["Il est figé", "Son empreinte est calculée", "Sa durée de conservation lui est appliquée", "Il devient modifiable par tous"], [0, 1, 2],
          "Le document est figé, son empreinte calculée, sa règle de conservation appliquée ; toute action ultérieure est tracée."),
        Q("Un document au format PDF est, par nature, un document d'archivage à long terme.", VF, 1,
          "Seul le profil PDF/A (ISO 19005) est conçu pour la conservation à long terme."),
        Q("Dans l'étude de cas, quelle était l'erreur décisive ?",
          ["Un cahier des charges qui ne décrivait pas les exigences d'un SAE", "Le choix d'un éditeur étranger", "L'absence de scanner", "Un nombre insuffisant d'utilisateurs"], 0,
          "Le besoin réel était probatoire ; faute d'exigences SAE dans le cahier des charges, l'outil retenu ne couvrait pas le risque."),
    ],
}

W3 = {
    "title": "Gouverner l'information : le records management", "minutes": 60,
    "html": """
<p class="lead">Le records management est l'ensemble des décisions et des contrôles qui font qu'une organisation crée les bons documents, les conserve le temps nécessaire et s'en sépare de manière maîtrisée. C'est d'abord un <strong>dispositif de gouvernance</strong>, et c'est à ce titre qu'il relève de la direction.</p>
<h3>1. Le système de gestion des documents d'activité</h3>
<p>La norme ISO 30301 applique au records management la logique des systèmes de management bien connue des dirigeants (qualité ISO 9001, sécurité ISO/IEC 27001) : <strong>une politique, des responsabilités, des objectifs, des processus, une évaluation et une amélioration continue</strong>. Elle peut faire l'objet d'une certification. Son intérêt pour vous est moins le certificat que la méthode : on ne « fait » pas du records management, on le pilote.</p>
<h3>2. Les quatre décisions qui reviennent à la direction</h3>
<ol><li><b>Adopter une politique</b>. Un texte court, signé au plus haut niveau, qui affirme que les documents d'activité appartiennent à l'organisation et non aux individus, qu'ils sont gérés selon des règles communes, et qui désigne les responsables.</li>
<li><b>Nommer un responsable</b> doté d'un mandat transversal : le records manager ou l'archiviste en chef. Rattaché trop bas, il ne pourra rien imposer aux directions métiers.</li>
<li><b>Répartir les rôles</b> : chaque direction est propriétaire de ses documents (elle décide de leur contenu), le records manager définit les règles, la DSI fournit les outils, le juriste valide les durées, l'audit interne contrôle.</li>
<li><b>Arbitrer les conflits</b> : entre l'envie de tout garder et l'obligation d'éliminer, entre la transparence et la confidentialité, entre l'urgence opérationnelle et la discipline documentaire.</li></ol>
<h3>3. La matrice des responsabilités</h3>
<table><thead><tr><th>Activité</th><th>Direction générale</th><th>Directions métiers</th><th>Records manager</th><th>DSI</th><th>Juridique</th></tr></thead><tbody>
<tr><td>Politique documentaire</td><td>Approuve</td><td>Consultées</td><td>Rédige</td><td>Consultée</td><td>Consulté</td></tr>
<tr><td>Plan de classement</td><td>—</td><td>Contribuent</td><td>Conçoit et maintient</td><td>Paramètre</td><td>—</td></tr>
<tr><td>Durées de conservation</td><td>Arbitre</td><td>Proposent</td><td>Coordonne</td><td>—</td><td>Valide</td></tr>
<tr><td>Élimination</td><td>Autorise les cas sensibles</td><td>Visent</td><td>Exécute et documente</td><td>Supprime techniquement</td><td>Vérifie l'absence de gel</td></tr>
<tr><td>Sécurité et accès</td><td>Fixe l'appétence au risque</td><td>Désignent les ayants droit</td><td>Définit les niveaux</td><td>Met en œuvre</td><td>—</td></tr></tbody></table>
<h3>4. Le principe de « capture » : agir au moment où le document naît</h3>
<p>L'erreur la plus coûteuse est de traiter l'archivage en fin de chaîne, quand les documents s'accumulent. Le records management moderne agit <strong>à la création</strong> : le document est enregistré dans le bon dossier, avec ses métadonnées, dès qu'il engage l'organisation. Chaque processus métier (achats, recrutement, contentieux, marchés) doit indiquer quels documents il produit et à quel moment ils deviennent des documents d'activité.</p>
""" + case("la politique qui n'a jamais quitté le tiroir", """
<p>Un ministère technique adopte en grande pompe une politique d'archivage de quarante pages. Aucun responsable n'est nommé, aucun budget n'est prévu, aucun indicateur n'est suivi. Trois ans plus tard, l'audit constate que rien n'a changé.</p>
<p><em>Analyse.</em> Une politique sans responsable, sans moyens et sans mesure n'est qu'une déclaration d'intention. Une politique de deux pages, portée par un responsable mandaté et évaluée chaque année en comité de direction, aurait eu plus d'effet.</p>""") + ask([
        "Avons-nous une politique documentaire signée ? Quand a-t-elle été évaluée pour la dernière fois ?",
        "Qui est notre records manager ? À qui rend-il compte ? Quel est son mandat écrit ?",
        "Nos processus métiers indiquent-ils quels documents ils produisent et où ceux-ci sont enregistrés ?",
        "Comment la question documentaire remonte-t-elle au comité de direction ?",
    ]) + key([
        "Le records management est un système de management : politique, rôles, processus, évaluation, amélioration.",
        "Quatre décisions relèvent de la direction : politique, responsable, répartition des rôles, arbitrages.",
        "Les documents appartiennent à l'organisation, pas aux individus.",
        "On gère le document à sa création, pas quand les cartons débordent.",
    ]) + deliverable("<p>Rédigez le projet de politique documentaire de votre organisation en deux pages maximum : objet, principes (cinq au plus), responsabilités, révision annuelle. Ce texte sera enrichi au fil du parcours.</p>") + further([
        "ISO 30301:2019 — Systèmes de gestion des documents d'activité : exigences.",
        "ISO 15489-1:2016, chapitres sur la politique et les responsabilités.",
        "ARCHIVA Academy, niveau 3, module 1 : « Les principes de l'ISO 15489 ».",
    ]),
    "quiz": [
        Q("Quelle norme applique au records management la logique d'un système de management certifiable ?",
          ["ISO 30301", "ISO 19005", "ISO 9660", "ISO 4217"], 0,
          "L'ISO 30301 fixe les exigences d'un système de gestion des documents d'activité, sur le modèle de l'ISO 9001."),
        Q("Quelles décisions relèvent de la direction générale ?",
          ["Adopter la politique documentaire", "Nommer un responsable mandaté", "Paramétrer les métadonnées dans l'outil", "Arbitrer les conflits entre conservation et élimination"], [0, 1, 3],
          "Le paramétrage relève de la DSI et du records manager. Politique, nomination et arbitrages relèvent de la direction."),
        Q("Selon le principe de capture, le meilleur moment pour gérer un document est…",
          ["Au moment où il est créé ou reçu et engage l'organisation", "Quand l'armoire est pleine", "Au départ en retraite de son auteur", "Lors d'un audit"], 0,
          "Agir à la création évite l'accumulation et garantit que le document est classé avec ses métadonnées."),
        Q("Dans la matrice des responsabilités, la validation juridique des durées de conservation revient à la DSI.", VF, 1,
          "Les durées sont proposées par les métiers, coordonnées par le records manager et validées par le juridique ; la direction arbitre."),
    ],
}

W4 = {
    "title": "Plan de classement et métadonnées : l'investissement invisible", "minutes": 60,
    "html": """
<p class="lead">Les projets documentaires qui échouent ont presque tous le même point commun : un outil installé sur un classement improvisé. Le plan de classement et les métadonnées ne se voient pas dans une démonstration commerciale. Ce sont pourtant eux qui déterminent si, dans cinq ans, vos équipes trouveront ce qu'elles cherchent.</p>
<h3>1. Classer par fonctions, pas par organigramme</h3>
<p>Un plan de classement organise les documents selon <strong>ce que fait l'organisation</strong> (ses fonctions et activités) plutôt que selon <strong>qui le fait</strong> (ses services). La raison est simple : les organigrammes changent à chaque réorganisation, les fonctions demeurent. « Gérer les ressources humaines / Recruter / Dossiers de recrutement » reste valable que le recrutement dépende de la DRH, d'un pôle mutualisé ou d'une filiale.</p>
<p>Un bon plan compte rarement plus de trois ou quatre niveaux et quelques centaines de rubriques. À chaque rubrique terminale sont rattachés une durée de conservation, un sort final et un niveau de confidentialité : <strong>le plan de classement devient ainsi le support de toutes les règles</strong>.</p>
<h3>2. Les métadonnées : ce que l'on sait du document</h3>
<p>Une métadonnée est une information sur le document : son type, sa date, son auteur, l'affaire ou le tiers concerné, son niveau de confidentialité, sa règle de conservation. Elles remplissent trois rôles :</p>
<ul><li><b>Retrouver</b> : « toutes les factures du fournisseur X supérieures à 5 millions FCFA en 2024 » est une requête sur des métadonnées, pas sur des noms de fichiers ;</li>
<li><b>Gouverner</b> : la date de clôture d'un dossier déclenche le calcul de sa durée de conservation ;</li>
<li><b>Prouver</b> : qui a créé, validé, versé, consulté le document, et quand.</li></ul>
<h3>3. La règle d'économie</h3>
<p>Chaque métadonnée demandée à un utilisateur a un coût : du temps, de l'agacement, des erreurs. L'art consiste à exiger <strong>peu de métadonnées saisies</strong> (trois à cinq par type de document) et à obtenir <strong>beaucoup de métadonnées déduites</strong> : héritées du dossier, extraites automatiquement par OCR et intelligence artificielle, renseignées par le système (dates, auteur, empreinte). Un dirigeant doit se méfier de deux excès : le formulaire de vingt champs que personne ne remplira, et l'absence totale de structure au nom de la « recherche plein texte qui suffit ».</p>
<h3>4. Ce que la recherche plein texte ne fera jamais</h3>
<p>Le plein texte retrouve des mots, pas des concepts ni des statuts. Il ne sait pas si un contrat est en vigueur, si un dossier est clos, ni si un document est confidentiel. Il ne déclenche aucune règle. Il est indispensable, mais il complète les métadonnées sans les remplacer.</p>
""" + case("deux banques, deux classements", """
<p>Deux banques de la sous-région déploient la même solution la même année. La première calque son classement sur l'organigramme et laisse chaque agence nommer ses dossiers. La seconde consacre dix semaines à un plan de classement fonctionnel et à cinq métadonnées obligatoires par type de document. Après la fusion de deux directions, la première doit reclasser des centaines de milliers de documents ; la seconde ne change que des droits d'accès.</p>
<p><em>Analyse.</em> Les dix semaines « perdues » au départ ont été l'investissement le plus rentable du projet.</p>""") + ask([
        "Notre classement actuel suit-il nos fonctions ou notre organigramme ?",
        "Combien de métadonnées demandons-nous aux utilisateurs pour un contrat ? Combien sont réellement renseignées ?",
        "Nos règles de conservation sont-elles rattachées au plan de classement ?",
        "Qui est chargé de faire évoluer le plan de classement, et selon quelle procédure ?",
    ]) + key([
        "Classer par fonctions, qui durent, et non par services, qui changent.",
        "Le plan de classement porte les règles : durée, sort final, confidentialité.",
        "Peu de métadonnées saisies, beaucoup de métadonnées déduites.",
        "La recherche plein texte complète les métadonnées, elle ne les remplace pas.",
    ]) + deliverable("<p>Esquissez les deux premiers niveaux du plan de classement de votre organisation : six à dix fonctions, et pour chacune trois à cinq activités. Soumettez-le à deux directeurs métiers et notez leurs objections.</p>") + further([
        "ISO 23081 — Métadonnées pour les documents d'activité.",
        "ARCHIVA Academy, niveau 3, modules 2 et 3 : « Construire un plan de classement » et « Les métadonnées ».",
    ]),
    "quiz": [
        Q("Pourquoi classer par fonctions plutôt que par services ?",
          ["Parce que les fonctions demeurent quand l'organigramme change", "Parce que c'est plus rapide à saisir", "Parce que la loi l'impose", "Parce que les services n'ont pas de documents"], 0,
          "Les fonctions sont stables ; les organigrammes changent à chaque réorganisation."),
        Q("Quels sont les trois rôles des métadonnées ?",
          ["Retrouver", "Gouverner", "Prouver", "Décorer"], [0, 1, 2],
          "Elles permettent de retrouver, de déclencher les règles (gouverner) et de tracer (prouver)."),
        Q("Une bonne pratique consiste à exiger une vingtaine de métadonnées saisies par document pour être exhaustif.", VF, 1,
          "Au contraire : trois à cinq métadonnées saisies par type de document, le reste étant hérité, extrait ou généré par le système."),
        Q("La recherche plein texte permet, à elle seule, de savoir si un contrat est en vigueur et de lui appliquer une durée de conservation.", VF, 1,
          "Le plein texte retrouve des mots ; les statuts et les règles reposent sur des métadonnées."),
    ],
}

W5 = {
    "title": "Durées de conservation et sort final : décider ce que l'on garde", "minutes": 60,
    "html": """
<p class="lead">Tout garder est la politique la plus répandue. C'est aussi l'une des plus coûteuses et des plus risquées. Décider de ce que l'on garde, combien de temps et ce que l'on en fait ensuite est un acte de gestion que la direction doit assumer, sur la base de règles écrites.</p>
<h3>1. Le référentiel de conservation</h3>
<p>Le référentiel (ou tableau de gestion) indique, pour chaque type de document, <strong>la durée d'utilité administrative (DUA)</strong>, le <strong>point de départ</strong> de cette durée et le <strong>sort final</strong>. Il se construit à partir de trois sources :</p>
<ol><li><b>Les obligations légales et réglementaires</b>. Exemple : dans l'espace OHADA, l'Acte uniforme relatif au droit comptable et à l'information financière impose de conserver les livres comptables et les pièces justificatives pendant dix ans.</li>
<li><b>Les délais de prescription</b> : tant qu'une action en justice est possible, la preuve doit rester disponible.</li>
<li><b>Le besoin de l'activité</b> : certaines informations restent utiles au-delà de toute obligation (plans d'un bâtiment pendant toute sa durée de vie, dossiers de carrière jusqu'à la liquidation de la retraite).</li></ol>
<p>La règle la plus longue l'emporte, à condition d'être justifiée. Chaque durée doit être <strong>documentée par sa source</strong> : c'est ce qui vous protégera devant un contrôleur ou un juge.</p>
<h3>2. Le point de départ, détail décisif</h3>
<p>« Dix ans » ne veut rien dire sans point de départ. Dix ans à compter de la création du document, de la clôture de l'exercice, de la fin du contrat ou du départ de l'agent ne produisent pas du tout le même résultat. Les durées attachées à un dossier courent généralement à compter de sa <strong>clôture</strong>, ce qui suppose que les dossiers soient effectivement clos.</p>
<h3>3. Les trois sorts finaux</h3>
<table><thead><tr><th>Sort final</th><th>Signification</th><th>Exemple</th></tr></thead><tbody>
<tr><td><b>Élimination</b></td><td>Destruction sécurisée et documentée</td><td>Pièces comptables courantes après le délai légal</td></tr>
<tr><td><b>Conservation définitive</b></td><td>Valeur historique ou probante permanente</td><td>Statuts, délibérations des organes de gouvernance, titres de propriété</td></tr>
<tr><td><b>Tri</b></td><td>Conservation d'un échantillon ou d'une sélection</td><td>Dossiers individuels dont on garde un échantillon représentatif</td></tr></tbody></table>
<h3>4. Le gel juridique</h3>
<p>Lorsqu'un litige, une enquête ou un contrôle est raisonnablement prévisible, les documents concernés doivent être <strong>soustraits à toute élimination</strong>, même si leur durée est échue. Détruire un document dans ces circonstances peut être interprété comme une volonté de faire disparaître une preuve. Le gel est décidé par le juridique, appliqué par le records manager et levé formellement à la fin de l'affaire.</p>
<h3>5. L'élimination, acte de gestion à part entière</h3>
<p>Une élimination maîtrisée suit quatre étapes : une <strong>proposition</strong> générée à partir du référentiel ; un <strong>visa</strong> du propriétaire métier et la vérification de l'absence de gel ; l'<strong>exécution</strong> sécurisée (broyage, effacement certifié) ; un <strong>certificat d'élimination</strong> conservé, lui, durablement. Pour les archives publiques, la réglementation nationale exige en général le visa de l'administration des archives.</p>
""" + case("le magasin saturé", """
<p>Une société industrielle loue chaque année de nouveaux mètres linéaires pour stocker ses cartons. Un inventaire révèle que 60 % des documents ont dépassé toute durée d'utilité, mais personne n'ose signer leur destruction : « on ne sait jamais ». Le coût du stockage, de l'assurance et des recherches dépasse celui d'un projet de records management complet.</p>
<p><em>Analyse.</em> L'absence de référentiel validé transforme chaque élimination en prise de risque personnelle. Le référentiel, approuvé par la direction et le juridique, transfère cette responsabilité à l'organisation et rend l'élimination routinière.</p>""") + ask([
        "Disposons-nous d'un référentiel de conservation écrit, validé par le juridique, avec les sources de chaque durée ?",
        "Nos dossiers sont-ils clos, de manière à faire courir les durées ?",
        "Quand avons-nous éliminé des documents pour la dernière fois ? Avec quel certificat ?",
        "Comment un gel juridique est-il déclenché, appliqué et levé chez nous ?",
    ]) + key([
        "Une durée de conservation se compose d'une durée, d'un point de départ et d'un sort final.",
        "Chaque durée doit être documentée par sa source : loi, prescription ou besoin de l'activité.",
        "Le gel juridique suspend toute élimination, même si la durée est échue.",
        "L'élimination est un acte documenté : proposition, visa, exécution, certificat.",
    ]) + deliverable("<p>Choisissez dix types de documents fréquents dans votre organisation. Pour chacun, renseignez : durée, point de départ, sort final, source de la règle. Faites valider les trois cas les plus délicats par votre juriste.</p>") + further([
        "Acte uniforme OHADA relatif au droit comptable et à l'information financière (AUDCIF), dispositions sur la conservation des documents comptables.",
        "ARCHIVA Academy, niveau 3, module 4 : « Conservation et sort final ».",
        "Démo interactive ARCHIVA360 : « Retention Center », gel juridique et certificat d'élimination.",
    ]),
    "quiz": [
        Q("Quels éléments composent une règle de conservation complète ?",
          ["Une durée", "Un point de départ", "Un sort final", "La couleur du classeur"], [0, 1, 2],
          "Durée, point de départ et sort final. Sans point de départ, la durée ne peut pas être calculée."),
        Q("Que doit-on faire d'un document dont la durée est échue mais qui concerne un litige prévisible ?",
          ["Le placer sous gel juridique et ne pas l'éliminer", "L'éliminer immédiatement", "Le renvoyer à son auteur", "Le numériser puis détruire l'original"], 0,
          "Le gel juridique suspend l'élimination tant que l'affaire n'est pas close."),
        Q("Dans l'espace OHADA, quelle durée de conservation l'AUDCIF fixe-t-il pour les livres comptables et pièces justificatives ?",
          ["Cinq ans", "Dix ans", "Trente ans", "Aucune durée"], 1,
          "L'Acte uniforme relatif au droit comptable impose une conservation de dix ans."),
        Q("Le certificat d'élimination peut être détruit en même temps que les documents qu'il concerne.", VF, 1,
          "Le certificat est la preuve que l'élimination a été régulière : il est conservé durablement."),
    ],
}

W6 = {
    "title": "Numériser : un projet industriel, pas une photocopie", "minutes": 60,
    "html": """
<p class="lead">La numérisation est souvent le premier projet visible d'une transformation documentaire, et celui qui coûte le plus quand il est mal conçu. La question n'est pas « combien coûte un scanner ? » mais « quels documents numériser, pour quel usage, avec quelle qualité et quelle valeur juridique ? ».</p>
<h3>1. Trois finalités, trois projets différents</h3>
<ul><li><b>Numériser pour consulter</b> : faciliter l'accès à des dossiers très demandés. On vise la rapidité et une bonne lisibilité ; l'original papier est conservé.</li>
<li><b>Numériser pour substituer</b> : remplacer l'original papier par une copie numérique, puis éliminer le papier. C'est possible seulement si la réglementation le permet pour ce type de document et si le processus garantit la fidélité de la copie (copie fiable, conditions de réalisation tracées). La décision relève de la direction, sur avis juridique.</li>
<li><b>Numériser pour préserver</b> : protéger des documents fragiles ou patrimoniaux en limitant leur manipulation. On vise la très haute qualité et la conservation de masters de référence.</li></ul>
<h3>2. Le coût réel d'une page numérisée</h3>
<p>Le passage au scanner ne représente qu'une fraction du coût. La chaîne complète comprend :</p>
<ol><li><b>la préparation</b> : désagrafage, défroissage, tri des pages et des doublons, souvent l'étape la plus longue ;</li>
<li><b>la numérisation</b> proprement dite ;</li>
<li><b>l'indexation</b> : rattachement au dossier, saisie ou extraction des métadonnées ;</li>
<li><b>le contrôle qualité</b> : échantillonnage, reprise des pages illisibles ;</li>
<li><b>la reconstitution</b> des dossiers papier et leur retour ou leur élimination ;</li>
<li><b>le versement</b> dans la GED ou le SAE, avec empreintes.</li></ol>
<p>Un devis qui ne détaille pas ces étapes est incomplet. Exigez un prix par étape et un taux d'erreur maximal contractuel.</p>
<h3>3. Qualité et OCR</h3>
<p>Une résolution de 300 points par pouce convient à la plupart des documents de bureau ; les documents anciens, les plans ou les photographies exigent davantage. La <strong>reconnaissance optique de caractères (OCR)</strong> rend le texte des images cherchable ; sa précision dépend de la qualité de l'original et de la langue. Elle n'est jamais parfaite : sur des documents dégradés, prévoyez une vérification humaine des métadonnées clés (montants, dates, noms).</p>
<h3>4. Prioriser : la matrice valeur / usage</h3>
<p>On ne numérise pas tout. On priorise selon deux axes : <strong>la valeur</strong> du document (preuve, risque, patrimoine) et <strong>sa fréquence d'usage</strong>. Les dossiers à forte valeur et fort usage passent en premier ; ceux à faible valeur et faible usage ne sont souvent jamais numérisés et vont directement au tri ou à l'élimination. Commencez aussi par arrêter le flux entrant : numériser le courrier du jour coûte bien moins cher que rattraper vingt ans de cartons.</p>
""" + case("trois millions de pages", """
<p>Une caisse de prévoyance décide de numériser l'intégralité de ses dossiers d'affiliés, soit environ trois millions de pages. Le premier prestataire, retenu sur le seul prix à la page, livre des images sans indexation fiable : personne ne retrouve rien. Le second marché découpe le projet en lots, impose un contrôle qualité par échantillonnage, une indexation sur le numéro d'affilié et un taux d'erreur contractuel. Il coûte plus cher à la page, mais il est le seul à produire de la valeur.</p>
<p><em>Analyse.</em> Le prix pertinent n'est pas celui de la page numérisée, mais celui de la page <strong>retrouvable</strong>.</p>""") + ask([
        "Pour chaque lot à numériser, quelle est la finalité : consulter, substituer ou préserver ?",
        "Notre devis détaille-t-il préparation, indexation, contrôle qualité et versement ?",
        "Avons-nous arrêté le flux entrant de papier avant de traiter le stock ?",
        "Avons-nous validé juridiquement les cas où l'original papier pourra être éliminé ?",
    ]) + key([
        "Consulter, substituer, préserver : trois finalités, trois cahiers des charges.",
        "Le scanner n'est qu'une étape : préparation, indexation et contrôle pèsent autant ou plus.",
        "Le bon indicateur est le coût de la page retrouvable, pas celui de la page numérisée.",
        "Arrêter le flux entrant avant de traiter le stock.",
    ]) + deliverable("<p>Classez vos principaux fonds documentaires dans une matrice valeur / usage (quatre cases). Déduisez-en les trois premiers lots à numériser, leur finalité et un ordre de grandeur des volumes.</p>") + further([
        "ARCHIVA Academy, niveau 2, module 3 : « Gérer le courrier (GEC) ».",
        "Blog ADA : « Numériser 3 millions de pages : la méthode ».",
        "Livre blanc ADA : « Numériser un fonds d'archives ».",
    ]),
    "quiz": [
        Q("Quelles sont les trois finalités possibles d'un projet de numérisation ?",
          ["Consulter", "Substituer", "Préserver", "Décorer"], [0, 1, 2],
          "Consulter, substituer ou préserver : chaque finalité appelle des exigences différentes."),
        Q("Le coût d'un projet de numérisation se limite essentiellement au passage au scanner.", VF, 1,
          "Préparation, indexation, contrôle qualité, reconstitution et versement représentent souvent l'essentiel du coût."),
        Q("Quel indicateur la leçon recommande-t-elle pour juger un projet de numérisation ?",
          ["Le coût de la page retrouvable", "Le nombre de scanners achetés", "La vitesse du scanner", "Le poids total des fichiers"], 0,
          "Une page numérisée mais non retrouvable n'a pas de valeur."),
        Q("Par quoi est-il généralement conseillé de commencer ?",
          ["Arrêter le flux entrant de papier", "Numériser les archives les plus anciennes", "Éliminer tous les originaux", "Acheter le scanner le plus rapide"], 0,
          "Traiter le flux du jour est bien moins coûteux que rattraper le stock, et empêche le problème de grossir."),
    ],
}

WEEKS_1_6 = [W1, W2, W3, W4, W5, W6]
