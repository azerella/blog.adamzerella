import logging

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404

from .forms import SignupForm
from .models import Blog


"""
Render the view for the about page
"""
def about(request):
    context = {}
    return render(request, 'app/about.html', context)


"""
Render the view for a blog page, the index page
"""
def blog(request):
    context = {
        "blogs": Blog.objects.all(),
        "highest_rated": Blog.objects.all().order_by('-rating').first()
    }
    return render(request, 'app/blog.html', context)


"""
Render the view for a blog entry page
"""
def blog_entry(request, slug):
    entry = get_object_or_404(Blog, slug=slug)
    context = {
        "entry": get_object_or_404(Blog, slug=slug)
    }

    #   Increment rating on page view
    entry.rating += 1
    #   Write updated rating to DB
    entry.save()

    return render(request, 'app/blog_entry.html', context)


"""
Render the view for the archive page
"""
def archive(request):
    context = {
        #   Return ALL blog entries ordered by rating descending
        "blogs": Blog.objects.all().order_by('-rating')
    }
    return render(request, 'app/archive.html', context)


"""
Handle requests on the SignupForm
"""
def register_subscriber(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            logging.info('[SUCCESS] : New sub: %s', form.data['username'])
            return HttpResponse('')
        logging.error('[FAIL] : Invalid sub: %s', form.data['username'])
        return HttpResponseBadRequest('')
    return HttpResponseBadRequest('')
        