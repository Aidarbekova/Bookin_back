from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=120)

class Book(models.Model):
    name = models.CharField(max_length=120)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
    author = models.CharField(max_length=5500)
    description = models.TextField()
    image = models.CharField(max_length=5500)
    price = models.FloatField()
