from typing import List

from django.contrib import auth
from django.contrib.auth.models import User
from django.core import management
from django.core.management.base import BaseCommand

from book.models.book import Book
from book.models.reading_list import ReadingList
from book.tests.test_utils.factories.book_factory import get_random_instance


class Command(BaseCommand):
    help = "Load initial data"

    def handle(self, *args, **options) -> None:
        fixtures = ["users"]
        management.call_command("loaddata", *fixtures)
        management.call_command("generate_book_data")

        reading_lists = create_reading_lists(3)
        self.stdout.write(f"n_reading_list: {len(reading_lists)}")

        self.stdout.write(self.style.SUCCESS("Successfully load initial data."))


def get_n_unique_books(n_books: int) -> List[Book]:
    n_books = min(Book.objects.count(), n_books)
    got_books = set()
    while len(got_books) < n_books:
        random_book = get_random_instance(Book)
        got_books.add(random_book)
    return list(got_books)


def create_reading_lists(n: int) -> List[ReadingList]:
    user_model = auth.get_user_model()
    testuser: User = user_model.objects.get(username="testuser")
    books = get_n_unique_books(n)

    reading_lists = [ReadingList(user=testuser, book=b) for b in books]
    return ReadingList.objects.bulk_create(reading_lists)
