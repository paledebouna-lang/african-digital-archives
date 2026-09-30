#!/usr/bin/env python3
"""Build the ADA website.

    python3 tools/build.py            # regenerate every page
    python3 tools/build.py --images   # also re-render the ARCHIVA360 screenshots and covers (needs Node + Playwright)

Site settings (contact e-mail, public URL…) live in tools/ada/core.py → SITE.
"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from ada import core, pages_main, pages_solutions, pages_archiva, pages_sectors, pages_services, pages_resources  # noqa: E402


def images():
    from ada import mockups, covers
    tmp = tempfile.mkdtemp()
    jobs = mockups.build(tmp) + covers.build(tmp)
    jf = os.path.join(tmp, "jobs.json")
    with open(jf, "w") as f:
        json.dump(jobs, f)
    subprocess.run(["node", os.path.join(HERE, "shoot.js"), jf, os.path.join(ROOT, core.SITE["uploads"])], check=True)


def main():
    if "--images" in sys.argv:
        images()
    pages_resources.build()          # blog posts first: other pages link to them
    pages_main.build_home()
    pages_solutions.build()
    pages_archiva.build()
    pages_sectors.build()
    pages_services.build()
    pages_main.build_company()
    pages_main.build_contact()
    pages_main.build_legal()
    pages_main.build_utility()
    pages_main.build_sitemap()
    n = core.write_all(ROOT)
    print(f"{n} pages générées")


if __name__ == "__main__":
    main()
