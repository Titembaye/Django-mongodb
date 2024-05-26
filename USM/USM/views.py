from etudiant.models import Etudiant
from filiere.models import Filiere, Enseignant, Etablissement
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm

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

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'Account created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def logout_view(request):
    logout(request)
    return redirect("/login/")