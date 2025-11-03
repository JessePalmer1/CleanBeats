from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_dashboard, name='playlists.dashboard'),
]
