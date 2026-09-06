from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/', views.articles_list, name='articles_list'),
    path('backoffice/', views.backoffice, name='backoffice'),
    path('backoffice/ajouter/', views.backoffice_add, name='backoffice_add'),
    path('backoffice/modifier/<slug:slug>/', views.backoffice_edit, name='backoffice_edit'),
    path('backoffice/supprimer/<slug:slug>/', views.backoffice_delete, name='backoffice_delete'),
]
