from django.urls import path
from . import views

urlpatterns = [
    # URLs pour Filiere
    path('filiere/', views.filiere_list, name='filiere_list'),
    path('filiere/create/', views.filiere_create, name='filiere_create'),
    path('filiere/<str:id>/', views.filiere_detail, name='filiere_detail'),
    path('filiere/<str:id>/update/', views.update_filiere, name='filiere_update'),
    path('filiere/<str:id>/delete/', views.delete_filiere, name='filiere_delete'),

    # URLs pour PersonnelAdministratif
    path('personnel-administratif/', views.personnel_administratif_list, name='personnel_list'),
    path('personnel-administratif/create/', views.personnel_administratif_create, name='personnel_create'),
    path('personnel-administratif/<str:id>/', views.personnel_administratif_detail, name='personnel_detail'),
    path('personnel-administratif/<str:id>/update/', views.update_personnel_administratif, name='personnel_update'),
    path('personnel-administratif/<str:id>/delete/', views.delete_personel_administratif, name='personnel_delete'),

    # URLs pour Enseignant
    path('enseignant/', views.enseignant_list, name='enseignant_list'),
    path('enseignant/create/', views.enseignant_create, name='enseignant_create'),
    path('enseignant/<str:id>/', views.enseignant_detail, name='enseignant_detail'),
    path('enseignant/<str:id>/update/', views.update_enseignant, name='enseignant_update'),
    path('enseignant/<str:id>/delete/', views.delete_enseignant, name='enseignant_delete'),

    # URLs pour UE
    path('ue/', views.ue_list, name='ue_list'),
    path('ue/create/', views.ue_create, name='ue_create'),
    path('ue/<str:id>/', views.ue_detail, name='ue_detail'),
    path('ue/<str:id>/update/', views.update_ue, name='ue_update'),
    path('ue/<str:id>/delete/', views.delete_ue, name='ue_delete'),


    path('etablissement/', views.etablissement_list, name='etablissement_list'),
    path('etablissement/create/', views.etablissement_create, name='etablissement_create'),
    path('etablissement/<str:id>/', views.etablissement_detail, name='etablissement_detail'),
    path('etablissement/<str:id>/update/', views.etablissement_update, name='etablissement_update'),
    path('etablissement/<str:id>/delete/', views.etablissement_delete, name='etablissement_delete'),
]
