from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Etudiant
from .forms import EtudiantForm
from django.shortcuts import render, redirect
from django.utils import timezone
from bson import ObjectId
from filiere.models import Filiere
from .models import Etudiant
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def etudiant_list(request):
    try:
        etudiants_list = list(Etudiant.objects.get_queryset())  # Utilisation de la méthode de gestion personnalisée

        paginator = Paginator(etudiants_list, 10)  # Nombre d'étudiants par page

        page = request.GET.get('page')
        try:
            etudiants = paginator.page(page)
        except PageNotAnInteger:
            etudiants = paginator.page(1)
        except EmptyPage:
            etudiants = paginator.page(paginator.num_pages)

        return render(request, 'etudiant/etudiant_list.html', {'etudiants': etudiants})
    except Exception as e:
        # Affiche le message d'erreur dans le template
        return render(request, 'etudiant/etudiant_list.html', {'error': str(e)})
def etudiant_detail(request, id):
    etudiant = get_object_or_404(Etudiant, _id=id)
    return render(request, 'etudiant/detail_etudiant.html', {'etudiant': etudiant})


def etudiant_create(request):
    filieres = Filiere.objects.all()
    errors = {}

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_nais = request.POST.get('date_nais')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        niveau = request.POST.get('niveau')
        filiere_id = request.POST.get('filiere')

        # Validation
        if not nom:
            errors['nom'] = "Le nom de l'étudiant est requis."
        if not prenom:
            errors['prenom'] = "Le prénom de l'étudiant est requis."
        if not date_nais:
            errors['date_nais'] = "La date de naissance de l'étudiant est requise."
        if not contact:
            errors['contact'] = "Le contact de l'étudiant est requis."
        if email:
            try:
                Etudiant.objects.get(email=email)
                errors['email'] = "Cet email est déjà utilisé."
            except Etudiant.DoesNotExist:
                pass
        if not niveau:
            errors['niveau'] = "Le niveau de l'étudiant est requis."
        if not filiere_id:
            errors['filiere'] = "La filière de l'étudiant est requise."
        else:
            try:
                filiere = Filiere.objects.get(_id=ObjectId(filiere_id))
            except Filiere.DoesNotExist:
                errors['filiere'] = "Filière invalide."

        if not errors:
            etudiant = Etudiant(
                nom=nom,
                prenom=prenom,
                date_nais=date_nais,
                contact=contact,
                email=email,
                niveau=niveau,
                filiere=filiere,
            )
            etudiant.save()
            return redirect('etudiant_list')

        return render(request, 'etudiant/add_etudiant.html', {
            'form': request.POST,
            'filieres': filieres,
            'errors': errors,
            'niveau_choices': Etudiant.Niveau.choices,  # Pass the choices to the template
        })
    else:
        return render(request, 'etudiant/add_etudiant.html', {
            'filieres': filieres,
            'niveau_choices': Etudiant.Niveau.choices,  # Pass the choices to the template
        })


def etudiant_update(request, id):
    etudiant = get_object_or_404(Etudiant, _id=ObjectId(id))
    filieres = Filiere.objects.all()
    errors = {}

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date_nais = request.POST.get('date_nais')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        niveau = request.POST.get('niveau')
        filiere_id = request.POST.get('filiere')

        # Validation
        if not nom:
            errors['nom'] = "Le nom de l'étudiant est requis."
        if not prenom:
            errors['prenom'] = "Le prénom de l'étudiant est requis."
        if not date_nais:
            errors['date_nais'] = "La date de naissance de l'étudiant est requise."
        if not contact:
            errors['contact'] = "Le contact de l'étudiant est requis."
        if email and email != etudiant.email:
            try:
                Etudiant.objects.get(email=email)
                errors['email'] = "Cet email est déjà utilisé."
            except Etudiant.DoesNotExist:
                pass
        if not niveau:
            errors['niveau'] = "Le niveau de l'étudiant est requis."
        if not filiere_id:
            errors['filiere'] = "La filière de l'étudiant est requise."
        else:
            try:
                filiere = Filiere.objects.get(_id=ObjectId(filiere_id))
            except Filiere.DoesNotExist:
                errors['filiere'] = "Filière invalide."

        if not errors:
            etudiant.nom = nom
            etudiant.prenom = prenom
            etudiant.date_nais = date_nais
            etudiant.contact = contact
            etudiant.email = email
            etudiant.niveau = niveau
            etudiant.filiere = filiere
            etudiant.save()
            return redirect('etudiant_list')

        return render(request, 'etudiant/update_etudiant.html', {
            'etudiant': etudiant,
            'form': request.POST,
            'filieres': filieres,
            'errors': errors,
            'niveau_choices': Etudiant.Niveau.choices,  # Pass the choices to the template
        })
    else:
        return render(request, 'etudiant/update_etudiant.html', {
            'etudiant': etudiant,
            'filieres': filieres,
            'niveau_choices': Etudiant.Niveau.choices,  # Pass the choices to the template
        })

""" def etudiant_delete(request, id):
    etudiant = get_object_or_404(Etudiant, _id=id)
    if request.method == 'POST':
        etudiant.delete()
        return redirect('etudiant_list')
    return render(request, 'etudiant/delete_etudiant.html', {'etudiant': etudiant})"""

def etudiant_delete(request, id):
    etudiant = get_object_or_404(Etudiant, _id=ObjectId(id))
    if request.method == 'POST':
        etudiant.is_deleted = True
        etudiant.save()
        return redirect('etudiant_list')
    return render(request, 'etudiant_confirm_delete.html', {'etudiant': etudiant})
