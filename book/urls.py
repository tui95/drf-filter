from django.urls import path
from rest_framework import routers

from book.views.author_view import AuthorShortcutFilterViewSet, AuthorSimpleFilterViewSet, AuthorViewSet
from book.views.book_view import BookExportView, BookViewSet, ReadingBookViewSet

router = routers.SimpleRouter()
router.register("authors-simple-filter", AuthorSimpleFilterViewSet, basename="authors-simple-filter")
router.register("authors-shortcut-filter", AuthorShortcutFilterViewSet, basename="authors-shortcut-filter")
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)
router.register("reading-books", ReadingBookViewSet, basename="reading-books")

urlpatterns = [
    *router.urls,
    path("books/export/", BookExportView.as_view(), name="books-export"),
]
