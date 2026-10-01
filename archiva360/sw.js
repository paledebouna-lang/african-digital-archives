// ARCHIVA360 — service worker (généré par tools/build.py, ne pas modifier à la main).
// Pages : réseau d'abord, copie locale si hors connexion. Fichiers du thème : copie locale, mise à jour en arrière-plan.
// Les appels à Appwrite (autre domaine) ne passent jamais par le cache.
const CACHE = 'archiva360-v1.6.0';
const PRECACHE = [
  "./connexion/",
  "./espace/",
  "./demo-interactive/",
  "./manifest.webmanifest",
  "../wp-content/themes/ada-archives/assets/css/archiva360-demo.css?ver=1.6.0",
  "../wp-content/themes/ada-archives/assets/js/archiva360-auth.js?ver=1.6.0",
  "../wp-content/themes/ada-archives/assets/js/archiva360-pwa.js?ver=1.6.0",
  "../wp-content/themes/ada-archives/assets/js/archiva360-demo.js?ver=1.6.0",
  "../wp-content/themes/ada-archives/assets/fonts/inter-latin.woff2",
  "../wp-content/uploads/2026/09/archiva360-app-192.png",
  "../wp-content/uploads/2026/09/archiva360-app-180.png",
  "../wp-content/uploads/2026/09/cropped-ada-icon-32x32.png"
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(keys => Promise.all(keys.filter(k => k.startsWith('archiva360-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    }).catch(() => caches.match(req, { ignoreSearch: true })
      .then(hit => hit || caches.match('./connexion/'))));
    return;
  }
  e.respondWith(caches.match(req).then(hit => {
    const net = fetch(req).then(res => {
      if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
      return res;
    });
    if (hit) { net.catch(() => {}); return hit; }
    return net;
  }));
});
