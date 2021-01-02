# Standard Library
import uuid

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.sites.models import Site
from django.http import HttpResponse
from django.utils.functional import cached_property

# Third Party Libraries
import pytest

TEST_PASSWORD = "testpass1"


class MockSession(dict):
    """Provides mock session dict with session key"""

    @cached_property
    def session_key(self):
        return str(uuid.uuid4())


@pytest.fixture
def test_password():
    return TEST_PASSWORD


@pytest.fixture
def mock_session():
    return MockSession


@pytest.fixture
def site():
    return Site.objects.get_current()


@pytest.fixture
def get_response():
    return lambda req: HttpResponse()


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture
def user(user_model, test_password):
    user = user_model(username="tester", email="tester@gmail.com")
    user.set_password(test_password)
    user.save()
    return user


@pytest.fixture
def anonymous_user():
    return AnonymousUser()


@pytest.fixture
def login_user(client, user, test_password):
    client.login(username=user.username, password=test_password)
    return user
