from django.shortcuts import render
from etudiant.models import Etudiant
from filiere.models import Filiere, Enseignant, Etablissement
from django.db.models import Count

def dashboard(request):
    total_etudiants = Etudiant.objects.count()
    total_etablissements = Etablissement.objects.count()
    total_enseignants = Enseignant.objects.count()

    students_by_level = Etudiant.objects.values('niveau').annotate(count=Count('niveau'))
    levels = [level['niveau'] for level in students_by_level]
    students_by_level_counts = [level['count'] for level in students_by_level]

    students_by_filiere = Etudiant.objects.values('filiere__intitule').annotate(count=Count('filiere'))
    filieres = [filiere['filiere__intitule'] for filiere in students_by_filiere]
    students_by_filiere_counts = [filiere['count'] for filiere in students_by_filiere]

    context = {
        'total_etudiants': total_etudiants,
        'total_etablissements': total_etablissements,
        'total_enseignants': total_enseignants,
        'levels': levels,
        'students_by_level': students_by_level_counts,
        'filieres': filieres,
        'students_by_filiere': students_by_filiere_counts,
        # Include additional data for other charts
    }

    return render(request, 'dashboard.html', context)
