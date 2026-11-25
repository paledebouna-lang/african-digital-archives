# Dossier de construction ARCHIVA360 pour Claude Code

Ce dossier sert à faire construire par Claude Code la version complète d'ARCHIVA360 (site adarchives.pro), à partir du cahier des charges de l'UFHB et des besoins d'autres structures.

## Contenu

| Fichier | Rôle |
|---|---|
| `CLAUDE.md` | Règles permanentes que Claude Code relit à chaque session. À copier à la racine du dépôt de code. |
| `01-VISION-ET-PERIMETRE.md` | Ce que le produit doit devenir : modules, publics visés, packs sectoriels. |
| `02-EXIGENCES.md` | Les exigences à satisfaire, par domaine, avec renvoi aux 160 lignes du tableau de conformité UFHB. |
| `03-ARCHITECTURE.md` | Les choix techniques imposés (sur site, multi-instances, sécurité, licences). |
| `04-FEUILLE-DE-ROUTE.md` | L'ordre de construction, lot par lot, avec les critères de fin de lot. |
| `05-PROMPTS.md` | Les messages à copier-coller dans Claude Code, étape par étape. |
| `06-HORS-CODE.md` | Ce que le code ne peut pas apporter et que vous devez mener en parallèle. |
| `annexes/CCAT-UFHB.txt` | Le texte intégral du cahier des charges UFHB, source de référence. |

## Mode d'emploi

1. Copiez tout ce dossier dans le dépôt de code d'adarchives.pro, sous `docs/dossier/`, et copiez `CLAUDE.md` à la racine du dépôt.
2. Ouvrez Claude Code dans ce dépôt.
3. Collez le **Prompt 0** de `05-PROMPTS.md`. Claude Code audite l'existant et vous rend un rapport. Il ne code rien à cette étape.
4. Lisez le rapport, répondez à ses questions, puis collez le **Prompt 1**, et ainsi de suite, un lot à la fois.
5. À la fin de chaque lot, collez le **Prompt de recette** avant de passer au suivant.

## Trois règles pour vous

- Un lot à la fois. Ne demandez jamais « construis tout ».
- Ne validez un lot que si vous avez vu la fonction marcher vous-même, sur un vrai serveur, avec de vrais fichiers.
- Menez les démarches de `06-HORS-CODE.md` dès maintenant : elles sont plus longues que le développement.

## Limite de ce dossier

Il a été rédigé à partir du site public adarchives.pro et du cahier des charges UFHB, sans accès au code. L'état « existant » indiqué dans `02-EXIGENCES.md` vient donc de ce que le site annonce ; le Prompt 0 le corrige d'après le code réel.
