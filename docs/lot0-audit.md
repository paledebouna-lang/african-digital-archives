# Lot 0 — Audit de l'existant et plan de mise à niveau

Rapport demandé par `docs/dossier/00-LISEZ-MOI.md` (Prompt 0). Aucun code n'a été écrit pour ce lot.
Date : 25 novembre 2026. Dépôt audité : `paledebouna-lang/african-digital-archives`, branche `main`.

## 1. Ce que contient réellement le dépôt

| Élément | Réalité du code | Volume |
|---|---|---|
| Site adarchives.pro | **Site statique** : 86 pages HTML générées par un script Python (`tools/build.py`, `tools/ada/*.py`), hébergées sur GitHub Pages. Aucun serveur applicatif, aucune base de données. | 20 modules Python, ~4 000 lignes |
| Comptes en ligne (`/archiva360/connexion`, `/archiva360/espace`) | Appwrite Cloud (offre gratuite, Francfort) : connexion, invitations, rôles (5), mot de passe oublié. E-mails envoyés par une fonction Appwrite via Brevo. Une seule équipe (`archiva360`) = une seule organisation. | `archiva360-auth.js` ~470 lignes, fonction ~170 lignes |
| Démo interactive (`/archiva360/demo-interactive`) | Application **100 % navigateur** : données en IndexedDB sur le poste du visiteur, jamais partagées. Dépôt, OCR (Tesseract.js), métadonnées proposées, recherche en langage naturel, versions, empreintes SHA-256, versement, règles de conservation, gel juridique, élimination avec certificat, boîtes et QR codes, journal d'audit chaîné, sauvegarde JSON. | `archiva360-demo.js` ~2 600 lignes |
| Application installable | PWA (manifeste + service worker). Ouvre la connexion, l'espace et la démo hors ligne. | — |
| ARCHIVA Academy | 6 niveaux + parcours dirigeant, quiz, examens, certificats vérifiables ; progression dans le navigateur. | 6 modules Python |
| Tests | Playwright : 39 tests site, 31 tests comptes (contre un faux Appwrite et un faux Brevo). | 504 lignes |
| Composants tiers | Appwrite (BSD-3), pdf.js 3.11 (Apache-2.0), Tesseract.js 5.1 (Apache-2.0), qrcode-generator 1.4 (MIT), police Inter (OFL), Playwright pour les tests (Apache-2.0). Tous permissifs. | — |

**Conclusion : il n'existe pas aujourd'hui de logiciel ARCHIVA360 au sens du dossier.** Il existe un site vitrine abouti, un service de comptes et une maquette fonctionnelle riche mais mono-poste. Rien de ce qui touche aux documents n'est multi-utilisateur, ni stocké côté serveur.

## 2. État réel des exigences (remplace la colonne « État » de `02-EXIGENCES.md`)

Légende : **Prod** = en production sur adarchives.pro ; **Démo** = présent dans la démo mono-poste, logique réutilisable ; **Absent** = rien.

| Groupe | Prod | Démo | Absent | Remarques |
|---|---|---|---|---|
| A. Socle (A1–A13) | A8 partiel (site FR seulement, EN annoncé) | A9 (tableau de bord fixe), A13 (plan de classement d'exemple) | A1–A7, A10 (PWA ≠ store), A11, A12 | Une seule organisation ; pas d'organigramme ; pas d'instances |
| B. Courrier (B1–B15) | — | B2 (QR codes sur boîtes, pas sur courriers) | B1, B3–B15 | Aucune notion de courrier |
| C. Archivage (C1–C5) | — | C1, C2 (règles de conservation, DUA, sort final, gel, certificat d'élimination), C3 partiel (boîtes, emplacements) | C4, C5 | Logique métier la plus avancée de l'existant |
| D. Capture (D1–D12) | — | D5 partiel (extraction de factures/contrats par règles), D12 partiel (OCR navigateur, fra+eng) | D1–D4, D6–D11 | Pas de serveur de capture, pas d'e-mail, pas de scanner |
| E. Documents (E1–E19) | — | E2 (versions, empreintes), E9 partiel (identifiant, horodatage), E16/E17 partiels (recherche plein texte et par critères sur l'index local), E11 (verrou simple) | E1, E3–E8, E10, E12–E15, E18, E19 | Types et métadonnées codés en dur, non administrables |
| F. Signature (F1–F11) | — | — | F1–F11 | Rien. Une page « signature » descriptive sur le site |
| G. Processus (G1–G8) | — | — | G1–G8 | Rien. Page descriptive seulement |
| H. Notifications, sécurité, technique (H1–H11) | H3 partiel (HTTPS GitHub Pages), H6 partiel (5 rôles, droits en interface seulement), H7 partiel (journal chaîné en démo), H10 partiel (Utilisateurs et rôles) | H8 (QR boîtes) | H1, H2, H4, H5, H9, H11 | Les règles de droits de la démo sont appliquées **dans le navigateur**, contraire au principe 4 de l'architecture |
| I. Modules métier | — | I4 partiel (extraction) | I1, I2, I3, I5 | — |
| J. Mobile | PWA | — | Applications natives sur les stores | La PWA est refusée par le CCAT (12) |

Décompte sur les 160 lignes du tableau de conformité : **environ 12 couvertes en production, 30 démontrées en démo mono-poste, 118 absentes.**

## 3. Conformité à `03-ARCHITECTURE.md`

| Contrainte | Respectée ? | Écart |
|---|---|---|
| Monolithe modulaire serveur | Non | Pas de serveur ; logique dans le navigateur |
| Tout se paramètre en web | Non | Types, métadonnées, règles codés en dur dans `archiva360-demo.js` |
| Sur site d'abord, sans dépendance externe obligatoire | Non | GitHub Pages, Appwrite Cloud, Brevo, CDN (pdf.js, Tesseract) sont tous externes et obligatoires |
| Sécurité côté serveur | Non | Droits appliqués côté client dans la démo ; Appwrite applique les siens, mais ne connaît pas les documents |
| PostgreSQL + couche d'accès multi-SGBD | Non | Aucune base |
| Fichiers hors base, NFS/CIFS/SMB | Non | IndexedDB |
| Moteur de recherche unique multilingue | Non | Index local en mémoire |
| Mobile natif publiable | Non | PWA |
| Multi-instances étanches | Non | Une équipe Appwrite |
| LDAP/AD, SSO, MFA | Non | Appwrite e-mail + mot de passe |
| Journal d'audit en ajout seul, chaîné, hors de portée de l'application | Partiel | Chaîné, mais stocké dans le navigateur de l'utilisateur, donc modifiable |
| PDF/A, TIFF, CMIS, SEDA, SAML, OIDC, LDAP, IMAP/POP/SMTP, BPMN 2.0 | Non | Aucun |
| Trois environnements, HA, supervision, sauvegardes testées | Non | — |
| Licences : produit propriétaire, composants permissifs listés | Partiel | Composants permissifs ; aucun `docs/licences.md` ; le site s'appuie sur Appwrite (BSD-3), remplaçable |

**Verdict : rien de l'existant ne peut servir de socle serveur.** Ce qui se réutilise : la charte graphique et les écrans (vocabulaire, navigation, composants), la logique métier de conservation, d'audit chaîné, d'extraction et de recherche (à porter côté serveur), l'Academy comme support de formation, les tests Playwright comme méthode.

## 4. Plan de mise à niveau

### 4.1 Décision de structure : un second dépôt, privé

Le dépôt actuel est **publié tel quel** sur GitHub Pages : tout fichier ajouté à sa racine devient public sur adarchives.pro. Y placer le code serveur d'un produit propriétaire exposerait le code source. Proposition :

- `african-digital-archives` (public) : reste le site vitrine, l'Academy, la démo, les comptes. Inchangé.
- **`archiva360`** (nouveau dépôt **privé**) : le produit. Structure : `server/` (application), `web/` (interface), `mobile/` (applications), `deploy/` (installeur, conteneurs, trois environnements), `docs/` (dossier, conformité, avancement, licences, guides), `packs/` (packs sectoriels importables).

Le `CLAUDE.md` du dossier ira à la racine de ce nouveau dépôt. Le site public gardera le sien.

### 4.2 Pile technique proposée (à valider avant le lot 1)

Le dossier demande de conserver la pile existante si elle tient les contraintes : ce n'est pas le cas. Proposition, choisie pour le « sur site », la légèreté sur connexions lentes, les SGBD commerciaux et la richesse des bibliothèques documentaires :

| Couche | Choix | Pourquoi |
|---|---|---|
| Serveur | **Python 3.12 + Django 5** (monolithe modulaire : une « app » Django par module A–O) | ORM multi-SGBD natif : PostgreSQL, **Oracle** en standard, **SQL Server** via `mssql-django` ; administration, migrations, internationalisation (FR/EN) intégrées ; écosystème documentaire (OCR, PDF, LDAP, SAML, OIDC, IMAP) mature ; même langage que l'outillage actuel |
| Base | **PostgreSQL 16** par défaut | Recherche plein texte intégrée au départ ; réplication pour la HA |
| Tâches de fond | **Celery + Redis** (ou RQ) | Capture, OCR, conversion PDF/A, indexation, e-mails, récapitulatifs : séparés du serveur web comme l'exige le CCAT (serveur de capture) |
| OCR et PDF | Tesseract (serveur) + OCRmyPDF, Ghostscript, LibreOffice headless pour PDF/A | Tout local, multilingue |
| Recherche | PostgreSQL FTS au lot 2 ; **OpenSearch** optionnel au lot 12 pour les gros volumes | Un seul moteur pour documents et données |
| Interface web | **Django templates + HTMX + Alpine.js**, charte ADA existante | Pages légères, fonctionnent sur connexions lentes et navigateurs modestes ; pas de compilation front lourde. Le concepteur de circuits (lot 4) et les tableaux de bord à widgets (lot 6) utiliseront des composants JavaScript dédiés |
| API | **Django REST Framework** + OpenAPI, SDK généré (Python, JavaScript), console de test intégrée | Exigences E12, lot 10 |
| Identité | django-auth-ldap, python3-saml, mozilla-django-oidc, django-otp (MFA) | Lot 10 |
| Signature | pyHanko (PAdES, CRL/OCSP) côté serveur ; **agent de signature poste de travail** (petit programme Windows) pour la clé USB/carte à puce PKCS#11 et le code PIN, que le navigateur ne peut pas atteindre | Lot 7 ; connecteur ARTCI à écrire avec le prestataire retenu |
| CMIS | Serveur CMIS 1.1 (Browser Binding) écrit dans le monolithe | Lot 10 |
| Mobile | **Flutter** (Android + iOS depuis un seul code) consommant l'API | Lot 11 ; publication sur les stores avec les comptes développeur d'ADA |
| Déploiement | Conteneurs (Docker Compose pour un site ; Kubernetes optionnel pour la HA), installeur scripté, Nginx TLS 1.2+ | Lot 12 |
| Tests | pytest + Playwright, intégration continue GitHub Actions, tests d'étanchéité inter-instances automatiques | Dès le lot 1 |

Alternative étudiée : Node.js/TypeScript (NestJS + Prisma). Écartée car Prisma ne couvre pas Oracle de façon stable, et parce que l'écosystème documentaire (OCR, PDF/A, SAML, LDAP, CMIS) est plus fourni en Python. Si ADA préfère JavaScript pour ses recrutements, c'est un choix défendable ; à trancher maintenant, pas après le lot 1.

Composants ci-dessus : tous sous licence permissive (BSD, MIT, Apache-2.0, LGPL pour quelques bibliothèques utilisées sans modification) ; `docs/licences.md` sera créé au lot 1 avec, pour chaque composant d'infrastructure libre, l'équivalent commercial acceptable (PostgreSQL → Oracle/SQL Server ; Redis → Redis Enterprise ; OpenSearch → Elastic ; Nginx → Nginx Plus/F5).

### 4.3 Lot 1 — ce qui sera livré (après validation de 4.1 et 4.2)

1. Dépôt privé `archiva360`, `CLAUDE.md`, intégration continue, environnement de développement en une commande.
2. Modèle de données du socle : instances, organisations/organigramme (arbre, codes, journalisation), utilisateurs, groupes, rôles, profils cumulables, permissions par action, deux familles d'administrateurs.
3. Étanchéité : identifiant d'instance sur chaque table métier, filtrage automatique côté serveur, tests d'accès croisés.
4. Journal d'audit : table en ajout seul, chaînage SHA-256, vérification périodique, écriture interdite à l'application hors du service d'audit.
5. Stockage de fichiers hors base avec empreinte à l'entrée, chemin par instance, montages NFS/CIFS/SMB documentés.
6. API REST documentée (OpenAPI), authentification par session et par jeton.
7. Interface web FR/EN : connexion, administration des instances, de l'organigramme, des utilisateurs et des droits, journal d'audit consultable.
8. `docs/conformite.md` (160 lignes, état et preuve), `docs/avancement.md`, `docs/licences.md`, guide administrateur du lot.

Durée estimée du lot 1 : 3 à 5 semaines avec une personne qui relit et teste.

## 5. Questions avant de commencer le lot 1

1. **Dépôt privé séparé** : d'accord pour créer `archiva360` (privé) et y mettre le produit, en laissant le site public tel quel ?
2. **Pile technique** : Django/PostgreSQL (recommandé) ou Node/TypeScript ?
3. **Hébergement de développement** : où tourneront les serveurs de développement et de recette (un VPS loué par ADA, un serveur chez vous, ou mon environnement de session pour commencer) ? Les lots exigent une recette « sur un vrai serveur, avec de vrais fichiers ».
4. **Nom des rôles** : garder les cinq rôles actuels (administrateur, archiviste, records manager, employé, auditeur) comme profils de départ, complétés par les profils UFHB (bureau d'ordre, signataire, administrateur fonctionnel, administrateur technique) ?
5. **Fichiers manquants du dossier** : `CLAUDE.md`, `05-PROMPTS.md` et `06-HORS-CODE.md` n'ont pas été transmis. Le lot 1 démarre avec le Prompt 1 ; merci de les joindre.

## 6. Ce qui reste vrai quelles que soient les réponses

- La démo interactive du site public reste en ligne comme argument commercial ; elle sera remplacée, le moment venu, par une instance de démonstration du vrai produit.
- Les comptes Appwrite servent au site public ; le produit aura sa propre gestion d'identité (lot 1), compatible LDAP/SSO (lot 10).
- Les démarches hors code (statut d'éditeur, partenaire de signature agréé ARTCI, comptes développeur Google et Apple, matériel, références) démarrent maintenant : elles sont sur le chemin critique.
