from rest_framework import routers

from book.views.author_view import AuthorShortcutFilterViewSet, AuthorSimpleFilterViewSet, AuthorViewSet
from book.views.book_view import BookViewSet, ReadingBookViewSet

router = routers.SimpleRouter()
router.register("authors-simple-filter", AuthorSimpleFilterViewSet)
router.register("authors-shortcut-filter", AuthorShortcutFilterViewSet)
router.register("authors", AuthorViewSet)
router.register("books", BookViewSet)
router.register("reading-books", ReadingBookViewSet)

urlpatterns = router.urls
