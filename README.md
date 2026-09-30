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
| `posts.py` / `pages_resources.py` | Articles du blog, guides, glossaire, Health Check, Academy |
| `mockups.py` / `covers.py` | Captures d'écran ARCHIVA360 et illustrations |

Après modification :

```bash
python3 tools/build.py            # régénère toutes les pages
python3 tools/build.py --images   # régénère aussi les images (Node + Playwright requis)
```

**À faire avant la mise en ligne :** remplacer `contact@example.com` par l'adresse réelle dans
`tools/ada/core.py` (`SITE["email"]`), compléter les mentions légales (RCCM, etc.) et les liens des réseaux sociaux.
