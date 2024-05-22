from django.urls import path
from . import views

urlpatterns = [
    path('', views.etudiant_list, name='etudiant_list'),
    path('create/', views.etudiant_create, name='etudiant_create'),
    path('<str:id>/', views.etudiant_detail, name='etudiant_detail'),
    path('<str:id>/update/', views.etudiant_update, name='etudiant_update'),
    path('<str:id>/delete/', views.etudiant_delete, name='etudiant_delete'),
]
