from . import views
from django.urls import path

urlpatterns = [
    path('meme/<str:theme>/', views.meme_generator, name='meme_generator'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('funny-videos/', views.funny_videos, name='funny_videos'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
]