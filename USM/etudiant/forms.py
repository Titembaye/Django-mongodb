from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'date_nais', 'contact', 'email', 'niveau', 'filiere']
        widgets = {
            'date_nais': forms.DateInput(attrs={'type': 'date'}),
        }
