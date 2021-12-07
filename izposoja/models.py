from django.db import models


class Lokacija(models.Model):
    ime = models.CharField(max_length=100)
    naslov = models.CharField(max_length=1000)
