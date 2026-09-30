// Renders the HTML mockups listed in a jobs file to PNG with Playwright.
// Usage: node tools/shoot.js <jobs.json> <output-dir>
const fs = require('fs');
const path = require('path');
let playwright;
try { playwright = require('playwright'); } catch (e) { playwright = require('/opt/node22/lib/node_modules/playwright'); }

(async () => {
  const [jobsFile, outDir] = process.argv.slice(2);
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const browser = await playwright.chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.w, height: j.h }, deviceScaleFactor: j.dpr || 1.25 });
    await page.goto('file://' + j.html);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(outDir, j.png), omitBackground: !!j.transparent });
    await page.close();
    process.stdout.write('.');
  }
  await browser.close();
  console.log(`\n${jobs.length} images`);
})();
