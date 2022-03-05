import factory

from book.models.author import Author
from core.tests.test_utils.factories.unique_faker import UniqueFaker


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = UniqueFaker("name")
    age = factory.Faker("random_int", min=18, max=90)
