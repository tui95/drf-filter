from rest_framework import serializers

from book.models.book import Book
from book.serializers.author_serializer import AuthorSerializer


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "isbn",
            "name",
            "pages",
            "rating",
            "price",
            "author",
            "publication_date",
        ]


class BookExportSerializer(BookSerializer):
    author = serializers.CharField(source="author.name")

    class Meta(BookSerializer.Meta):
        pass
