from core.tests.test_utils.models import Author
from core.utils.admin_utils import ListDisplayBuilder


def test_list_display_builder_build() -> None:
    expected_list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
    ]
    actual_list_display = ListDisplayBuilder.build(Author)
    assert actual_list_display == expected_list_display


def test_list_display_builder_build_with_fields_arg() -> None:
    expected_list_display = ["first_name", "last_name"]
    actual_list_display = ListDisplayBuilder.build(Author, fields=["first_name", "last_name"])
    assert actual_list_display == expected_list_display


def test_list_display_builder_build_with_exclude_arg() -> None:
    expected_list_display = [
        "id",
        "first_name",
        "last_name",
    ]
    actual_list_display = ListDisplayBuilder.build(Author, exclude=["username"])
    assert actual_list_display == expected_list_display


def test_list_display_builder_get_model_field_names() -> None:
    expected_field_names = [
        "id",
        "username",
        "first_name",
        "last_name",
    ]
    actual_field_names = ListDisplayBuilder.get_model_field_names(Author)
    assert actual_field_names == expected_field_names
