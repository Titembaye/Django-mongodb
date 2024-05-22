from django import forms
from .models import Filiere, PersonnelAdministratif, Enseignant, UE, Etablissement

class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['code', 'intitule', 'etablissement', 'ueOptionnelles', 'ueObligatoires']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'intitule': forms.TextInput(attrs={'class': 'form-control'}),
            'etablissement': forms.Select(attrs={'class': 'form-control'}),
        }

class PersonnelAdministratifForm(forms.ModelForm):
    class Meta:
        model = PersonnelAdministratif
        fields = ['nom', 'prenom', 'poste', 'contact', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }

class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom', 'specialite', 'grade', 'contact', 'email']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UEForm(forms.ModelForm):
    class Meta:
        model = UE
        fields = ['code', 'intitule', 'description', 'nbCredits', 'responsable']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'intitule': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissement
        fields = ['nom', 'doyen', 'type']
