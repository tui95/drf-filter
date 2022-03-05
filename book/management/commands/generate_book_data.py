import random

import factory.random
from django.core.management.base import BaseCommand, CommandParser

from book.models.author import Author
from book.models.book import Book
from book.tests.test_utils.factories.author_factory import AuthorFactory
from book.tests.test_utils.factories.book_factory import BookFactory


class Command(BaseCommand):
    help = "Generates book data"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("--n_authors", type=int, default=6, help="number of authors to be generated")
        parser.add_argument("--n_books", type=int, default=15, help="number of books to be generated")

    def handle(self, *args, **options) -> None:
        n_authors = options.get("n_authors")
        n_books = options.get("n_books")

        factory.random.reseed_random("lorem ipsum")
        # seed for random.choice in BookFactory
        random.seed(0)
        # clear old data so that unique constraint won't raise
        Author.objects.all().delete()
        Book.objects.all().delete()

        AuthorFactory.create_batch(size=n_authors)
        BookFactory.create_batch(size=n_books)

        self.stdout.write(self.style.SUCCESS("Successfully generated book data."))
        self.stdout.write(f"n_authors: {n_authors}")
        self.stdout.write(f"n_books:: {n_books}")
