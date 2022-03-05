from django.http import FileResponse
from drf_spectacular.utils import extend_schema
from rest_framework import generics, mixins, viewsets
from rest_framework.request import Request

from book.filters.book_filter import BookFilterSet, ReadingBookFilterSet
from book.models.book import Book
from book.serializers.book_serializer import BookSerializer
from book.services.book_export_service import export_books_as_excel
from core.renderers import XLSXRenderer


class BookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.with_related_objects()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet


class ReadingBookViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Book.objects.with_related_objects()
    serializer_class = BookSerializer
    filterset_class = ReadingBookFilterSet


class BookExportView(generics.GenericAPIView):
    queryset = Book.objects.with_related_objects()
    serializer_class = BookSerializer
    filterset_class = BookFilterSet
    renderer_classes = [XLSXRenderer]

    @extend_schema(filters=True, responses=bytes)
    def get(self, request: Request, **kwargs) -> FileResponse:
        # Note: no need to manually instantiate filterset classes, use `filter_queryset` method from `GenericAPIView`.
        # Any subclass of `GenericAPIView` have access to this method, for example, `ModelViewSet`
        filtered_queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(filtered_queryset, many=True)
        excel_stream = export_books_as_excel(serializer.data)
        return FileResponse(excel_stream, filename="books.xlsx", as_attachment=True)
