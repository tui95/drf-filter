from django_filters import rest_framework as filters

from book.models.author import Author


class AuthorSimpleFilterSet(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=["name", "age"],
    )

    class Meta:
        model = Author
        fields = ["name", "age"]


class AuthorFilterSet(filters.FilterSet):
    ordering = filters.OrderingFilter(
        fields=["name", "age"],
    )

    class Meta:
        model = Author
        fields = {
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
