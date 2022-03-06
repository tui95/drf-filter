from django.db import models
from django_filters import rest_framework as filters

from book.models.book import Book

TEXT_FIELD_LOOKUP_EXPRS = ["exact", "iexact", "icontains", "in"]
NUMBER_FIELD_LOOKUP_EXPRS = ["exact", "lt", "lte", "gt", "gte"]


class BookFilterSet(filters.FilterSet):
    # notice that declared fields don't need to be included in class Meta's fields unlike ModelSerializer
    author = filters.CharFilter(field_name="author__name", lookup_expr="exact")
    author__icontains = filters.CharFilter(field_name="author__name", lookup_expr="icontains")
    # notice exclude=True. This will filter only the ones that don't match the condition
    name__not_icontains = filters.CharFilter(field_name="name", lookup_expr="icontains", exclude=True)

    author_with_n_books = filters.NumericRangeFilter(method="filter_author_with_n_books")

    ordering = filters.OrderingFilter(
        fields=[
            # field name, exposed name
            ("author__name", "author"),
            "isbn",
            "name",
            "pages",
            "rating",
            "price",
            "publication_date",
        ]
    )

    class Meta:
        model = Book
        fields = {
            "isbn": TEXT_FIELD_LOOKUP_EXPRS,
            "name": TEXT_FIELD_LOOKUP_EXPRS,
            "rating": NUMBER_FIELD_LOOKUP_EXPRS,
            "pages": NUMBER_FIELD_LOOKUP_EXPRS,
            "price": NUMBER_FIELD_LOOKUP_EXPRS,
            "publication_date": NUMBER_FIELD_LOOKUP_EXPRS,
        }

    def filter_author_with_n_books(
        self,
        queryset: models.QuerySet[Book],
        name: str,
        value: slice,
    ) -> models.QuerySet[Book]:
        """
        Filter books that were written by authors who have written n books

        Args:
            queryset (models.QuerySet[Book]): queryset passed from view class
            name (str): attribute name of this field in FilterSet class
            value (bool): value from request.query_param

        Returns:
            models.QuerySet[Book]: filtered queryset

        Notes:
            Custom method like this one must have same signature of parameters ordering, (queryset, name, value).
            Parameter names don't matter.

            Expect value to not be empty since it is handled before this method is called.
            If value is empty, it will exit and won't even reach this method.

        """
        author_books_count_queryset = queryset.annotate(books_count=models.Count("author__book"))

        q_object = models.Q()
        if value.start is not None:
            q_object &= models.Q(books_count__gte=value.start)
        if value.stop is not None:
            q_object &= models.Q(books_count__lte=value.stop)

        return author_books_count_queryset.filter(q_object)


class ReadingBookFilterSet(BookFilterSet):
    class Meta(BookFilterSet.Meta):
        pass

    @property
    def qs(self) -> models.QuerySet[Book]:
        """
        Override `qs` property and filter queryset against view's `request.user`

        Returns:
            models.QuerySet[Book]: books being read by current logged-in user
        """
        queryset = super().qs
        # request attribute is set by view
        user = getattr(self.request, "user", None)
        if user is None or not user.is_authenticated:
            return queryset.none()
        return queryset.filter(readinglist__user=user)
