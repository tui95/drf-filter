from django_filters import rest_framework as dj_filters
from rest_framework import filters, mixins, viewsets

from book.filters.author_filter import AuthorFilterSet, AuthorSimpleFilterSet
from book.models.author import Author
from book.serializers.author_serializer import AuthorSerializer


class AuthorSimpleShortcutFilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.OrderingFilter]
    # fields must match model fields
    # if value is "__all__", will auto create filter with all model fields except `id` field
    filterset_fields = ["name", "age"]
    # need to set `rest_framework.filters.OrderingFilter` in filter_backends
    # if not specified, will default to serializer's fields
    # if value is "__all__", will allow ordering by fields in any model field or queryset aggregate
    ordering_fields = ["name", "age"]


class AuthorSimpleFilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorSimpleFilterSet


class AuthorComplexShortcutFilterViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [dj_filters.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        "name": [
            "exact",
            "iexact",
            "icontains",
            "in",
        ],
        "age": [
            "exact",
            "lt",
            "lte",
            "gt",
            "gte",
            "in",
        ],
    }
    ordering_fields = ["name", "age"]


class AuthorViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilterSet
