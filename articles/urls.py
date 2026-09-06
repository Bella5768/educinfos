from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/', views.articles_list, name='articles_list'),
    path('gestion/', views.dashboard, name='dashboard'),
    path('gestion/ajouter/', views.article_create, name='article_create'),
    path('gestion/modifier/<slug:slug>/', views.article_edit, name='article_edit'),
    path('gestion/supprimer/<slug:slug>/', views.article_delete, name='article_delete'),
]
