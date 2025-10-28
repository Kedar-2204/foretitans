from django.contrib import admin
from django.urls import path
from admin_dashboard import views

urlpatterns = [

    path("dashboard", views.dashboard, name= "dashboard"),
    path("add_advertise", views.add_advertise, name= "add_advertise"),
    path("organisors", views.organisors, name= "organisors"),
    path("add_mentors", views.add_mentors, name= "add_mentors"),
    path("add_sponsors", views.add_sponsors, name= "add_sponsors"),
    path("add_tournaments", views.add_tournaments, name= "add_tournaments"),
    path("add_team/", views.add_team, name="add_team"),
    path("add_player/", views.add_player, name="add_player"),
    path("contacts", views.contacts, name= "contacts"),
    path("cricket_news", views.cricket_news, name= "cricket_news"),
    path("announcements", views.announcements, name= "announcements"),
    path("results", views.results, name= "results"),
    path('upload_slider', views.upload_slider, name='upload_slider'),
    path('upload_team', views.upload_team, name='upload_team'),
    path("gallery_upload", views.gallery_upload, name="gallery_upload"),



]



