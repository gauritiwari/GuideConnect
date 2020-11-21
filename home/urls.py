from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('guide',views.guide,name='guide'),
    path('tourist',views.tourist,name='tourist'),
    path('login',views.login,name='login'),
]
