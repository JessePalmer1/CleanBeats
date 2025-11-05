from django.conf import settings
from datetime import timedelta
from django.utils import timezone
import requests
from .models import SpotifyToken

TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE = "https://api.spotify.com/v1"


def refresh_spotify_token_for_user(user):
    try:
        st = SpotifyToken.objects.get(user=user)
    except SpotifyToken.DoesNotExist:
        raise RuntimeError("No Spotify token for user")
    if not st.refresh_token:
        raise RuntimeError("No refresh token available")
    data = {
<<<<<<< HEAD
        'grant_type': 'refresh_token',
        'refresh_token': st.refresh_token,
        'client_id': settings.SPOTIFY_CLIENT_ID,
        'client_secret': settings.SPOTIFY_CLIENT_SECRET,
=======
        "grant_type": "refresh_token",
        "refresh_token": st.refresh_token,
        "client_id": settings.SPOTIFY_CLIENT_ID,
        "client_secret": settings.SPOTIFY_CLIENT_SECRET,
>>>>>>> main
    }
    r = requests.post(TOKEN_URL, data=data)
    r.raise_for_status()
    token_data = r.json()
<<<<<<< HEAD
    st.access_token = token_data.get('access_token')
    expires_in = token_data.get('expires_in')
    st.expires_at = timezone.now() + timedelta(seconds=expires_in) if expires_in else None
    # Spotify may or may not return a new refresh_token
    if token_data.get('refresh_token'):
        st.refresh_token = token_data.get('refresh_token')
=======
    st.access_token = token_data.get("access_token")
    expires_in = token_data.get("expires_in")
    st.expires_at = (
        timezone.now() + timedelta(seconds=expires_in) if expires_in else None
    )
    # Spotify may or may not return a new refresh_token
    if token_data.get("refresh_token"):
        st.refresh_token = token_data.get("refresh_token")
>>>>>>> main
    st.save()
    return st


def get_user_playlists(user):
    st = SpotifyToken.objects.get(user=user)
    if st.is_expired():
        st = refresh_spotify_token_for_user(user)
<<<<<<< HEAD
    headers = {'Authorization': f'Bearer {st.access_token}'}
=======
    headers = {"Authorization": f"Bearer {st.access_token}"}
>>>>>>> main
    url = f"{API_BASE}/me/playlists"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()
<<<<<<< HEAD
=======


def get_playlist_tracks(user, playlist_id):
    st = SpotifyToken.objects.get(user=user)
    if st.is_expired():
        st = refresh_spotify_token_for_user(user)
    headers = {"Authorization": f"Bearer {st.access_token}"}

    tracks = []
    url = f"{API_BASE}/playlists/{playlist_id}/tracks"

    while url:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        data = r.json()
        tracks.extend(data["items"])  # each item contains a track
        url = data["next"]  # Spotify paginates, so 'next' gives next page or None

    return tracks


def get_track_info(user, track_id):
    st = SpotifyToken.objects.get(user=user)
    if st.is_expired():
        st = refresh_spotify_token_for_user(user)
    headers = {"Authorization": f"Bearer {st.access_token}"}
    url = f"{API_BASE}/tracks/{track_id}"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()
>>>>>>> main
