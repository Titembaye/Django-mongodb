# Generated by Django 4.1.13 on 2024-05-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filiere', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enseignant',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='etablissement',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='filiere',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personneladministratif',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ue',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]