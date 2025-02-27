from django.shortcuts import render
from .models import Meme
import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
import requests
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def meme_generator(request, theme="programming"):
    memes = Meme.objects.filter(theme=theme)  # Filtrer selon le thème
    meme = random.choice(memes) if memes else None
    return render(request, 'memeGenerator/meme.html', {'meme': meme, 'theme': theme})


# Inscription
def inscription(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après inscription
            return redirect('connexion')  # Rediriger vers la page d'accueil
    else:
        form = CustomUserCreationForm()
    return render(request, 'memeGenerator/inscription.html', {'form': form})

# Vue de connexion
def connexion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('meme_generator')  # Rediriger après connexion
    else:
        form = AuthenticationForm()
    return render(request, 'memeGenerator/connexion.html', {'form': form})


# Remplace avec ta propre clé API
YOUTUBE_API_KEY = "AIzaSyCOwVyRm9VRA_AjJhNjX0G9knI-2huv3KY"
def funny_videos(request):
    search_term = "funny"  # Cherche des vidéos avec le mot clé 'funny'
    limit = 5  # Nombre de vidéos à récupérer
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={search_term}&type=video&maxResults={limit}&key={YOUTUBE_API_KEY}"

    # Faire la requête à l'API YouTube
    response = requests.get(url)
    data = response.json()

    videos = []

    # Vérifie si des vidéos ont été retournées
    if "items" in data:
        for item in data["items"]:
            video = {
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"],
                "video_id": item["id"]["videoId"],
                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"]
            }
            videos.append(video)

    # Pagination
    paginator = Paginator(videos, 1)  # Afficher 1 vidéo par page
    page = request.GET.get('page')

    try:
        videos_page = paginator.page(page)
    except PageNotAnInteger:
        videos_page = paginator.page(1)
    except EmptyPage:
        videos_page = paginator.page(paginator.num_pages)

    return render(request, "memeGenerator/video.html", {"videos": videos_page})



def deconnexion(request):
    logout(request)  # Déconnecte l'utilisateur
    return redirect('connexion')  # Redirige vers la page de connexion
