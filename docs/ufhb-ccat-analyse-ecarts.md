# Marché UFHB « Archivage numérique et transformation digitale » — analyse d'écarts ARCHIVA360

Source : Cahier des clauses techniques (CCAT), 160 exigences du tableau de conformité, 51 pages.
Date de l'analyse : 25 novembre 2026. Plateforme évaluée : ARCHIVA360 telle que publiée sur adarchives.pro
(site, comptes Appwrite, démo interactive, application installable).

## 1. Ce que demande le marché, en une page

| Point clé | Exigence du CCAT |
|---|---|
| Objet | Solution clé en main GEC + GED + BPM (workflow graphique) + RPA, avec parapheur et signature électronique, en **mode on premise** à l'UFHB |
| Volumes | ~150 utilisateurs, 11 000 courriers entrants/an (5 pages), 40 000 documents métier/an, 25 signataires, 25 utilisateurs mobiles |
| Délai | 120 jours calendaires : 30 (étude) + 60 (réalisation, recette) + 30 (formation, mise en production) ; garantie 12 mois ; incidents résolus en 4 h |
| Paiement | 30 % / 50 % / 20 % par phase ; 16 livrables (L1 à L16) en Word/Excel, en français |
| Contraintes éliminatoires probables | **Tous les composants du même éditeur** (1) ; **logiciels éditeurs sous licence avec maintenance éditeur, open source refusé** (3) ; **application mobile native sur Google Play et App Store, pas de navigateur** (12) ; **certificat d'homologation du parapheur** par une entité gouvernementale ; signature avancée avec certificat **ARTCI** (88) ; **CMIS** (142) ; **SSO Active Directory / SAML / OpenID Connect + MFA** (141) ; **LDAP** (139) ; **3 environnements** (dev, préproduction, production) ; **infrastructure et logiciels (OS, SGBD) fournis par le prestataire** ; haute disponibilité et équilibrage de charge |
| Contrat | TMA annuelle reconductible après garantie ; formation des référents (5 jours/10 personnes), administrateurs fonctionnels (10) et techniques (5) |

## 2. État d'ARCHIVA360 face aux 160 exigences

Légende : **Couvert** = existe en production ; **Démo** = existe dans la démo interactive (données locales au navigateur, non multi-utilisateur) ; **Absent** = à construire.

| Domaine (n° du tableau) | État | Commentaire |
|---|---|---|
| Comptes, rôles, invitations, e-mails (139-148, partiel) | Couvert | Appwrite : 5 rôles, invitations, mot de passe oublié. Pas de LDAP, SSO, MFA, organigramme |
| Dépôt, OCR, métadonnées proposées, recherche en langage naturel (89-100) | Démo | IndexedDB dans le navigateur ; à reconstruire côté serveur (stockage, index plein texte) |
| Versions, empreintes SHA-256, journal d'audit chaîné (70-74, 149-150) | Démo | Principe validé ; à porter côté serveur |
| Règles de conservation, DUA, gel juridique, certificat d'élimination (32-36) | Démo | Bon alignement avec le CCAT ; manque bordereaux SEDA, localisation physique complète |
| Archives physiques, boîtes, QR codes (18, 62-63, 151) | Démo | — |
| Sauvegarde / restauration (partiel) | Démo | — |
| GEC : registres arrivée/départ/interne, numérotation chrono, accusés, bureaux d'ordre, casiers (17-31, 44) | Absent | Cœur du marché, à construire |
| Workflow graphique, formulaires, délégation/intérim, échéances, relances (102-119, 133-134) | Absent | Cœur du marché, à construire |
| Parapheur, signature simple (image), co-signature, signature en masse (84-88, 120-132) | Absent | Signature **visuelle** constructible ; signature **avancée ARTCI** et **homologation** = partenariat et procédure externes |
| Capture multicanal : scanners, e-mail IMAP/POP en masse et sélective, XML, LAD/RAD, serveur de capture, NFS/CIFS (37-46) | Absent | Capture par dépôt et OCR existent en démo ; le reste à construire ; add-ins Outlook/Word (80-81) à développer |
| Thésaurus, formulaires et métadonnées administrables, modèles avec publipostage (53-61, 66) | Absent | — |
| Tableaux de bord à widgets, KPI, rapports personnalisables, BI (10, 124, 135-136, 158) | Démo (partiel) | Tableau de bord fixe en démo |
| Notifications e-mail, récapitulatif hebdomadaire (133-134) | Absent | Brevo est en place pour l'envoi |
| Web services + SDK, CMIS, capture depuis le SI (77-79, 142) | Absent | Appwrite expose une API, mais pas CMIS ni SDK ARCHIVA360 |
| Application mobile native sur les stores (12) | Absent | L'application installable (PWA) est **explicitement refusée** par le CCAT ; il faut des applications publiées, donc comptes développeur Google (25 $) et Apple (99 $/an) |
| Multi-instances étanches, roll-out filiales (5, 13) | Absent | — |
| Multilingue (9, 94) | Absent | Site en français uniquement |
| Aide en ligne : documentation PDF, vidéos (8) | Partiel | Academy et livres blancs existent ; pas d'aide contextuelle ni de vidéos |
| On premise, 3 environnements, HA, LDAP, SSO, MFA, TLS 1.2, filtrage des extensions (137-141, 154) | Absent | Aujourd'hui hébergé sur GitHub Pages + Appwrite Cloud, incompatible avec « on premise » |

**Bilan : environ 15 exigences couvertes, 35 démontrées hors production, 110 absentes.** La démo interactive est une maquette fonctionnelle convaincante ; elle n'est pas un logiciel multi-utilisateur exploitable par 150 agents.

## 3. Points qui ne dépendent pas du développement

Ces points conditionnent la recevabilité de l'offre et relèvent d'ADA, pas du code :

1. **Statut d'éditeur.** Le CCAT exige des « logiciels éditeurs sous licence » du « même éditeur ». ADA doit se présenter comme éditeur d'ARCHIVA360 avec un contrat de licence (L4) et un contrat de maintenance éditeur. C'est possible si tout le socle est développé par ADA ou intégré sous licence commerciale. Le socle actuel (Appwrite, PDF.js, Tesseract) est open source : à remplacer ou à encadrer juridiquement (licences permissives intégrées dans un produit propriétaire ; à valider par un juriste).
2. **Références.** « Solution qui a fait ses preuves grâce à des expériences similaires » : prévoir au moins un déploiement pilote réel avant la soumission.
3. **Parapheur homologué et signature ARTCI.** Nécessite un partenariat avec un prestataire de services de confiance agréé en Côte d'Ivoire et une procédure d'homologation ; délai de plusieurs mois, indépendant du développement.
4. **Hébergement on premise.** Le prestataire fournit serveurs, OS et SGBD : budget matériel et compétences d'exploitation à prévoir ; ARCHIVA360 doit pouvoir s'installer sur les serveurs de l'UFHB (conteneurs), ce qui exclut le modèle actuel GitHub Pages + Appwrite Cloud.
5. **Capacité de production des 16 livrables** et d'une équipe projet (chef de projet, archiviste, développeurs, formateurs) sur 120 jours.

## 4. Chemin proposé : ARCHIVA360 v2

Objectif : un logiciel installable, multi-utilisateur, couvrant le tableau de conformité. Ordre de grandeur réaliste : **6 à 9 mois de développement** pour une équipe de 3 à 5 personnes, avant de pouvoir répondre à un marché de ce type avec un produit démontrable.

| Lot | Contenu | Exigences visées |
|---|---|---|
| 0. Socle | Application serveur installable (conteneurs), base de données, stockage de fichiers, authentification locale + LDAP/SSO/MFA, organigramme, multi-instances, journal d'audit chaîné, API REST + SDK, 3 environnements | 1-7, 13-15, 137-153, 157-160 |
| 1. GED | Types de documents, formulaires et métadonnées administrables, thésaurus, versions, réservation, plan de classement, recherche plein texte et multicritères, zone de persistance, modèles avec publipostage | 47-76, 89-101 |
| 2. GEC | Registres arrivée/départ/interne, numérotation, bureaux d'ordre, casiers virtuels, accusés de réception, liens arrivée/départ, annotations, échéances et alertes, QR codes | 17-31, 44, 62-68 |
| 3. Workflow | Designer graphique (séquentiel/parallèle), formulaires, rôles, délégation/intérim, relances, traitement en masse, RPA simple | 102-119, 69 |
| 4. Capture | Serveur de capture, scanners (TWAIN/dossier surveillé), e-mail IMAP/POP en masse, XML, LAD/RAD, séparation par codes-barres, PDF/A, NFS/CIFS | 37-46, 78 |
| 5. Parapheur | Parapheur, signature visuelle et tactile, co-signature, signature en masse, intégration d'un prestataire de signature avancée (ARTCI), vérification des certificats | 84-88, 120-132, 155-156 |
| 6. Archivage | Calendrier de conservation, sort final, bordereaux, localisation physique, export SEDA | 32-36 |
| 7. Pilotage | Tableaux de bord à widgets, KPI, rapports personnalisables, récapitulatifs hebdomadaires, supervision des anomalies | 10, 124, 133-136, 138, 158 |
| 8. Intégrations | CMIS, add-ins Outlook et Word, capture depuis le SI, multilingue, aide en ligne et vidéos | 8-9, 54, 77-83, 94, 142 |
| 9. Mobile | Applications Android et iOS publiées sur les stores : espaces, recherche, tâches, transfert, notifications | 12 |

Ce qui existe déjà est réutilisable : la charte et les écrans de la démo, la logique de conservation et d'audit, les comptes et rôles, l'Academy pour la formation (L11-L13), les livres blancs pour l'aide en ligne.

## 5. Décision à prendre avant de lancer les travaux

- **Option A — viser ce marché** : lancer ARCHIVA360 v2 selon les lots ci-dessus, en commençant par le socle et la GEC, et engager en parallèle les démarches non techniques (statut d'éditeur, partenaire de signature, matériel, références). Le marché UFHB actuel (120 jours) est hors de portée ; les suivants deviennent accessibles.
- **Option B — viser d'abord des marchés plus petits** : administrations et PME sans exigence on premise ni parapheur homologué, avec la version cloud actuelle enrichie progressivement des lots 1, 2 et 7. Chiffre d'affaires et références plus rapides, puis option A.

Le dossier local « DOSSIER-CLAUDE-CODE-ARCHIVA360 » n'a pas pu être lu depuis cet environnement : cette analyse sera ajustée dès qu'il sera accessible.
