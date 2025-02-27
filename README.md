
# Meme Generator

Une application web basée sur Django pour créer et partager des mèmes amusants et regarder des vidéos humoristiques.

## Installation

git clone  https://github.com/ArianeRakotomalala/memegenerator.git 
cd memeGenerator
python -m venv venv
source venv/bin/activate # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Fonctionnalités
*   Génération de mèmes thématiques
*   Lecture de vidéos amusantes depuis YouTube
*   Inscription et connexion des utilisateurs

## Dépendances

Voir le fichier `requirements.txt`.

