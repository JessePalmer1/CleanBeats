from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import SpotifyToken

def index(request):
    """Home page. If logged in and connected to Spotify, go straight to playlists."""
    if request.user.is_authenticated:
        if SpotifyToken.objects.filter(user=request.user).exists():
            return redirect('playlists.dashboard')
        else:
            # Logged in but not connected to Spotify
            return render(request, 'home/index.html', {
                'template_data': {'title': 'Welcome'}
            })
    else:
        # Not logged in — show landing/login/signup
        return render(request, 'home/index.html', {
            'template_data': {'title': 'Welcome'}
        })
