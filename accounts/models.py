from django.conf import settings
from django.db import models
from django.utils import timezone


class SpotifyToken(models.Model):
	"""Store Spotify OAuth tokens for a user."""
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	access_token = models.CharField(max_length=1000)
	refresh_token = models.CharField(max_length=1000, blank=True, null=True)
	scope = models.CharField(max_length=1000, blank=True)
	expires_at = models.DateTimeField(blank=True, null=True)

	def is_expired(self):
		if not self.expires_at:
			return True
		return timezone.now() >= self.expires_at

	def __str__(self):
		return f"SpotifyToken(user={self.user})"
