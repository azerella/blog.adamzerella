from django.shortcuts import render
from django.template import Context

from .models import Blog

def index(request):
    context = {
        "blogs": Blog.objects.all()[:5], 
        "page_title": Blog.objects.get(pk=1).title    
    }
    return render(request, 'app/index.html', context)
