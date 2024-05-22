from django.urls import reverse
from djongo import models
from django.utils import timezone

class Filiere(models.Model):
    _id = models.ObjectIdField()
    code = models.CharField(max_length=50)
    intitule = models.CharField(max_length=255)
    etablissement = models.ForeignKey('Etablissement', to_field='_id', on_delete=models.CASCADE)
    ueObligatoires = models.ManyToManyField('UE', related_name='filieres_obligatoires')
    ueOptionnelles = models.ManyToManyField('UE', related_name='filieres_optionnelles')
    responsable = models.ForeignKey('Enseignant', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce


    class Meta:
        db_table = "filieres"

    def __str__(self):
        return self.intitule

    def delete(self):
        self.is_deleted = True
        self.save()

    def get_object_id(self):
        return str(self._id)

    def get_absolute_url_edit(self):
        return reverse('filiere_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('filiere_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('filiere_detail', kwargs={'id': str(self._id)})


class PersonnelAdministratif(models.Model):
    _id = models.ObjectIdField()
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce


    class Meta:
        db_table = 'personnels'

    def __str__(self):
        return self.nom

    def delete(self):
        self.is_deleted = True
        self.save()

    def get_object_id(self):
        return str(self._id)

    def get_absolute_url_edit(self):
        return reverse('personnel_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('personnel_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('personnel_detail', kwargs={'id': str(self._id)})


class Enseignant(models.Model):
    _id = models.ObjectIdField()
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=255)
    grade = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    ues = models.ManyToManyField('UE')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce


    class Meta:
        db_table = 'enseignants'


    def get_object_id(self):
        return str(self._id)

    def delete(self):
        self.is_deleted = True
        self.save()

    def get_absolute_url_edit(self):
        return reverse('enseignant_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('enseignant_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('enseignant_detail', kwargs={'id': str(self._id)})


class UE(models.Model):
    _id = models.ObjectIdField()
    code = models.CharField(max_length=50)
    intitule = models.CharField(max_length=255)
    description = models.TextField()
    nbCredits = models.IntegerField()
    responsable = models.ForeignKey('Enseignant', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_mise_a_jour = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce


    class Meta:
        db_table = 'ues'

    def __str__(self):
        return self.intitule

    def delete(self):
        self.is_deleted = True
        self.save()

    def get_object_id(self):
        return str(self._id)

    def get_absolute_url_edit(self):
        return reverse('ue_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('ue_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('ue_detail', kwargs={'id': str(self._id)})

class Etablissement(models.Model):
    _id = models.ObjectIdField()
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    doyen = models.ForeignKey('Enseignant', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)  # Champ pour suppression douce


    class Meta:
        db_table = "etablissements"

    def get_object_id(self):
        return str(self._id)

    def delete(self):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.nom

    def get_object_id(self):
        return str(self._id)

    def get_absolute_url_edit(self):
        return reverse('etablissement_update', kwargs={'id': str(self._id)})

    def get_absolute_url_delete(self):
        return reverse('etablissement_delete', kwargs={'id': str(self._id)})

    def get_absolute_url_detail(self):
        return reverse('etablissement_detail', kwargs={'id': str(self._id)})

