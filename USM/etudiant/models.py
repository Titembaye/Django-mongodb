from djongo import models
from django.utils import timezone
from bson import ObjectId
from filiere.models import Filiere
from django.urls import reverse
from pymongo import MongoClient


class Etudiant(models.Model):
    _id = models.ObjectIdField()
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_nais = models.DateField()
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True, null=True, blank=True)

    class Niveau(models.TextChoices):
        LICENCE_1 = 'L1', 'Licence 1'
        LICENCE_2 = 'L2', 'Licence 2'
        LICENCE_3 = 'L3', 'Licence 3'
        MASTER_1 = 'M1', 'Master 1'
        MASTER_2 = 'M2', 'Master 2'
        DOCTORAT = 'D', 'Doctorat'

    niveau = models.CharField(max_length=2, choices=Niveau.choices, default=Niveau.LICENCE_1)

    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce




    def __str__(self):
        return f'{self.prenom} {self.nom}'


    def get_object_id(self):
        return str(self._id)


    class Meta:
        verbose_name = 'Etudiant'
        verbose_name_plural = 'Etudiants'
        ordering = ['nom', 'prenom']
        db_table = "etudiants"


    def get_absolute_url_edit(self):
        return reverse('etudiant_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('etudiant_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('etudiant_detail', kwargs={'id': str(self._id)})
