import os
import pytest
from django.conf import settings


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ["DB_TEST_ENGINE"],
        "HOST": os.environ["DB_TEST_HOST"],
        "NAME": os.environ["DB_TEST_DATABASE"],
        "PORT": os.environ["DB_TEST_PORT"],
        "USER": os.environ["DB_TEST_USER"],
        "PASSWORD": os.environ["DB_TEST_PASSWORD"],
    }
