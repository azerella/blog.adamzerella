from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from .models import Blog, Subscriber

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

    #   Increment rating on page view
    entry.rating +=1
    #   Write updated rating to DB
    entry.save()

    return render(request, 'app/blog_entry.html', { 'entry':entry })

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
        form = SignupForm(request.POST or None)

        if form.is_valid():
            username = form.clean_username()
            if Subscriber.objects.filter(username=username).exists():
                raise ValidationError(('Username: ' + username + ' already exists!'), code='invalid')
                #TODO Add visual feedback on INVALID input
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

            print("New user subscribed: %s!", username)
            Subscriber.objects.create(username=username)
            #TODO Add visual feedback on VALID input
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("GET request")
