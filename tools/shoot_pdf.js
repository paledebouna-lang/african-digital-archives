// Renders the white paper print layouts to PDF. Usage: node tools/shoot_pdf.js <jobs.json> <output-dir>
const fs = require('fs');
const path = require('path');
let playwright;
try { playwright = require('playwright'); } catch (e) { playwright = require('/opt/node22/lib/node_modules/playwright'); }
(async () => {
  const [jobsFile, outDir] = process.argv.slice(2);
  fs.mkdirSync(outDir, { recursive: true });
  const jobs = JSON.parse(fs.readFileSync(jobsFile, 'utf8'));
  const browser = await playwright.chromium.launch();
  for (const j of jobs) {
    const page = await browser.newPage();
    await page.goto('file://' + j.html);
    await page.evaluate(() => document.fonts.ready);
    await page.pdf({ path: path.join(outDir, j.pdf), format: 'A4', printBackground: true, displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: `<div style="width:100%;font:8px Arial,sans-serif;color:#8E98BD;padding:0 20mm;display:flex;justify-content:space-between"><span>ADA — ${j.title}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`,
      margin: { top: '22mm', bottom: '22mm', left: '20mm', right: '20mm' } });
    await page.close();
    process.stdout.write('.');
  }
  await browser.close();
  console.log(`\n${jobs.length} PDF`);
})();
