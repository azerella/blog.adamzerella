from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ValidationError

from .models import Blog, Subscriber
from .forms import SignupForm

"""
"""
def about(request):
    context = {}
    return render(request, 'app/about.html', context)


"""
"""
def blog(request):
    context = {
        "blogs": Blog.objects.all(),
        "highest_rated": Blog.objects.all().order_by('-rating').first()
    }

    return render(request, 'app/blog.html', context)


"""
"""
def blog_entry(request, slug):
    entry = get_object_or_404(Blog, slug=slug)
    context = {
        "entry": get_object_or_404(Blog, slug=slug)
    }

    #   Increment rating on page view
    entry.rating +=1
    #   Write updated rating to DB
    entry.save()

    return render(request, 'app/blog_entry.html', context)


"""
"""
def archive(request):
    context = {
        #   Return ALL blog entries ordered by rating descending
        "blogs": Blog.objects.all().order_by('-rating')
    }
    return render(request, 'app/archive.html', context)


"""
"""
def register_subscriber(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print('[SUCCESS] : New sub: %s' % form.data['username'])
            return HttpResponse('')
        else:
            print('[FAIL] : Invalid sub: %s' % form.data['username'])
            return HttpResponseBadRequest('')
    return render(request, 'app/blog.html', {})
