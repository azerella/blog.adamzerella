from django.contrib.sitemaps import Sitemap
from .models import Blog

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Blog.objects.filter(status=1)

    def lastmod(self, obj):
        return obj.modified_date

    def location(self, item):
        return "/blog/" + item.slug + "/"

class BaseSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return [
            "",         #Root ('index.html')
            "/about",   
            "/blog",
            "/archive"
        ]

    def location(self, item):
        return item + "/"
