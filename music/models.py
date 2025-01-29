from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    image_url = models.URLField()
    song_url = models.URLField()
