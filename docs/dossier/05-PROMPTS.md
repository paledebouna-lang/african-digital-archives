# 05 — Messages à coller dans Claude Code

Collez un message à la fois. Attendez la fin et lisez la réponse avant le suivant.

## Prompt 0 — Audit (aucun code)

```
Lis CLAUDE.md puis tout le dossier docs/dossier/, y compris annexes/CCAT-UFHB.txt.

Ensuite, audite ce dépôt sans rien modifier :
1. Décris la pile technique, l'arborescence, ce qui tourne côté serveur et ce qui n'est qu'une démo dans le navigateur.
2. Pour chaque exigence de 02-EXIGENCES.md, indique l'état réel : fait et testé, fait sans test, partiel, simulé, absent. Cite le fichier qui le prouve.
3. Compare l'existant à 03-ARCHITECTURE.md et liste les écarts, du plus grave au moins grave.
4. Liste les dépendances et leurs licences ; signale celles qui ne sont pas permissives.
5. Dis si la pile actuelle peut porter le produit complet ou s'il faut la changer, avec tes raisons et le coût des deux options.
6. Propose le découpage détaillé du lot 1 en tâches de quelques heures.

Écris le résultat dans docs/audit.md et crée docs/conformite.md, docs/avancement.md et docs/licences.md. Termine par la liste des décisions que tu attends de moi. Ne commence aucun développement.
```

## Prompt 1 — Lancer un lot (à réutiliser pour chaque lot)

Remplacez N par le numéro du lot.

```
Nous attaquons le lot N de docs/dossier/04-FEUILLE-DE-ROUTE.md.

1. Relis les exigences de ce lot dans 02-EXIGENCES.md et les passages correspondants de annexes/CCAT-UFHB.txt.
2. Écris un plan dans docs/lots/lot-N.md : modèle de données, écrans, API, tests, ordre des tâches, risques, questions.
3. Attends mon accord avant de coder.
```

## Prompt 2 — Exécuter le plan

```
Plan du lot N validé. Réalise-le tâche par tâche.
Pour chaque tâche : écris le test, écris le code, lance tous les tests, puis dis-moi comment vérifier moi-même à l'écran.
Arrête-toi et demande dès qu'un choix sort du plan.
```

## Prompt 3 — Recette du lot

```
Fais la recette du lot N comme un évaluateur d'appel d'offres méfiant.
1. Relance tous les tests et donne le résultat exact.
2. Pour chaque exigence du lot, donne : l'écran, le test, et l'état honnête (fait, partiel, simulé).
3. Essaie de casser le lot : accès depuis une autre instance, compte sans droits, fichier interdit, gros volume, saisie invalide.
4. Vérifie que tout se paramètre en administration web, sans toucher au code.
5. Mets à jour docs/conformite.md et docs/avancement.md.
Liste ce qui empêche de répondre « oui, en standard » et corrige-le, ou explique pourquoi tu ne peux pas.
```

## Prompt 4 — Reprendre après une pause

```
Lis CLAUDE.md, docs/avancement.md et docs/conformite.md. Résume où nous en sommes en dix lignes, puis propose la prochaine tâche.
```

## Prompt 5 — Créer un pack sectoriel (après le lot 9)

```
Crée le pack « NOM DU PACK » décrit dans docs/dossier/01-VISION-ET-PERIMETRE.md, uniquement par configuration : types de dossiers, métadonnées, formulaires, circuits, modèles, règles de conservation, tableau de bord. Exporte-le en fichier de pack importable.
Si une fonction du moteur manque pour y arriver sans code spécifique, arrête-toi et décris l'évolution du moteur nécessaire.
```

## Prompt 6 — Préparer une réponse à un appel d'offres

```
Voici un nouveau cahier des charges : [chemin du fichier].
Compare chaque exigence à docs/conformite.md. Rends un tableau : exigence, réponse (oui en standard, oui par paramétrage, partiel, non), preuve (écran et test), effort pour combler l'écart. N'écris « oui » que si un test le prouve.
```
