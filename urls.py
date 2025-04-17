from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription_sous_admin, name='inscription'),
    path('creer_groupe/', views.creer_groupe, name='creer_groupe'),
    path('<int:groupe_id>/activites/', views.liste_activites, name='liste_activites'),
]