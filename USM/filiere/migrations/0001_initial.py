# Generated by Django 4.1.13 on 2024-05-20 22:49

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=100)),
                ('specialite', models.CharField(max_length=255)),
                ('grade', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'enseignants',
            },
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('doyen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filiere.enseignant')),
            ],
            options={
                'db_table': 'etablissements',
            },
        ),
        migrations.CreateModel(
            name='PersonnelAdministratif',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=100)),
                ('poste', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'personnels',
            },
        ),
        migrations.CreateModel(
            name='UE',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('intitule', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('nbCredits', models.IntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filiere.enseignant')),
            ],
            options={
                'db_table': 'ues',
            },
        ),
        migrations.CreateModel(
            name='Filiere',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('intitule', models.CharField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_mise_a_jour', models.DateTimeField(auto_now=True)),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filiere.etablissement')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filiere.enseignant')),
                ('ueObligatoires', models.ManyToManyField(related_name='filieres_obligatoires', to='filiere.ue')),
                ('ueOptionnelles', models.ManyToManyField(related_name='filieres_optionnelles', to='filiere.ue')),
            ],
            options={
                'db_table': 'filieres',
            },
        ),
        migrations.AddField(
            model_name='enseignant',
            name='ues',
            field=models.ManyToManyField(to='filiere.ue'),
        ),
    ]
