// Tests des comptes en ligne ARCHIVA360, contre un faux serveur Appwrite local.
// 1. Servir le site :   python3 -m http.server 8765
// 2. Lancer :           node tools/test_accounts.js [url-de-base]
// Le faux serveur reproduit les routes Appwrite utilisées par archiva360-auth.js et appwrite_setup.mjs.
const http = require('http');
const path = require('path');
const crypto = require('crypto');
const { execFile } = require('child_process');
// Le script tourne dans un processus séparé et asynchrone : le faux serveur de ce processus doit rester disponible.
const run = env => new Promise((ok, ko) => execFile('node', [path.join(__dirname, 'appwrite_setup.mjs')], { env: Object.assign({}, process.env, env), encoding: 'utf8' }, (e, out) => (e ? ko(e) : ok(out))));
let playwright;
try { playwright = require('playwright'); } catch (e) { playwright = require('/opt/node22/lib/node_modules/playwright'); }

const BASE = (process.argv[2] || 'http://localhost:8765/').replace(/\/?$/, '/');
const MOCK_PORT = 8766, ENDPOINT = `http://localhost:${MOCK_PORT}/v1`, PROJECT = 'ada-test', KEY = 'secret-key';
const results = [];
function check(name, ok, detail) { results.push({ ok: !!ok }); console.log(`${ok ? '✔' : '✘'} ${name}${detail ? ' — ' + detail : ''}`); }

/* ---------- Faux Appwrite ---------- */
const db = { users: [], teams: [], memberships: [], sessions: {}, mail: [] };
const id = () => crypto.randomBytes(8).toString('hex');
const now = () => new Date().toISOString();
const COOKIE = 'a_session_' + PROJECT;
function mock(req, res) {
  const cors = { 'Access-Control-Allow-Origin': req.headers.origin || '*', 'Access-Control-Allow-Credentials': 'true',
    'Access-Control-Allow-Headers': 'Content-Type, X-Appwrite-Project, X-Appwrite-Key, X-Fallback-Cookies, X-Appwrite-Response-Format',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, PATCH, DELETE', 'Access-Control-Expose-Headers': 'X-Fallback-Cookies' };
  const send = (code, body, extra) => { res.writeHead(code, Object.assign({ 'Content-Type': 'application/json' }, cors, extra || {})); res.end(code === 204 ? '' : JSON.stringify(body)); };
  const fail = (code, type, message) => send(code, { code, type, message: message || type });
  if (req.method === 'OPTIONS') return send(204);
  let raw = '';
  req.on('data', c => (raw += c));
  req.on('end', () => {
    const u = new URL(req.url, 'http://x'), p = u.pathname.replace(/^\/v1/, ''), b = raw ? JSON.parse(raw) : {};
    if (req.headers['x-appwrite-project'] !== PROJECT) return fail(404, 'project_not_found');
    const server = req.headers['x-appwrite-key'] === KEY;
    let fb = {}; try { fb = JSON.parse(req.headers['x-fallback-cookies'] || '{}'); } catch (e) {}
    const me = db.users.find(x => x.$id === db.sessions[fb[COOKIE]]);
    const publicUser = x => ({ $id: x.$id, name: x.name, email: x.email, registration: x.registration, $createdAt: x.registration });
    const session = user => { const t = id(); db.sessions[t] = user.$id; return { 'X-Fallback-Cookies': JSON.stringify({ [COOKIE]: t }) }; };
    const team = p.match(/^\/teams\/([^/]+)\/memberships(?:\/([^/]+))?(\/status)?$/);
    const ms = t => db.memberships.filter(m => m.teamId === t);
    const isOwner = t => server || ms(t).some(m => me && m.userId === me.$id && m.confirm && m.roles.includes('owner'));
    const M = m => { const x = db.users.find(y => y.$id === m.userId); return Object.assign({}, m, { userName: x.name, userEmail: x.email, secret: undefined }); };

    if (p === '/health/version') return send(200, { version: 'mock' });
    if (p === '/__mail') return send(200, db.mail);
    if (p === '/teams' && req.method === 'POST' && server) {
      if (db.teams.some(t => t.$id === b.teamId)) return fail(409, 'team_already_exists');
      db.teams.push({ $id: b.teamId, name: b.name }); return send(201, db.teams.at(-1));
    }
    if (p === '/users' && req.method === 'GET' && server) return send(200, { users: db.users.filter(x => x.email.includes(u.searchParams.get('search') || '')).map(publicUser) });
    if (p === '/users' && req.method === 'POST' && server) {
      const x = { $id: id(), email: b.email, name: b.name, password: b.password, registration: now() }; db.users.push(x); return send(201, publicUser(x));
    }
    if (/^\/users\/[^/]+\/verification$/.test(p) && server) return send(200, {});
    if (p === '/account/sessions/email' && req.method === 'POST') {
      const x = db.users.find(y => y.email === b.email && y.password && y.password === b.password);
      if (!x) return fail(401, 'user_invalid_credentials');
      return send(201, { $id: id() }, session(x));
    }
    if (p === '/account/recovery' && req.method === 'POST') {
      const x = db.users.find(y => y.email === b.email); if (!x) return fail(404, 'user_not_found');
      x.recovery = id(); db.mail.push({ to: x.email, link: `${b.url}&userId=${x.$id}&secret=${x.recovery}&expire=x` }); return send(201, {});
    }
    if (p === '/account/recovery' && req.method === 'PUT') {
      const x = db.users.find(y => y.$id === b.userId && y.recovery && y.recovery === b.secret);
      if (!x) return fail(401, 'user_invalid_token'); x.password = b.password; x.recovery = null; return send(200, {});
    }
    if (p.startsWith('/account') && !me) return fail(401, 'general_unauthorized_scope');
    if (p === '/account' && req.method === 'GET') return send(200, publicUser(me));
    if (p === '/account/name') { me.name = b.name; return send(200, publicUser(me)); }
    if (p === '/account/password') {
      if (me.password && me.password !== b.oldPassword) return fail(401, 'user_invalid_credentials');
      me.password = b.password; return send(200, publicUser(me));
    }
    if (p === '/account/sessions/current' || p === '/account/sessions') {
      for (const t of Object.keys(db.sessions)) if ((p === '/account/sessions' && db.sessions[t] === me.$id) || t === fb[COOKIE]) delete db.sessions[t];
      return send(204);
    }
    if (team) {
      const [, t, mid, status] = team;
      if (status) {
        const m = db.memberships.find(x => x.$id === mid);
        if (!m || m.secret !== b.secret || m.userId !== b.userId) return fail(401, 'team_invalid_secret');
        m.confirm = true; m.joined = now(); m.secret = null;
        return send(200, M(m), session(db.users.find(x => x.$id === m.userId)));
      }
      if (!server && !(me && ms(t).some(m => m.userId === me.$id && m.confirm))) return fail(401, 'user_unauthorized');
      if (req.method === 'GET') return send(200, { total: ms(t).length, memberships: ms(t).map(M) });
      if (!isOwner(t)) return fail(401, 'user_unauthorized');
      if (req.method === 'POST') {
        let x = b.userId ? db.users.find(y => y.$id === b.userId) : db.users.find(y => y.email === b.email);
        if (!x) { x = { $id: id(), email: b.email, name: b.name, password: null, registration: now() }; db.users.push(x); }
        if (ms(t).some(m => m.userId === x.$id)) return fail(409, 'team_invite_already_exists');
        const m = { $id: id(), teamId: t, userId: x.$id, roles: b.roles, invited: now(), joined: server ? now() : null, confirm: server, secret: server ? null : id() };
        db.memberships.push(m);
        if (!server) db.mail.push({ to: x.email, link: `${b.url}&membershipId=${m.$id}&userId=${x.$id}&secret=${m.secret}&teamId=${t}` });
        return send(201, M(m));
      }
      const m = db.memberships.find(x => x.$id === mid); if (!m) return fail(404, 'membership_not_found');
      if (req.method === 'PATCH') { m.roles = b.roles; return send(200, M(m)); }
      if (req.method === 'DELETE') { db.memberships.splice(db.memberships.indexOf(m), 1); return send(204); }
    }
    fail(404, 'general_route_not_found', req.method + ' ' + p);
  });
}

(async () => {
  const srv = http.createServer(mock).listen(MOCK_PORT);
  const lastMail = to => db.mail.filter(m => m.to === to).at(-1).link;

  // Script d'installation
  const out = await run({ APPWRITE_ENDPOINT: ENDPOINT, APPWRITE_PROJECT: PROJECT, APPWRITE_API_KEY: KEY, ADMIN_EMAIL: 'assa@eletude.org', ADMIN_NAME: 'Assa Admin' });
  const pass = (out.match(/Mot de passe provisoire : (\S+)/) || [])[1];
  check('Installation : équipe et administrateur créés', pass && db.memberships[0].roles.includes('owner'));
  const again = await run({ APPWRITE_ENDPOINT: ENDPOINT, APPWRITE_PROJECT: PROJECT, APPWRITE_API_KEY: KEY });
  check('Installation : relance sans doublon', /déjà présent/.test(again) && db.users.length === 1 && db.memberships.length === 1);

  // Les pages réécrites par route.fulfill n'ont pas d'espace d'adresses connu : on lève le contrôle d'accès au réseau local.
  const browser = await playwright.chromium.launch({ args: ['--disable-features=LocalNetworkAccessChecks,PrivateNetworkAccessRespectPreflightResults'] });
  const errs = [];
  async function context() {
    // Service worker bloqué : sinon les pages qu'il sert échapperaient à la réécriture de configuration ci-dessous.
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 860 }, serviceWorkers: 'block' });
    // Branche la page sur le faux serveur (le site publié n'a pas encore de projet configuré).
    await ctx.route(/archiva360\/(connexion|espace)\/(\?.*)?$/, async route => {
      const r = await route.fetch();
      const html = (await r.text()).replace(/"endpoint": "[^"]*", "project": "[^"]*"/, `"endpoint": "${ENDPOINT}", "project": "${PROJECT}"`);
      route.fulfill({ response: r, body: html });
    });
    ctx.on('page', pg => { pg.on('pageerror', e => errs.push(e.message)); pg.on('console', m => process.env.DEBUG && console.log('  [console]', m.text())); });
    ctx.on('dialog', d => d.accept());
    return ctx;
  }
  const L = BASE + 'archiva360/connexion/', E = BASE + 'archiva360/espace/';

  // Administrateur
  const admin = await (await context()).newPage();
  await admin.goto(E);
  await admin.waitForURL(/connexion/);
  check('Espace : redirection vers la connexion si non connecté', true);
  await admin.waitForSelector('#login-form');
  await admin.fill('#l-email', 'assa@eletude.org'); await admin.fill('#l-pass', 'mauvais'); await admin.click('#login-form button');
  await admin.waitForSelector('#auth-msg .notice');
  check('Connexion : mauvais mot de passe refusé', (await admin.textContent('#auth-msg')).includes('incorrect'), await admin.textContent('#auth-msg'));
  if (process.env.SHOTS) await admin.screenshot({ path: path.join(process.env.SHOTS, 'connexion.png') });
  await admin.fill('#l-pass', pass); await admin.click('#login-form button');
  await admin.waitForURL(/espace/); await admin.waitForSelector('#view h1');
  check('Connexion : administrateur connecté', (await admin.textContent('#view')).includes('Administrateur') && (await admin.textContent('#who-name')) === 'Assa Admin');

  await admin.click('[data-go="utilisateurs"]'); await admin.waitForSelector('#invite-form');
  await admin.fill('#i-name', 'Awa Koné'); await admin.fill('#i-email', 'awa@example.org'); await admin.selectOption('#i-role', 'archiviste');
  await admin.click('#invite-form button'); await admin.waitForSelector('#inv-msg .notice.ok');
  if (process.env.SHOTS) await admin.screenshot({ path: path.join(process.env.SHOTS, 'utilisateurs.png'), fullPage: true });
  check('Utilisateurs : invitation envoyée', (await admin.textContent('#view tbody')).includes('Invitation envoyée') && db.mail.some(m => m.to === 'awa@example.org'));
  await admin.fill('#i-name', 'Awa'); await admin.fill('#i-email', 'AWA@example.org'); await admin.click('#invite-form button');
  check('Utilisateurs : doublon refusé', (await admin.textContent('#inv-msg')).includes('déjà partie'));
  check('Utilisateurs : propre rôle non modifiable', await admin.isDisabled(`[data-role="${db.memberships[0].$id}"]`));

  // Invitée : accepte l'invitation et choisit son mot de passe
  const awaCtx = await context(); const awa = await awaCtx.newPage();
  await awa.goto(lastMail('awa@example.org'));
  await awa.waitForSelector('#invite-form');
  await awa.fill('#p1', 'court'); await awa.fill('#p2', 'court'); await awa.click('#invite-form button');
  check('Invitation : mot de passe faible refusé', (await awa.textContent('#auth-msg')).includes('10 caractères'));
  await awa.fill('#p1', 'Archives2026!'); await awa.fill('#p2', 'Archives2026!'); await awa.click('#invite-form button');
  await awa.waitForURL(/espace/); await awa.waitForSelector('#view h1');
  check('Invitation : compte activé avec le bon rôle', (await awa.textContent('#view')).includes('Archiviste') && (await awa.textContent('#view')).includes('activé'));
  check('Rôles : pas de gestion des utilisateurs hors administrateur', !(await awa.$('[data-go="utilisateurs"]')));

  // L'administrateur change le rôle
  await admin.reload(); await admin.waitForSelector('#invite-form');
  const awaM = db.memberships.find(m => m.userId !== db.memberships[0].userId);
  await admin.selectOption(`[data-role="${awaM.$id}"]`, 'auditeur'); await admin.waitForSelector('#toast:not([hidden])');
  check('Utilisateurs : rôle modifié', awaM.roles.join() === 'auditeur' && (await admin.textContent('#view tbody')).includes('Actif'));
  await awa.reload(); await awa.waitForSelector('#view h1');
  check('Rôles : nouveau rôle pris en compte', (await awa.textContent('#who-role')) === 'Auditeur');

  // Mon compte
  await awa.goto(E + '#compte'); await awa.waitForSelector('#pw-form');
  await awa.fill('#a-name', 'Awa Koné (Archives)'); await awa.click('#name-form button'); await awa.waitForTimeout(300);
  check('Mon compte : nom modifié', (await awa.textContent('#who-name')) === 'Awa Koné (Archives)');
  await awa.fill('#a-old', 'faux'); await awa.fill('#p1', 'Nouveau2026x'); await awa.fill('#p2', 'Nouveau2026x'); await awa.click('#pw-form button');
  await awa.waitForSelector('#pw-msg .notice');
  check('Mon compte : ancien mot de passe vérifié', (await awa.textContent('#pw-msg')).includes('incorrect'));
  await awa.click('.top [data-act="logout"]'); await awa.waitForURL(/connexion/);
  check('Déconnexion', true);

  // Mot de passe oublié
  await awa.waitForSelector('[data-act="forgot"]'); await awa.click('[data-act="forgot"]');
  await awa.fill('#f-email', 'awa@example.org'); await awa.click('#forgot-form button'); await awa.waitForSelector('#auth-msg .notice.ok');
  await awa.goto(lastMail('awa@example.org')); await awa.waitForSelector('#reset-form');
  await awa.fill('#p1', 'Recuperation2026'); await awa.fill('#p2', 'Recuperation2026'); await awa.click('#reset-form button');
  await awa.waitForSelector('#login-form');
  await awa.fill('#l-email', 'awa@example.org'); await awa.fill('#l-pass', 'Recuperation2026'); await awa.click('#login-form button');
  await awa.waitForURL(/espace/); await awa.waitForSelector('#view h1');
  check('Mot de passe oublié : réinitialisation puis connexion', (await awa.textContent('#view')).includes('Bonjour'));
  await awa.goto(L); await awa.waitForURL(/espace/);
  check('Connexion : utilisateur déjà connecté redirigé vers l’espace', true);

  // Retrait de l'accès
  await admin.reload(); await admin.waitForSelector('#invite-form');
  await admin.click(`[data-act="remove"][data-id="${awaM.$id}"]`); await admin.waitForSelector('#toast:not([hidden])');
  check('Utilisateurs : accès retiré', !db.memberships.includes(awaM));
  await awa.reload(); await awa.waitForSelector('#view h1');
  check('Accès retiré : plus aucun accès à l’organisation', (await awa.textContent('#view')).includes('aucune organisation'));

  // Site sans projet configuré
  const plain = await browser.newPage();
  await plain.route(/archiva360\/connexion\/$/, async route => {
    const r = await route.fetch();
    route.fulfill({ response: r, body: (await r.text()).replace(/"endpoint": "[^"]*", "project": "[^"]*"/, '"endpoint": "", "project": ""') });
  });
  await plain.goto(L); await plain.waitForSelector('#auth-card .notice');
  check('Sans configuration : message « en cours d’activation »', (await plain.textContent('#auth-card')).includes('activation'));
  check('Aucune erreur JavaScript', !errs.length, errs.slice(0, 2).join(' | '));

  await browser.close(); srv.close();
  const failed = results.filter(r => !r.ok).length;
  console.log(`\n${results.length - failed}/${results.length} tests réussis`);
  process.exit(failed ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
