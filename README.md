# African Digital Archives (ADA) — site web

Site institutionnel d'ADA et de la plateforme ARCHIVA360, publié en statique (GitHub Pages).
Le thème reprend la structure d'un site WordPress (`wp-content/themes/ada-archives/`, blocs Gutenberg,
fil d'Ariane Yoast, formulaires Contact Form 7, bandeau cookies).

## Modifier le site

Les pages sont générées à partir des fichiers Python de `tools/ada/` :

| Fichier | Contenu |
|---|---|
| `core.py` | Réglages (`SITE` : e-mail de contact, URL publique), menu, en-tête, pied de page |
| `pages_main.py` | Accueil, Entreprise, Contact, Espace client, pages légales, recherche, 404 |
| `pages_solutions.py` | Solutions (GED, SAE, records management…) |
| `pages_archiva.py` | ARCHIVA360 : modules, ARCHIVA AI, ARCHIVA GO, offres et tarifs, démo |
| `pages_sectors.py` / `pages_services.py` | Secteurs et services |
| `posts.py` / `pages_resources.py` | Articles du blog, guides, livres blancs, glossaire, Health Check |
| `whitepapers.py` / `whitepaper_pdf.py` | Texte des livres blancs et mise en page PDF |
| `academy_n1_n2.py`, `academy_n3_n4.py`, `academy_n5_n6.py` | Cours, quiz et questions d'examen des 6 niveaux de l'Academy |
| `pages_academy.py` | Catalogue, lecteur de cours, certificats, vérification |
| `pages_demo.py` | Démo interactive ARCHIVA360 (application : `wp-content/themes/ada-archives/assets/js/archiva360-demo.js`) |
| `mockups.py` / `covers.py` | Captures d'écran ARCHIVA360 et illustrations |

Après modification :

```bash
python3 tools/build.py            # régénère toutes les pages
python3 tools/build.py --pdf      # régénère aussi les PDF des livres blancs (Node + Playwright requis)
python3 tools/build.py --images   # régénère aussi les captures, illustrations et PDF
node tools/test_site.js           # rejoue les tests automatiques (site servi sur http://localhost:8765)
```

## Fonctions interactives

- **ARCHIVA Academy** (`/academy/`) : 6 niveaux, 24 modules, quiz corrigés (75 %), examen final de 15 questions
  tirées au hasard (70 %), certificat imprimable avec code de vérification SHA-256 (`/academy/verifier/`).
  La progression est enregistrée dans le navigateur de l'apprenant.
- **Démo interactive ARCHIVA360** (`/archiva360/demo-interactive/`) : import de documents, extraction de texte (PDF,
  OCR des images via Tesseract chargé à la demande), métadonnées proposées, recherche en langage naturel, versions,
  empreintes et contrôle d'intégrité, versement au SAE, règles de conservation, Retention Center, gel juridique,
  élimination avec certificat, archives physiques et QR codes, rôles, journal d'audit chaîné, conformité,
  sauvegarde et restauration. Les données restent dans le navigateur (IndexedDB).
- **Comptes en ligne ARCHIVA360** (`/archiva360/connexion/`, `/archiva360/espace/`) : connexion, mot de passe
  oublié, invitation par e-mail, « Mon compte » et « Utilisateurs et rôles » (Administrateur, Archiviste, Records
  manager, Employé, Auditeur). Les comptes sont hébergés sur Appwrite Cloud (offre gratuite) ; voir ci-dessous.
- **Application installable ARCHIVA GO / ARCHIVA360** (PWA) : `archiva360/manifest.webmanifest` et `archiva360/sw.js`
  sont générés par `tools/build.py`. Bouton « Installer l'application » sur Android, mode d'emploi sur iPhone,
  écrans disponibles hors connexion. Icônes : `wp-content/uploads/2026/09/archiva360-app-*.png`.
- **Document Health Check**, recherche interne, glossaire filtrable, démonstration d'empreinte.

## Réglages (`tools/ada/core.py` → `SITE`)

- `email` : adresse de contact (actuellement `assa@eletude.org`).
- `form_endpoint` : adresse d'un service de réception de formulaires (Formspree ou équivalent). Vide, les formulaires
  ouvrent la messagerie du visiteur avec un message prérempli.
- `appwrite` : projet Appwrite des comptes en ligne (`endpoint`, `project`, `team`). Vide, la page de connexion
  indique que les comptes sont en cours d'activation.
- `social` : liens LinkedIn, Facebook, YouTube, WhatsApp. Seuls les liens renseignés s'affichent.

Les informations légales de la société (forme, capital, RCCM, compte contribuable, directeur de la publication, déclaration ARTCI) se complètent dans `tools/ada/pages_legal.py` → `COMPANY`.

## Comptes en ligne (Appwrite, gratuit)

1. Créez un compte sur [cloud.appwrite.io](https://cloud.appwrite.io) (offre *Free*), puis un projet « ARCHIVA360 »
   (région Francfort par exemple). Notez son **Project ID** et son **API endpoint** (Settings).
2. Dans le projet, *Overview → Apps → Add app → Web* : nom « Site ADA », hostname `paledebouna-lang.github.io`
   (ajoutez aussi votre futur nom de domaine). Sans cela, le navigateur refuse les connexions.
3. *Overview → API keys → Add API key* avec les portées `users.read`, `users.write`, `teams.read`, `teams.write`.
   Gardez-la pour vous : elle ne sert qu'à l'installation et ne doit jamais être publiée.
4. Sur votre ordinateur (Node 18 ou plus), à la racine du dépôt :

   ```sh
   APPWRITE_ENDPOINT=https://fra.cloud.appwrite.io/v1 APPWRITE_PROJECT=<Project ID> \
   APPWRITE_API_KEY=<clé API> ADMIN_EMAIL=assa@eletude.org ADMIN_NAME="Votre nom" \
   node tools/appwrite_setup.mjs
   ```

   Le script crée l'équipe « archiva360 » et le compte administrateur, puis affiche un mot de passe provisoire.
5. Renseignez `endpoint` et `project` dans `SITE["appwrite"]`, régénérez (`python3 tools/build.py`) et publiez.
6. Connectez-vous sur `/archiva360/connexion/`, changez le mot de passe (« Mon compte »), puis invitez les autres
   personnes depuis « Utilisateurs et rôles ». Chacune reçoit un e-mail et choisit son mot de passe.

Facultatif : dans *Auth → Templates*, personnalisez en français les e-mails d'invitation et de récupération.
Tests : `node tools/test_accounts.js` rejoue tout le parcours contre un faux serveur Appwrite local.
