from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index ,name='index'),
    path('aboutpage',views.aboutPage ,name='aboutPage'),
    path('fromPage',views.fromPage ,name='fromPage'),
]