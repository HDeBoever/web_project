from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Henri',
        'title' : 'blog post 1',
        'content' : 'First post contents',
        'date_posted' : '2020/9/11'
    },
    {
        'author' : 'Amanda',
        'title' : 'blog post 2',
        'content' : 'Second post contents',
        'date_posted' : '2020/9/10'
    }
]

# Home page route, returns a rendered template
def home(request):

    context = {'posts' : posts}
    return render(request, 'blog/home.html', context)

# About page route, returns a rendered template
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
