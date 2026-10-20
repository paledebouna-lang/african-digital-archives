// Convertit en WebP les captures et couvertures (PNG) du dossier uploads. Usage : node tools/webp.js <dossier>
const fs = require('fs'), path = require('path');
let playwright; try { playwright = require('playwright'); } catch (e) { playwright = require('/opt/node22/lib/node_modules/playwright'); }
const KEEP = /^(ada-logo|archiva360-app|cropped-ada-icon|og-ada)/;   // logos, icônes et image de partage restent en PNG
(async () => {
  const dir = process.argv[2];
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.png') && !KEEP.test(f));
  const browser = await playwright.chromium.launch();
  const page = await browser.newPage();
  let before = 0, after = 0;
  for (const f of files) {
    const src = path.join(dir, f);
    const data = 'data:image/png;base64,' + fs.readFileSync(src).toString('base64');
    const url = await page.evaluate(async d => {
      const img = new Image(); img.src = d; await img.decode();
      const c = document.createElement('canvas'); c.width = img.width; c.height = img.height;
      c.getContext('2d').drawImage(img, 0, 0); return c.toDataURL('image/webp', 0.82);
    }, data);
    const out = Buffer.from(url.split(',')[1], 'base64');
    before += fs.statSync(src).size; after += out.length;
    fs.writeFileSync(src.replace(/\.png$/, '.webp'), out);
    fs.unlinkSync(src);
  }
  await browser.close();
  console.log(`${files.length} images : ${Math.round(before / 1024)} Ko → ${Math.round(after / 1024)} Ko`);
})();
