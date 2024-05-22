from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),  # Ajoutez cette ligne pour la page d'accueil
    path('', include('filiere.urls')),
    path('etudiant/', include('etudiant.urls'))
]
