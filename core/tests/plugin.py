"""
Test plugin.

Notes:
    To prevent `django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS,
    but settings are not configured` error, use typing.TYPE_CHECKING to import django or drf modules required for
    typing and use `from __future__ import annotations` so that typings don't need to be quoted.

    Use local imports to prevent triggering django setting not configure error.

"""

from __future__ import annotations

import typing
from typing import Generator

import pytest

if typing.TYPE_CHECKING:
    from rest_framework import test


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db: None) -> None:
    """Enable db access for all tests"""


@pytest.fixture
def api_client() -> Generator[test.APIClient, None, None]:
    """Yield rest framework's APIClient"""
    from rest_framework import test

    yield test.APIClient()
