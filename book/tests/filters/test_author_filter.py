from typing import Any, Dict, List, NamedTuple

import pytest
from pytest_django import asserts

from book.filters.author_filter import AuthorFilterSet
from book.models.author import Author
from book.tests.test_utils.factories.author_factory import AuthorFactory


@pytest.fixture(autouse=True)
def glenn_charles_author() -> Author:
    return AuthorFactory(name="Glenn Charles", age=38)


@pytest.fixture(autouse=True)
def karen_campos_author() -> Author:
    return AuthorFactory(name="Karen Campos", age=48)


@pytest.fixture(autouse=True)
def betty_chandler_author() -> Author:
    return AuthorFactory(name="Betty Chandler", age=18)


@pytest.fixture(autouse=True)
def danielle_thomas_author() -> Author:
    return AuthorFactory(name="Danielle Thomas", age=18)


class AutherFilterSetTestParam(NamedTuple):
    data_filter: Dict[str, Any]
    author_fixtures: List[str]
    parametrize_id: str
    assert_order: bool = False


def get_test_author_filter_set_parametrize_argvalues():
    return [
        AutherFilterSetTestParam(
            data_filter={
                "ordering": "age",
            },
            author_fixtures=[
                "betty_chandler_author",
                "danielle_thomas_author",
                "glenn_charles_author",
                "karen_campos_author",
            ],
            assert_order=True,
            parametrize_id="order_by_age",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "ordering": "-age",
            },
            author_fixtures=[
                "karen_campos_author",
                "glenn_charles_author",
                "betty_chandler_author",
                "danielle_thomas_author",
            ],
            assert_order=True,
            parametrize_id="order_by_age_desc",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "ordering": "name",
            },
            author_fixtures=[
                "betty_chandler_author",
                "danielle_thomas_author",
                "glenn_charles_author",
                "karen_campos_author",
            ],
            assert_order=True,
            parametrize_id="order_by_name",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "ordering": "name,age",
            },
            author_fixtures=[
                "betty_chandler_author",
                "danielle_thomas_author",
                "glenn_charles_author",
                "karen_campos_author",
            ],
            assert_order=True,
            parametrize_id="order_by_name_age",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "name": "Karen Campos",
            },
            author_fixtures=[
                "karen_campos_author",
            ],
            parametrize_id="name",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "name__iexact": "karen campos",
            },
            author_fixtures=[
                "karen_campos_author",
            ],
            parametrize_id="name__iexact",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "name__icontains": "ch",
            },
            author_fixtures=[
                "betty_chandler_author",
                "glenn_charles_author",
            ],
            parametrize_id="name__icontains",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "name__in": "Karen Campos,Danielle Thomas",
            },
            author_fixtures=[
                "karen_campos_author",
                "danielle_thomas_author",
            ],
            parametrize_id="name__in",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "age__lt": 18,
            },
            author_fixtures=[],
            parametrize_id="age__lt_18",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "age__lte": 18,
            },
            author_fixtures=[
                "betty_chandler_author",
                "danielle_thomas_author",
            ],
            parametrize_id="age__lte_18",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "age__in": "18,38",
            },
            author_fixtures=[
                "betty_chandler_author",
                "danielle_thomas_author",
                "glenn_charles_author",
            ],
            parametrize_id="age__in_18,38",
        ),
        AutherFilterSetTestParam(
            data_filter={
                "age__gt": "20",
                "age__lt": "40",
            },
            author_fixtures=[
                "glenn_charles_author",
            ],
            parametrize_id="age__gt_20_and_age__lt_40",
        ),
    ]


def get_test_author_filter_set_parametrize_id(test_param: AutherFilterSetTestParam):
    return test_param.parametrize_id


def get_author_name(author: Author):
    return author.name


@pytest.mark.parametrize(
    argnames="test_param",
    argvalues=get_test_author_filter_set_parametrize_argvalues(),
    ids=get_test_author_filter_set_parametrize_id,
)
def test_author_filter_set(test_param: AutherFilterSetTestParam, request: pytest.FixtureRequest) -> None:
    expected_authors: List[Author] = [request.getfixturevalue(f) for f in test_param.author_fixtures]
    expected_author_names = [get_author_name(a) for a in expected_authors]

    actual_filter_set = AuthorFilterSet(data=test_param.data_filter, queryset=Author.objects.all())

    asserts.assertQuerysetEqual(
        actual_filter_set.qs,
        expected_author_names,
        transform=get_author_name,
        ordered=test_param.assert_order,
    )
