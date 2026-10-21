# E-mails ARCHIVA360 depuis contact@adarchives.pro

Par défaut, Appwrite envoie les invitations et les e-mails « mot de passe oublié » depuis une adresse générique.
Cette fonction Appwrite les envoie à la place depuis **contact@adarchives.pro**, via Brevo (gratuit : 300 e-mails par jour),
avec les textes d'ADA. Tout reste sur les offres gratuites d'Appwrite et de Brevo.

Comptez une trentaine de minutes. Trois étapes : Brevo, la fonction dans Appwrite, le site.

## 1. Brevo (service d'envoi)

1. Créez un compte gratuit sur https://www.brevo.com (nom de l'entreprise : African Digital Archives).
2. Menu **Expéditeurs, domaines et IP dédiées → Expéditeurs** : **Ajouter un expéditeur** avec
   `contact@adarchives.pro`. Brevo envoie un e-mail de confirmation à cette adresse : cliquez sur le lien.
3. *(Recommandé, pour éviter les indésirables)* **Domaines → Ajouter un domaine** : `adarchives.pro`.
   Brevo affiche des enregistrements DNS (TXT « brevo-code », DKIM, parfois DMARC) à créer dans la zone DNS LWS,
   puis **Vérifier**. Cela peut prendre quelques heures.
4. Menu en haut à droite (votre nom) → **SMTP & API → Clés API → Générer une nouvelle clé API**.
   Nommez-la `archiva360` et **copiez la clé** : elle ne sera plus affichée. Ne la partagez avec personne.

## 2. La fonction dans Appwrite

1. Console Appwrite, projet ARCHIVA360, menu **Functions → Create function**.
   - Choisissez **Manual** (ou « Create manually »), nom `archiva360-mail`, runtime **Node.js 20** (ou plus récent).
   - Entrypoint : `src/main.js`. Laissez la commande de build vide.
2. Onglet **Settings** de la fonction :
   - **Execute access** : `Any` (la fonction vérifie elle-même qui l'appelle ; un visiteur non connecté ne peut
     que demander un e-mail de réinitialisation, comme sur n'importe quel site).
   - **Timeout** : 30 secondes.
   - **Environment variables**, ajoutez :

     | Variable | Valeur |
     |---|---|
     | `BREVO_API_KEY` | la clé Brevo copiée à l'étape 1.4 |
     | `APPWRITE_API_KEY` | une clé API Appwrite (voir ci-dessous) |
     | `SENDER_EMAIL` | `contact@adarchives.pro` |
     | `SENDER_NAME` | `ARCHIVA360 — African Digital Archives` |
     | `SITE_URL` | `https://adarchives.pro` |
     | `TEAM_ID` | `archiva360` |
     | `ORG_NAME` | `African Digital Archives` |

     Clé API Appwrite : menu **Overview → API keys → Add API key**, nom `archiva360-mail`, expiration « Never »,
     portées **users.read, users.write, teams.read, teams.write**. Copiez la clé dans la variable ci-dessus.
3. Onglet **Deployments → Create deployment → Manual** : déposez le fichier `tools/appwrite-function.tar.gz`
   (téléchargeable depuis le dépôt GitHub : ouvrez le fichier, bouton « Download »). Activez « Activate deployment
   after build ». Attendez le statut **Ready**.
4. En haut de la page de la fonction, copiez le **Function ID** (une suite de lettres et chiffres).

## 3. Le site

Dans `tools/ada/core.py`, `SITE["appwrite"]["function"]` : collez le Function ID. Régénérez (`python3 tools/build.py`)
et publiez. Sans cet identifiant, le site continue d'utiliser les e-mails génériques d'Appwrite : rien ne casse.

## Vérifier

1. Sur https://adarchives.pro/archiva360/espace/, « Utilisateurs et rôles », invitez une adresse que vous contrôlez.
   L'e-mail doit arriver de `contact@adarchives.pro`, en français, avec le bouton « Activer mon compte ».
2. Sur la page de connexion, « Mot de passe oublié » avec la même adresse : e-mail « Réinitialisation de votre mot de passe ».
3. En cas d'échec, la console Appwrite, **Functions → archiva360-mail → Executions**, montre chaque exécution et son
   message d'erreur (clé Brevo refusée, expéditeur non validé, clé API Appwrite insuffisante…).

## Comment ça marche

- **Invitation** : la fonction crée le compte (sans mot de passe), l'ajoute à l'équipe avec le rôle choisi, note
  l'invitation « en attente » dans les préférences de l'équipe, génère un jeton valable 7 jours et envoie l'e-mail.
  Le lien ouvre une session puis la page « choisissez votre mot de passe ». Un administrateur peut renvoyer l'invitation.
- **Mot de passe oublié** : jeton valable 1 heure, à usage unique ; la fonction enregistre le nouveau mot de passe et
  ferme les autres sessions. La réponse est la même que l'adresse existe ou non.
- Seuls les administrateurs (rôle `owner` de l'équipe) peuvent inviter : la fonction le vérifie à partir de l'identité
  transmise par Appwrite, pas à partir de ce que le navigateur déclare.
- Mettre à jour la fonction : `cd tools/appwrite-function && tar -czf ../appwrite-function.tar.gz package.json src`,
  puis un nouveau déploiement manuel.
- Tests : `node tools/test_accounts.js` exécute la fonction contre un faux Appwrite et un faux Brevo.
