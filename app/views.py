from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.db.models import Max

from .models import Blog

def about(request):
    context = {}
    return render(request, 'app/about.html', context)

def blog(request):
    context = {
        "blogs": Blog.objects.all(),
        "highest_rated": Blog.objects.all().order_by('-rating').first()
    }
    return render(request, 'app/blog.html', context)

def blog_entry(request, slug):
    entry = get_object_or_404(Blog, slug=slug)
    context = {
        "entry": get_object_or_404(Blog, slug=slug),
    }

    #   Increment rating on page view
    entry.rating +=1
    #   Write updated rating to DB
    entry.save()

    return render(request, 'app/blog_entry.html', context)

def archive(request):
    context = {
        #   Return ALL blog entries ordered by rating descending
        "blogs": Blog.objects.all().order_by('-rating')
    }
    return render(request, 'app/archive.html', context)
