# 03 — Architecture et choix techniques

Ces choix sont des contraintes. Le Prompt 0 vérifie si le code existant les respecte et propose, le cas échéant, un plan de mise en conformité avant tout nouveau module.

## Principes

1. **Monolithe modulaire.** Une application serveur, des modules aux frontières nettes, une seule base de code et un seul numéro de version. Pas de microservices au départ. Seuls la capture/OCR et l'indexation tournent en processus séparés, car le cahier des charges demande un serveur de capture distinct.
2. **Tout se paramètre.** Types de documents, métadonnées, formulaires, circuits, modèles, casiers, échéances, droits, rapports et tableaux de bord sont des données, modifiables en web sans arrêt de service.
3. **Sur site d'abord.** Aucune fonction obligatoire ne dépend d'un service externe. L'OCR, la recherche et l'IA ont une option locale. Les services externes (SMS, signature qualifiée, IA en ligne) sont des connecteurs désactivables.
4. **Sécurité côté serveur.** Aucune règle de droit n'est appliquée seulement dans l'interface.

## Pile technique

- Conserver la pile existante du dépôt si l'audit montre qu'elle tient ces contraintes. Sinon, proposer une pile et attendre l'accord.
- Base de données relationnelle : PostgreSQL par défaut, avec une couche d'accès qui permet Microsoft SQL Server ou Oracle, car certains acheteurs imposent un SGBD sous licence commerciale.
- Stockage des fichiers : hors base, sur système de fichiers ou stockage objet, avec montage NFS, CIFS et SMB.
- Recherche plein texte : un moteur unique pour documents et données, multilingue.
- Mobile : vraies applications Android et iOS publiables sur Google Play et l'App Store. L'accès par navigateur mobile ne suffit pas.
- Interface web : tous navigateurs courants (Chrome, Firefox, Edge, Safari), HTTPS avec TLS 1.2 au minimum.

## Multi-instances

- Une instance = une entité autonome : son organigramme, ses référentiels, ses documents, ses utilisateurs.
- Étanchéité stricte : chaque table métier porte l'identifiant d'instance ; chaque requête le filtre côté serveur ; les fichiers sont séparés par instance. Des tests automatiques tentent des accès croisés et doivent échouer.
- Échanges entre instances : authentifiés, chiffrés, journalisés.
- Créer une instance se fait dans l'administration, sans code ni redéploiement.

## Identité et droits

- Annuaire LDAP et Active Directory, avec synchronisation des utilisateurs et des groupes.
- SSO : authentification Windows intégrée, SAML 2.0, OpenID Connect. Double authentification.
- L'organigramme est le socle des droits. Droits par rôle, profil, groupe, dossier, document, champ de métadonnée, fichier joint et type d'action (voir, traiter, imprimer, exporter, capturer, publier).
- Deux familles d'administrateurs : fonctionnel et technique.
- Niveaux de confidentialité sur la fiche et sur les fichiers.

## Traçabilité et preuve

- Journal d'audit en ajout seul, chaîné par empreintes, non modifiable par l'application.
- Empreinte SHA-256 de chaque fichier à l'entrée, vérifiée périodiquement.
- Horodatage de chaque capture à la seconde.
- Identifiant unique, code-barres et QR code sur tout document créé, téléchargé ou imprimé.

## Signature

- Signature simple : image du spécimen et cachet, tracée et horodatée.
- Signature tactile au stylet.
- Signature avancée : PDF signé (PAdES) avec certificat X.509 sur clé USB ou carte à puce via PKCS#11, saisie du code PIN, magasin de certificats, contrôle d'expiration et de révocation (CRL, OCSP).
- Architecture à connecteurs : le prestataire de confiance et l'autorité de certification sont interchangeables. Le premier connecteur vise les certificats reconnus par l'ARTCI.
- Toute question sur la valeur probante est remontée au responsable du projet ; ne rien affirmer dans l'interface.

## Formats et normes à respecter

PDF/A (ISO 19005-1) avec conversion automatique des fichiers bureautiques ; TIFF multipage ; CMIS 1.1 (serveur) ; SEDA (export d'archives) ; SAML 2.0 ; OpenID Connect ; LDAP v3 ; IMAP, IMAPS, POP, POPS, SMTP ; BPMN 2.0 pour la notation des circuits ; ISO 15489 et ISO 14721 (OAIS) pour la logique d'archivage.

## Exploitation

- Trois environnements : développement, recette, production. Installation scriptée et documentée.
- Haute disponibilité et répartition de charge : serveurs applicatifs sans état, sessions et fichiers partagés, base répliquée.
- Supervision : état des services, files de capture, erreurs remontées aux administrateurs techniques.
- Sauvegarde et restauration testées. Filtrage paramétrable des extensions interdites (.exe, .cmd, .vbs, etc.).
- Cible de dimensionnement de départ : 150 utilisateurs, 11 000 courriers de 5 pages et 40 000 documents par an, avec des tests de charge à dix fois ce volume.

## Licences

Le produit livré est propriétaire, sous licence ADA. Les acheteurs publics refusent souvent les « solutions open source ». Tenir `docs/licences.md` à jour : composant, version, licence, rôle. Licences permissives seulement. Prévoir, pour chaque composant d'infrastructure libre, l'équivalent commercial que le client peut imposer.
