import django_filters

from book.models.author import Author


class AuthorSimpleFilterSet(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
        fields=["name", "age"],
    )

    class Meta:
        model = Author
        fields = ["name", "age"]


class AuthorFilterSet(django_filters.FilterSet):
    ordering = django_filters.OrderingFilter(
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
