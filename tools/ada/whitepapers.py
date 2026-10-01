"""Livres blancs ADA (contenu)."""

WHITEPAPERS = [
    {
        "slug": "archiver-en-cote-divoire",
        "title": "Archiver en Côte d'Ivoire",
        "subtitle": "Cadre juridique, bonnes pratiques et points de vigilance pour l'archivage électronique",
        "pages": "12 pages", "icon": "scale",
        "summary": "Les textes ivoiriens sur les transactions électroniques, la signature, l'archivage électronique et la protection des données, et ce qu'ils impliquent concrètement pour un projet d'archivage.",
        "sections": [
            ("Pourquoi ce livre blanc", """
<p>De nombreuses organisations ivoiriennes souhaitent dématérialiser leurs documents : pour gagner de la place, retrouver plus vite l'information, sécuriser leur mémoire face aux sinistres. Une question revient toujours : <strong>un document numérique a-t-il la même valeur qu'un original papier ?</strong> Et que faut-il respecter pour qu'il la garde ?</p>
<p>Ce document présente les repères du cadre ivoirien et les bonnes pratiques qui en découlent. Il s'adresse aux directions générales, juridiques, financières et informatiques. Il ne remplace pas l'avis d'un juriste : chaque organisation doit faire valider son dispositif selon son secteur et ses obligations propres.</p>"""),
            ("Les textes de référence", """
<p>La Côte d'Ivoire dispose d'un ensemble de textes relatifs à la confiance numérique, recensés notamment par l'ANSSI Côte d'Ivoire.</p>
<table><thead><tr><th>Texte</th><th>Objet</th></tr></thead><tbody>
<tr><td>Loi n°2013-546</td><td>Transactions électroniques. Reconnaît l'écrit électronique et définit l'archivage électronique sécurisé comme l'ensemble des modalités de conservation et de gestion destinées à garantir la valeur juridique des archives électroniques pendant la durée nécessaire.</td></tr>
<tr><td>Loi n°2013-450</td><td>Protection des données à caractère personnel : collecte, traitement, transmission, stockage et utilisation.</td></tr>
<tr><td>Décret n°2014-106</td><td>Conditions de l'écrit et de la signature électroniques.</td></tr>
<tr><td>Décret n°2016-851 du 19 octobre 2016</td><td>Modalités de mise en œuvre de l'archivage électronique.</td></tr>
<tr><td>Décret n°2021-916</td><td>Référentiel général de sécurité des systèmes d'information (RGSSI).</td></tr></tbody></table>
<p>L'ARTCI est l'autorité de protection des données personnelles. L'ANSSI Côte d'Ivoire intervient sur la sécurité des systèmes d'information et la confiance numérique.</p>"""),
            ("Ce qui fait la valeur d'une archive électronique", """
<p>Les textes et les normes internationales convergent sur quatre exigences. Une archive électronique conserve sa valeur si l'on peut démontrer :</p>
<ul><li><strong>son origine</strong> : qui l'a produite ou reçue, dans quel contexte ;</li>
<li><strong>son intégrité</strong> : elle n'a pas été modifiée depuis son archivage, ce que l'on prouve par une empreinte cryptographique et un journal ;</li>
<li><strong>sa date</strong> : idéalement par un horodatage délivré par un tiers de confiance ;</li>
<li><strong>sa lisibilité</strong> pendant toute sa durée de conservation, grâce à des formats pérennes et à une politique de préservation.</li></ul>
<p>C'est la différence entre un simple stockage et un <strong>système d'archivage électronique</strong> : le second documente et garantit ces quatre points.</p>"""),
            ("Durées de conservation : la règle d'or", """
<p>Combien de temps garder ses factures, contrats, dossiers du personnel, procès-verbaux ? La réponse dépend de la réglementation applicable, du secteur, des besoins de preuve et des engagements contractuels. <strong>Une durée de conservation ne s'invente pas</strong> : elle se fonde sur un texte ou une décision motivée, et elle est validée par un juriste.</p>
<p>Notre recommandation : formaliser un <strong>référentiel de conservation</strong> qui indique, pour chaque série de documents, la durée, l'événement déclencheur (fin de contrat, départ d'un salarié, clôture d'exercice), le sort final et le fondement. C'est ce référentiel que la plateforme appliquera ensuite automatiquement.</p>"""),
            ("Données personnelles : intégrer la protection dès la conception", """
<p>Les archives contiennent énormément de données personnelles. La loi n°2013-450 s'applique donc pleinement aux projets d'archivage :</p>
<ul><li>conserver pour une finalité définie, et pas « au cas où » ;</li>
<li>limiter la durée de conservation des données personnelles ;</li>
<li>restreindre et tracer les accès, chiffrer les données sensibles ;</li>
<li>permettre l'exercice des droits des personnes dans les conditions prévues par la loi ;</li>
<li>encadrer les prestataires (hébergement, numérisation) par contrat.</li></ul>"""),
            ("Numériser puis détruire le papier ?", """
<p>C'est l'une des questions les plus sensibles. La numérisation fidèle d'un document, conservée dans un système d'archivage électronique conforme, peut dans certains cas se substituer à l'original. Mais tous les documents ne s'y prêtent pas : actes authentiques, titres, documents pour lesquels un texte exige l'original.</p>
<p>Notre position : <strong>ne jamais détruire d'originaux sans une analyse juridique documentée</strong>, série par série. En attendant, la numérisation sert à la consultation et à la sauvegarde, et les originaux sont inventoriés, localisés et conservés dans de bonnes conditions.</p>"""),
            ("Notre check-list", """
<ul class="wp-block-list is-style-check">
<li>Un inventaire des fonds papier et numériques existe.</li>
<li>Un plan de classement commun est validé.</li>
<li>Un référentiel de conservation est rédigé et validé par un juriste.</li>
<li>Les documents archivés reçoivent une empreinte et sont tracés dans un journal.</li>
<li>Les formats de conservation sont pérennes (PDF/A pour les documents).</li>
<li>Les accès sont nominatifs, limités et revus au moins une fois par an.</li>
<li>La sauvegarde suit la règle 3-2-1 et la restauration est testée.</li>
<li>Les prestataires sont encadrés par contrat (sécurité, confidentialité, localisation des données).</li>
<li>Aucune destruction d'original sans analyse juridique documentée.</li>
<li>Le dispositif a été revu par un archiviste, un juriste et un expert en sécurité.</li></ul>"""),
        ],
    },
    {
        "slug": "de-la-ged-a-la-preservation",
        "title": "De la GED à la préservation",
        "subtitle": "Construire une stratégie documentaire complète, étape par étape",
        "pages": "14 pages", "icon": "layers",
        "summary": "Comment passer d'une GED de partage à une véritable chaîne documentaire : records management, archivage électronique, préservation numérique, et dans quel ordre avancer.",
        "sections": [
            ("Le constat", """
<p>Beaucoup d'organisations ont acheté une GED et constatent quelques années plus tard que le problème n'est pas résolu : les documents sont mieux partagés, mais personne ne sait combien de temps les garder, les doublons se multiplient, et rien ne garantit qu'un document n'a pas été modifié. La raison est simple : la GED n'est qu'un maillon d'une chaîne plus longue.</p>"""),
            ("Quatre fonctions à ne pas confondre", """
<table><thead><tr><th>Fonction</th><th>Question à laquelle elle répond</th><th>Référence</th></tr></thead><tbody>
<tr><td>GED</td><td>Comment travailler ensemble sur les documents ?</td><td>—</td></tr>
<tr><td>Records management</td><td>Quels documents garder, combien de temps, sous la responsabilité de qui ?</td><td>ISO 15489</td></tr>
<tr><td>Archivage électronique (SAE)</td><td>Comment prouver qu'un document est intègre et authentique ?</td><td>Cadre national, journal, empreintes</td></tr>
<tr><td>Préservation numérique</td><td>Pourra-t-on encore lire ce document dans 30 ans ?</td><td>ISO 14721 (OAIS)</td></tr></tbody></table>"""),
            ("Étape 1 : poser les règles", """
<p>Avant tout logiciel : un <strong>plan de classement</strong> fondé sur les fonctions et activités, un <strong>référentiel de conservation</strong> validé par un juriste, et une <strong>politique d'archivage</strong> qui fixe les rôles. Ce travail prend quelques semaines et conditionne tout le reste.</p>"""),
            ("Étape 2 : maîtriser le flux quotidien", """
<p>La GED et la gestion du courrier organisent le flux : capture, métadonnées, classement, circuits de validation. Le bon réflexe : peu de métadonnées obligatoires mais toujours remplies, des listes de valeurs, des circuits simples, des référents par service. L'OCR et l'extraction automatique réduisent la saisie.</p>"""),
            ("Étape 3 : archiver avec valeur de preuve", """
<p>À un moment défini (signature, clôture, fin d'exercice), le document est <strong>versé</strong> dans le système d'archivage : il est figé, son empreinte est calculée et enregistrée, sa règle de conservation s'applique, chaque consultation est tracée. Les éliminations à l'échéance sont décidées par un responsable, documentées par un certificat, et suspendues en cas de gel juridique.</p>"""),
            ("Étape 4 : préserver dans la durée", """
<p>Pour les documents conservés plus de dix ans : formats pérennes, identification et validation des formats à l'entrée, contrôle périodique des empreintes, copies multiples (3-2-1), migration documentée quand un format vieillit. C'est le cœur du modèle OAIS.</p>"""),
            ("Ne pas oublier le papier", """
<p>Dans la plupart des organisations africaines, le papier reste majoritaire et beaucoup de dossiers sont hybrides. Une stratégie complète intègre les archives physiques : inventaire, identifiant et QR code par boîte, localisation précise, suivi des mouvements, lien entre l'original et sa version numérique.</p>"""),
            ("Par où commencer ?", """
<ol><li>Un <strong>audit documentaire</strong> pour mesurer les volumes, les risques et les priorités.</li>
<li>Un <strong>projet pilote</strong> sur un fonds représentatif : plan de classement, numérisation, import, règles.</li>
<li>Un <strong>déploiement progressif</strong> service par service, avec formation.</li>
<li>Une <strong>montée en maturité</strong> : archivage électronique, puis préservation.</li></ol>
<p>Cette progression, de la transformation documentaire vers la plateforme, est précisément l'approche d'ADA.</p>"""),
        ],
    },
    {
        "slug": "numeriser-un-fonds-darchives",
        "title": "Numériser un fonds d'archives",
        "subtitle": "Préparer, chiffrer et piloter un projet de numérisation de masse",
        "pages": "12 pages", "icon": "scan",
        "summary": "Volumes, préparation, choix techniques, contrôle qualité, indexation, chiffrage : la méthode pour réussir un projet de numérisation, du pilote à la production.",
        "sections": [
            ("Numériser, pour quoi faire ?", """
<p>Avant de choisir un scanner, clarifiez l'objectif, car il détermine tous les choix techniques :</p>
<ul><li><strong>Consultation</strong> : retrouver et partager vite. Qualité standard, OCR, indexation soignée.</li>
<li><strong>Sauvegarde</strong> : protéger contre la perte des originaux. Copie hors site indispensable.</li>
<li><strong>Preuve</strong> : remplacer, quand c'est permis, la consultation de l'original. Processus documenté et contrôlé.</li>
<li><strong>Patrimoine</strong> : préserver et diffuser des fonds historiques. Haute résolution, formats de préservation, manipulation adaptée.</li></ul>"""),
            ("Mesurer le fonds", """
<p>Un projet se chiffre à partir de quelques données : métrage linéaire ou nombre de boîtes, nombre moyen de pages par boîte, formats (A4, A3, plans, registres reliés), état de conservation, présence d'agrafes et de documents collés, nombre de dossiers à indexer. Un échantillonnage de quelques boîtes représentatives donne des estimations fiables.</p>"""),
            ("La préparation, poste le plus sous-estimé", """
<p>La cadence d'un projet dépend surtout de la <strong>préparation</strong> : dégrafage, défroissage, réparation des pages déchirées, insertion des intercalaires de séparation, contrôle de l'ordre des pièces. Sur des fonds anciens ou mal tenus, la préparation peut prendre plus de temps que le scan lui-même.</p>"""),
            ("Les choix techniques", """
<table><thead><tr><th>Usage</th><th>Résolution indicative</th><th>Format</th></tr></thead><tbody>
<tr><td>Documents administratifs courants</td><td>200 à 300 ppp</td><td>PDF/A avec texte OCR</td></tr>
<tr><td>Plans et grands formats</td><td>300 ppp ou plus</td><td>PDF/A, TIFF</td></tr>
<tr><td>Fonds patrimoniaux</td><td>300 à 600 ppp selon les documents</td><td>TIFF non compressé ou sans perte, JPEG 2000</td></tr></tbody></table>
<p>Ces valeurs sont indicatives : le pilote permet de les valider sur vos documents réels.</p>"""),
            ("OCR et indexation", """
<p>L'OCR rend le texte recherchable ; l'indexation rend le document <em>trouvable</em>. Les deux se complètent. L'indexation repose sur les métadonnées définies avec vous (date, numéro d'acte, nom, montant, service). Une partie peut être extraite automatiquement puis contrôlée ; une partie reste saisie par des opérateurs, en particulier pour les documents manuscrits.</p>"""),
            ("Le contrôle qualité", """
<ul><li>Contrôles automatiques : pages blanches, images floues, orientation, nombre de pages attendu.</li>
<li>Contrôles visuels par échantillonnage sur chaque lot.</li>
<li>Contrôle des métadonnées : complétude et cohérence.</li>
<li>Rapprochement final : nombre de documents et de pages entre l'inventaire et le résultat.</li></ul>
<p>Chaque lot livré est accompagné d'un rapport, et chaque fichier reçoit son empreinte dès la production.</p>"""),
            ("Chiffrer un projet", """
<p>Le prix dépend des équipements, de la main-d'œuvre, de la préparation, du contrôle qualité, du stockage, de l'OCR, du transport et de la marge. Les offres se facturent à la page (scan simple, scan + OCR, scan + OCR + indexation, traitement complexe) ou au forfait pour une migration de fonds. Méfiez-vous des prix à la page très bas qui excluent la préparation et le contrôle qualité.</p>"""),
            ("Commencer par un pilote", """
<p>Notre recommandation : un pilote sur un fonds représentatif (par exemple 1 000 dossiers). Il permet de valider le plan de classement, les métadonnées, la qualité d'image, la cadence réelle et donc le budget, avant d'engager la production. C'est la meilleure protection contre les mauvaises surprises.</p>"""),
        ],
    },
]
