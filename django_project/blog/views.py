from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Home page route, returns a rendered template
def home(request):

    # Uses the posts from the post database
    context = {'posts' : Post.objects.all()}
    return render(request, 'blog/home.html', context)

# About page route, returns a rendered template
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
