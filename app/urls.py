from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("about", views.about, name= "about"),
    path("contact", views.contact, name= "contact"),
    path("gallary", views.gallary, name= "gallary"),
    path("news", views.news, name= "news"),
    path("our_work", views.our_work, name= "our_work"),
    path("blog", views.blog, name= "blog"),
    path("current_tournaments", views.current_tournaments, name= "current_tournaments"),
    path("upcoming_tournaments", views.upcoming_tournaments, name= "upcoming_tournaments"),
    path("past_tournaments", views.past_tournaments, name= "past_tournaments"),
    path("tournaments", views.tournaments, name= "tournaments"),
    # path("organisers", views.organisers, name= "organisers"),
    # path("advisory_board", views.advisory_board, name= "advisory_board"),
    # path("team", views.team, name= "team"),
    # path("mentor", views.mentor, name= "mentor"),
    # path("sponsorship", views.sponsorship, name= "sponsorship"),
    # path("crickets_news", views.crickets_news, name= "crickets_news"),
    # path('announcement', views.announcement_view, name='announcement'),
    # path('matches', views.matches, name='matches'),



]