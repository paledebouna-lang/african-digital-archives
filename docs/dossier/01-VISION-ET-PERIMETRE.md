# 01 — Vision et périmètre

## Le produit visé

ARCHIVA360 devient une plateforme unique, d'un seul éditeur (ADA), qui couvre toute la chaîne documentaire : capture, courrier, documents, processus, signature, archivage, pilotage. Elle s'installe sur site, en cloud privé ou en SaaS, à partir de la même base de code.

Référence de départ : le cahier des charges de l'UFHB (`annexes/CCAT-UFHB.txt`), qui est représentatif des appels d'offres publics d'Afrique francophone pour ce type de solution.

## Publics

- Administrations, ministères, collectivités, établissements publics.
- Universités et grandes écoles.
- Banques, assurances, microfinance.
- Santé, industrie, énergie, immobilier, cabinets juridiques, ONG.

## Modules du socle (exigés par l'UFHB)

| # | Module | Rôle |
|---|---|---|
| A | Capture multicanal | Papier, e-mail, fichiers d'applications métier, XML, formulaires web, fax numérique ; OCR ; reconnaissance automatique (LAD/RAD) ; casiers virtuels |
| B | Courrier (GEC) | Courrier arrivée, départ, interne ; bureaux d'ordre ; registres ; accusés ; suivi |
| C | Documents (GED) | Types, métadonnées, formulaires, thésaurus, versions, réservation, dossiers, modèles, recherche |
| D | Processus (BPM / workflow) | Concepteur graphique, formulaires, délais, délégations, intérim, suivi |
| E | Automatisation (RPA) | Robots pour les tâches répétitives, déclencheurs, supervision |
| F | Parapheur et signature | Visa, annotation, signature simple et avancée, en masse, co-signature, vérification |
| G | Archivage et records management | Plan de classement, calendrier de conservation, bordereaux, export SEDA, archives physiques |
| H | Contrats | Cycle de vie, échéances, renouvellements |
| I | Appels d'offres | Dossiers, étapes, commissions, décisions |
| J | Factures | Réception, extraction, rapprochement, validation |
| K | Pilotage | Tableaux de bord à widgets, indicateurs, générateur de rapports |
| L | Mobile | Applications Android et iOS publiées sur les stores |
| M | Administration | Organigramme, instances, droits, référentiels, paramétrage complet en web |
| N | Interopérabilité | LDAP / Active Directory, SSO, CMIS, webservices, SDK, Outlook, Word |
| O | Aide en ligne | Documentation, recherche, tutoriels vidéo |

Les 20 modules déjà annoncés sur adarchives.pro (tableau de bord, documents, dossiers, numérisation, OCR + IA, recherche, Archive AI, workflow, courrier, signature, coffre-fort, records management, centre de conservation, archives physiques, QR code, journal d'audit, centre de sécurité, sauvegarde, portail public, administration) sont conservés et rangés sous ces modules.

## Packs sectoriels (autres logiciels que d'autres structures demandent)

Un pack n'est pas un nouveau logiciel. C'est un jeu de configuration livré avec le produit : types de dossiers, métadonnées, formulaires, circuits, modèles de documents, règles de conservation, tableaux de bord. Le moteur doit donc permettre d'importer et d'exporter un pack sans toucher au code.

| Pack | Contenu | Demandeurs typiques |
|---|---|---|
| Instances et délibérations | Ordres du jour, convocations, séances, votes, procès-verbaux, suivi des décisions | Conseils d'université, conseils d'administration, collectivités |
| Guichet et démarches en ligne | Formulaires publics, dépôt de pièces, suivi par l'usager, réclamations | Administrations, universités, banques |
| Dossier du personnel | Dossier agent, pièces, contrats, congés, évaluations | Toutes structures |
| Scolarité | Dossier étudiant, inscriptions, relevés, diplômes, authentification de diplôme par QR code | Universités, écoles |
| Marchés publics | Du besoin à l'attribution, pièces, commissions, contrats, exécution | Administrations, établissements publics |
| Comptabilité fournisseurs | Bon de commande, réception, facture, bon à payer, rapprochement | Toutes structures |
| Dossier client et conformité | Entrée en relation, pièces d'identité, échéances de révision | Banques, assurances, microfinance |
| Sinistres et crédits | Instruction de dossiers avec pièces et décisions | Assurances, banques |
| Dossier juridique et contentieux | Affaires, pièces, échéances, actes | Directions juridiques, cabinets |
| Qualité | Procédures, versions applicables, diffusion contrôlée, non-conformités | Industrie, santé, laboratoires |
| Foncier et immobilier | Titres, baux, plans, dossiers par bien | Immobilier, domaines |
| Patrimoine et bibliothèque numérique | Fonds historiques, notices, consultation publique | Archives nationales, musées, bibliothèques |
| Archivage électronique à valeur probante | Coffre, empreintes, horodatage, journal scellé, réversibilité | Tous secteurs réglementés |

Ordre conseillé : Instances et délibérations, Guichet, Marchés publics, Scolarité, puis les autres selon les appels d'offres visés.

## Ce qui rend le produit compétitif

- Répondre « oui, en standard » à chaque ligne du tableau de conformité, avec un écran à montrer.
- Un paramétrage complet en web, démontrable en direct devant une commission.
- Une installation sur site documentée et répétable en une journée.
- Le français d'abord, l'anglais ensuite ; les référentiels locaux (ARTCI, textes ivoiriens et UEMOA) pris en compte.
- Un poids léger : fonctionnement correct sur des serveurs modestes et des connexions lentes.
