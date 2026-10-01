"""ARCHIVA360 interactive demo (in-browser application)."""
from .core import Page, add, SITE


def build():
    body = f'''<div class="app">
<div class="demo-banner"><b>Démo interactive ARCHIVA360</b><span>Données d'exemple fictives. Tout reste dans votre navigateur : rien n'est envoyé à ADA. <span id="persist-note"></span></span>
<span class="sp"><a href="~/academy/niveau-6/">Exercices guidés (Academy, niveau 6)</a><a href="~/archiva360/">← Retour au site</a></span></div>
<aside class="side"><div class="brand"><i>A</i>ARCHIVA360</div><div class="org"><span>Espace</span><b>Organisation démo</b></div>
<nav class="nav" id="nav" aria-label="Modules"></nav><div class="foot">Démo · version MVP<br>Hébergement : votre navigateur</div></aside>
<div class="main"><div class="top"><form id="top-search" role="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg><label class="sr" for="top-q">Rechercher</label><input id="top-q" placeholder="Rechercher : « factures supérieures à 5 millions FCFA »…"></form>
<div class="who"><span class="av" id="who-av">AK</span><label for="who">Connecté en tant que</label><select id="who"></select></div></div>
<main class="content" id="view" aria-live="polite"><p class="sub">Chargement de la démo…</p></main></div></div>
<div id="drawer"></div><div class="toast" id="toast" role="status" hidden></div>
<noscript><p style="padding:20px">La démo ARCHIVA360 nécessite JavaScript.</p></noscript>'''
    add(Page("archiva360/demo-interactive", "Démo interactive ARCHIVA360", body,
             seo_title="Démo interactive ARCHIVA360 | ADA",
             description="Essayez ARCHIVA360 dans votre navigateur : import, OCR, recherche, empreintes, conservation, archives physiques, audit trail.",
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo", extra_head=pwa_head(),
             scripts=f'<script src="~/{SITE["theme"]}assets/js/archiva360-demo.js?ver={SITE["version"]}"></script>' + pwa_script()))


def _aw_config():
    import json
    aw = SITE["appwrite"]
    cfg = {"endpoint": aw["endpoint"], "project": aw["project"], "team": aw["team"],
           "orgName": SITE["name"], "contact": SITE["email"]}
    return '<script type="application/json" id="aw-config">' + json.dumps(cfg, ensure_ascii=False) + '</script>'


def build_accounts():
    """Real online accounts (Appwrite): sign-in page and signed-in workspace."""
    script = f'{_aw_config()}<script src="~/{SITE["theme"]}assets/js/archiva360-auth.js?ver={SITE["version"]}"></script>' + pwa_script()
    login = f'''<div class="auth">
<a class="auth-brand" href="~/"><i>A</i>ARCHIVA360</a>
<div class="auth-card" id="auth-card" aria-live="polite"><p class="sub">Chargement…</p></div>
<button class="btn install-btn" type="button" data-install hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3v12m0 0l-4-4m4 4l4-4M5 21h14"/></svg>Installer l’application</button>
<p class="auth-foot"><a href="~/">← Retour au site African Digital Archives</a> · <a href="~/politique-de-confidentialite/">Confidentialité</a></p>
</div>
<div class="toast" id="toast" role="status" hidden></div>
<noscript><p style="padding:20px">La connexion à ARCHIVA360 nécessite JavaScript.</p></noscript>'''
    add(Page("archiva360/connexion", "Connexion à ARCHIVA360", login,
             seo_title="Connexion | ARCHIVA360", description="Connexion à votre espace ARCHIVA360.",
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo archiva360-login", extra_head=pwa_head(), scripts=script))
    espace = '''<div class="app is-espace">
<aside class="side"><div class="brand"><i>A</i>ARCHIVA360</div><div class="org"><span>Organisation</span><b>African Digital Archives</b></div>
<nav class="nav" id="nav" aria-label="Espace"></nav><div class="foot"><a href="~/">← Retour au site</a></div></aside>
<div class="main"><div class="top"><span class="top-title">Espace ARCHIVA360</span>
<div class="who"><span class="av" id="who-av">…</span><span class="who-txt"><b id="who-name"></b><small id="who-role"></small></span>
<button class="btn sm" type="button" data-install hidden>Installer</button><button class="btn sm o" type="button" data-act="logout">Se déconnecter</button></div></div>
<main class="content" id="view" tabindex="-1" aria-live="polite"><p class="sub">Chargement de votre espace…</p></main></div></div>
<div class="toast" id="toast" role="status" hidden></div>
<noscript><p style="padding:20px">L'espace ARCHIVA360 nécessite JavaScript.</p></noscript>'''
    add(Page("archiva360/espace", "Espace ARCHIVA360", espace,
             seo_title="Espace | ARCHIVA360", description="Votre espace ARCHIVA360.",
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo archiva360-espace", extra_head=pwa_head(), scripts=script))


# ---------------------------------------------------------------------------
# Application installable (PWA) : manifeste, service worker, balises d'en-tête
# ---------------------------------------------------------------------------
APP_PAGES = ["archiva360/connexion/", "archiva360/espace/", "archiva360/demo-interactive/"]


def pwa_head():
    up = SITE["uploads"]
    return (f'<link rel="manifest" href="~/archiva360/manifest.webmanifest">'
            '<meta name="theme-color" content="#0A1541">'
            '<meta name="mobile-web-app-capable" content="yes">'
            '<meta name="apple-mobile-web-app-capable" content="yes">'
            '<meta name="apple-mobile-web-app-title" content="ARCHIVA360">'
            '<meta name="apple-mobile-web-app-status-bar-style" content="default">'
            f'<link rel="apple-touch-icon" href="~/{up}archiva360-app-180.png">')


def pwa_script():
    return f'<script src="~/{SITE["theme"]}assets/js/archiva360-pwa.js?ver={SITE["version"]}"></script>'


def write_pwa(root):
    import json
    import os
    up = "../" + SITE["uploads"]
    manifest = {
        "id": "./espace/",
        "name": "ARCHIVA360",
        "short_name": "ARCHIVA360",
        "description": "ARCHIVA360 par African Digital Archives : vos archives, vos utilisateurs et vos rôles, depuis votre téléphone.",
        "lang": "fr",
        "dir": "ltr",
        "start_url": "./espace/",
        "scope": "./",
        "display": "standalone",
        "orientation": "any",
        "background_color": "#0A1541",
        "theme_color": "#0A1541",
        "categories": ["business", "productivity"],
        "icons": [
            {"src": up + "archiva360-app-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
            {"src": up + "archiva360-app-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": up + "archiva360-app-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
        ],
        "shortcuts": [
            {"name": "Utilisateurs et rôles", "url": "./espace/#utilisateurs"},
            {"name": "Mon compte", "url": "./espace/#compte"},
            {"name": "Démo interactive", "url": "./demo-interactive/"},
        ],
    }
    with open(os.path.join(root, "archiva360/manifest.webmanifest"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    theme, v = "../" + SITE["theme"], SITE["version"]
    precache = ["./connexion/", "./espace/", "./demo-interactive/", "./manifest.webmanifest",
                f"{theme}assets/css/archiva360-demo.css?ver={v}", f"{theme}assets/js/archiva360-auth.js?ver={v}",
                f"{theme}assets/js/archiva360-pwa.js?ver={v}", f"{theme}assets/js/archiva360-demo.js?ver={v}",
                f"{theme}assets/fonts/inter-latin.woff2", up + "archiva360-app-192.png", up + "archiva360-app-180.png",
                "../wp-content/uploads/2026/09/cropped-ada-icon-32x32.png"]
    sw = f"""// ARCHIVA360 — service worker (généré par tools/build.py, ne pas modifier à la main).
// Pages : réseau d'abord, copie locale si hors connexion. Fichiers du thème : copie locale, mise à jour en arrière-plan.
// Les appels à Appwrite (autre domaine) ne passent jamais par le cache.
const CACHE = 'archiva360-v{v}';
const PRECACHE = {json.dumps(precache, indent=2)};

self.addEventListener('install', e => {{
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
}});

self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('archiva360-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
}});

self.addEventListener('fetch', e => {{
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  if (req.mode === 'navigate') {{
    e.respondWith(fetch(req).then(res => {{
      if (res.ok) {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }}
      return res;
    }}).catch(() => caches.match(req, {{ ignoreSearch: true }})
      .then(hit => hit || caches.match('./connexion/'))));
    return;
  }}
  e.respondWith(caches.match(req).then(hit => {{
    const net = fetch(req).then(res => {{
      if (res.ok) {{ const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }}
      return res;
    }});
    if (hit) {{ net.catch(() => {{}}); return hit; }}
    return net;
  }}));
}});
"""
    with open(os.path.join(root, "archiva360/sw.js"), "w", encoding="utf-8") as f:
        f.write(sw)
