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

class Manager(models.Model):
    name = models.CharField(max_length=222)
    username = models.CharField(max_length=222)
    password = models.CharField(max_length=222)
    email = models.CharField(max_length=222)

class Order(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)