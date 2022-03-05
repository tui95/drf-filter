from __future__ import annotations

from django.db import models

from book.models.author import Author


class BookManager(models.Manager):
    def with_related_objects(self) -> models.QuerySet[Book]:
        return self.select_related("author")


class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=255)
    pages = models.PositiveIntegerField()
    rating = models.FloatField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    objects = BookManager()
