from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.spotify import get_user_playlists
import requests

@login_required
def playlist_dashboard(request):
    """Fetch the user's playlists from Spotify and render them."""
    try:
        data = get_user_playlists(request.user)
        playlists = data.get('items', [])
    except requests.RequestException as e:
        playlists = []
        error_message = f"Failed to fetch playlists: {e}"
        return render(request, 'playlists/dashboard.html', {
            'error_message': error_message,
            'playlists': playlists
        })

    return render(request, 'playlists/dashboard.html', {
        'playlists': playlists
    })
