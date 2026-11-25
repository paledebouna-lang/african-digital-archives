# 04 — Feuille de route

Un lot = un ensemble livrable et démontrable. On ne commence pas un lot tant que le précédent n'a pas passé sa recette. Les identifiants (A3, B1, etc.) renvoient à `02-EXIGENCES.md`.

## Critères de fin, valables pour tous les lots

- Chaque exigence du lot a un test automatisé qui passe.
- La fonction marche sur un serveur réel, avec un compte non administrateur et des droits restreints.
- L'étanchéité entre deux instances est testée pour les nouvelles données du lot.
- Les actions du lot apparaissent au journal d'audit.
- Les écrans sont en français et en anglais.
- `docs/conformite.md`, `docs/avancement.md` et `docs/licences.md` sont à jour.
- Le guide utilisateur et le guide administrateur du lot sont écrits.

## Les lots

| Lot | Contenu | Exigences |
|---|---|---|
| 0. Audit | État réel du code, écarts avec l'architecture, plan de mise à niveau. Aucun code. | — |
| 1. Socle serveur | Application serveur réelle, base de données, stockage des fichiers, comptes, instances étanches, organigramme, rôles et droits, journal d'audit chaîné, API documentée, traduction, tests et intégration continue | A1 à A5, A11, H6, H7 |
| 2. Documents | Types, métadonnées, formulaires, thésaurus, règles de saisie, versions, réservation, liens, fonds de dossier, modèles et fusion, recherche complète, vues dynamiques, zone de persistance, traitements en masse | A12, A13, E1 à E11, E16 à E19 |
| 3. Capture | Scan, lots et intercalaires, OCR multilingue, PDF/A, LAD/RAD, e-mails en masse, dossiers surveillés pour les applications métier, XML, serveur de capture séparé, casiers virtuels, stockage réseau | A4, D1 à D12 |
| 4. Processus | Concepteur graphique, moteur d'exécution, formulaires de circuit, rôles, délais, relances, déclencheurs, absences et délégations, suivi | G1 à G8, E15 |
| 5. Courrier | Arrivée, départ, interne, bureaux d'ordre, registres, numérotation, accusés, annotations, modèles de réponse, validation et expédition, suivi, statistiques | B1 à B15 |
| 6. Notifications et pilotage | Centre de notifications, échéances et alertes par type, récapitulatifs, tableaux de bord à widgets, générateur de rapports, indicateurs | A9, H1, H2, H10, I5 |
| 7. Parapheur et signature | Parapheur, signature simple, tactile, avancée par certificat, en masse, co-signature, refus, vérification, signature physique rescannée | F1 à F11 |
| 8. Archivage | Plan de classement, calendrier de conservation, sort final, gel, bordereaux, versement, export SEDA, archives physiques et localisation, contrôle d'intégrité | C1 à C5 |
| 9. Modules métier | Contrats, appels d'offres, factures, construits comme des packs sur le moteur ; puis RPA | I1 à I4, E8 |
| 10. Interopérabilité | LDAP et Active Directory, SSO, double authentification, serveur CMIS, SDK et console de test, compléments Outlook et Word, édition Office en web | H4, H5, E12, E13, E14, D4 |
| 11. Mobile | Applications Android et iOS : espaces de travail, recherche, tâches, transfert, notifications, parapheur ; publication sur les stores | A10, J |
| 12. Industrialisation | Installeur sur site, trois environnements, haute disponibilité, supervision, sauvegarde et restauration, filtrage des extensions, tests de charge, audit de sécurité, aide en ligne avec vidéos, supports de formation | A7, H3, H9, H11 |
| 13. Packs sectoriels | Import et export de packs ; Instances et délibérations, Guichet, Marchés publics, Scolarité, puis les autres | `01-VISION-ET-PERIMETRE.md` |
| 14. IA documentaire | Résumé, classement proposé, extraction, recherche en langage naturel, détection de doublons ; toujours avec une option locale | A6 |

## Pourquoi cet ordre

- Les lots 1 et 2 portent tout le reste : instances, droits, types et métadonnées.
- Le moteur de processus (4) vient avant le courrier (5), car le courrier est un ensemble de circuits.
- La signature (7) vient après le courrier, qui en est le premier usage, mais ses démarches hors code commencent dès le lot 0.
- Les modules métier (9) et les packs (13) ne sont que de la configuration si les lots 2 et 4 sont bien faits. S'il faut du code spécifique pour un pack, c'est que le moteur est incomplet : corriger le moteur.

## Ordre de grandeur

Avec Claude Code et une personne qui relit et teste à plein temps : plusieurs semaines par lot pour les lots 1 à 8, davantage pour 7 et 10. Compter de l'ordre d'un an pour un produit défendable devant une commission, à affiner après le lot 0. Ce chiffre est une estimation prudente, pas un engagement.

## Jalons commerciaux

- **Fin du lot 5** : démonstration courrier + documents + circuits sur un serveur réel. Premier client pilote possible.
- **Fin du lot 8** : cœur du cahier des charges UFHB couvert. Recherche de deux références signées.
- **Fin du lot 12** : tableau de conformité rempli avec preuves. Produit présentable en appel d'offres.
