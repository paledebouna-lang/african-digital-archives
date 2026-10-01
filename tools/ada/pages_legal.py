"""Mentions légales, politique de confidentialité et conditions d'utilisation.

Les informations propres à la société (forme, capital, RCCM, etc.) sont regroupées dans COMPANY :
il suffit de les compléter ici puis de relancer le build.
"""
from .core import Page, add, section, page_hero, notice, SITE

# ---------------------------------------------------------------------------
# À compléter après l'immatriculation (laisser "" tant que l'information n'existe pas)
# ---------------------------------------------------------------------------
COMPANY = {
    "raison_sociale": "African Digital Archives",
    "sigle": "ADA",
    "forme": "",            # ex. « Société à responsabilité limitée (SARL) » ou « Société par actions simplifiée (SAS) »
    "capital": "",          # ex. « 1 000 000 FCFA »
    "siege": "Abidjan, Côte d'Ivoire",   # adresse complète : commune, quartier, rue, lot, BP
    "rccm": "",             # ex. « CI-ABJ-03-2026-B12-XXXXX »
    "ncc": "",              # numéro de compte contribuable (DGI)
    "telephone": "",
    "directeur_publication": "",   # nom et fonction du représentant légal
    "artci": "",            # référence de la déclaration / autorisation de traitement auprès de l'ARTCI
}
UPDATED = "1er octobre 2026"


def _v(key, label=None):
    """Value, or a visible 'to be completed' marker."""
    val = COMPANY.get(key, "")
    return val if val else f'<span class="todo-field">{label or "à compléter"}</span>'


def _wrap(h):
    """Let wide tables scroll on small screens instead of widening the page."""
    return h.replace("<table>", '<figure class="wp-block-table"><table>').replace("</table>", "</table></figure>")


def _toc(items):
    return '<nav class="toc"><p>Sommaire</p><ol>' + "".join(f'<li><a href="#{a}">{t}</a></li>' for a, t in items) + "</ol></nav>"


def build():
    email = SITE["email"]
    missing = [k for k in ("forme", "capital", "rccm", "ncc", "directeur_publication") if not COMPANY[k]]
    pending = notice("Certaines informations légales seront publiées dès l'immatriculation de la société (forme juridique, capital, RCCM, compte contribuable, directeur de la publication). Elles apparaissent ci-dessous comme « en cours d'immatriculation ».", "warning") if missing else ""

    # ------------------------------------------------------------------ mentions légales
    ml_toc = [("editeur", "Éditeur du site"), ("publication", "Direction de la publication"), ("hebergement", "Hébergement"),
              ("cadre", "Cadre juridique applicable"), ("pi", "Propriété intellectuelle"), ("contenus", "Nature des contenus et responsabilité"),
              ("outils", "Outils en ligne : Academy, démo, Health Check"), ("liens", "Liens hypertextes"), ("donnees", "Données personnelles et cookies"),
              ("droit", "Droit applicable et juridiction"), ("contact", "Contact")]
    ml = f'''{_toc(ml_toc)}
<h2 id="editeur">1. Éditeur du site</h2>
<p>Le présent site est édité par :</p>
<table><tbody>
<tr><td>Dénomination</td><td><strong>{COMPANY["raison_sociale"]}</strong> ({COMPANY["sigle"]})</td></tr>
<tr><td>Forme juridique</td><td>{_v("forme", "en cours d'immatriculation")}</td></tr>
<tr><td>Capital social</td><td>{_v("capital", "en cours d'immatriculation")}</td></tr>
<tr><td>Siège social</td><td>{COMPANY["siege"]}</td></tr>
<tr><td>Registre du commerce (RCCM)</td><td>{_v("rccm", "en cours d'immatriculation")}</td></tr>
<tr><td>Compte contribuable (NCC)</td><td>{_v("ncc", "en cours d'immatriculation")}</td></tr>
<tr><td>E-mail</td><td><a href="mailto:{email}">{email}</a></td></tr>
<tr><td>Téléphone</td><td>{_v("telephone", "communiqué prochainement")}</td></tr></tbody></table>
<p>Ces informations sont publiées conformément à l'obligation d'identification des personnes qui exercent une activité par voie électronique, prévue par la loi ivoirienne n°2013-546 du 30 juillet 2013 relative aux transactions électroniques. {'La société est immatriculée' if COMPANY['rccm'] else 'La société est en cours de constitution'} conformément à l'Acte uniforme OHADA relatif au droit des sociétés commerciales et du groupement d'intérêt économique.</p>

<h2 id="publication">2. Direction de la publication</h2>
<p>Directeur ou directrice de la publication : {_v("directeur_publication", "en cours de désignation")}. Pour toute question relative aux contenus : <a href="mailto:{email}">{email}</a>.</p>

<h2 id="hebergement">3. Hébergement</h2>
<p>Le site est hébergé par <strong>GitHub, Inc.</strong> (service GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis — <a href="https://github.com" rel="noopener" target="_blank">github.com</a>.</p>
<p>Le site est statique : il ne comporte ni base de données ni compte utilisateur côté serveur. L'hébergeur peut toutefois enregistrer des données techniques de connexion (adresse IP, date et heure) pour la sécurité et le bon fonctionnement de son service. Voir la <a href="~/politique-de-confidentialite/">politique de confidentialité</a>.</p>

<h2 id="cadre">4. Cadre juridique applicable</h2>
<p>ADA exerce son activité dans le respect, notamment, des textes suivants.</p>
<h3>Droit ivoirien</h3>
<ul>
<li>Loi n°2013-546 du 30 juillet 2013 relative aux transactions électroniques ;</li>
<li>Loi n°2013-450 du 19 juin 2013 relative à la protection des données à caractère personnel ;</li>
<li>Loi n°2013-451 du 19 juin 2013 relative à la lutte contre la cybercriminalité ;</li>
<li>Décret n°2014-106 relatif à l'écrit et à la signature électroniques ;</li>
<li>Décret n°2016-851 du 19 octobre 2016 relatif aux modalités de mise en œuvre de l'archivage électronique ;</li>
<li>Décret n°2021-916 portant référentiel général de sécurité des systèmes d'information (RGSSI) ;</li>
<li>Loi n°2016-555 du 26 juillet 2016 relative au droit d'auteur et aux droits voisins.</li></ul>
<p>Autorités compétentes : l'<strong>ARTCI</strong> (Autorité de régulation des télécommunications/TIC de Côte d'Ivoire), autorité de protection des données à caractère personnel ; l'<strong>ANSSI Côte d'Ivoire</strong> pour la sécurité des systèmes d'information.</p>
<h3>Cadres régionaux et internationaux</h3>
<ul>
<li><strong>OHADA</strong> : Acte uniforme relatif au droit des sociétés commerciales et du GIE, Acte uniforme portant sur le droit commercial général (registre du commerce) ;</li>
<li><strong>OAPI</strong> : Accord de Bangui, pour la protection des marques et autres titres de propriété industrielle dans les États membres ;</li>
<li><strong>CEDEAO</strong> : Acte additionnel A/SA.1/01/10 relatif à la protection des données à caractère personnel dans l'espace CEDEAO ;</li>
<li><strong>Union africaine</strong> : Convention sur la cybersécurité et la protection des données à caractère personnel (Convention de Malabo), cadre de référence continental ;</li>
<li><strong>Union européenne</strong> : Règlement général sur la protection des données (RGPD, règlement (UE) 2016/679), lorsqu'il s'applique aux personnes situées dans l'Union européenne.</li></ul>
<p>Les références aux normes internationales (ISO 15489, ISO 14721, ISO 23081, ISO 19005, ISO 27001…) présentes sur ce site décrivent la méthode de travail d'ADA. <strong>Elles ne valent pas certification</strong> : ADA ne revendique aucune certification qui n'a pas été délivrée par un organisme accrédité.</p>

<h2 id="pi">5. Propriété intellectuelle</h2>
<p>L'ensemble des éléments du site (textes, cours de l'ARCHIVA Academy, livres blancs, articles, captures d'écran, illustrations, logos, code source, mise en page) est protégé par la loi n°2016-555 relative au droit d'auteur et aux droits voisins et par les conventions internationales applicables. Toute reproduction, représentation, adaptation ou diffusion, totale ou partielle, sans l'autorisation écrite d'ADA est interdite, à l'exception des usages autorisés par la loi (courte citation avec mention de la source, usage privé).</p>
<p>Les dénominations <strong>ADA</strong>, <strong>African Digital Archives</strong>, <strong>ARCHIVA360</strong>, <strong>ARCHIVA AI</strong>, <strong>ARCHIVA GO</strong> et <strong>ARCHIVA Academy</strong> sont utilisées par ADA ; leur dépôt à titre de marques auprès de l'OAPI est en cours d'étude. La police de caractères Inter est utilisée sous licence SIL Open Font License.</p>

<h2 id="contenus">6. Nature des contenus et responsabilité</h2>
<ul>
<li>Les informations publiées (articles, guides, livres blancs, cours, glossaire), notamment sur le cadre juridique, ont une <strong>valeur informative et pédagogique</strong>. Elles ne constituent pas un conseil juridique. Chaque organisation doit faire valider son dispositif par un juriste selon son secteur.</li>
<li>Les durées de conservation citées en exemple ne sont pas des durées légales : elles doivent être fixées avec un archiviste et validées par un juriste.</li>
<li>Les <strong>tarifs</strong> affichés sont des tarifs de lancement indicatifs, hors taxes, qui ne constituent pas une offre ferme. Seule une proposition commerciale écrite engage ADA.</li>
<li>Les <strong>captures d'écran</strong> d'ARCHIVA360 et les données de la démo interactive sont fictives (organisation, personnes, montants).</li>
<li>Les fonctionnalités présentées comme « Version 2 » ou « Version 3 » sont en cours de développement.</li></ul>
<p>ADA s'efforce d'assurer l'exactitude et la mise à jour des informations, sans pouvoir garantir l'absence d'erreur. Signalez toute erreur à <a href="mailto:{email}">{email}</a>.</p>

<h2 id="outils">7. Outils en ligne : Academy, démo, Health Check</h2>
<ul>
<li><strong>ARCHIVA Academy</strong> : l'accès aux cours est gratuit. Les certificats délivrés sont des <strong>certificats internes de suivi de formation</strong> ; ils ne constituent ni un diplôme d'État ni une certification professionnelle réglementée. Le code de vérification permet de contrôler qu'un certificat n'a pas été modifié.</li>
<li><strong>Démo interactive ARCHIVA360</strong> : outil de démonstration, fourni en l'état, sans garantie de disponibilité ni de conservation des données. Il ne doit pas être utilisé pour conserver des documents réels ou confidentiels. Les fichiers importés restent dans le navigateur de l'utilisateur et ne sont pas transmis à ADA.</li>
<li><strong>Document Health Check</strong> : outil d'orientation ; le score obtenu n'est pas une certification ni un audit.</li></ul>

<h2 id="liens">8. Liens hypertextes</h2>
<p>Le site peut contenir des liens vers des sites tiers (autorités, normes, partenaires). ADA n'exerce aucun contrôle sur ces sites et décline toute responsabilité quant à leur contenu. La création d'un lien vers le présent site est libre, à condition de ne pas porter atteinte à l'image d'ADA et de ne pas présenter ses contenus comme les siens.</p>

<h2 id="donnees">9. Données personnelles et cookies</h2>
<p>Le traitement des données personnelles est décrit dans la <a href="~/politique-de-confidentialite/">politique de confidentialité</a>, qui précise notamment les finalités, les durées de conservation, vos droits et la gestion des cookies.</p>

<h2 id="droit">10. Droit applicable et juridiction</h2>
<p>Les présentes mentions et l'utilisation du site sont régies par le <strong>droit ivoirien</strong>. En cas de litige, et à défaut de solution amiable recherchée en priorité, les juridictions compétentes d'Abidjan seront seules compétentes, sous réserve des règles impératives applicables aux consommateurs.</p>

<h2 id="contact">11. Contact</h2>
<p>Pour toute question relative au site : <a href="mailto:{email}">{email}</a>.</p>
<p class="has-muted-color has-small-font-size">Dernière mise à jour : {UPDATED}.</p>'''

    add(Page("mentions-legales", "Mentions légales", section(pending + f'<div class="legal-content entry-content">{_wrap(ml)}</div>'),
             description="Mentions légales du site African Digital Archives (ADA) : éditeur, hébergement, cadre juridique ivoirien et international, propriété intellectuelle, responsabilité.",
             hero=page_hero("Mentions légales", "Informations sur l'éditeur du site et le cadre juridique applicable.", [("Mentions légales", None)], light=True),
             nav="", search=False))

    # ------------------------------------------------------------------ confidentialité
    pc_toc = [("responsable", "Responsable du traitement"), ("principes", "Nos principes"), ("traitements", "Données traitées et finalités"),
              ("local", "Données conservées uniquement dans votre navigateur"), ("destinataires", "Destinataires et sous-traitants"),
              ("transferts", "Transferts hors de Côte d'Ivoire"), ("durees", "Durées de conservation"), ("securite", "Sécurité"),
              ("droits", "Vos droits"), ("cookies", "Cookies et stockage local"), ("mineurs", "Mineurs"), ("modifs", "Modifications")]
    pc = f'''{_toc(pc_toc)}
<p>ADA est une entreprise de gestion documentaire et d'archivage : la protection des données personnelles est au cœur de son métier. Cette politique explique quelles données ce site traite, pourquoi, et comment exercer vos droits. Elle est établie conformément à la loi ivoirienne n°2013-450 du 19 juin 2013 relative à la protection des données à caractère personnel et, lorsqu'ils s'appliquent, à l'Acte additionnel de la CEDEAO A/SA.1/01/10 et au règlement européen (UE) 2016/679 (RGPD).</p>

<h2 id="responsable">1. Responsable du traitement</h2>
<p><strong>{COMPANY["raison_sociale"]} ({COMPANY["sigle"]})</strong>, {COMPANY["siege"]}. Contact pour toute question relative à vos données : <a href="mailto:{email}">{email}</a>.</p>
<p>Déclaration ou autorisation auprès de l'ARTCI : {_v("artci", "formalités en cours")}.</p>

<h2 id="principes">2. Nos principes</h2>
<ul><li><strong>Minimisation</strong> : nous ne collectons que ce qui est nécessaire pour vous répondre.</li>
<li><strong>Pas de vente</strong> de données, pas de publicité ciblée, pas de traceur publicitaire.</li>
<li><strong>Traitement local</strong> chaque fois que possible : vos résultats de diagnostic, votre progression de formation et les fichiers de la démo restent dans votre navigateur.</li>
<li><strong>Transparence</strong> : cette page décrit l'intégralité des traitements liés au site.</li></ul>

<h2 id="traitements">3. Données traitées et finalités</h2>
<table><thead><tr><th>Traitement</th><th>Données</th><th>Finalité</th><th>Fondement</th></tr></thead><tbody>
<tr><td>Formulaires de contact, d'audit, de démonstration, de devis, questions sur les articles</td><td>Nom, organisation, fonction, e-mail, téléphone, pays, secteur, volume d'archives, message</td><td>Répondre à votre demande et préparer une proposition</td><td>Votre consentement et les mesures précontractuelles prises à votre demande</td></tr>
<tr><td>Lettre d'information</td><td>Adresse e-mail</td><td>Vous envoyer la lettre mensuelle d'ADA</td><td>Votre consentement, retirable à tout moment</td></tr>
<tr><td>Échanges par e-mail</td><td>Contenu des échanges</td><td>Suivi de la relation</td><td>Intérêt légitime et mesures précontractuelles</td></tr>
<tr><td>Données techniques de connexion (hébergeur)</td><td>Adresse IP, date et heure, navigateur</td><td>Sécurité et fonctionnement du service d'hébergement</td><td>Intérêt légitime de l'hébergeur</td></tr></tbody></table>
<p><strong>Comment les formulaires fonctionnent aujourd'hui :</strong> ils ouvrent votre propre logiciel de messagerie avec un message prérempli à l'attention de <a href="mailto:{email}">{email}</a>. Rien n'est envoyé tant que vous ne validez pas l'envoi depuis votre messagerie, et le site lui-même ne stocke aucune donnée. Si un service de réception de formulaires est mis en place ultérieurement, cette page sera mise à jour pour l'indiquer.</p>

<h2 id="local">4. Données conservées uniquement dans votre navigateur</h2>
<p>Ces données sont enregistrées dans le stockage local de votre navigateur (localStorage ou IndexedDB). <strong>Elles ne sont pas transmises à ADA</strong> et ADA n'y a pas accès :</p>
<ul><li><strong>ARCHIVA Academy</strong> : nom saisi pour les certificats, progression, scores des quiz et des examens, certificats obtenus ;</li>
<li><strong>Démo interactive ARCHIVA360</strong> : fichiers que vous importez, métadonnées, journal d'audit de la démo ;</li>
<li><strong>Document Health Check</strong> : vos réponses sont calculées dans la page et ne sont pas enregistrées ;</li>
<li><strong>Bandeau cookies</strong> : votre choix (accepter ou refuser).</li></ul>
<p>Vous pouvez effacer ces données à tout moment en supprimant les données de site de votre navigateur, ou, pour la démo, avec le bouton « Réinitialiser la démo ». N'importez pas de documents réels ou confidentiels dans la démo.</p>

<h2 id="destinataires">5. Destinataires et sous-traitants</h2>
<p>Les données transmises par e-mail sont destinées aux seules personnes d'ADA chargées de vous répondre. Elles ne sont ni vendues, ni louées, ni cédées. Interviennent techniquement : l'hébergeur du site (GitHub, Inc.) et le fournisseur de messagerie d'ADA. Certaines bibliothèques techniques de la démo (lecture des PDF, OCR, QR codes) sont chargées à la demande depuis des réseaux de diffusion de contenus (cdnjs, jsDelivr), qui reçoivent à cette occasion les données techniques de connexion habituelles ; vos documents ne leur sont pas transmis.</p>

<h2 id="transferts">6. Transferts hors de Côte d'Ivoire</h2>
<p>L'hébergeur du site est établi aux États-Unis et les réseaux de diffusion de contenus peuvent servir les fichiers depuis différents pays. Ces transferts portent sur des données techniques de connexion. Conformément à la loi n°2013-450, ADA veille à ce que tout transfert de données personnelles vers un pays tiers s'accompagne de garanties appropriées et, le cas échéant, des formalités requises auprès de l'ARTCI.</p>

<h2 id="durees">7. Durées de conservation</h2>
<table><thead><tr><th>Données</th><th>Durée</th></tr></thead><tbody>
<tr><td>Demandes sans suite commerciale</td><td>3 ans après le dernier contact</td></tr>
<tr><td>Données clients</td><td>Durée de la relation, puis durées légales applicables (comptabilité, fiscalité)</td></tr>
<tr><td>Lettre d'information</td><td>Jusqu'à votre désinscription</td></tr>
<tr><td>Données stockées dans votre navigateur</td><td>Jusqu'à ce que vous les effaciez</td></tr></tbody></table>

<h2 id="securite">8. Sécurité</h2>
<p>Le site est servi en HTTPS. Il ne comporte ni compte utilisateur ni base de données en ligne. Les échanges avec ADA sont traités par des personnes habilitées, tenues à la confidentialité. En cas de violation de données susceptible d'engendrer un risque pour vos droits, ADA en informera l'autorité compétente et les personnes concernées dans les conditions prévues par la loi.</p>

<h2 id="droits">9. Vos droits</h2>
<p>Conformément à la loi n°2013-450, vous disposez des droits suivants sur vos données : <strong>information</strong>, <strong>accès</strong>, <strong>rectification</strong>, <strong>opposition</strong> pour des motifs légitimes et à la prospection, et <strong>suppression</strong> des données inexactes, incomplètes ou dont la conservation n'est plus justifiée. Si le RGPD vous est applicable, vous disposez en outre des droits à la limitation et à la portabilité.</p>
<p>Pour exercer vos droits : <a href="mailto:{email}">{email}</a>, en précisant votre demande. Une réponse vous est apportée dans les meilleurs délais. Vous pouvez également saisir l'<strong>ARTCI</strong> (Autorité de régulation des télécommunications/TIC de Côte d'Ivoire) ou, si le RGPD s'applique, l'autorité de protection des données de votre pays de résidence.</p>

<h2 id="cookies">10. Cookies et stockage local</h2>
<p>Ce site <strong>n'utilise aucun cookie publicitaire ni outil de mesure d'audience</strong>. Il utilise uniquement le stockage local du navigateur pour les fonctions décrites ci-dessus (choix relatif aux cookies, progression de formation, démo). Si un outil de mesure d'audience était ajouté, il ne serait activé qu'avec votre accord, recueilli par le bandeau prévu à cet effet, et cette page serait mise à jour.</p>

<h2 id="mineurs">11. Mineurs</h2>
<p>Les services d'ADA s'adressent aux organisations et aux professionnels. Les formations de l'Academy sont ouvertes à tous ; aucune donnée n'est collectée par ADA lors de leur utilisation.</p>

<h2 id="modifs">12. Modifications</h2>
<p>Cette politique peut évoluer, notamment lors de l'ouverture du portail client ARCHIVA360. La date de mise à jour figure ci-dessous.</p>
<p class="has-muted-color has-small-font-size">Dernière mise à jour : {UPDATED}.</p>'''
    add(Page("politique-de-confidentialite", "Politique de confidentialité", section(f'<div class="legal-content entry-content">{_wrap(pc)}</div>'),
             description="Politique de confidentialité d'ADA : données traitées, finalités, stockage local, durées, droits (loi ivoirienne n°2013-450, CEDEAO, RGPD), cookies.",
             hero=page_hero("Politique de confidentialité", "Quelles données ce site traite, pourquoi, et comment exercer vos droits.", [("Politique de confidentialité", None)], light=True),
             nav="", search=False))
