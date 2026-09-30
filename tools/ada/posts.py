"""Blog posts and guides (content only)."""

POSTS = [
    {
        "slug": "ged-sae-records-management-difference",
        "title": "GED, SAE, records management : ne plus confondre",
        "cat": ("guides", "Guides"), "date": "2026-09-28", "cover": "cover-ged-sae-records.png", "read": 7,
        "tags": ["GED", "SAE", "Records management"],
        "excerpt": "Trois notions souvent mélangées, trois besoins différents. Comprendre la différence évite d'acheter le mauvais outil.",
        "body": """
<p>Quand une organisation décide de « mettre ses archives en numérique », elle parle souvent de GED. Pourtant, la GED ne couvre qu'une partie du besoin. Confondre gestion documentaire, archivage électronique et records management conduit à des projets qui stockent beaucoup mais ne prouvent rien.</p>
<h2 id="ged">La GED : travailler sur les documents</h2>
<p>La gestion électronique des documents sert à créer, capturer, classer, modifier, partager et rechercher des documents <em>vivants</em>. C'est l'outil du quotidien : un contrat en cours de négociation, une note de service en relecture, un dossier client qui s'enrichit.</p>
<p>Une bonne GED offre des versions, des droits d'accès, une recherche efficace et des circuits de validation. Mais elle n'est pas conçue pour garantir qu'un document restera identique pendant dix ans.</p>
<h2 id="sae">Le SAE : conserver avec valeur de preuve</h2>
<p>Le système d'archivage électronique intervient quand un document doit être conservé selon des règles définies, avec intégrité, traçabilité et contrôle de son cycle de vie. Une facture archivée ne doit plus pouvoir être modifiée ; chaque consultation doit être tracée ; sa destruction, à l'échéance, doit être décidée et documentée.</p>
<p>En Côte d'Ivoire, la loi n°2013-546 relative aux transactions électroniques parle d'« archivage électronique sécurisé » : des modalités de conservation destinées à garantir la valeur juridique des archives électroniques pendant la durée nécessaire.</p>
<h2 id="records">Le records management : gérer le cycle de vie</h2>
<p>Le records management gère les documents d'activité selon leur contexte, leurs responsables, leurs métadonnées, leurs règles et leur cycle de vie. La norme ISO 15489-1:2016 en fixe les principes. C'est lui qui répond à des questions comme : combien de temps garder ce document ? Qui en est responsable ? Que fait-on à l'échéance ?</p>
<h2 id="preservation">La préservation numérique : rester lisible</h2>
<p>Enfin, la préservation numérique vise à maintenir l'accès à l'information malgré l'évolution des logiciels, des formats et des supports. Le modèle OAIS (ISO 14721:2025) en est la référence.</p>
<h2 id="en-pratique">En pratique</h2>
<figure class="wp-block-table"><table><thead><tr><th>Besoin</th><th>Outil</th><th>Question typique</th></tr></thead><tbody>
<tr><td>Travailler ensemble</td><td>GED</td><td>Où est la dernière version du contrat ?</td></tr>
<tr><td>Prouver</td><td>SAE</td><td>Ce document a-t-il été modifié depuis son archivage ?</td></tr>
<tr><td>Gouverner</td><td>Records management</td><td>Combien de temps garder les dossiers du personnel ?</td></tr>
<tr><td>Durer</td><td>Préservation</td><td>Pourra-t-on lire ce fichier dans 30 ans ?</td></tr></tbody></table></figure>
<p>Une plateforme réellement utile combine ces quatre dimensions et fait passer un document de l'une à l'autre au bon moment. C'est le principe d'ARCHIVA360.</p>""",
    },
    {
        "slug": "regle-3-2-1-sauvegarde-archives",
        "title": "La règle 3-2-1 : protéger vos archives contre l'incendie et le ransomware",
        "cat": ("securite", "Sécurité"), "date": "2026-09-24", "cover": "cover-regle-3-2-1.png", "read": 5,
        "tags": ["Sauvegarde", "Sécurité", "Reprise d'activité"],
        "excerpt": "Trois copies, deux supports, une copie hors site : une règle simple qui sauve des décennies d'archives.",
        "body": """
<p>Les archives disparaissent rarement faute de logiciel. Elles disparaissent dans un incendie, un dégât des eaux, une attaque par rançongiciel, une suppression accidentelle, une panne électrique ou la destruction d'un bâtiment. La première protection n'est pas technologique : c'est une discipline de sauvegarde.</p>
<h2 id="regle">La règle en une phrase</h2>
<p><strong>3 copies</strong> de vos données, sur <strong>2 supports</strong> différents, dont <strong>1 copie hors site</strong>.</p>
<ul class="wp-block-list is-style-check"><li><strong>Trois copies</strong> : l'original et deux sauvegardes. Une seule sauvegarde, c'est un point de défaillance unique.</li>
<li><strong>Deux supports</strong> : par exemple un stockage de production et un stockage de sauvegarde d'une autre technologie, pour qu'une même panne ne touche pas les deux.</li>
<li><strong>Une copie hors site</strong> : dans un autre bâtiment, une autre ville ou un cloud distinct. C'est elle qui survit à l'incendie.</li></ul>
<h2 id="ransomware">Et le ransomware ?</h2>
<p>Un rançongiciel chiffre tout ce qu'il peut atteindre, y compris des sauvegardes accessibles depuis le réseau. D'où l'importance d'une copie isolée ou immuable, que l'attaquant ne peut ni modifier ni supprimer, et de droits d'administration strictement limités.</p>
<h2 id="tester">Une sauvegarde non testée n'existe pas</h2>
<p>Beaucoup d'organisations découvrent le jour de l'incident que leurs sauvegardes sont incomplètes ou illisibles. Un test de restauration régulier, documenté, est indispensable. Dans ARCHIVA360, le Compliance Center signale les sauvegardes non vérifiées.</p>
<h2 id="papier">Et le papier ?</h2>
<p>La numérisation est aussi une sauvegarde de vos archives papier. Un registre numérisé, dont la copie est conservée hors site, survit à la perte de l'original. C'est souvent l'argument décisif pour les administrations et les fonds historiques.</p>
<h2 id="checklist">Votre check-list</h2>
<ul class="wp-block-list is-style-check"><li>Mes sauvegardes sont-elles automatiques ?</li><li>Existe-t-il une copie hors site ?</li><li>Quand ai-je testé une restauration pour la dernière fois ?</li><li>Qui peut supprimer une sauvegarde ?</li><li>Combien de temps faut-il pour tout restaurer ?</li></ul>""",
    },
    {
        "slug": "archivage-electronique-cote-divoire-cadre-juridique",
        "title": "Archivage électronique en Côte d'Ivoire : ce que disent les textes",
        "cat": ("conformite", "Conformité"), "date": "2026-09-21", "cover": "cover-cadre-ivoirien.png", "read": 6,
        "tags": ["Côte d'Ivoire", "Conformité", "Signature électronique"],
        "excerpt": "Transactions électroniques, signature, archivage, données personnelles, sécurité des systèmes : les repères du cadre ivoirien.",
        "body": """
<p>La Côte d'Ivoire dispose d'un cadre spécifique autour de l'écrit électronique et de l'archivage. C'est l'une des raisons pour lesquelles ADA démarre à Abidjan. Voici les principaux textes à connaître. Cet article est une introduction : il ne remplace pas l'avis d'un juriste.</p>
<h2 id="transactions">La loi n°2013-546 relative aux transactions électroniques</h2>
<p>Elle définit notamment l'« archivage électronique sécurisé » comme des modalités de conservation et de gestion destinées à garantir la valeur juridique des archives électroniques pendant la durée nécessaire.</p>
<h2 id="signature">Le décret n°2014-106 sur l'écrit et la signature électroniques</h2>
<p>Il encadre les conditions dans lesquelles l'écrit et la signature électroniques produisent leurs effets. En pratique, ARCHIVA360 s'intègre à des prestataires de signature de confiance plutôt que de réinventer la signature.</p>
<h2 id="archivage">Le décret n°2016-851 du 19 octobre 2016</h2>
<p>Il porte sur les modalités de mise en œuvre de l'archivage électronique. L'ANSSI Côte d'Ivoire le recense parmi les textes de référence.</p>
<h2 id="donnees">La loi n°2013-450 sur la protection des données personnelles</h2>
<p>Elle encadre la collecte, le traitement, la transmission, le stockage et l'utilisation des données personnelles. Les archives contiennent énormément de données personnelles : dossiers du personnel, dossiers clients, dossiers patients. La protection des données doit donc être intégrée dès la conception.</p>
<h2 id="securite">Le RGSSI (décret n°2021-916)</h2>
<p>L'ANSSI référence le référentiel général de sécurité des systèmes d'information adopté par ce décret. Il éclaire les exigences de sécurité attendues, notamment pour les administrations.</p>
<h2 id="consequences">Ce que cela change pour votre projet</h2>
<ul class="wp-block-list is-style-check"><li>Travailler avec un archiviste, un juriste, un expert en cybersécurité et un spécialiste de la protection des données.</li>
<li>Fixer les durées de conservation avec un juriste, selon votre secteur : la plateforme ne doit jamais inventer une durée légale.</li>
<li>Documenter les conditions de conservation : intégrité, traçabilité, sécurité.</li>
<li>Ne pas présenter un dispositif comme « conforme à tout » avant une validation juridique et technique indépendante.</li></ul>""",
    },
    {
        "slug": "blockchain-archives-empreinte-pas-document",
        "title": "Blockchain et archives : pourquoi nous ancrons l'empreinte, pas le document",
        "cat": ("innovation", "Innovation"), "date": "2026-09-17", "cover": "cover-blockchain-preuve.png", "read": 5,
        "tags": ["Blockchain", "Intégrité", "Preuve"],
        "excerpt": "Mettre des documents sur une blockchain est coûteux et souvent inutile. Y inscrire leur empreinte peut en revanche prouver beaucoup.",
        "body": """
<p>La blockchain revient souvent dans les projets d'archivage. Elle peut être utile, à condition de lui confier le bon rôle : celui de <strong>registre de preuve</strong>, et non de stockage principal.</p>
<h2 id="empreinte">L'empreinte cryptographique</h2>
<p>Chaque document archivé dans ARCHIVA360 reçoit une empreinte, par exemple SHA-256 : une suite de caractères calculée à partir de son contenu. Modifier une seule lettre du document change complètement l'empreinte. Si l'empreinte actuelle diffère de l'empreinte d'origine, la plateforme signale une altération.</p>
<figure class="wp-block-table"><table><tbody><tr><td>Document</td><td><code>CONTRAT_2026_00451.pdf</code></td></tr><tr><td>Empreinte</td><td><code>A84F…92BC</code></td></tr></tbody></table></figure>
<h2 id="pourquoi-pas">Pourquoi ne pas mettre le document sur la blockchain ?</h2>
<ul class="wp-block-list is-style-dash"><li>C'est coûteux : les blockchains ne sont pas faites pour stocker des fichiers volumineux.</li><li>C'est risqué pour la confidentialité : un registre distribué est, par nature, partagé.</li><li>C'est contraire au droit à l'effacement et aux durées de conservation : ce qui est inscrit ne s'efface pas.</li></ul>
<h2 id="architecture">L'architecture que nous retenons</h2>
<p>Document → empreinte → horodatage → registre de preuve. Le fichier reste dans l'archive sécurisée. Le registre distribué peut servir à prouver que « ce document existait sous cette forme à cette date », et qu'il a été modifié ou non depuis.</p>
<h2 id="usages">Des usages concrets</h2>
<ul class="wp-block-list is-style-check"><li>Vérifier l'authenticité d'un diplôme délivré par une université.</li><li>Prouver l'état d'un acte foncier à une date donnée.</li><li>Garantir à un auditeur que les pièces d'un projet n'ont pas été modifiées.</li></ul>
<p>Cette fonction « ARCHIVA TRUST » fait partie de la version 3 de la plateforme. L'empreinte et le contrôle d'intégrité sont, eux, présents dès le lancement.</p>""",
    },
    {
        "slug": "numeriser-3-millions-de-pages-methode",
        "title": "Numériser 3 millions de pages : la méthode en 10 étapes",
        "cat": ("numerisation", "Numérisation"), "date": "2026-09-12", "cover": "cover-numerisation-mairie.png", "read": 8,
        "tags": ["Numérisation", "OCR", "Administrations"],
        "excerpt": "Une mairie, des armoires pleines et des décennies de registres. Comment passer du carton à la recherche en quelques secondes.",
        "body": """
<p>Prenons une mairie qui possède 3 millions de pages papier : registres, délibérations, arrêtés, dossiers d'urbanisme, courrier. Retrouver un document y prend parfois des heures. Voici comment nous menons un tel projet.</p>
<h2 id="etapes">Les dix étapes</h2>
<ol class="steps">
<li><div><h3>Audit</h3><p>Visite des locaux, estimation des volumes, état de conservation, priorités, contraintes d'accès.</p></div></li>
<li><div><h3>Classement</h3><p>Construction d'un plan de classement avec les services de la mairie.</p></div></li>
<li><div><h3>Inventaire</h3><p>Chaque boîte reçoit un identifiant et un QR code ; son contenu est décrit.</p></div></li>
<li><div><h3>Numérisation</h3><p>Préparation (dégrafage, défroissage), scan adapté au format et à l'état des documents.</p></div></li>
<li><div><h3>OCR</h3><p>Reconnaissance du texte pour permettre la recherche plein texte.</p></div></li>
<li><div><h3>Indexation</h3><p>Saisie ou extraction des métadonnées : dates, numéros d'actes, noms, quartiers.</p></div></li>
<li><div><h3>Contrôle qualité</h3><p>Pages manquantes, lisibilité, cohérence des métadonnées, par échantillonnage et contrôles automatiques.</p></div></li>
<li><div><h3>Import dans ARCHIVA360</h3><p>Chaque document entre avec son empreinte et sa place dans le plan de classement.</p></div></li>
<li><div><h3>Règles de conservation</h3><p>Durées et sort final fixés avec l'archiviste et le juriste.</p></div></li>
<li><div><h3>Mise en ligne des archives autorisées</h3><p>Les documents communicables peuvent être publiés sur un portail public.</p></div></li></ol>
<h2 id="volumes">Quelques ordres de grandeur</h2>
<p>La cadence dépend surtout de la préparation des documents, bien plus que des scanners. Des documents agrafés, pliés ou abîmés demandent un temps de préparation important. C'est pourquoi nous commençons toujours par un pilote : il permet de mesurer la cadence réelle et de chiffrer le projet sur des bases solides.</p>
<h2 id="resultat">Le résultat</h2>
<p>La mairie retrouve un document en quelques secondes au lieu de chercher manuellement dans des armoires. Les originaux, reconditionnés et localisés, sont mieux protégés. Et les archives historiques peuvent enfin être partagées avec les chercheurs et les citoyens, dans le respect des règles de communicabilité.</p>""",
    },
    {
        "slug": "durees-de-conservation-ne-jamais-inventer",
        "title": "Durées de conservation : pourquoi une plateforme ne doit jamais les inventer",
        "cat": ("records-management", "Records management"), "date": "2026-09-08", "cover": "cover-durees-conservation.png", "read": 5,
        "tags": ["Conservation", "Records management", "Conformité"],
        "excerpt": "5, 10, 30 ans ou permanent ? La réponse dépend de votre secteur, de vos obligations et de vos documents. Pas d'un logiciel.",
        "body": """
<p>« Combien de temps devons-nous garder nos factures ? » C'est l'une des questions les plus fréquentes. Et c'est précisément celle à laquelle un logiciel ne doit pas répondre seul.</p>
<h2 id="pourquoi">Pourquoi ?</h2>
<p>Les durées de conservation dépendent de la réglementation applicable, du secteur d'activité, du type de document, des engagements contractuels et parfois des exigences des bailleurs ou des autorités de contrôle. Elles varient d'un pays à l'autre. Une durée « par défaut » intégrée dans un logiciel peut conduire à détruire trop tôt un document qui aurait servi de preuve, ou à conserver trop longtemps des données personnelles.</p>
<h2 id="qui">Qui les fixe ?</h2>
<p>Votre organisation, avec un archiviste et un juriste. Nous les accompagnons pour construire un <strong>référentiel de conservation</strong> : pour chaque type de document, une durée, un événement déclencheur (fin de contrat, départ d'un salarié, clôture d'exercice) et un sort final.</p>
<h2 id="plateforme">Le rôle de la plateforme</h2>
<ul class="wp-block-list is-style-check"><li>Appliquer les règles validées, automatiquement, à chaque document.</li><li>Calculer les échéances et alerter à l'avance : « 1 250 documents arrivent à échéance dans 90 jours ».</li><li>Permettre le gel juridique en cas de contentieux.</li><li>Ne jamais détruire sans décision humaine, tracée, prise par une personne habilitée.</li></ul>
<h2 id="exemple">Un exemple de tableau</h2>
<figure class="wp-block-table"><table><thead><tr><th>Document</th><th>Échéance</th><th>Action</th></tr></thead><tbody><tr><td>Contrat A</td><td>2028</td><td>Examiner</td></tr><tr><td>Facture B</td><td>2027</td><td>Conserver</td></tr><tr><td>Dossier C</td><td>2035</td><td>Conservation longue</td></tr><tr><td>Archive D</td><td>Permanente</td><td>Préserver</td></tr></tbody></table></figure>
<p>Ces valeurs sont illustratives : les vôtres seront établies avec vos experts.</p>""",
    },
    {
        "slug": "oais-preservation-numerique-expliquee",
        "title": "OAIS expliqué simplement : préserver un fichier pendant 30 ans",
        "cat": ("preservation", "Préservation"), "date": "2026-09-03", "cover": "cover-oais.png", "read": 6,
        "tags": ["OAIS", "Préservation", "Formats"],
        "excerpt": "Un fichier lisible aujourd'hui peut ne plus l'être demain. Le modèle OAIS décrit comment l'éviter.",
        "body": """
<p>Qui peut encore ouvrir un fichier créé avec un traitement de texte des années 1990 ? Les formats, les logiciels et les supports changent. Un document numérique n'est pas éternel par nature : il faut organiser sa préservation.</p>
<h2 id="oais">Le modèle OAIS</h2>
<p>Le modèle OAIS (Open Archival Information System), normalisé sous la référence ISO 14721:2025, décrit ce que doit faire une archive pour préserver l'information à long terme. Il couvre notamment l'entrée des documents, le stockage archivistique, la gestion des données, l'accès et la diffusion, ainsi que la migration vers de nouveaux supports et formats.</p>
<h2 id="concret">Concrètement</h2>
<ul class="wp-block-list is-style-check"><li><strong>Identifier le format</strong> de chaque fichier dès son entrée.</li><li><strong>Valider</strong> qu'il respecte la norme de son format.</li><li><strong>Convertir</strong> si nécessaire vers un format pérenne, comme le PDF/A (ISO 19005).</li><li><strong>Contrôler l'intégrité</strong> périodiquement grâce aux empreintes.</li><li><strong>Migrer</strong> quand un format devient obsolète (ISO 13008), en gardant la trace de chaque transformation.</li></ul>
<h2 id="qui">Qui est concerné ?</h2>
<p>Toutes les organisations qui conservent des documents au-delà de dix ans : administrations, universités, banques, institutions patrimoniales. Pour les autres, un format de conservation adapté et un contrôle d'intégrité régulier constituent déjà une très bonne base.</p>
<h2 id="audit">Et la certification ?</h2>
<p>La norme ISO 16363 permet d'auditer et de certifier un dépôt numérique fiable. C'est un objectif de long terme pour les archives qui préservent un patrimoine.</p>""",
    },
    {
        "slug": "ia-documentaire-ce-quelle-fait-et-ne-doit-pas-faire",
        "title": "IA documentaire : ce qu'elle fait bien, ce qu'elle ne doit jamais faire",
        "cat": ("innovation", "Innovation"), "date": "2026-08-29", "cover": "cover-ia-documentaire.png", "read": 5,
        "tags": ["IA", "OCR", "Gouvernance"],
        "excerpt": "Lire, classer, extraire, résumer : l'IA fait gagner des heures. Détruire, décider, ouvrir des droits : jamais sans un humain.",
        "body": """
<p>L'intelligence artificielle transforme la gestion documentaire. Mais dans l'archivage, où la preuve et la confiance sont essentielles, elle doit être encadrée.</p>
<h2 id="bien">Ce qu'elle fait très bien</h2>
<ul class="wp-block-list is-style-check"><li><strong>Lire</strong> : l'OCR rend le texte des documents scannés exploitable.</li><li><strong>Classer</strong> : identifier le type de document et proposer sa place dans le plan de classement.</li><li><strong>Extraire</strong> : dates, montants, parties, numéros, services.</li><li><strong>Chercher</strong> : comprendre une question comme « les factures supérieures à 10 millions FCFA ».</li><li><strong>Résumer et comparer</strong> : un contrat, deux versions, la chronologie d'un dossier.</li><li><strong>Détecter</strong> les doublons et les documents sans métadonnées.</li></ul>
<h2 id="jamais">Ce qu'elle ne doit jamais faire seule</h2>
<ul class="wp-block-list is-style-dash"><li>Détruire un document.</li><li>Décider du classement définitif.</li><li>Attribuer ou modifier des droits d'accès.</li><li>Voir des documents auxquels l'utilisateur n'a pas accès.</li></ul>
<h2 id="regle">Notre règle</h2>
<p>L'IA assiste, elle ne décide pas. Dans ARCHIVA360, les propositions de l'IA sont présentées avec leur niveau de confiance, validées par une personne habilitée et inscrites dans le journal d'audit. Les réponses de l'assistant citent les documents sources.</p>""",
    },
    {
        "slug": "guide-construire-plan-de-classement",
        "title": "Guide : construire votre premier plan de classement",
        "cat": ("guides", "Guides"), "date": "2026-08-25", "cover": "cover-guide-plan-classement.png", "read": 9,
        "tags": ["Plan de classement", "Méthode", "Records management"],
        "excerpt": "Une méthode en six étapes pour passer de dossiers partagés désordonnés à une structure commune.",
        "body": """
<p>Le plan de classement est la colonne vertébrale de votre gestion documentaire. Sans lui, chaque service range à sa façon et les documents se perdent. Voici une méthode simple pour construire le vôtre.</p>
<h2 id="1">1. Partir des activités, pas de l'organigramme</h2>
<p>Les organigrammes changent ; les activités restent. Classez d'abord par grandes fonctions : direction, finances, ressources humaines, juridique, commercial, achats, technique, archives historiques.</p>
<h2 id="2">2. Descendre en séries</h2>
<p>Pour chaque fonction, listez les séries de documents. Exemple pour la Direction financière : comptabilité, factures clients, factures fournisseurs, états financiers, déclarations fiscales, audits.</p>
<h2 id="3">3. Définir les types de documents</h2>
<p>Pour chaque série : quels types de documents la composent ? Facture, bon de commande, bon de livraison, relevé…</p>
<h2 id="4">4. Attacher les règles</h2>
<p>Pour chaque série ou type : durée de conservation, événement déclencheur, sort final, niveau de confidentialité, propriétaire, service responsable. Les durées se fixent avec un juriste.</p>
<h2 id="5">5. Choisir les métadonnées</h2>
<p>Quelles informations permettront de retrouver le document ? Titre, auteur, dates, numéro, client, projet, montant… Limitez-vous à ce qui sert réellement.</p>
<h2 id="6">6. Tester, valider, versionner</h2>
<p>Testez le plan sur un échantillon réel de documents, ajustez-le avec les services, faites-le valider et donnez-lui un numéro de version. Il évoluera avec l'organisation.</p>
<div class="notice"><p>Notre service <a href="~/services/conseil/">Conseil</a> accompagne cette démarche avec un archiviste, puis paramètre le plan dans ARCHIVA360.</p></div>""",
    },
    {
        "slug": "guide-metadonnees-essentielles",
        "title": "Guide : les métadonnées essentielles d'un document archivé",
        "cat": ("guides", "Guides"), "date": "2026-08-20", "cover": "cover-guide-metadonnees.png", "read": 6,
        "tags": ["Métadonnées", "ISO 23081", "Méthode"],
        "excerpt": "Sans métadonnées, un document archivé est introuvable et sans contexte. Voici celles qu'il ne faut jamais oublier.",
        "body": """
<p>Les métadonnées sont les informations qui décrivent un document : qui l'a produit, quand, pourquoi, où il se trouve, combien de temps le garder. Elles font partie des concepts fondamentaux du records management selon l'ISO 15489 ; l'ISO 23081 leur est entièrement consacrée.</p>
<h2 id="identification">Identification</h2>
<p>Identifiant unique, titre, type de document, numéro, version.</p>
<h2 id="contexte">Contexte</h2>
<p>Auteur, service, propriétaire, client ou projet concerné, dossier de rattachement.</p>
<h2 id="dates">Dates</h2>
<p>Date de création, de réception, de capture, d'archivage. La bonne date déclenche la bonne durée de conservation.</p>
<h2 id="gestion">Gestion</h2>
<p>Classement, niveau de confidentialité, règle de conservation, début et fin de conservation, statut.</p>
<h2 id="technique">Technique et preuve</h2>
<p>Format de fichier, taille, empreinte (checksum), statut OCR, signature électronique, horodatage.</p>
<h2 id="localisation">Localisation</h2>
<p>Emplacement numérique et, pour les dossiers hybrides, localisation physique de l'original.</p>
<div class="notice"><p>Bonne nouvelle : dans ARCHIVA360, une grande partie de ces métadonnées est calculée ou proposée automatiquement (dates, empreinte, format, extraction par l'IA). L'utilisateur valide.</p></div>""",
    },
]

CATEGORIES = [("guides", "Guides"), ("securite", "Sécurité"), ("conformite", "Conformité"), ("innovation", "Innovation"),
              ("numerisation", "Numérisation"), ("records-management", "Records management"), ("preservation", "Préservation")]
