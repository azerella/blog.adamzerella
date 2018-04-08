from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('archive/', views.archive, name='archive'),
    # path('robots.txt/', views.robots, name='robots')
]
