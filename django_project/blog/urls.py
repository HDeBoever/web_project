from django.urls import path
from . import views
urlpatterns = [

    # This pattern matches the empty route
    path('', views.home, name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
]
