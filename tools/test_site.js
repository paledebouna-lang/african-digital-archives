// Tests automatiques du site ADA (Playwright).
// 1. Servir le site :   python3 -m http.server 8765
// 2. Lancer :           node tools/test_site.js [url-de-base]
const fs = require('fs');
const path = require('path');
let playwright;
try { playwright = require('playwright'); } catch (e) { playwright = require('/opt/node22/lib/node_modules/playwright'); }

const BASE = (process.argv[2] || 'http://localhost:8765/').replace(/\/?$/, '/');
const ROOT = path.resolve(__dirname, '..');
const results = [];
function check(name, ok, detail) { results.push({ name, ok: !!ok, detail: detail || '' }); console.log(`${ok ? '✔' : '✘'} ${name}${detail ? ' — ' + detail : ''}`); }
// Ressources externes chargées à la demande (CDN) : leur échec réseau n'est pas une erreur du site.
const IGNORED = /ERR_TUNNEL_CONNECTION_FAILED|ERR_NAME_NOT_RESOLVED|ERR_INTERNET_DISCONNECTED|cdnjs|jsdelivr/;

function pages() {
  const out = [];
  (function walk(d) {
    for (const f of fs.readdirSync(d)) {
      if (['tools', 'wp-content', '.git', 'node_modules'].includes(f)) continue;
      const p = path.join(d, f);
      if (fs.statSync(p).isDirectory()) walk(p);
      else if (f === 'index.html') out.push(path.relative(ROOT, path.dirname(p)));
    }
  })(ROOT);
  return out.map(p => (p ? p + '/' : ''));
}

function linkCheck(list) {
  let broken = [];
  for (const p of list) {
    const file = path.join(ROOT, p, 'index.html');
    const html = fs.readFileSync(file, 'utf8');
    for (const m of html.matchAll(/(?:href|src)="([^"#?]+)[^"]*"/g)) {
      const u = m[1];
      if (/^(https?:|mailto:|data:|tel:|javascript:)/.test(u)) continue;
      let t = path.normalize(path.join(path.dirname(file), u));
      if (u.endsWith('/') || (fs.existsSync(t) && fs.statSync(t).isDirectory())) t = path.join(t, 'index.html');
      if (!fs.existsSync(t)) broken.push(p + ' → ' + u);
    }
  }
  return [...new Set(broken)];
}

(async () => {
  const list = pages();
  const broken = linkCheck(list);
  check(`Liens internes (${list.length} pages)`, !broken.length, broken.slice(0, 5).join(' | '));

  const browser = await playwright.chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, acceptDownloads: true });
  const page = await ctx.newPage();
  let errs = [];
  page.on('pageerror', e => errs.push(e.message));
  page.on('console', m => { if (m.type() === 'error' && !IGNORED.test(m.text())) errs.push(m.text()); });

  // Erreurs JavaScript et débordement mobile sur toutes les pages
  const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  const jsErr = [], overflow = [];
  for (const p of list) {
    errs = [];
    await page.goto(BASE + p, { waitUntil: 'load' });
    if (errs.length) jsErr.push(p + ': ' + errs[0]);
    await mobile.goto(BASE + p, { waitUntil: 'load' });
    const w = await mobile.evaluate(() => document.documentElement.scrollWidth);
    if (w > 392) overflow.push(p + ' (' + w + 'px)');
  }
  check('Aucune erreur JavaScript', !jsErr.length, jsErr.slice(0, 3).join(' | '));
  check('Aucun débordement horizontal à 390 px', !overflow.length, overflow.slice(0, 3).join(' | '));
  await mobile.close();

  // Formulaire de contact
  await page.goto(BASE + 'contact/?sujet=demo&diagnostic=64');
  check('Contact : objet prérempli depuis l’URL', (await page.inputValue('#cf7-subject')) === 'demo');
  check('Contact : message prérempli depuis le Health Check', (await page.inputValue('#cf7-message')).includes('64/100'));
  await page.click('.wpcf7-submit');
  check('Contact : validation des champs obligatoires', (await page.locator('.wpcf7-not-valid-tip').count()) >= 3);

  // Document Health Check
  await page.goto(BASE + 'ressources/document-health-check/');
  for (let i = 1; i <= 20; i++) await page.check(`input[name=q${i}][value="${i % 2 ? '1' : '0.5'}"]`);
  check('Health Check : score calculé', (await page.textContent('#hc-score')) === '75', 'score ' + (await page.textContent('#hc-score')));

  // Recherche, glossaire, empreinte
  await page.goto(BASE + 'recherche/?s=numérisation');
  check('Recherche interne', /\d+ résultat/.test(await page.textContent('#search-title')));
  await page.goto(BASE + 'ressources/glossaire/');
  await page.fill('#glossary-filter', 'ocr');
  check('Glossaire : filtre', (await page.locator('.glossary-term:not(.is-hidden)').count()) >= 1);
  await page.goto(BASE + 'archiva360/modules/');
  await page.fill('#hash-input', 'modifié');
  check('Démonstration d’empreinte : altération détectée', (await page.textContent('.hash-status span')).startsWith('Altéré'));

  // Livres blancs
  const wpPdf = await ctx.request.get(BASE + 'wp-content/uploads/2026/10/archiver-en-cote-divoire.pdf');
  check('Livres blancs : PDF téléchargeable', wpPdf.ok() && (await wpPdf.body()).slice(0, 4).toString() === '%PDF');

  // ARCHIVA Academy : parcours complet du niveau 1
  await page.goto(BASE + 'academy/');
  await page.fill('#learner-name', 'Test Apprenant');
  await page.click('#learner-form button');
  await page.goto(BASE + 'academy/niveau-1/#m1');
  const data = JSON.parse(await page.textContent('#course-data'));
  for (let m = 0; m < data.modules.length; m++) {
    await page.goto(BASE + `academy/niveau-1/#m${m + 1}-quiz`);
    const f = `[data-quiz-form="${m}"]`;
    if (await page.locator(`${f}.is-graded`).count()) await page.click(`${f} button[type=submit]`);
    const qs = data.modules[m].quiz;
    for (let i = 0; i < qs.length; i++) for (const a of qs[i].a) await page.check(`${f} input[name="niveau-1-q${m}-${i}"][value="${a}"]`);
    await page.click(`${f} button[type=submit]`);
  }
  await page.goto(BASE + 'academy/niveau-1/#examen');
  check('Academy : examen déverrouillé après les quiz', await page.isHidden('#exam-locked'));
  await page.click('#exam-start');
  const pool = [].concat(...data.modules.map(m => m.quiz), data.examExtra);
  const legends = await page.$$eval('#exam-form .quiz-q legend', ls => ls.map(l => l.childNodes[1].textContent));
  for (let i = 0; i < legends.length; i++) for (const a of pool.find(q => q.q === legends[i]).a) await page.check(`#exam-form input[name="niveau-1-exam-${i}"][value="${a}"]`);
  await page.click('#exam-form button[type=submit]');
  await page.waitForSelector('#exam-result:not([hidden])');
  check('Academy : examen réussi', (await page.textContent('#exam-result')).includes('Félicitations'));
  await page.click('#exam-result a');
  await page.waitForSelector('.certificate__code');
  const code = await page.textContent('.certificate__code');
  const exam = await page.evaluate(() => JSON.parse(localStorage.getItem('ada_academy_v1')).levels['niveau-1'].exam);
  check('Academy : certificat généré', /^[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}$/.test(code), code);
  await page.goto(BASE + 'academy/verifier/');
  await page.fill('#v-name', 'test apprenant'); await page.fill('#v-date', exam.date); await page.fill('#v-score', String(exam.score)); await page.fill('#v-code', code);
  await page.click('#verify-form button');
  await page.waitForSelector('#verify-result .notice');
  check('Academy : certificat vérifié', (await page.textContent('#verify-result')).includes('authentique'));
  await page.fill('#v-score', String(exam.score - 1)); await page.click('#verify-form button'); await page.waitForTimeout(200);
  check('Academy : certificat falsifié rejeté', (await page.textContent('#verify-result')).includes('ne correspond pas'));

  // Démo ARCHIVA360
  const D = BASE + 'archiva360/demo-interactive/';
  await page.goto(D + '#dashboard');
  await page.waitForSelector('.kpi', { timeout: 15000 });
  check('Démo : espace d’exemple créé', Number(await page.textContent('.kpi b')) >= 13);
  await page.fill('#top-q', 'Factures supérieures à 5 millions FCFA'); await page.press('#top-q', 'Enter');
  check('Démo : recherche en langage naturel', (await page.textContent('#view .box h2')).startsWith('3 résultat'));
  await page.click('[data-go="documents"]');
  await page.setInputFiles('#file-input', { name: 'Facture_TEST.txt', mimeType: 'text/plain', buffer: Buffer.from('SOCIETE TEST SA\nFACTURE N° FAC-9001\nDate : 15/09/2026\nTotal TTC : 2 500 000 FCFA') });
  await page.waitForSelector('.drawer');
  check('Démo : métadonnées proposées à l’import', (await page.locator('.field.proposed').count()) >= 4);
  await page.click('#meta-form button'); await page.waitForTimeout(200);
  await page.click('[data-act="archive"]'); await page.waitForTimeout(500);
  check('Démo : versement au SAE', (await page.textContent('.drawer .sub')).includes('Archivé'));
  await page.click('[data-tab="versions"]'); await page.click('[data-act="tamper"]'); await page.waitForTimeout(300);
  await page.click('[data-act="verify"]'); await page.waitForTimeout(500);
  check('Démo : altération détectée par l’empreinte', (await page.textContent('#verify-out')).includes('altéré'));
  await page.keyboard.press('Escape');
  await page.click('[data-go="retention"]'); await page.selectOption('#horizon', 'past');
  const holdBtn = await page.$('[data-act="eliminate"][disabled]');
  check('Démo : élimination bloquée par le gel juridique', !!holdBtn);
  const free = await page.$('[data-act="eliminate"]:not([disabled])');
  await free.click(); await page.click('[data-act="eliminate-confirm"]'); await page.waitForTimeout(500);
  check('Démo : élimination avec certificat', (await page.textContent('#view')).includes('CERT-ELIM-'));
  await page.selectOption('#who', 'u2'); await page.click('[data-go="documents"]');
  check('Démo : documents confidentiels masqués pour un employé', (await page.textContent('#view')).includes('ne sont pas visibles'));
  await page.selectOption('#who', 'u1');
  await page.click('[data-go="backup"]');
  const [dl] = await Promise.all([page.waitForEvent('download'), page.click('[data-act="backup-export"]')]);
  const bp = path.join(require('os').tmpdir(), 'ada-backup-test.json'); await dl.saveAs(bp);
  await page.setInputFiles('#restore-input', bp); await page.waitForSelector('#restore-result .notice', { timeout: 10000 });
  check('Démo : sauvegarde puis restauration', /Restauration/.test(await page.textContent('#restore-result')));
  await page.click('[data-go="audit"]'); await page.click('[data-act="verify-chain"]');
  await page.waitForSelector('#chain-result .notice', { timeout: 10000 });
  check('Démo : journal d’audit chaîné intègre', (await page.textContent('#chain-result')).includes('intègre'));
  await page.goto(D + '#dashboard'); await page.reload(); await page.waitForSelector('.kpi');
  check('Démo : données conservées après rechargement', Number(await page.textContent('.kpi b')) >= 13);

  await browser.close();
  const failed = results.filter(r => !r.ok);
  console.log(`\n${results.length - failed.length}/${results.length} tests réussis`);
  process.exit(failed.length ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
