from rest_framework import mixins, viewsets

from book.filters.book_filter import BookFilterSet, ReadingBookFilterSet
from book.models.book import Book
from book.serializers.book_serializer import BookSerializer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.with_related_objects()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet


class ReadingBookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.with_related_objects()
    serializer_class = BookSerializer
    filterset_class = ReadingBookFilterSet
