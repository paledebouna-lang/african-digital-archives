# E-mails ARCHIVA360 en français (modèles Appwrite)

Dans la console Appwrite : **Auth → Templates**. Pour chaque modèle ci-dessous, choisissez le type d'e-mail,
puis la langue **French (fr)**, collez le sujet et le message, et enregistrez. Appwrite utilise automatiquement
la version française pour les comptes dont la langue est `fr` ; le site ARCHIVA360 la demande pour tous ses envois.

Champs communs à tous les modèles :

- **Sender name** : `ARCHIVA360 — African Digital Archives`
- **Sender email** : laissez la valeur proposée par Appwrite, sauf si vous avez configuré votre propre serveur
  d'envoi (Settings → SMTP) avec une adresse `@adarchives.pro`.
- **Reply to** : `contact@adarchives.pro`

Les mots entre doubles accolades (`{{user}}`, `{{team}}`, `{{redirect}}`, `{{project}}`) sont remplacés par
Appwrite au moment de l'envoi : ne les modifiez pas.

---

## 1. Invitation (type « Invitation »)

**Sujet**

```
Invitation à rejoindre {{team}} sur ARCHIVA360
```

**Message**

```
Bonjour {{user}},

{{owner}} vous invite à rejoindre l'espace « {{team}} » sur ARCHIVA360, la plateforme d'archivage
et de gestion documentaire d'African Digital Archives.

Pour activer votre compte et choisir votre mot de passe, cliquez sur ce lien :

{{redirect}}

Ce lien est personnel : ne le transmettez pas. Si vous n'attendiez pas cette invitation,
vous pouvez ignorer ce message.

Bien cordialement,
L'équipe African Digital Archives
https://adarchives.pro
```

## 2. Mot de passe oublié (type « Password recovery » / « Recovery »)

**Sujet**

```
Réinitialisation de votre mot de passe ARCHIVA360
```

**Message**

```
Bonjour {{user}},

Vous avez demandé à réinitialiser le mot de passe de votre compte ARCHIVA360.
Pour choisir un nouveau mot de passe, cliquez sur ce lien :

{{redirect}}

Ce lien expire dans une heure. Si vous n'êtes pas à l'origine de cette demande,
ignorez ce message : votre mot de passe actuel reste valable.

Bien cordialement,
L'équipe African Digital Archives
https://adarchives.pro
```

## 3. Vérification d'adresse e-mail (type « Verification »)

Non utilisé par le site pour l'instant ; à renseigner tout de même pour éviter un e-mail en anglais si la
fonction est activée plus tard.

**Sujet**

```
Confirmez votre adresse e-mail ARCHIVA360
```

**Message**

```
Bonjour {{user}},

Merci de confirmer l'adresse e-mail de votre compte ARCHIVA360 en cliquant sur ce lien :

{{redirect}}

Si vous n'avez pas créé de compte, ignorez ce message.

Bien cordialement,
L'équipe African Digital Archives
https://adarchives.pro
```

## 4. Connexion par lien (type « Magic URL ») et code de sécurité (type « OTP »)

Non utilisés par le site. Si Appwrite vous demande ces modèles, utilisez :

**Sujet** : `Votre lien de connexion ARCHIVA360`
**Message** :

```
Bonjour,

Voici votre lien de connexion à ARCHIVA360 : {{redirect}}

Il est valable quelques minutes. Si vous n'avez pas demandé à vous connecter, ignorez ce message.

L'équipe African Digital Archives
```

---

## Vérifier

1. Dans l'espace ARCHIVA360, « Utilisateurs et rôles », invitez une adresse que vous contrôlez.
2. Vous devez recevoir l'e-mail n° 1 en français, et le lien doit ouvrir la page « Bienvenue dans ARCHIVA360 ».
3. Sur la page de connexion, « Mot de passe oublié » : vous devez recevoir l'e-mail n° 2.

Si un e-mail arrive encore en anglais, vérifiez que la langue **fr** est bien sélectionnée dans le modèle
(et non seulement la langue par défaut), puis enregistrez à nouveau.
