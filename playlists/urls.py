from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.playlist_dashboard, name='playlists.dashboard'),
=======
    path("", views.playlist_dashboard, name="playlists.dashboard"),
    path("edit", views.render_edit, name="playlists.edit"),
>>>>>>> main
]
