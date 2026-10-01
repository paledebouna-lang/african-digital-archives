"""ARCHIVA Academy: catalogue, course players, certificates and verification."""
import json

from .core import Page, add, section, intro, cols, card, feature, ul, btn, buttons, page_hero, notice, cta_band, SITE
from .icons import icon
from .academy_n1_n2 import N1, N2
from .academy_n3_n4 import N3, N4
from .academy_n5_n6 import N5, N6
from .academy_dirigeant2 import DIR

LEVELS = [N1, N2, N3, N4, N5, N6]
COURSES = LEVELS + [DIR]        # tout ce qui se joue dans le lecteur de cours et donne un certificat
QUIZ_PASS = 75
EXAM_PASS = 70
EXAM_SIZE = 15



def label(c):
    return c.get("label") or f"Niveau {c['num']} — {c['title']}"


def unit(c):
    return c.get("unit", "Module")


def exam_size(c):
    return c.get("exam_size", EXAM_SIZE)


def _scripts(extra=""):
    return f'<script src="~/{SITE["theme"]}assets/js/academy.js?ver={SITE["version"]}"></script>{extra}'


def _minutes(lv):
    return sum(m["minutes"] for m in lv["modules"])


def build():
    # ------------------------------------------------------------------ catalogue
    cards = ""
    for lv in LEVELS:
        cards += f'''<article class="course-card" data-level="{lv["slug"]}">
<div class="course-card__head"><span class="course-card__num">{lv["num"]:02d}</span><span class="course-status" data-status>Non commencé</span></div>
<h3><a href="~/academy/{lv["slug"]}/">Niveau {lv["num"]} — {lv["title"]}</a></h3>
<p>{lv["intro"]}</p>
<ul class="course-meta"><li>{icon("clock")}{lv["duration"]}</li><li>{icon("layers")}{len(lv["modules"])} modules</li><li>{icon("users")}{lv["audience"]}</li></ul>
<div class="course-progress" aria-hidden="true"><i data-bar style="width:0%"></i></div>
<div class="course-card__foot"><span class="has-small-font-size has-muted-color" data-progress-label>0 % terminé</span>
<a class="more-link" href="~/academy/{lv["slug"]}/" data-cta>Commencer {icon("arrow-right")}</a></div></article>'''
    weeks = "".join(
        f'<li><a href="~/academy/{DIR["slug"]}/#m{i}"><span class="week-list__num">S{i:02d}</span><span>{w["title"]}</span></a></li>'
        for i, w in enumerate(DIR["modules"], 1))
    dir_card = f'''<article class="course-card course-card--wide" data-level="{DIR["slug"]}" data-modules="{len(DIR["modules"])}">
<div class="course-card__head"><span class="course-card__num">12</span><span class="course-status" data-status>Non commencé</span></div>
<h3><a href="~/academy/{DIR["slug"]}/">Parcours dirigeant</a></h3>
<p>{DIR["intro"]}</p>
<ul class="course-meta"><li>{icon("clock")}12 × 1 h</li><li>{icon("layers")}12 semaines, 1 livrable chaque semaine</li><li>{icon("star")}Examen final et certificat</li></ul>
<div class="course-progress" aria-hidden="true"><i data-bar style="width:0%"></i></div>
<div class="course-card__foot"><span class="has-small-font-size has-muted-color" data-progress-label>0 % terminé</span>
<a class="more-link" href="~/academy/{DIR["slug"]}/" data-cta>Commencer {icon("arrow-right")}</a></div></article>'''
    how = cols(*[feature(t, d, ic) for t, d, ic in [
        ("1. Lisez les leçons", "Chaque module contient une leçon illustrée d'exemples africains, un encadré « À retenir » et une mise en pratique.", "book"),
        ("2. Validez les quiz", f"Un quiz de 4 questions conclut chaque module. Il faut {QUIZ_PASS} % de bonnes réponses pour le valider, avec correction détaillée.", "check-circle"),
        ("3. Passez l'examen", f"Quand tous les modules sont validés, l'examen final ({EXAM_SIZE} questions tirées au hasard) s'ouvre. Seuil de réussite : {EXAM_PASS} %.", "target"),
        ("4. Obtenez le certificat", "Un certificat ARCHIVA Academy nominatif, daté et doté d'un code de vérification, à imprimer ou enregistrer en PDF.", "star")]], n=4, cls="gap-sm")
    add(Page("academy", "ARCHIVA Academy",
             description="ARCHIVA Academy : six niveaux de formation en ligne à l'archivage et un parcours dirigeant de 12 semaines, avec leçons, quiz, examens finaux et certificats vérifiables.",
             hero=page_hero("ARCHIVA Academy", "Six niveaux de formation en ligne et un parcours dirigeant de 12 semaines, gratuits, pour comprendre, pratiquer et piloter l'archivage : leçons, études de cas, quiz corrigés, examens finaux et certificats vérifiables.",
                            [("ARCHIVA Academy", None)], "Formation",
                            buttons(btn("Commencer le niveau 1", "~/academy/niveau-1/", "white"), btn("Mes certificats", "~/academy/certificat/", "outline"))),
             body=section(f'''<div class="learner-bar" id="learner-bar">
<div><span class="eyebrow mb-0">Votre espace</span><h2 class="learner-bar__title" id="learner-greeting">Bienvenue dans l'Academy</h2>
<p class="has-muted-color mb-0" id="learner-summary">Votre progression est enregistrée dans ce navigateur. Indiquez votre nom tel qu'il doit figurer sur vos certificats.</p></div>
<form class="learner-form" id="learner-form"><label for="learner-name">Nom et prénom</label><div class="learner-form__row"><input id="learner-name" name="name" autocomplete="name" placeholder="Ex. : Awa Koné" maxlength="80"><button class="button" type="submit">Enregistrer</button></div></form></div>'''
                          + intro("Six niveaux progressifs", "Commencez au niveau 1 si vous débutez. Les niveaux peuvent aussi être suivis séparément selon votre métier.", "Parcours", split=True)
                          + f'<div class="course-grid">{cards}</div>')
             + section(intro("Comment ça marche", "", "Fonctionnement") + how, "mist")
             + section('<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">'
                       + intro("Parcours dirigeant : 12 semaines", "Pour les dirigeants, membres de comités de direction et secrétaires généraux : une heure par semaine pour comprendre, décider, investir et piloter, sans devenir archiviste. Chaque semaine associe une leçon, une étude de cas africaine, les questions à poser à vos équipes, un quiz et un livrable. Les douze livrables forment, à la fin, la feuille de route documentaire de votre organisation.", "Programme")
                       + dir_card
                       + f'</div><div class="wp-block-column"><ol class="week-list">{weeks}</ol></div></div>', id="parcours-dirigeant")
             + section(cols(card("Vérifier un certificat", "Un employeur ou un partenaire peut contrôler l'authenticité d'un certificat ARCHIVA Academy avec son code.", "fingerprint", "~/academy/verifier/", "Vérifier un certificat"),
                            card("Formations en groupe", "Sessions en présentiel à Abidjan, à distance ou sur mesure pour vos équipes, avec un formateur ADA.", "users", "~/contact/?sujet=formation", "Demander un programme"),
                            card("ARCHIVA Certified Partner", "À terme, certification d'intégrateurs partenaires dans chaque pays de la sous-région.", "globe", "~/contact/?sujet=partenariat", "Devenir partenaire"), n=3), "mist")
             + section(notice("Les certificats ARCHIVA Academy sont des certificats internes de suivi de formation. Ils ne constituent pas un diplôme d'État ni une certification professionnelle réglementée.")),
             nav="academy", scripts=_scripts()))

    # ------------------------------------------------------------------ course players
    for i, lv in enumerate(COURSES):
        U, XS = unit(lv), exam_size(lv)
        data = {
            "slug": lv["slug"], "num": lv["num"], "title": lv["title"], "label": label(lv), "unit": U,
            "quizPass": QUIZ_PASS, "examPass": EXAM_PASS, "examSize": XS,
            "modules": [{"title": m["title"], "quiz": m["quiz"]} for m in lv["modules"]],
            "examExtra": lv["exam_extra"],
        }
        nav = ""
        for j, m in enumerate(lv["modules"], 1):
            nav += (f'<li class="course-nav__module" data-module="{j-1}"><span class="course-nav__label">{U} {j}</span>'
                    f'<a href="#m{j}" data-view="m{j}"><span class="course-nav__state" data-state="lesson-{j-1}"></span>{m["title"]}<small>{m["minutes"]} min</small></a>'
                    f'<a href="#m{j}-quiz" data-view="m{j}-quiz" class="is-quiz"><span class="course-nav__state" data-state="quiz-{j-1}"></span>Quiz {"de la semaine" if U == "Semaine" else "du module"} {j}<small>4 questions</small></a></li>')
        nav += (f'<li class="course-nav__module"><span class="course-nav__label">Évaluation finale</span>'
                f'<a href="#examen" data-view="examen" class="is-exam"><span class="course-nav__state" data-state="exam"></span>Examen final<small>{XS} questions · {EXAM_PASS} %</small></a></li>')
        overview = f'''<section class="course-view" id="view-intro" data-view-id="intro">
<span class="eyebrow">{label(lv) if U == "Semaine" else "Niveau " + str(lv["num"])}</span><h2>À propos de {"ce parcours" if U == "Semaine" else "ce niveau"}</h2><p class="lead">{lv["intro"]}</p>
<h3>Objectifs</h3>{ul(lv["objectives"])}
<div class="course-facts"><div><b>{lv["duration"]}</b><span>Durée estimée</span></div><div><b>{len(lv["modules"])}</b><span>{U}s</span></div><div><b>{len(lv["modules"]) * 4 + len(lv["exam_extra"])}</b><span>Questions d'évaluation</span></div><div><b>{lv["audience"]}</b><span>Public</span></div></div>
<div class="wp-block-buttons mt-m"><div class="wp-block-button"><a class="wp-block-button__link" href="#m1" data-resume>Commencer {"la semaine" if U == "Semaine" else "le module"} 1{icon("arrow-right")}</a></div></div></section>'''
        lessons = ""
        for j, m in enumerate(lv["modules"], 1):
            nxt = f'#m{j}-quiz'
            lessons += (f'<article class="course-view lesson" id="view-m{j}" data-view-id="m{j}" hidden>'
                        f'<span class="eyebrow">{U} {j} · {m["minutes"]} min</span><h2>{m["title"]}</h2>{m["html"]}'
                        f'<div class="lesson-nav"><button class="button is-secondary" type="button" data-mark-read="{j-1}">{icon("check")}Marquer comme lu</button>'
                        f'<a class="wp-block-button__link" href="{nxt}">Passer au quiz{icon("arrow-right")}</a></div></article>'
                        f'<section class="course-view quiz-view" id="view-m{j}-quiz" data-view-id="m{j}-quiz" data-quiz="{j-1}" hidden>'
                        f'<span class="eyebrow">Quiz · {U} {j}</span><h2>{m["title"]}</h2>'
                        f'<p class="has-muted-color">4 questions. Il faut {QUIZ_PASS} % de bonnes réponses pour valider {"la semaine" if U == "Semaine" else "le module"}. Les questions à cases à cocher peuvent avoir plusieurs bonnes réponses.</p>'
                        f'<form class="quiz" data-quiz-form="{j-1}" novalidate></form></section>')
        exam = f'''<section class="course-view quiz-view" id="view-examen" data-view-id="examen" hidden>
<span class="eyebrow">Évaluation finale</span><h2>Examen final — {label(lv)}</h2>
<div id="exam-locked" class="notice is-warning"><p>L'examen s'ouvre quand les {len(lv["modules"])} quiz {"hebdomadaires" if U == "Semaine" else "de modules"} sont validés. <span id="exam-missing"></span></p></div>
<div id="exam-ready" hidden><p class="has-muted-color">{XS} questions tirées au hasard parmi l'ensemble {"du parcours, dont des cas de décision" if U == "Semaine" else "du niveau"}. Seuil de réussite : {EXAM_PASS} %. Vous pouvez repasser l'examen autant de fois que nécessaire.</p>
<div class="wp-block-buttons"><div class="wp-block-button"><button class="wp-block-button__link" type="button" id="exam-start">Commencer l'examen{icon("arrow-right")}</button></div></div></div>
<form class="quiz" id="exam-form" novalidate hidden></form>
<div id="exam-result" hidden></div></section>'''
        if lv in LEVELS:
            prev_lv = LEVELS[i - 1] if i > 0 else None
            next_lv = LEVELS[i + 1] if i + 1 < len(LEVELS) else None
        else:
            prev_lv = next_lv = None
        pager = '<nav class="course-pager">' + (f'<a href="~/academy/{prev_lv["slug"]}/">← Niveau {prev_lv["num"]} : {prev_lv["title"]}</a>' if prev_lv else '<a href="~/academy/">← ARCHIVA Academy</a>') \
            + (f'<a href="~/academy/{next_lv["slug"]}/">Niveau {next_lv["num"]} : {next_lv["title"]} →</a>' if next_lv else "<span></span>") + "</nav>"
        body = f'''<div class="container"><div class="course-layout" id="course" data-level="{lv["slug"]}">
<aside class="course-nav" aria-label="Sommaire du niveau"><div class="course-nav__progress"><div class="course-progress"><i id="course-bar" style="width:0%"></i></div><span id="course-progress-label">0 % terminé</span></div>
<ol>{nav}</ol><a class="course-nav__cert" href="~/academy/certificat/">{icon("star")}Mes certificats</a></aside>
<a id="cert-link" href="~/academy/certificat/" hidden></a><div class="course-main">{overview}{lessons}{exam}{pager}</div></div></div>
<script type="application/json" id="course-data">{json.dumps(data, ensure_ascii=False)}</script>'''
        short = lv["title"] if U == "Semaine" else f"Niveau {lv['num']}"
        add(Page(f"academy/{lv['slug']}", label(lv), body,
                 description=f"ARCHIVA Academy, {label(lv)} : {lv['intro']}",
                 hero=page_hero(label(lv), lv["intro"], [("ARCHIVA Academy", "academy/"), (short, None)], "ARCHIVA Academy", light=True),
                 nav="academy", body_class="page academy-course", scripts=_scripts()))

    # ------------------------------------------------------------------ certificates
    levels_js = json.dumps({lv["slug"]: {"num": lv["num"], "title": lv["title"], "label": label(lv),
                                         "short": lv["title"] if unit(lv) == "Semaine" else f"Niveau {lv['num']}"} for lv in COURSES}, ensure_ascii=False)
    add(Page("academy/certificat", "Mes certificats",
             f'''<div class="container cert-page"><div id="cert-empty" class="notice" hidden><p>Vous n'avez pas encore de certificat dans ce navigateur. Réussissez l'examen final d'un niveau pour l'obtenir. <a href="~/academy/">Voir les niveaux</a></p></div>
<div id="cert-list" class="cert-list"></div>
<div id="cert-view" hidden><div class="cert-toolbar"><button class="button" type="button" id="cert-print">{icon("download")}Imprimer / enregistrer en PDF</button><button class="button is-secondary" type="button" id="cert-copy">{icon("link")}Copier le code</button><span id="cert-copy-msg" class="has-small-font-size has-muted-color" aria-live="polite"></span></div>
<div class="certificate" id="certificate"></div></div></div>
<script type="application/json" id="levels-data">{levels_js}</script>''',
             description="Vos certificats ARCHIVA Academy.",
             hero=page_hero("Mes certificats", "Les certificats obtenus dans ce navigateur. Imprimez-les ou enregistrez-les en PDF.", [("ARCHIVA Academy", "academy/"), ("Mes certificats", None)], light=True),
             nav="academy", search=False, body_class="page academy-cert", scripts=_scripts()))

    lv_opts = "".join(f'<option value="{lv["slug"]}">{label(lv)}</option>' for lv in COURSES)
    add(Page("academy/verifier", "Vérifier un certificat",
             section(f'''<div class="wp-block-columns cols-2 gap-lg" style="--cols:2"><div class="wp-block-column">
<div class="form-card"><form id="verify-form" novalidate>
<p><label for="v-name">Nom figurant sur le certificat</label><input id="v-name" required></p>
<p><label for="v-level">Niveau</label><select id="v-level">{lv_opts}</select></p>
<div class="wpcf7 form-row"><span><label for="v-date">Date de délivrance</label><input id="v-date" type="date" required></span><span><label for="v-score">Score (%)</label><input id="v-score" type="number" min="0" max="100" required></span></div>
<p><label for="v-code">Code de vérification</label><input id="v-code" placeholder="XXXX-XXXX-XXXX" required></p>
<button class="button" type="submit">Vérifier</button></form>
<div id="verify-result" class="mt-m" aria-live="polite"></div></div></div>
<div class="wp-block-column">{intro("Comment fonctionne la vérification", "Le code d'un certificat est calculé à partir du nom, du niveau, de la date et du score avec la fonction SHA-256 : c'est la même technique d'empreinte que celle utilisée pour prouver l'intégrité des archives. Si une seule de ces informations a été modifiée, le code ne correspond plus.", "Principe")}
{notice("La vérification confirme que les informations du certificat n'ont pas été modifiées. Pour une attestation officielle de suivi, contactez ADA.")}</div></div>
<script type="application/json" id="levels-data">{levels_js}</script>'''),
             description="Vérifiez l'authenticité d'un certificat ARCHIVA Academy grâce à son code.",
             hero=page_hero("Vérifier un certificat", "Saisissez les informations figurant sur le certificat pour contrôler son code.", [("ARCHIVA Academy", "academy/"), ("Vérifier", None)], light=True),
             nav="academy", search=False, scripts=_scripts()))
