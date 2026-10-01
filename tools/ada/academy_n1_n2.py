"""ARCHIVA Academy — contenus des niveaux 1 et 2."""


def Q(q, options, answer, explain, kind=None):
    """Question. `answer` is an index or a list of indexes (multi)."""
    if kind is None:
        kind = "multi" if isinstance(answer, list) else ("tf" if options == ["Vrai", "Faux"] else "single")
    return {"q": q, "o": options, "a": answer if isinstance(answer, list) else [answer], "e": explain, "t": kind}


VF = ["Vrai", "Faux"]

N1 = {
    "num": 1, "slug": "niveau-1", "title": "Introduction à l'archivage",
    "audience": "Tous publics, aucun prérequis", "duration": "3 h",
    "intro": "Comprendre ce qu'est une archive, pourquoi elle compte et comment un document vit de sa création à son sort final.",
    "objectives": ["Définir une archive et ses trois valeurs : preuve, gestion, mémoire",
                   "Distinguer archives papier, numériques et hybrides",
                   "Expliquer le cycle de vie d'un document et la théorie des trois âges",
                   "Identifier les principaux risques qui menacent les archives d'une organisation"],
    "modules": [
        {
            "title": "Qu'est-ce qu'une archive ?", "minutes": 35,
            "html": """
<p>Dans le langage courant, « archives » évoque des cartons poussiéreux au fond d'une cave. Pour un archiviste, la définition est bien plus large : <strong>les archives sont l'ensemble des documents produits ou reçus par une personne ou une organisation dans l'exercice de son activité, quels que soient leur date, leur forme et leur support.</strong></p>
<p>Trois mots de cette définition méritent attention.</p>
<ul>
<li><strong>Produits ou reçus</strong> : une facture envoyée par un fournisseur est une archive de votre organisation au même titre que le contrat que vous avez rédigé.</li>
<li><strong>Dans l'exercice de son activité</strong> : c'est le lien avec une activité qui fait l'archive. Un magazine acheté pour la salle d'attente n'en est pas une ; le procès-verbal d'un conseil d'administration, si.</li>
<li><strong>Quels que soient leur date et leur support</strong> : un courriel d'hier est une archive, comme un registre de 1950. Un fichier Excel, une photo, un message vocal, une vidéo peuvent l'être.</li>
</ul>
<h3>Les trois valeurs d'une archive</h3>
<p><strong>La valeur de preuve.</strong> Une archive prouve un droit, une obligation ou un fait : un titre foncier prouve une propriété, un contrat de travail prouve un engagement, une quittance prouve un paiement.</p>
<p><strong>La valeur de gestion.</strong> L'organisation a besoin de ses documents pour travailler : retrouver le dernier avenant d'un contrat, consulter le dossier d'un client, préparer un budget à partir des comptes passés.</p>
<p><strong>La valeur de mémoire.</strong> Certaines archives racontent l'histoire d'une institution, d'une ville ou d'un pays. Les registres d'une mairie, les délibérations d'une université, les photographies d'un chantier deviennent un patrimoine.</p>
<h3>Archives publiques et archives privées</h3>
<p>Les archives produites par l'État, les collectivités et les établissements publics sont des <strong>archives publiques</strong> : elles obéissent à des règles particulières de conservation et de communication. Les archives d'une entreprise, d'une association ou d'une famille sont des <strong>archives privées</strong>, ce qui ne les dispense pas d'obligations légales (comptabilité, données personnelles, droit du travail).</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Une archive se définit par son lien avec une activité, pas par son âge ni son support.</li><li>Elle a une valeur de preuve, de gestion et parfois de mémoire.</li><li>Un document peut avoir plusieurs valeurs à la fois.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Choisissez cinq documents sur votre bureau ou dans votre messagerie. Pour chacun, indiquez s'il s'agit d'une archive de votre organisation et quelle valeur il porte : preuve, gestion ou mémoire.</p></div>""",
            "quiz": [
                Q("Lequel de ces éléments correspond le mieux à la définition d'une archive ?",
                  ["Un document de plus de 30 ans", "Un document produit ou reçu dans l'exercice d'une activité, quel que soit son support", "Un document papier rangé dans un carton", "Un document qui n'est plus utilisé"], 1,
                  "C'est le lien avec une activité qui fait l'archive, pas l'âge ni le support. Un courriel d'hier peut être une archive."),
                Q("Un courriel reçu d'un fournisseur pour confirmer une commande peut être une archive.", VF, 0,
                  "Oui : il est reçu dans le cadre d'une activité (les achats) et il peut servir de preuve."),
                Q("Quelles sont les trois valeurs d'une archive vues dans ce module ?",
                  ["Preuve", "Gestion", "Décoration", "Mémoire"], [0, 1, 3],
                  "Preuve, gestion et mémoire. Un même document peut les cumuler."),
                Q("Les archives d'une entreprise privée ne sont soumises à aucune obligation légale.", VF, 1,
                  "Faux : comptabilité, droit du travail, données personnelles, fiscalité imposent des règles de conservation aux organisations privées."),
            ],
        },
        {
            "title": "Archives papier, numériques et hybrides", "minutes": 30,
            "html": """
<p>Une organisation conserve aujourd'hui trois grandes familles d'archives. Les connaître est la première étape de tout projet.</p>
<h3>Les archives papier</h3>
<p>Contrats, factures, dossiers clients et fournisseurs, dossiers du personnel, courriers, rapports, procès-verbaux, registres, dossiers médicaux ou scolaires, actes administratifs, plans, cartes. Le papier reste majoritaire dans beaucoup d'administrations africaines. Ses ennemis : l'humidité, la chaleur, le feu, les insectes, les rongeurs, la lumière et les manipulations répétées.</p>
<h3>Les archives numériques</h3>
<p>PDF, documents Word, tableurs Excel, présentations, images, vidéos, fichiers audio, courriels, bases de données, fichiers comptables, RH ou techniques. Elles sont faciles à copier et à partager, mais aussi faciles à perdre : un disque qui tombe en panne, une clé USB égarée, un compte de messagerie supprimé au départ d'un salarié, une attaque par rançongiciel.</p>
<p>Elles ont un autre point faible : <strong>l'obsolescence</strong>. Un fichier n'est lisible qu'avec un logiciel capable de l'ouvrir. Dans vingt ans, certains formats d'aujourd'hui ne le seront plus.</p>
<h3>Les archives hybrides</h3>
<p>C'est le cas le plus courant : une partie du dossier existe sur papier, une autre sous forme numérique. Le dossier d'un agent contient l'original signé de son contrat, mais ses évaluations sont dans un logiciel RH et ses échanges dans une messagerie. Pour que le dossier soit complet, il faut savoir où se trouve chaque partie.</p>
<h3>Où se cachent les archives ?</h3>
<p>Un diagnostic révèle presque toujours des documents dispersés : armoires des bureaux, caves, ordinateurs personnels, clés USB, disques externes, serveurs partagés, messageries, groupes WhatsApp. Cette dispersion entraîne des doublons, des documents introuvables et des documents confidentiels accessibles à trop de personnes.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Papier, numérique et hybride : une bonne gestion couvre les trois.</li><li>Le numérique a deux faiblesses : la perte et l'obsolescence des formats.</li><li>La dispersion est le premier problème à résoudre.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Listez tous les endroits où votre service conserve des documents : armoires, serveur, messageries, téléphones… Pour chacun, estimez le volume et qui y a accès.</p></div>""",
            "quiz": [
                Q("Un dossier dont le contrat original est sur papier et les évaluations dans un logiciel est un dossier…",
                  ["Papier", "Numérique", "Hybride", "Incomplet par définition"], 2,
                  "Une partie papier et une partie numérique : c'est un dossier hybride, le cas le plus fréquent."),
                Q("Quelles sont les deux grandes faiblesses des archives numériques citées dans ce module ?",
                  ["La perte (panne, suppression, attaque)", "Le poids des cartons", "L'obsolescence des formats", "Les insectes"], [0, 2],
                  "Le numérique se perd facilement et peut devenir illisible quand un format devient obsolète."),
                Q("Les groupes WhatsApp peuvent contenir des documents d'activité qu'il faut prendre en compte.", VF, 0,
                  "Oui : tout document reçu ou produit dans une activité est une archive, y compris sur une messagerie instantanée."),
                Q("Lequel de ces facteurs n'est PAS un ennemi du papier ?",
                  ["L'humidité", "La lumière", "Les insectes", "La compression de fichier"], 3,
                  "La compression concerne les fichiers numériques. Humidité, lumière et insectes dégradent le papier."),
            ],
        },
        {
            "title": "Le cycle de vie des documents", "minutes": 40,
            "html": """
<p>Un document ne garde pas la même utilité toute sa vie. La <strong>théorie des trois âges</strong>, formulée par l'archiviste français Yves Pérotin en 1961, décrit ce parcours. Elle reste la base de l'organisation de l'archivage dans le monde francophone.</p>
<h3>Premier âge : les archives courantes (ou actives)</h3>
<p>Le document est utilisé régulièrement pour le travail quotidien : un contrat en cours, un dossier client actif, la comptabilité de l'exercice. Il reste dans le service, au plus près de ceux qui l'utilisent.</p>
<h3>Deuxième âge : les archives intermédiaires (ou semi-actives)</h3>
<p>Le document n'est plus utilisé tous les jours, mais il doit être conservé pour des raisons administratives ou juridiques : un contrat terminé qui pourrait faire l'objet d'un litige, les comptes des exercices passés. Il peut être déplacé dans un local d'archives ou un espace d'archivage, mais il reste consultable.</p>
<h3>Troisième âge : les archives définitives (ou historiques)</h3>
<p>Une fois la durée d'utilité administrative écoulée, le document est soit <strong>éliminé</strong>, soit <strong>conservé définitivement</strong> pour sa valeur historique ou patrimoniale. C'est ce qu'on appelle le <strong>sort final</strong>.</p>
<h3>La durée d'utilité administrative</h3>
<p>La période pendant laquelle un document doit être conservé s'appelle la <strong>durée d'utilité administrative</strong> (DUA) ou durée de conservation. Elle dépend de la réglementation, du secteur, du type de document et des besoins de l'organisation. Elle commence à courir à partir d'un <strong>événement déclencheur</strong> : la fin d'un contrat, la clôture d'un exercice, le départ d'un salarié.</p>
<p>Le modèle anglo-saxon du <strong>records continuum</strong> présente le cycle de façon plus continue, adaptée au numérique : un document peut être géré comme archive dès sa création. Dans la pratique, les deux approches se complètent.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Trois âges : courant, intermédiaire, définitif.</li><li>La durée de conservation court à partir d'un événement déclencheur.</li><li>À l'échéance, le sort final est l'élimination ou la conservation définitive, jamais l'oubli.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Prenez un contrat de votre organisation. À quel âge se trouve-t-il ? Quel événement fera courir sa durée de conservation ?</p></div>""",
            "quiz": [
                Q("Dans la théorie des trois âges, un contrat terminé conservé en cas de litige relève des archives…",
                  ["Courantes", "Intermédiaires", "Définitives", "Personnelles"], 1,
                  "Il n'est plus utilisé au quotidien mais doit être gardé pour des raisons juridiques : âge intermédiaire."),
                Q("Que désigne le « sort final » d'un document ?",
                  ["Sa numérisation", "Son élimination ou sa conservation définitive à l'issue de la durée de conservation", "Sa dernière modification", "Son transfert dans un autre service"], 1,
                  "Le sort final est la décision prise à l'échéance : éliminer ou conserver définitivement."),
                Q("La durée de conservation d'un dossier du personnel commence en général à courir…",
                  ["À la création du dossier", "Au départ du salarié", "Au 1er janvier de chaque année", "À la numérisation"], 1,
                  "Le départ du salarié est l'événement déclencheur habituel pour les dossiers du personnel."),
                Q("Qui a formulé la théorie des trois âges en 1961 ?",
                  ["Yves Pérotin", "Paul Otlet", "Melvil Dewey", "Theodore Schellenberg"], 0,
                  "Yves Pérotin, archiviste français, a proposé cette théorie en 1961."),
            ],
        },
        {
            "title": "Pourquoi archiver ? Risques et enjeux", "minutes": 35,
            "html": """
<p>Bien gérer ses archives n'est pas une affaire de rangement. C'est une question de droits, de coûts et de survie de l'organisation.</p>
<h3>Prouver et se défendre</h3>
<p>En cas de litige avec un client, un fournisseur, un salarié ou l'administration, c'est le document qui fait la preuve. Une organisation incapable de produire un contrat signé, une quittance ou un procès-verbal perd souvent son procès, quel que soit le fond de l'affaire.</p>
<h3>Respecter ses obligations</h3>
<p>Comptabilité, fiscalité, droit du travail, protection des données personnelles, marchés publics : de nombreux textes imposent de conserver certains documents pendant une durée minimale, et d'en protéger d'autres. En Côte d'Ivoire, la loi n°2013-450 encadre par exemple le traitement et la conservation des données personnelles.</p>
<h3>Travailler plus vite</h3>
<p>Le temps passé à chercher un document est un coût caché considérable. Une recherche de vingt minutes, répétée plusieurs fois par jour dans chaque service, représente des semaines de travail perdues chaque année.</p>
<h3>Survivre aux sinistres</h3>
<p>Les risques sont bien réels :</p>
<ul><li><strong>Incendie et dégât des eaux</strong> : un local d'archives détruit, c'est parfois des décennies de mémoire perdues.</li>
<li><strong>Rançongiciel</strong> : une attaque chiffre les serveurs et exige une rançon.</li>
<li><strong>Erreur humaine</strong> : suppression accidentelle, départ d'un salarié qui emporte ses fichiers.</li>
<li><strong>Panne</strong> : disque dur, coupure électrique, serveur hors service.</li></ul>
<h3>Préserver la mémoire</h3>
<p>Les archives d'une institution racontent son histoire et celle de son territoire. En Afrique, une part importante de ce patrimoine documentaire est menacée faute de conditions de conservation adaptées. L'archivage est aussi une responsabilité envers les générations futures.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Archiver, c'est pouvoir prouver, respecter la loi, gagner du temps et survivre aux sinistres.</li><li>Les risques principaux : feu, eau, rançongiciel, erreur humaine, panne.</li><li>La première protection est une organisation claire, avant toute technologie.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Faites le <a href="~/ressources/document-health-check/">Document Health Check</a> pour votre service. Notez les trois points les plus faibles.</p></div>""",
            "quiz": [
                Q("Quels risques menacent directement la conservation des archives ?",
                  ["Le rançongiciel", "Le dégât des eaux", "La suppression accidentelle", "Un plan de classement validé"], [0, 1, 2],
                  "Rançongiciel, eau et erreur humaine sont des risques majeurs. Un plan de classement est au contraire une protection."),
                Q("En cas de litige, l'absence d'un document signé peut faire perdre un procès même si l'on a raison sur le fond.", VF, 0,
                  "La preuve repose sur les documents : ne pas pouvoir les produire affaiblit fortement une position."),
                Q("En Côte d'Ivoire, quelle loi encadre la protection des données à caractère personnel ?",
                  ["Loi n°2013-450", "Loi n°2013-546", "Décret n°2016-851", "Décret n°2014-106"], 0,
                  "La loi n°2013-450 du 19 juin 2013 porte sur la protection des données à caractère personnel."),
                Q("Quelle est la première protection des archives selon ce module ?",
                  ["Un logiciel coûteux", "Une organisation claire", "Un coffre-fort", "Une assurance"], 1,
                  "Sans organisation (qui fait quoi, où, selon quelles règles), aucune technologie ne suffit."),
            ],
        },
    ],
    "exam_extra": [
        Q("Un message vocal laissé par un client pour annuler une commande peut constituer une archive.", VF, 0,
          "Le support importe peu : s'il est reçu dans le cadre d'une activité, c'est une archive."),
        Q("Quel âge correspond aux documents utilisés quotidiennement dans le service ?",
          ["Archives courantes", "Archives intermédiaires", "Archives définitives", "Archives mortes"], 0,
          "Les archives courantes (ou actives) servent au travail quotidien."),
        Q("Pourquoi la dispersion des documents est-elle un problème ?",
          ["Elle crée des doublons", "Elle rend des documents introuvables", "Elle expose des documents confidentiels", "Elle réduit le coût de stockage"], [0, 1, 2],
          "Dispersion = doublons, pertes de temps et fuites possibles."),
        Q("À l'issue de la durée de conservation, un document peut simplement être oublié dans un carton.", VF, 1,
          "Non : un sort final doit être décidé (élimination tracée ou conservation définitive)."),
    ],
}

N2 = {
    "num": 2, "slug": "niveau-2", "title": "Gestion documentaire",
    "audience": "Utilisateurs, assistants, secrétariats", "duration": "3 h 30",
    "intro": "Organiser les documents du quotidien : GED, nommage, classement, courrier et circuits de validation.",
    "objectives": ["Expliquer à quoi sert une GED et ce qu'elle ne fait pas",
                   "Appliquer des règles de nommage et de classement communes",
                   "Organiser l'enregistrement et le suivi du courrier",
                   "Concevoir un circuit de validation simple"],
    "modules": [
        {
            "title": "La GED : principes et fonctions", "minutes": 35,
            "html": """
<p>La <strong>gestion électronique des documents</strong> (GED) regroupe les outils et les méthodes qui permettent de capturer, classer, retrouver, partager et faire évoluer les documents d'une organisation.</p>
<h3>Les fonctions essentielles</h3>
<ul>
<li><strong>Capturer</strong> : importer un fichier, numériser un papier, enregistrer une pièce jointe, recevoir un document par API.</li>
<li><strong>Décrire</strong> : renseigner des métadonnées (type, date, auteur, client, montant…).</li>
<li><strong>Classer</strong> : ranger le document au bon endroit d'une arborescence commune.</li>
<li><strong>Retrouver</strong> : rechercher par mots du texte, par métadonnées, par filtres.</li>
<li><strong>Versionner</strong> : garder l'historique des modifications et savoir quelle version fait foi.</li>
<li><strong>Contrôler l'accès</strong> : chacun voit et modifie uniquement ce que son rôle autorise.</li>
<li><strong>Partager</strong> : donner accès à un collègue ou à un partenaire externe, avec des limites.</li>
</ul>
<h3>Ce que la GED n'est pas</h3>
<p>Un dossier partagé sur un serveur n'est pas une GED : il n'impose ni métadonnées, ni droits fins, ni historique fiable. Et une GED n'est pas un système d'archivage électronique : elle gère des documents <em>vivants</em>, qu'on modifie. Quand un document doit être figé pour faire preuve pendant des années, il passe dans un <strong>SAE</strong> (niveau 4).</p>
<h3>Les conditions de réussite</h3>
<p>Un projet de GED échoue rarement à cause du logiciel. Il échoue quand chacun continue à classer « à sa façon », quand les métadonnées sont trop nombreuses ou quand personne n'est responsable du plan de classement. Les clés : un classement commun simple, quelques métadonnées obligatoires bien choisies, un référent par service et une formation des utilisateurs.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>GED = capturer, décrire, classer, retrouver, versionner, contrôler, partager.</li><li>Un serveur de fichiers n'est pas une GED ; une GED n'est pas un SAE.</li><li>La réussite dépend d'abord des règles communes et des personnes.</li></ul></div>""",
            "quiz": [
                Q("Lesquelles de ces fonctions relèvent d'une GED ?",
                  ["Versionner les documents", "Contrôler les accès", "Rechercher par métadonnées", "Calculer la paie"], [0, 1, 2],
                  "Versions, droits et recherche sont au cœur de la GED. La paie relève d'un logiciel RH."),
                Q("Un simple dossier partagé sur un serveur constitue une GED complète.", VF, 1,
                  "Il manque les métadonnées, les droits fins et un historique fiable."),
                Q("Quand un document doit être figé pour faire preuve pendant des années, il doit passer…",
                  ["Dans un autre dossier de la GED", "Dans un système d'archivage électronique (SAE)", "Sur une clé USB", "Dans la corbeille"], 1,
                  "Le SAE garantit intégrité et traçabilité sur la durée ; la GED gère les documents vivants."),
                Q("Quelle est la cause d'échec la plus fréquente d'un projet de GED ?",
                  ["Un logiciel trop lent", "L'absence de règles communes et de responsables", "Un manque de couleurs dans l'interface", "Le coût de l'électricité"], 1,
                  "Sans classement commun ni référents, chacun reprend ses habitudes et la GED se vide de sens."),
            ],
        },
        {
            "title": "Nommer et classer les documents", "minutes": 40,
            "html": """
<p>Un document bien nommé et bien classé se retrouve en quelques secondes, même par quelqu'un qui ne l'a jamais vu. Voici des règles simples, applicables dès aujourd'hui.</p>
<h3>Une convention de nommage</h3>
<p>Adoptez un format unique et documenté, par exemple : <code>AAAA-MM-JJ_Type_Objet_Version</code>.</p>
<ul>
<li><code>2026-09-14_PV_Conseil-administration_v1.pdf</code></li>
<li><code>2026-03-02_Contrat_ABC-SA_maintenance_signe.pdf</code></li>
</ul>
<p>Pourquoi la date en premier, au format année-mois-jour (norme ISO 8601) ? Parce que les fichiers se trient alors automatiquement dans l'ordre chronologique.</p>
<p>Quelques règles complémentaires :</p>
<ul><li>Éviter les espaces, accents et caractères spéciaux (<code>/ \\ : * ? " &lt; &gt; |</code>), source d'erreurs entre systèmes.</li>
<li>Bannir « final », « final2 », « vraiment-final » : utiliser un numéro de version, ou mieux, le versionnage de la GED.</li>
<li>Rester court : le nom identifie, les métadonnées décrivent.</li></ul>
<h3>Une arborescence commune</h3>
<p>Classez par <strong>activité</strong> plutôt que par personne. « Dossiers de Mariam » devient illisible quand Mariam change de poste ; « Achats › Contrats fournisseurs › 2026 » reste clair.</p>
<p>Limitez la profondeur : au-delà de quatre ou cinq niveaux, on ne retrouve plus rien. Évitez le dossier « Divers », qui grossit indéfiniment.</p>
<h3>Le rôle des métadonnées</h3>
<p>Une GED permet de retrouver un document autrement que par son emplacement : un contrat peut être retrouvé par fournisseur, par date de fin ou par montant. Choisissez peu de métadonnées obligatoires, mais toujours remplies.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Format de nom unique, date ISO en premier, pas de caractères spéciaux.</li><li>Classer par activité, pas par personne ; quatre ou cinq niveaux au maximum.</li><li>Peu de métadonnées, mais toujours renseignées.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Renommez dix fichiers de votre poste selon la convention <code>AAAA-MM-JJ_Type_Objet</code>. Combien de temps avez-vous gagné pour les retrouver ?</p></div>""",
            "quiz": [
                Q("Quel nom de fichier respecte le mieux les bonnes pratiques ?",
                  ["PV conseil final2.docx", "2026-09-14_PV_Conseil-administration_v1.pdf", "14/09/2026 PV.pdf", "Document de Mariam.pdf"], 1,
                  "Date ISO en premier, type, objet, version, sans espaces ni caractères interdits."),
                Q("Pourquoi placer la date au format AAAA-MM-JJ en début de nom ?",
                  ["C'est plus joli", "Les fichiers se trient automatiquement par ordre chronologique", "C'est obligatoire dans Windows", "Cela réduit la taille du fichier"], 1,
                  "Le format ISO 8601 se trie correctement dans l'ordre alphabétique."),
                Q("Il est préférable de classer les documents par nom d'employé.", VF, 1,
                  "Classer par activité reste valable quand les personnes changent de poste."),
                Q("Quelles pratiques faut-il éviter ?",
                  ["Un dossier « Divers »", "Des noms comme « final2 »", "Plus de quatre ou cinq niveaux de dossiers", "Un numéro de version"], [0, 1, 2],
                  "Le numéro de version est une bonne pratique ; les trois autres créent du désordre."),
            ],
        },
        {
            "title": "Gérer le courrier (GEC)", "minutes": 35,
            "html": """
<p>Le courrier est souvent la porte d'entrée des documents dans une organisation, et un point de friction : lettres égarées, délais de réponse dépassés, personne ne sait qui traite quoi. La <strong>gestion électronique du courrier</strong> (GEC) apporte de l'ordre.</p>
<h3>Le circuit du courrier entrant</h3>
<ol>
<li><strong>Réception</strong> : le courrier arrive (papier, courriel, plateforme).</li>
<li><strong>Enregistrement</strong> : il reçoit un numéro chronologique unique, une date d'arrivée, un expéditeur, un objet. Le papier est numérisé.</li>
<li><strong>Affectation</strong> : il est attribué à un service ou à une personne, avec un délai de traitement.</li>
<li><strong>Traitement</strong> : l'agent prépare la réponse ou l'action demandée.</li>
<li><strong>Réponse</strong> : la réponse est validée, signée et envoyée ; elle est liée au courrier d'origine.</li>
<li><strong>Archivage</strong> : le courrier et sa réponse rejoignent le dossier concerné.</li>
</ol>
<h3>Le registre chronologique</h3>
<p>Le registre (ou « chrono ») est la colonne vertébrale de la GEC : il prouve qu'un courrier a été reçu à une date donnée. Dans une administration, il peut avoir une valeur juridique importante, par exemple pour établir qu'une demande a été déposée dans les délais.</p>
<h3>Le courrier sortant et interne</h3>
<p>Le courrier sortant suit le même principe : numéro, date, destinataire, objet, signataire. Le courrier interne (notes de service, circulaires) mérite aussi d'être enregistré quand il engage l'organisation.</p>
<h3>Les indicateurs</h3>
<p>Une GEC permet de suivre le nombre de courriers reçus, le délai moyen de traitement, les courriers en retard par service. Ces indicateurs améliorent la qualité du service rendu aux usagers.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Réception, enregistrement, affectation, traitement, réponse, archivage.</li><li>Le registre chronologique prouve la date de réception.</li><li>La GEC rend visibles les délais et les retards.</li></ul></div>""",
            "quiz": [
                Q("Quelle étape attribue un numéro chronologique unique au courrier ?",
                  ["La réception", "L'enregistrement", "L'affectation", "L'archivage"], 1,
                  "L'enregistrement donne au courrier son numéro, sa date d'arrivée et ses informations de base."),
                Q("Le registre chronologique peut servir à prouver la date de réception d'une demande.", VF, 0,
                  "C'est l'une de ses fonctions essentielles, notamment dans les administrations."),
                Q("Remettez dans l'ordre : quelle étape vient juste après l'affectation ?",
                  ["L'enregistrement", "Le traitement", "La réception", "L'archivage"], 1,
                  "Réception → enregistrement → affectation → traitement → réponse → archivage."),
                Q("Quels indicateurs une GEC permet-elle de suivre ?",
                  ["Le délai moyen de traitement", "Les courriers en retard par service", "Le nombre de courriers reçus", "La météo"], [0, 1, 2],
                  "Volumes, délais et retards : de quoi piloter la qualité de service."),
            ],
        },
        {
            "title": "Workflows et validation", "minutes": 35,
            "html": """
<p>Un <strong>workflow</strong> (circuit de validation) est l'enchaînement des étapes par lesquelles passe un document : contrôle, avis, validation, signature, archivage. L'automatiser évite les parapheurs égarés et les relances par téléphone.</p>
<h3>Concevoir un circuit</h3>
<p>Pour chaque circuit, posez cinq questions :</p>
<ol><li><strong>Quel document ?</strong> Contrat, facture, note de service…</li>
<li><strong>Quelles étapes ?</strong> Par exemple : dépôt → contrôle juridique → validation de la direction → signature → archivage.</li>
<li><strong>Qui à chaque étape ?</strong> Un rôle ou un groupe plutôt qu'une personne nommément, pour gérer les absences.</li>
<li><strong>Quel délai ?</strong> Et que se passe-t-il en cas de dépassement : relance, délégation ?</li>
<li><strong>Quelles conditions ?</strong> Par exemple, au-delà de 50 millions FCFA, ajouter une étape au conseil d'administration.</li></ol>
<h3>Les décisions possibles</h3>
<p>À chaque étape, l'intervenant peut valider, refuser (avec un commentaire obligatoire) ou demander une correction. Chaque décision est horodatée et tracée : c'est ce qui donne sa valeur au circuit.</p>
<h3>La signature électronique</h3>
<p>En fin de circuit, la signature électronique remplace la signature manuscrite. En Côte d'Ivoire, le décret n°2014-106 encadre l'écrit et la signature électroniques. Une bonne pratique consiste à s'appuyer sur un prestataire de signature de confiance, puis à archiver le document signé avec ses preuves (certificat, horodatage).</p>
<h3>Garder la simplicité</h3>
<p>Un circuit à huit étapes que personne ne respecte vaut moins qu'un circuit à trois étapes appliqué par tous. Commencez par un ou deux circuits à fort volume (factures, contrats), mesurez les délais, puis étendez.</p>
<div class="lesson-key"><p><strong>À retenir</strong></p><ul><li>Document, étapes, rôles, délais, conditions : cinq questions pour concevoir un circuit.</li><li>Chaque décision est horodatée et tracée.</li><li>Commencer simple, mesurer, puis étendre.</li></ul></div>
<div class="lesson-practice"><p><strong>Mise en pratique</strong></p><p>Dessinez sur papier le circuit actuel de validation d'une facture dans votre organisation. Combien d'étapes ? Où se perd le plus de temps ?</p></div>""",
            "quiz": [
                Q("Pourquoi désigner un rôle plutôt qu'une personne à chaque étape d'un circuit ?",
                  ["Pour gérer les absences et les changements de poste", "Pour aller plus vite à l'impression", "Parce que c'est moins cher", "Pour éviter la signature"], 0,
                  "Un rôle ou un groupe survit aux absences et aux mutations ; une personne nommée bloque le circuit."),
                Q("Lors d'un refus dans un workflow, quelle bonne pratique s'applique ?",
                  ["Refuser sans explication", "Exiger un commentaire", "Supprimer le document", "Redémarrer le circuit depuis le début automatiquement"], 1,
                  "Le commentaire permet au dépositaire de corriger et garde une trace de la décision."),
                Q("En Côte d'Ivoire, quel texte encadre l'écrit et la signature électroniques ?",
                  ["Décret n°2014-106", "Loi n°2013-450", "Décret n°2021-916", "ISO 15489"], 0,
                  "Le décret n°2014-106 porte sur l'écrit et la signature électroniques."),
                Q("Un circuit long et complet est toujours préférable à un circuit court.", VF, 1,
                  "Un circuit simple et appliqué vaut mieux qu'un circuit complexe contourné."),
            ],
        },
    ],
    "exam_extra": [
        Q("Une GED doit-elle permettre de savoir quelle version d'un document fait foi ?", ["Oui", "Non"], 0,
          "Le versionnage est une fonction essentielle de la GED."),
        Q("Quels caractères faut-il éviter dans les noms de fichiers ?",
          ["Barre oblique /", "Deux-points :", "Point d'interrogation ?", "Tiret -"], [0, 1, 2],
          "Le tiret est sans danger ; / : ? posent problème entre systèmes."),
        Q("Le courrier interne qui engage l'organisation mérite d'être enregistré.", VF, 0,
          "Notes de service et circulaires engageant l'organisation doivent être tracées."),
        Q("Dans un workflow, que permet l'horodatage de chaque décision ?",
          ["De prouver qui a décidé quoi et quand", "D'accélérer l'ordinateur", "De supprimer les étapes inutiles", "De traduire le document"], 0,
          "L'horodatage et la traçabilité donnent sa valeur probante au circuit."),
    ],
}
