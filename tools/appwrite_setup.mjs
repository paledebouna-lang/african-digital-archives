#!/usr/bin/env node
// Installation des comptes en ligne ARCHIVA360 sur Appwrite (à lancer une seule fois).
//
// Crée l'équipe « ARCHIVA360 » (qui porte les rôles) et le compte administrateur.
// Sans dépendance : Node 18 ou plus suffit.
//
//   APPWRITE_ENDPOINT=https://fra.cloud.appwrite.io/v1 \
//   APPWRITE_PROJECT=<ID du projet> \
//   APPWRITE_API_KEY=<clé API : portées users.read, users.write, teams.read, teams.write> \
//   ADMIN_EMAIL=assa@eletude.org ADMIN_NAME="Assa" \
//   node tools/appwrite_setup.mjs
//
// Le script peut être relancé sans risque : ce qui existe déjà est conservé.
import { randomBytes } from 'node:crypto';

const env = process.env;
const ENDPOINT = (env.APPWRITE_ENDPOINT || '').replace(/\/$/, '');
const PROJECT = env.APPWRITE_PROJECT;
const KEY = env.APPWRITE_API_KEY;
const TEAM = env.APPWRITE_TEAM || 'archiva360';
const EMAIL = (env.ADMIN_EMAIL || 'assa@eletude.org').toLowerCase();
const NAME = env.ADMIN_NAME || 'Administrateur ADA';

if (!ENDPOINT || !PROJECT || !KEY) {
  console.error('Renseignez APPWRITE_ENDPOINT, APPWRITE_PROJECT et APPWRITE_API_KEY (voir l’en-tête du script).');
  process.exit(1);
}

async function api(method, path, body) {
  const res = await fetch(ENDPOINT + path, {
    method,
    headers: { 'Content-Type': 'application/json', 'X-Appwrite-Project': PROJECT, 'X-Appwrite-Key': KEY, 'X-Appwrite-Response-Format': '1.6.0' },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = res.status === 204 ? {} : await res.json().catch(() => ({}));
  if (!res.ok) { const e = new Error(`${method} ${path} → ${res.status} ${data.message || ''}`); e.status = res.status; throw e; }
  return data;
}

// Mot de passe provisoire : 20 caractères, lettres et chiffres garantis.
const tempPassword = () => 'Ada' + randomBytes(12).toString('base64url').replace(/[-_]/g, 'x') + '7';

const step = (s) => console.log('• ' + s);

try {
  await api('GET', '/health/version').catch(() => null);

  try {
    await api('POST', '/teams', { teamId: TEAM, name: 'ARCHIVA360' });
    step(`Équipe « ${TEAM} » créée.`);
  } catch (e) {
    if (e.status !== 409) throw e;
    step(`Équipe « ${TEAM} » déjà présente.`);
  }

  const found = await api('GET', '/users?search=' + encodeURIComponent(EMAIL));
  let user = (found.users || []).find((u) => u.email.toLowerCase() === EMAIL);
  let password = null;
  if (user) {
    step(`Compte ${EMAIL} déjà présent (mot de passe inchangé).`);
  } else {
    password = tempPassword();
    user = await api('POST', '/users', { userId: 'unique()', email: EMAIL, password, name: NAME });
    await api('PATCH', `/users/${user.$id}/verification`, { emailVerification: true }).catch(() => null);
    step(`Compte ${EMAIL} créé.`);
  }

  const members = await api('GET', `/teams/${TEAM}/memberships`);
  const mine = (members.memberships || []).find((m) => m.userId === user.$id);
  if (mine) {
    await api('PATCH', `/teams/${TEAM}/memberships/${mine.$id}`, { roles: ['owner', 'admin'] });
    step('Rôle Administrateur confirmé.');
  } else {
    // Avec une clé API, l'adhésion est confirmée immédiatement (aucun e-mail envoyé).
    await api('POST', `/teams/${TEAM}/memberships`, { userId: user.$id, roles: ['owner', 'admin'], url: 'https://localhost/' });
    step('Rôle Administrateur attribué.');
  }

  console.log('\nInstallation terminée.');
  if (password) {
    console.log(`\n  Identifiant : ${EMAIL}\n  Mot de passe provisoire : ${password}\n`);
    console.log('  Notez-le maintenant : il ne sera plus affiché. Changez-le dès la première connexion (« Mon compte »).');
  }
  console.log(`\nDernière étape : dans tools/ada/core.py, renseignez
  "appwrite": {"endpoint": "${ENDPOINT}", "project": "${PROJECT}", "team": "${TEAM}"}
puis régénérez le site (python3 tools/build.py) et publiez-le.`);
} catch (e) {
  console.error('\nÉchec : ' + e.message);
  if (e.status === 401) console.error('Vérifiez la clé API et ses portées (users.read, users.write, teams.read, teams.write).');
  process.exit(1);
}
