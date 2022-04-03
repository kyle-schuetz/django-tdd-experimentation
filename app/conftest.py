import os

from django.conf import settings

import pytest

DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"

@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_NAME"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"]
    }

@pytest.fixture(scope="module")
def foo():
    # set up code
    yield "bar"
    # tear down code


# Given - th state of the application before the test runs (setup code, fixtures, database state)
# When - the behavior/logic being tested (code under test)
# Then - the expected changes based on thee behavior (asserts)