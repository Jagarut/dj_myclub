from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.all_events, name='show-events'),
    path('add_venue/', views.add_venue, name='add-venue'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
]