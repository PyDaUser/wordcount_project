
from django.urls import path
from . import views# . mean from this folder

urlpatterns = [
    path("", views.home, name = 'home'),
    path("count/", views.count, name = 'count'),
    path("about/", views.about, name = 'about')
]
