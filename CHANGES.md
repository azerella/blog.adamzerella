## 0.0.3
*   Tested viability of Bootstrap4, concluded no need.
*   `base.html` CSS layout correction
*   Added `<code>...</code>` blocks with css styling
*   Added `Subscriber` model to `models.py`
*   `Archive.html` entries colour is reflective of the rating (darker == less)
*   Implemented two column layouts for `blog.html` and `archive.html`
*   Added Google Analytics & Google AdSense snippets to `base.html`
*   Various CSS tweaks, mostly `<a>` and layout related
*   Modified footer content to `blog.adamzerella.com`, placeholder for now
*   Modified `.travis.yml`
---
## 0.0.2
*   Restructured static asset directories.
*   Created `base.html` template for all pages.
*   Added new pages/views/urls for `About.html`, `Archive.html`, `Blog.html` accordingly.
*   Created `base.css` theme.
*   Added `archive.html` and `archive.css`
*   Added `createsuperuser` note to README.md
*   Added `loaddata` note to README.md
*   Added `export BAZ_STATIC_ROOT="/var/www/example.com/static/"` note to README.md
*   Redefined `models.Blog` schema
*   Created `fixtures` folder with `blog.json` mock data
*   Added `.travis.yml` database config
*   Implemented `/sitemap.xml`
*   Added `django.contrib.sitemaps` app for sitemap functionality
*   Updated mock database fixture data, minor corrections and new entry
*   Added `face256.png` asset
*   Modified `base.css` to use face image, hid `#ad` div (for now)
*   Reverted `blogadamzerella/settings.py` BAZ_SQL_PASS back to `root`
*   Modified `views.py` contexts to now use `get_object_or_404`
*   Removed `index.html` temporarily from project
*   Added rating score increase on page view
*   Modified archive page order based on blog rating score
*   Added `</hr>` and most popular blog to `blog.html` under top 5
*   Modified face redirect now goes to `blog.html` page (default)
*   Added `Max` package to `views.py`
*   `Sidebar #ad` is now transparent

---
## 0.0.1
*   Created `index.html` page with relevant meta info.
*   Created `Blog` and `Author` models, applied migrations accordingly.
*   Initialised Django project with `django-admin startproject` and `django-admin startproject`.
