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
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo",
             scripts=f'<script src="~/{SITE["theme"]}assets/js/archiva360-demo.js?ver={SITE["version"]}"></script>'))


def _aw_config():
    import json
    aw = SITE["appwrite"]
    cfg = {"endpoint": aw["endpoint"], "project": aw["project"], "team": aw["team"],
           "orgName": SITE["name"], "contact": SITE["email"]}
    return '<script type="application/json" id="aw-config">' + json.dumps(cfg, ensure_ascii=False) + '</script>'


def build_accounts():
    """Real online accounts (Appwrite): sign-in page and signed-in workspace."""
    script = f'{_aw_config()}<script src="~/{SITE["theme"]}assets/js/archiva360-auth.js?ver={SITE["version"]}"></script>'
    login = f'''<div class="auth">
<a class="auth-brand" href="~/"><i>A</i>ARCHIVA360</a>
<div class="auth-card" id="auth-card" aria-live="polite"><p class="sub">Chargement…</p></div>
<p class="auth-foot"><a href="~/">← Retour au site African Digital Archives</a> · <a href="~/politique-de-confidentialite/">Confidentialité</a></p>
</div>
<div class="toast" id="toast" role="status" hidden></div>
<noscript><p style="padding:20px">La connexion à ARCHIVA360 nécessite JavaScript.</p></noscript>'''
    add(Page("archiva360/connexion", "Connexion à ARCHIVA360", login,
             seo_title="Connexion | ARCHIVA360", description="Connexion à votre espace ARCHIVA360.",
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo archiva360-login", scripts=script))
    espace = '''<div class="app is-espace">
<aside class="side"><div class="brand"><i>A</i>ARCHIVA360</div><div class="org"><span>Organisation</span><b>African Digital Archives</b></div>
<nav class="nav" id="nav" aria-label="Espace"></nav><div class="foot"><a href="~/">← Retour au site</a></div></aside>
<div class="main"><div class="top"><span class="top-title">Espace ARCHIVA360</span>
<div class="who"><span class="av" id="who-av">…</span><span class="who-txt"><b id="who-name"></b><small id="who-role"></small></span>
<button class="btn sm o" type="button" data-act="logout">Se déconnecter</button></div></div>
<main class="content" id="view" tabindex="-1" aria-live="polite"><p class="sub">Chargement de votre espace…</p></main></div></div>
<div class="toast" id="toast" role="status" hidden></div>
<noscript><p style="padding:20px">L'espace ARCHIVA360 nécessite JavaScript.</p></noscript>'''
    add(Page("archiva360/espace", "Espace ARCHIVA360", espace,
             seo_title="Espace | ARCHIVA360", description="Votre espace ARCHIVA360.",
             kind="app", nav="archiva360", search=False, body_class="archiva360-demo archiva360-espace", scripts=script))
