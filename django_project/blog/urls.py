from django.urls import path
from . import views
urlpatterns = [

    # This patternmatches the empty route
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]
