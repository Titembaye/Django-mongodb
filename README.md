### Documentation Complète de l'Application Universitaire

#### Table des Matières

1. [Introduction](#introduction)
2. [Installation et Configuration](#installation-et-configuration)
    - [Prérequis](#prérequis)
    - [Installation](#installation)
    - [Configuration de la Base de Données avec Docker](#configuration-de-la-base-de-données-avec-docker)
3. [Fonctionnalités](#fonctionnalités)
    - [Gestion des Étudiants](#gestion-des-étudiants)
    - [Gestion des Filières](#gestion-des-filières)
    - [Gestion des Enseignants](#gestion-des-enseignants)
    - [Gestion des Établissements](#gestion-des-établissements)
    - [Tableau de Bord](#tableau-de-bord)
4. [Sécurité](#sécurité)
    - [Authentification et Autorisation](#authentification-et-autorisation)
    - [Sécurisation des Données](#sécurisation-des-données)
    - [Bonnes Pratiques de Développement](#bonnes-pratiques-de-développement)
5. [Utilisation](#utilisation)
    - [Accès à l'Application](#accès-à-lapplication)
    - [Navigation dans l'Application](#navigation-dans-lapplication)
6. [Développement et Contribution](#développement-et-contribution)
    - [Structure du Projet](#structure-du-projet)
    - [Normes de Codage](#normes-de-codage)
    - [Contribution](#contribution)
7. [Support](#support)

---

## Introduction

Cette documentation couvre l'application universitaire, une plateforme de gestion académique permettant de gérer les étudiants, les filières, les enseignants et les établissements. L'application inclut un tableau de bord interactif pour visualiser diverses statistiques académiques.

## Installation et Configuration

### Prérequis

- Python 3.11
- Django 4.1.13
- Docker
- Docker Compose
- Git

### Installation

1. Clonez le dépôt du projet :

    ```bash
    git clone <URL_DU_DÉPÔT>
    cd University
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Pour Windows, utilisez `.venv\Scripts\activate`
    ```

3. Installez les dépendances du projet :

    ```bash
    pip install -r requirements.txt
    ```

### Configuration de la Base de Données avec Docker

1. Créez un fichier `docker-compose.yml` à la racine du projet avec le contenu suivant :

    ```yaml
    version: '3.8'
    services:
      mongo:
        image: mongo:4.4
        container_name: university_mongo
        restart: always
        ports:
          - 27017:27017
        environment:
          MONGO_INITDB_ROOT_USERNAME: root
          MONGO_INITDB_ROOT_PASSWORD: example
    ```

2. Démarrez le conteneur Docker :

    ```bash
    docker-compose up -d
    ```

3. Configurez Django pour utiliser MongoDB. Dans `settings.py`, configurez la base de données comme suit :

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'university',
            'ENFORCE_SCHEMA': False,
            'CLIENT': {
                'host': 'localhost',
                'port': 27017,
                'username': 'root',
                'password': 'example',
                'authSource': 'admin'
            }
        }
    }
    ```

4. Appliquez les migrations :

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Fonctionnalités

### Gestion des Étudiants

- **Ajouter des Étudiants**
- **Modifier des Étudiants**
- **Supprimer des Étudiants** (Suppression Logique)
- **Lister des Étudiants avec Pagination**

### Gestion des Filières

- **Ajouter des Filières**
- **Modifier des Filières**
- **Supprimer des Filières**
- **Lister des Filières**

### Gestion des Enseignants

- **Ajouter des Enseignants**
- **Modifier des Enseignants**
- **Supprimer des Enseignants**
- **Lister des Enseignants**

### Gestion des Établissements

- **Ajouter des Établissements**
- **Modifier des Établissements**
- **Supprimer des Établissements**
- **Lister des Établissements**

### Tableau de Bord

- **Statistiques Globales** : Nombre total d'étudiants, d'enseignants, de filières et d'établissements.
- **Répartition des Étudiants par Niveau**
- **Répartition des Étudiants par Filière**
- **Distribution des Âges des Étudiants**
- **Évolution des Inscriptions au Fil du Temps**

## Sécurité

### Authentification et Autorisation

- **Authentification** : Utilisation du système d'authentification intégré de Django.
- **Autorisation** : Mise en place de permissions pour restreindre l'accès à certaines fonctionnalités.

### Sécurisation des Données

- **Utilisation de HTTPS** : Assurez-vous que l'application est déployée avec HTTPS pour sécuriser les communications.
- **Gestion des Données Sensibles** : Stockage sécurisé des mots de passe et autres informations sensibles.

### Bonnes Pratiques de Développement

- **Validation des Données** : Validation des entrées utilisateur pour éviter les injections SQL et autres attaques.
- **Gestion des Erreurs** : Gestion appropriée des erreurs pour éviter les divulgations d'informations sensibles.

## Utilisation

### Accès à l'Application

Accédez à l'application via l'URL définie lors du déploiement. L'application utilise les routes par défaut de Django pour la gestion des ressources.

### Navigation dans l'Application

- **Page d'Accueil** : Vue d'ensemble des statistiques.
- **Gestion des Étudiants** : Accès via le menu principal.
- **Gestion des Filières** : Accès via le menu principal.
- **Gestion des Enseignants** : Accès via le menu principal.
- **Gestion des Établissements** : Accès via le menu principal.

## Développement et Contribution

### Structure du Projet

- `etudiant/` : Application pour la gestion des étudiants.
- `filiere/` : Application pour la gestion des filières.
- `enseignant/` : Application pour la gestion des enseignants.
- `etablissement/` : Application pour la gestion des établissements.
- `templates/` : Dossiers contenant les templates HTML.
- `static/` : Dossier contenant les fichiers statiques (CSS, JS).

### Normes de Codage

- **PEP 8** : Suivez les conventions de codage de PEP 8.
- **Commentaires** : Documentez le code avec des commentaires appropriés.
- **Tests** : Écrivez des tests unitaires pour toutes les fonctionnalités.

### Contribution

1. Forkez le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/new-feature`).
3. Commitez vos changements (`git commit -m 'Add new feature'`).
4. Poussez votre branche (`git push origin feature/new-feature`).
5. Ouvrez une Pull Request.

## Support

Pour toute question ou problème, veuillez ouvrir une issue sur le dépôt GitHub du projet. Vous pouvez également contacter l'équipe de développement via [email@example.com](mailto:email@example.com).

---

Cette documentation fournit une vue d'ensemble complète de l'application universitaire, couvrant l'installation, les fonctionnalités, la sécurité et les contributions. Assurez-vous de suivre les bonnes pratiques de développement et de maintenir la sécurité de l'application.
