from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    isbn = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
