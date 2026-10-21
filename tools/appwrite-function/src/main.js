// ARCHIVA360 — fonction Appwrite « archiva360-mail »
// Envoie les e-mails d'invitation et de réinitialisation de mot de passe depuis contact@adarchives.pro (via Brevo),
// à la place des e-mails génériques d'Appwrite. Aucune dépendance : fetch natif de Node 18+.
//
// Variables d'environnement de la fonction (Appwrite → Functions → Settings → Environment variables) :
//   APPWRITE_API_KEY  clé API du projet (portées users.read, users.write, teams.read, teams.write)
//   BREVO_API_KEY     clé API Brevo (SMTP & API → API keys)
//   SENDER_EMAIL      contact@adarchives.pro (expéditeur validé dans Brevo)
//   SENDER_NAME       ARCHIVA360 — African Digital Archives
//   SITE_URL          https://adarchives.pro
//   TEAM_ID           archiva360
// Fournies par Appwrite : APPWRITE_FUNCTION_API_ENDPOINT, APPWRITE_FUNCTION_PROJECT_ID.

const ROLES = { admin: ['owner', 'admin'], archiviste: ['archiviste'], records: ['records'], employe: ['employe'], auditeur: ['auditeur'] };
const ROLE_LABELS = { admin: 'Administrateur', archiviste: 'Archiviste', records: 'Records manager', employe: 'Employé', auditeur: 'Auditeur' };
const TOKEN_TTL = 7 * 24 * 3600;      // validité du lien d'invitation : 7 jours
const RECOVERY_TTL = 3600;            // validité du lien de réinitialisation : 1 heure

const env = (k, d) => (process.env[k] || d || '').trim();
const esc = s => String(s == null ? '' : s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const validEmail = e => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);

function appwrite() {
  const endpoint = env('APPWRITE_FUNCTION_API_ENDPOINT', 'https://fra.cloud.appwrite.io/v1').replace(/\/$/, '');
  const headers = { 'Content-Type': 'application/json', 'X-Appwrite-Project': env('APPWRITE_FUNCTION_PROJECT_ID'), 'X-Appwrite-Key': env('APPWRITE_API_KEY'), 'X-Appwrite-Response-Format': '1.6.0' };
  return async (method, path, body) => {
    const res = await fetch(endpoint + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
    const data = res.status === 204 ? {} : await res.json().catch(() => ({}));
    if (!res.ok) { const e = new Error(data.message || ('Appwrite ' + res.status)); e.status = res.status; e.type = data.type; throw e; }
    return data;
  };
}

async function sendMail(to, toName, subject, html, text) {
  const res = await fetch('https://api.brevo.com/v3/smtp/email', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'api-key': env('BREVO_API_KEY') },
    body: JSON.stringify({
      sender: { email: env('SENDER_EMAIL'), name: env('SENDER_NAME', 'ARCHIVA360') },
      replyTo: { email: env('SENDER_EMAIL') },
      to: [{ email: to, name: toName || undefined }],
      subject, htmlContent: html, textContent: text,
    }),
  });
  if (!res.ok) throw new Error('Brevo ' + res.status + ' ' + (await res.text()).slice(0, 200));
}

function layout(title, lines, button, footer) {
  const site = env('SITE_URL', 'https://adarchives.pro');
  const html = `<!doctype html><html lang="fr"><body style="margin:0;background:#F4F6FA;font-family:Inter,Arial,sans-serif;color:#1B2233">
<table width="100%" cellpadding="0" cellspacing="0" style="background:#F4F6FA;padding:32px 12px"><tr><td align="center">
<table width="100%" cellpadding="0" cellspacing="0" style="max-width:560px;background:#fff;border-radius:12px;overflow:hidden">
<tr><td style="background:#0A1541;padding:22px 28px;color:#fff;font-weight:800;font-size:18px">ARCHIVA360 <span style="font-weight:500;color:#AEB8DA;font-size:13px">· African Digital Archives</span></td></tr>
<tr><td style="padding:28px">
<h1 style="font-size:20px;margin:0 0 14px;color:#0A1541">${esc(title)}</h1>
${lines.map(l => `<p style="font-size:15px;line-height:1.55;margin:0 0 12px">${l}</p>`).join('')}
${button ? `<p style="margin:22px 0"><a href="${esc(button.url)}" style="display:inline-block;background:#006EEF;color:#fff;text-decoration:none;font-weight:600;padding:12px 20px;border-radius:7px">${esc(button.label)}</a></p>
<p style="font-size:12.5px;color:#6C728D;line-height:1.5;margin:0 0 12px">Si le bouton ne fonctionne pas, copiez ce lien dans votre navigateur :<br><a href="${esc(button.url)}" style="color:#006EEF;word-break:break-all">${esc(button.url)}</a></p>` : ''}
<p style="font-size:13px;color:#6C728D;line-height:1.5;margin:18px 0 0">${footer}</p>
</td></tr>
<tr><td style="padding:16px 28px;background:#F4F6FA;font-size:12px;color:#6C728D">African Digital Archives · Abidjan, Côte d'Ivoire · <a href="${esc(site)}" style="color:#6C728D">${esc(site.replace(/^https?:\/\//, ''))}</a></td></tr>
</table></td></tr></table></body></html>`;
  const text = [title, '', ...lines.map(l => l.replace(/<[^>]+>/g, '')), button ? '\n' + button.label + ' : ' + button.url : '', '', footer.replace(/<[^>]+>/g, '')].join('\n');
  return { html, text };
}

// Qui appelle ? Appwrite transmet l'identifiant de l'utilisateur connecté qui exécute la fonction.
async function callerIsOwner(api, team, userId) {
  if (!userId) return false;
  const r = await api('GET', `/teams/${team}/memberships?queries[]=${encodeURIComponent(JSON.stringify({ method: 'equal', attribute: 'userId', values: [userId] }))}`);
  const m = (r.memberships || []).find(x => x.userId === userId);
  return !!(m && m.confirm && m.roles.includes('owner'));
}

async function findUser(api, email) {
  const r = await api('GET', '/users?search=' + encodeURIComponent(email));
  return (r.users || []).find(u => u.email.toLowerCase() === email) || null;
}

async function invite(api, body, callerId) {
  const team = env('TEAM_ID', 'archiva360');
  const site = env('SITE_URL', 'https://adarchives.pro').replace(/\/$/, '');
  if (!(await callerIsOwner(api, team, callerId))) return [401, { message: 'Seul un administrateur peut inviter des utilisateurs.' }];
  const email = String(body.email || '').trim().toLowerCase(), name = String(body.name || '').trim().slice(0, 128), role = String(body.role || 'employe');
  if (!validEmail(email) || !name || !ROLES[role]) return [400, { message: 'Nom, adresse e-mail ou rôle invalide.' }];

  let user = await findUser(api, email);
  if (!user) user = await api('POST', '/users', { userId: 'unique()', email, name });
  const members = await api('GET', `/teams/${team}/memberships?queries[]=${encodeURIComponent(JSON.stringify({ method: 'limit', values: [100] }))}`);
  let membership = (members.memberships || []).find(m => m.userId === user.$id);
  if (membership && membership.confirm && !(await isPending(api, team, user.$id))) return [409, { message: 'Cette personne fait déjà partie de l’organisation.' }];
  if (!membership) membership = await api('POST', `/teams/${team}/memberships`, { userId: user.$id, roles: ROLES[role], url: site + '/' });
  else await api('PATCH', `/teams/${team}/memberships/${membership.$id}`, { roles: ROLES[role] });
  await setPending(api, team, user.$id, true);

  const token = await api('POST', `/users/${user.$id}/tokens`, { length: 32, expire: TOKEN_TTL });
  const url = `${site}/archiva360/connexion/?invite=1&tk=1&userId=${encodeURIComponent(user.$id)}&secret=${encodeURIComponent(token.secret)}`;
  const caller = await api('GET', '/users/' + callerId).catch(() => ({}));
  const mail = layout('Vous êtes invité sur ARCHIVA360',
    [`Bonjour ${esc(name)},`,
     `${esc(caller.name || 'Votre administrateur')} vous invite à rejoindre l’espace <b>${esc(env('ORG_NAME', 'African Digital Archives'))}</b> sur ARCHIVA360, la plateforme d’archivage et de gestion documentaire d’African Digital Archives, avec le rôle <b>${esc(ROLE_LABELS[role])}</b>.`,
     'Pour activer votre compte et choisir votre mot de passe, cliquez sur le bouton ci-dessous.'],
    { label: 'Activer mon compte', url },
    'Ce lien est personnel et valable 7 jours. Si vous n’attendiez pas cette invitation, ignorez simplement ce message.');
  await sendMail(email, name, 'Invitation à rejoindre ARCHIVA360', mail.html, mail.text);
  return [200, { ok: true, membershipId: membership.$id }];
}

async function recover(api, body) {
  const site = env('SITE_URL', 'https://adarchives.pro').replace(/\/$/, '');
  const email = String(body.email || '').trim().toLowerCase();
  if (!validEmail(email)) return [400, { message: 'Adresse e-mail invalide.' }];
  const user = await findUser(api, email);
  // Même réponse que le compte existe ou non : on ne révèle pas les adresses inscrites.
  if (!user || user.status === false) return [200, { ok: true }];
  const token = await api('POST', `/users/${user.$id}/tokens`, { length: 32, expire: RECOVERY_TTL });
  const url = `${site}/archiva360/connexion/?reset=1&tk=1&userId=${encodeURIComponent(user.$id)}&secret=${encodeURIComponent(token.secret)}`;
  const mail = layout('Réinitialisation de votre mot de passe',
    [`Bonjour ${esc(user.name || '')},`.replace(' ,', ','),
     'Vous avez demandé à réinitialiser le mot de passe de votre compte ARCHIVA360. Pour en choisir un nouveau, cliquez sur le bouton ci-dessous.'],
    { label: 'Choisir un nouveau mot de passe', url },
    'Ce lien expire dans une heure. Si vous n’êtes pas à l’origine de cette demande, ignorez ce message : votre mot de passe actuel reste valable.');
  await sendMail(email, user.name, 'Réinitialisation de votre mot de passe ARCHIVA360', mail.html, mail.text);
  return [200, { ok: true }];
}

// Invitations en attente : mémorisées dans les préférences de l'équipe (lisibles par tous ses membres).
async function getPending(api, team) { const p = await api('GET', `/teams/${team}/prefs`); return (p && p.pending) || {}; }
async function isPending(api, team, userId) { return !!(await getPending(api, team))[userId]; }
async function setPending(api, team, userId, on) {
  const pending = await getPending(api, team);
  if (on) pending[userId] = new Date().toISOString(); else delete pending[userId];
  await api('PUT', `/teams/${team}/prefs`, { prefs: { pending } });
}

// L'utilisateur vient de choisir son mot de passe : son invitation n'est plus en attente.
async function activated(api, callerId) {
  if (!callerId) return [401, { message: 'Non connecté.' }];
  await setPending(api, env('TEAM_ID', 'archiva360'), callerId, false);
  return [200, { ok: true }];
}

// Nouveau mot de passe après un lien de réinitialisation (la session a été ouverte par le jeton du lien).
async function setPassword(api, body, callerId) {
  if (!callerId) return [401, { message: 'Non connecté.' }];
  const pw = String(body.password || '');
  if (pw.length < 10 || !/[a-zA-Z]/.test(pw) || !/[0-9]/.test(pw)) return [400, { message: 'Le mot de passe doit contenir au moins 10 caractères, avec des lettres et des chiffres.' }];
  await api('PATCH', `/users/${callerId}/password`, { password: pw });
  await setPending(api, env('TEAM_ID', 'archiva360'), callerId, false);
  return [200, { ok: true }];
}

// Message compréhensible pour l'administrateur, selon l'étape qui a échoué.
function explain(e) {
  const m = String(e.message || '');
  if (m.startsWith('Brevo 401')) return 'Brevo refuse la clé API : vérifiez la variable BREVO_API_KEY de la fonction.';
  if (m.startsWith('Brevo 400') && /sender/i.test(m)) return 'Brevo refuse l’expéditeur : confirmez contact@adarchives.pro dans Brevo (Expéditeurs) et vérifiez SENDER_EMAIL.';
  if (m.startsWith('Brevo 4')) return 'Brevo a refusé l’envoi : ' + m.replace(/^Brevo \d+ /, '').slice(0, 160);
  if (m.startsWith('Brevo')) return 'Brevo est momentanément indisponible. Réessayez dans quelques instants.';
  if (e.status === 401) return 'Appwrite refuse la clé API de la fonction : vérifiez APPWRITE_API_KEY et ses portées (users.read, users.write, teams.read, teams.write).';
  if (e.status === 404 && /team/i.test(m)) return 'Équipe introuvable : vérifiez la variable TEAM_ID (archiva360).';
  if (e.status) return 'Appwrite a répondu « ' + m.slice(0, 160) + ' ».';
  if (!env('BREVO_API_KEY') || !env('APPWRITE_API_KEY') || !env('SENDER_EMAIL')) return 'Variables manquantes dans la fonction : BREVO_API_KEY, APPWRITE_API_KEY ou SENDER_EMAIL.';
  return 'L’envoi a échoué : ' + m.slice(0, 160);
}

export default async ({ req, res, log, error }) => {
  const api = appwrite();
  let body = {};
  try { body = typeof req.bodyJson === 'object' && req.bodyJson ? req.bodyJson : JSON.parse(req.bodyText || req.body || '{}'); } catch (e) { body = {}; }
  const callerId = req.headers['x-appwrite-user-id'] || '';
  try {
    let out;
    if (body.action === 'invite') out = await invite(api, body, callerId);
    else if (body.action === 'recover') out = await recover(api, body);
    else if (body.action === 'activated') out = await activated(api, callerId);
    else if (body.action === 'setPassword') out = await setPassword(api, body, callerId);
    else out = [400, { message: 'Action inconnue.' }];
    return res.json(out[1], out[0]);
  } catch (e) {
    error(String(e.stack || e));
    return res.json({ message: explain(e), detail: String(e.message || e).slice(0, 300) }, 500);
  }
};
