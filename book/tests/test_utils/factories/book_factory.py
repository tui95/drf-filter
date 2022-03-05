import random
from typing import Optional, Type, TypeVar

import factory
from django.db import models

from book.models.author import Author
from book.models.book import Book
from core.tests.test_utils.factories.unique_faker import UniqueFaker

Model = TypeVar("Model", bound=models.Model)


def get_random_instance(model: Type[Model]) -> Optional[Model]:
    ids = model.objects.values_list("id", flat=True)
    if not ids:
        return None
    random_id = random.choice(ids)
    return model.objects.get(pk=random_id)


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    isbn = UniqueFaker("isbn10")
    name = factory.Faker("text", max_nb_chars=30)
    pages = factory.Faker("pyint", min_value=10)
    rating = factory.Faker("pyfloat", min_value=0, max_value=10, right_digits=1)
    price = factory.Faker("pydecimal", min_value=1, max_value=500, left_digits=4, right_digits=2)
    # get existing random author
    author = factory.LazyFunction(lambda: get_random_instance(Author))
    publication_date = factory.Faker("date_this_century", before_today=True)
