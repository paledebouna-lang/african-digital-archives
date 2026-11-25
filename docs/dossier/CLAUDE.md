# ARCHIVA360 — règles permanentes pour Claude Code

Tu construis ARCHIVA360, plateforme de gestion documentaire, de courrier, de processus et d'archivage éditée par African Digital Archives (ADA), Abidjan. La cible est de pouvoir répondre « oui, en standard » aux appels d'offres d'administrations, d'universités, de banques et d'entreprises d'Afrique francophone. Le dossier de référence est dans `docs/dossier/`. Lis-le avant tout travail.

## Ce que le client final exige toujours

- Les fonctions existent **en standard** et se règlent **par paramétrage dans l'interface d'administration web**, sans développement spécifique par client. Tout ce qui varie d'un client à l'autre (organigramme, types de documents, métadonnées, formulaires, circuits, modèles, casiers, échéances, rapports, droits) est une donnée de configuration, jamais du code.
- Le produit s'installe **sur site**, chez le client, sans dépendre d'un service cloud pour fonctionner.
- Un seul produit, une seule base de code, un seul cycle de version pour tous les modules.

## Règles de travail

1. Un lot à la fois, dans l'ordre de `04-FEUILLE-DE-ROUTE.md`. Si une demande sort du lot en cours, dis-le et propose de la noter pour plus tard.
2. Avant de coder un lot : relis ses exigences dans `02-EXIGENCES.md` et le passage correspondant de `annexes/CCAT-UFHB.txt`, puis écris un plan court et attends l'accord.
3. Chaque exigence livrée a un test automatisé qui la prouve. Mets à jour `docs/conformite.md` (identifiant de l'exigence, état, test, écran concerné) à chaque lot.
4. Une fonction n'est « faite » que si elle marche de bout en bout sur un serveur réel : base de données, fichiers stockés, droits vérifiés côté serveur. Une maquette dans le navigateur ne compte pas. Ne déclare jamais « fait » ce qui est simulé ; écris « simulé » ou « partiel ».
5. Chaque accès à une donnée vérifie l'instance, les droits et la confidentialité côté serveur. Chaque action est inscrite au journal d'audit.
6. Toute chaîne affichée passe par le système de traduction (français et anglais au minimum, structure prête pour l'arabe et le portugais).
7. Avant d'ajouter une dépendance : vérifie sa licence et inscris-la dans `docs/licences.md`. Licences permissives uniquement (MIT, Apache 2.0, BSD, ISC). Pas de GPL, AGPL ni SSPL dans le produit livré. En cas de doute, demande.
8. Ne modifie pas le site vitrine pour annoncer une fonction avant qu'elle soit livrée et testée. Le site ne revendique aucune conformité ni certification non obtenue.
9. Pas de secret dans le code ni dans le dépôt. Pas de données réelles de clients dans les tests.
10. En fin de session : résume ce qui est fait, ce qui est partiel, ce qui reste, et mets à jour `docs/avancement.md`.

## Quand t'arrêter et demander

- Un choix d'architecture difficile à défaire (base de données, moteur de recherche, format de stockage, modèle multi-instances).
- Une exigence ambiguë ou contradictoire.
- Tout ce qui touche à la signature à valeur probante, au chiffrement, à la destruction de documents ou à la migration de données existantes.
- Une dépendance payante ou une licence douteuse.
