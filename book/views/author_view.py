from django_filters import rest_framework as dj_filters
from rest_framework import filters, mixins, viewsets

from book.filters.author_filter import AuthorFilterSet, AuthorSimpleFilterSet
from book.models.author import Author
from book.serializers.author_serializer import AuthorSerializer


class AuthorShortcutFilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.OrderingFilter]
    # fields must match model fields
    filterset_fields = ["name", "age"]
    # need to set `rest_framework.filters.OrderingFilter` in filter_backends
    # if not specified, will default to serializer's fields
    # if value is "__all__", will allow ordering by fields in any model field or queryset aggregate
    ordering_fields = ["name"]


class AuthorSimpleFilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorSimpleFilterSet


class AuthorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilterSet
