from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .sitemap import BlogSitemap, BaseSitemap
from . import views

sitemaps = {
    'base': BaseSitemap(),
    'blog': BlogSitemap()
}

urlpatterns = [
    path('', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_entry, name='blog_entry'),
    path('archive/', views.archive, name='archive'),
    path('register_subscriber/', views.register_subscriber,
         name='register_subscriber'),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
