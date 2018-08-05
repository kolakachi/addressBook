from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.welcomeView, name='welcome'),
    path('list', views.listView, name='list'),
    path('add', views.addView, name='add'),
    path('addanewcontact', views.addANewContact, name='addcontact'),
]
