from django.shortcuts import render
from django.template import Context

from .models import Blog

def index(request):
    context = {}
    return render(request, 'app/index.html', context)

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def blog(request):
    context = {
        "blogs": Blog.objects.all()[:5],
        "popular_blog_title": Blog.objects.get(pk=1).title
    }
    return render(request, 'app/blog.html', context)

def blog_entry(request):
    context = {}
    return render(request, 'app/blog_entry.html', context)

def archive(request):
    context = {
        "blogList": Blog.objects.all()
    }
    return render(request, 'app/archive.html', context)
