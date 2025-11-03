from django.contrib import admin
from .models import SpotifyToken


@admin.register(SpotifyToken)
class SpotifyTokenAdmin(admin.ModelAdmin):
	list_display = ('user', 'expires_at', 'scope')
	readonly_fields = ('access_token', 'refresh_token')
