from django.contrib import admin
from django.urls import path, include
from article import views

urlpatterns = [
    path('list', views.list, name='article_list'),
    path('add', views.add, name='article_add'),
    path('vote/<int:id>/', views.vote, name='article_vote'),
]
