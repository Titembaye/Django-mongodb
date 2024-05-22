from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Filiere, PersonnelAdministratif, Enseignant, UE, Etablissement
from .forms import FiliereForm, PersonnelAdministratifForm, EnseignantForm, UEForm, EtablissementForm
from pprint import pprint
from bson.errors import InvalidId  # Ajout de l'import
from .models import Enseignant, UE
from bson import ObjectId
from django.core.exceptions import ValidationError



def filiere_list(request):
    filieres = Filiere.objects.all()
    return render(request, 'filiere/filiere_list.html', {'filieres': filieres})


def filiere_create(request):
    etablissements = Etablissement.objects.all()
    ues = UE.objects.all()
    enseignants = Enseignant.objects.all()

    if request.method == 'POST':
        code = request.POST.get('code')
        intitule = request.POST.get('intitule')
        etablissement_id = request.POST.get('etablissement')
        ue_obligatoires_ids = request.POST.getlist('ue_obligatoires')
        ue_optionnelles_ids = request.POST.getlist('ue_optionnelles')
        responsable_id = request.POST.get('responsable')
        errors = {}

        if not code:
            errors['code'] = "Le code de la filière est requis."
        if not intitule:
            errors['intitule'] = "L'intitulé de la filière est requis."
        if not etablissement_id:
            errors['etablissement'] = "L'établissement de la filière est requis."
        else:
            try:
                etablissement = Etablissement.objects.get(_id=ObjectId(etablissement_id))
            except (Etablissement.DoesNotExist, InvalidId):
                errors['etablissement'] = "Établissement invalide."

        if not responsable_id:
            errors['responsable'] = "Le responsable de la filière est requis."
        else:
            try:
                responsable = Enseignant.objects.get(_id=ObjectId(responsable_id))
            except (Enseignant.DoesNotExist, InvalidId):
                errors['responsable'] = "Responsable invalide."

        if not ue_obligatoires_ids and not ue_optionnelles_ids:
            errors['ues'] = "Au moins une UE doit être sélectionnée."

        if not errors:
            filiere = Filiere.objects.create(
                code=code,
                intitule=intitule,
                etablissement=etablissement,
                responsable=responsable
            )
            for ue_id in ue_obligatoires_ids:
                try:
                    ue = UE.objects.get(_id=ObjectId(ue_id))
                    filiere.ueObligatoires.add(ue)
                except (UE.DoesNotExist, InvalidId):
                    pass

            for ue_id in ue_optionnelles_ids:
                try:
                    ue = UE.objects.get(_id=ObjectId(ue_id))
                    filiere.ueOptionnelles.add(ue)
                except (UE.DoesNotExist, InvalidId):
                    pass

            return redirect('filiere_list')

        return render(request, 'filiere/add_filiere.html', {
            'form': request.POST,
            'errors': errors,
            'etablissements': etablissements,
            'ues': ues,
            'enseignants': enseignants,
        })

    return render(request, 'filiere/add_filiere.html', {
        'etablissements': etablissements,
        'ues': ues,
        'enseignants': enseignants,
    })


def filiere_detail(request, id):
    filiere = get_object_or_404(Filiere, _id=ObjectId(id))
    return render(request, 'filiere/filiere_detail.html', {'filiere': filiere})


def update_filiere(request, id):
    filiere = get_object_or_404(Filiere, _id=ObjectId(id))
    etablissements = Etablissement.objects.all()
    ues = UE.objects.all()
    enseignants = Enseignant.objects.all()
    errors = {}

    if request.method == 'POST':
        code = request.POST.get('code')
        intitule = request.POST.get('intitule')
        etablissement_id = request.POST.get('etablissement')
        ue_obligatoires_ids = request.POST.getlist('ue_obligatoires')
        ue_optionnelles_ids = request.POST.getlist('ue_optionnelles')
        responsable_id = request.POST.get('responsable')

        if not code:
            errors['code'] = "Le code de la filière est requis."
        if not intitule:
            errors['intitule'] = "L'intitulé de la filière est requis."
        if not etablissement_id:
            errors['etablissement'] = "L'établissement de la filière est requis."
        else:
            try:
                etablissement = Etablissement.objects.get(_id=ObjectId(etablissement_id))
            except (Etablissement.DoesNotExist, ValidationError):
                errors['etablissement'] = "Établissement invalide."

        if not responsable_id:
            errors['responsable'] = "Le responsable de la filière est requis."
        else:
            try:
                responsable = Enseignant.objects.get(_id=ObjectId(responsable_id))
            except (Enseignant.DoesNotExist, ValidationError):
                errors['responsable'] = "Responsable invalide."

        if not ue_obligatoires_ids and not ue_optionnelles_ids:
            errors['ues'] = "Au moins une UE doit être sélectionnée."

        if not errors:
            filiere.code = code
            filiere.intitule = intitule
            filiere.etablissement = etablissement
            filiere.responsable = responsable
            filiere.ueObligatoires.clear()
            filiere.ueOptionnelles.clear()

            for ue_id in ue_obligatoires_ids:
                try:
                    ue = UE.objects.get(_id=ObjectId(ue_id))
                    filiere.ueObligatoires.add(ue)
                except (UE.DoesNotExist, ValidationError):
                    pass

            for ue_id in ue_optionnelles_ids:
                try:
                    ue = UE.objects.get(_id=ObjectId(ue_id))
                    filiere.ueOptionnelles.add(ue)
                except (UE.DoesNotExist, ValidationError):
                    pass

            filiere.save()
            return redirect('filiere_list')

    return render(request, 'filiere/update_filiere.html', {
        'filiere': filiere,
        'errors': errors,
        'etablissements': etablissements,
        'ues': ues,
        'enseignants': enseignants,
    })



def delete_filiere(request, id):
    filiere = get_object_or_404(Filiere, id=ObjectId(id))
    if request.method == 'POST':
        filiere.delete()
        return redirect('filiere_list')
    return render(request, 'filiere/delete_filiere.html', {'filiere': filiere})
#--------------------------------------------------------------------------------------#
def personnel_administratif_list(request):
    personnels = PersonnelAdministratif.objects.all()
    return render(request, 'personnels/personnel_list.html', {'personnels': personnels})


def personnel_administratif_detail(request, id):
    personnel = get_object_or_404(PersonnelAdministratif, _id=ObjectId(id))
    return render(request, 'personnels/personnel_detail.html', {'personnel': personnel})


def personnel_administratif_create(request):
    if request.method == 'POST':
        form = PersonnelAdministratifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personnel_list')
    else:
        form = PersonnelAdministratifForm()

    return render(request, 'personnels/add_personnel.html', {'form': form})

def update_personnel_administratif(request, id):
    personnel_administratif = get_object_or_404(PersonnelAdministratif, _id=ObjectId(id))
    if request.method == 'POST':
        form = PersonnelAdministratifForm(request.POST, instance=personnel_administratif)
        if form.is_valid():
            form.save()
            return redirect('personnel_list')
    else:
        form = PersonnelAdministratifForm(instance=personnel_administratif)
    return render(request, 'personnels/personnel_update.html', {'form': form})



def delete_personel_administratif(request, id):
    filiere = get_object_or_404(Filiere, id=ObjectId(id))
    if request.method == 'POST':
        filiere.delete()
        return redirect('filiere_list')
    return render(request, 'personnels/delete_personnel.html', {'filiere': filiere})
#--------------------------------------------------------------------------------------#
def enseignant_list(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'enseignant/enseignant_list.html', {'enseignants': enseignants})


def enseignant_create(request):
    etablissements = Etablissement.objects.all()
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enseignant_list')  # Rediriger vers la liste des enseignants après ajout
    else:
        form = EnseignantForm()
    return render(request, 'enseignant/add_enseignant.html', {'form': form, 'etablissements':etablissements})


def enseignant_detail(request, id):
    enseignant = get_object_or_404(Enseignant, _id=ObjectId(id))
    return render(request, 'enseignant/enseignant_detail.html', {'enseignant': enseignant})



def update_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, _id=ObjectId(id))
    ues = UE.objects.all()
    errors = {}

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        specialite = request.POST.get('specialite')
        grade = request.POST.get('grade')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        ues_ids = request.POST.getlist('ues')

        if not nom:
            errors['nom'] = "Le nom de l'enseignant est requis."
        if not prenom:
            errors['prenom'] = "Le prénom de l'enseignant est requis."
        if not specialite:
            errors['specialite'] = "La spécialité de l'enseignant est requise."
        if not grade:
            errors['grade'] = "Le grade de l'enseignant est requis."
        if not contact:
            errors['contact'] = "Le contact de l'enseignant est requis."
        if not email:
            errors['email'] = "L'email de l'enseignant est requis."
        else:
            try:
                enseignant.email = email
                enseignant.full_clean()  # This will check if the email is unique
            except ValidationError:
                errors['email'] = "Cet email est déjà utilisé."

        if not errors:
            enseignant.nom = nom
            enseignant.prenom = prenom
            enseignant.specialite = specialite
            enseignant.grade = grade
            enseignant.contact = contact
            enseignant.email = email
            enseignant.ues.clear()

            for ue_id in ues_ids:
                try:
                    ue = UE.objects.get(_id=ObjectId(ue_id))
                    enseignant.ues.add(ue)
                except (UE.DoesNotExist, ValidationError):
                    pass

            enseignant.save()
            return redirect('enseignant_list')

    return render(request, 'enseignant/update_enseignant.html', {
        'enseignant': enseignant,
        'errors': errors,
        'ues': ues,
    })


def delete_enseignant(request, id):
    enseignant = get_object_or_404(Filiere, id=ObjectId(id))
    if request.method == 'POST':
        enseignant.delete()
        return redirect('enseignant_list')
    return render(request, 'enseignant/enseignant_filiere.html', {'enseignant': enseignant})
#--------------------------------------------------------------------------------------#
def ue_list(request):
    ues = UE.objects.all()
    return render(request, 'ue/ue_list.html', {'ues': ues})

def ue_create(request):
    enseignants = Enseignant.objects.all()
    if request.method == 'POST':
        form = UEForm(request.POST)
        code = request.POST.get('code')
        intitule = request.POST.get('intitule')
        description = request.POST.get('description')
        responsable_id = request.POST.get('responsable')

        if form.is_bound:
            if not code:
                return HttpResponse("Code de l'UE requis.")
            if not intitule:
                return HttpResponse("Intitulé de l'UE requis.")
            if not description:
                return HttpResponse("Description de l'UE requise.")
            if not responsable_id:
                return HttpResponse("Un responsable est requis pour cette UE.")

            try:
                responsable = Enseignant.objects.get(_id=ObjectId(responsable_id))
            except Enseignant.DoesNotExist:
                return HttpResponse(f"Enseignant avec l'identifiant {responsable_id} est inexistant.")
            except InvalidId:
                return HttpResponse(f"Identifiant invalide: {responsable_id}")

            UE.objects.create(
                code=code,
                intitule=intitule,
                description=description,
                responsable=responsable
            )
            return redirect('ue_list')  # Remplacez 'ue_list' par le nom de votre vue de liste des UEs
    else:
        form = UEForm()
    return render(request, 'ue/add_ue.html', {'form': form, 'enseignants': enseignants})


def ue_detail(request, id):
    ue = get_object_or_404(UE, _id=ObjectId(id))
    return render(request, 'ue/detail_ue.html', {'ue': ue})


def update_ue(request, id):
    ue = get_object_or_404(UE, _id=ObjectId(id))
    if request.method == 'POST':
        form = UEForm(request.POST, instance=ue)
        if form.is_valid():
            form.save()
            return redirect('ue_list')
    else:
        form = UEForm(instance=ue)
    return render(request, 'ue/update_ue.html', {'form': form, 'ue': ue})


def delete_ue(request, id):
    ue = get_object_or_404(UE, id=ObjectId(id))
    if request.method == 'POST':
        ue.delete()
        return redirect('ue_list')
    return render(request, 'ue/delete_ue.html', {'ue': ue})



def etablissement_list(request):
    etablissements = Etablissement.objects.all()
    return render(request, 'etablissement/etablissement_list.html', {'etablissements': etablissements})

def etablissement_detail(request, id):
    try:
        etablissement = get_object_or_404(Etablissement, _id=ObjectId(id))
        return render(request, 'etablissement/etablissement_detail.html', {'etablissement': etablissement})
    except Etablissement.DoesNotExist:
        # Gérer le cas où l'objet d'établissement n'existe pas
        return render(request, 'etablissement/not_found.html', status=404)

def etablissement_create(request):
    enseignants = Enseignant.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('nom')
        type = request.POST.get('type')
        doyen_id = request.POST.get('doyen')
        errors = {}

        if not nom:
            errors['nom'] = "Le nom de l'établissement est requis."
        if not type:
            errors['type'] = "Le type d'établissement est requis."
        if not doyen_id:
            errors['doyen'] = "Le doyen de l'établissement est requis."
        else:
            try:
                doyen = Enseignant.objects.get(_id=ObjectId(doyen_id))
            except (Enseignant.DoesNotExist, InvalidId):
                errors['doyen'] = "Doyen invalide."

        if not errors:
            Etablissement.objects.create(nom=nom, type=type, doyen=doyen)
            return redirect('etablissement_list')

        return render(request, 'etablissement/etablissement_form.html', {
            'form': request.POST,
            'enseignants': enseignants,
            'errors': errors,
        })
    else:
        return render(request, 'etablissement/etablissement_form.html', {
            'enseignants': enseignants
        })
def etablissement_update(request, id):
    try:
        etablissement = Etablissement.objects.get(_id=ObjectId(id))
    except (Etablissement.DoesNotExist, InvalidId):
        return redirect('etablissement_list')

    enseignants = Enseignant.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('nom')

        type = request.POST.get('type')
        doyen_id = request.POST.get('doyen')
        errors = {}

        if not nom:
            errors['nom'] = "Le nom de l'établissement est requis."
        if not type:
            errors['type'] = "Le type d'établissement est requis."
        if not doyen_id:
            errors['doyen'] = "Le doyen de l'établissement est requis."
        else:
            try:
                doyen = Enseignant.objects.get(_id=ObjectId(doyen_id))
            except (Enseignant.DoesNotExist, InvalidId):
                errors['doyen'] = "Doyen invalide."

        if not errors:
            etablissement.nom = nom
            etablissement.type = type
            etablissement.doyen = doyen
            etablissement.save()
            return redirect('etablissement_list')

        return render(request, 'etablissement/etablissement_update.html', {
            'form': request.POST,
            'etablissement': etablissement,
            'enseignants': enseignants,
            'errors': errors,
        })
    else:
        return render(request, 'etablissement/etablissement_update.html', {
            'etablissement': etablissement,
            'enseignants': enseignants
        })


def etablissement_delete(request, id):
    etablissement = get_object_or_404(Etablissement, _id=ObjectId(id))
    if request.method == 'POST':
        etablissement.delete()
        return redirect('etablissement_list')
    return render(request, 'etablissement/etablissement_confirm_delete.html', {'etablissement': etablissement})
from django.shortcuts import render

# Create your views here.
