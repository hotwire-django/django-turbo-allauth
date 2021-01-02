# Standard Library
import uuid

# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.utils.functional import cached_property

# Third Party Libraries
import pytest
from allauth.account.forms import EmailAwarePasswordResetTokenGenerator
from allauth.account.utils import user_pk_to_url_str
from allauth.socialaccount.models import SocialAccount, SocialLogin

TEST_PASSWORD = "testpass1"

default_token_generator = EmailAwarePasswordResetTokenGenerator()


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


@pytest.fixture
def user_with_unusable_password(user):
    user.set_unusable_password()
    user.save()
    return user


@pytest.fixture
def login_user_with_unusable_password(client, user_with_unusable_password):
    client.force_login(user_with_unusable_password)
    return user_with_unusable_password


@pytest.fixture
def password_reset_kwargs(user):
    return dict(
        uidb36=user_pk_to_url_str(user), key=default_token_generator.make_token(user)
    )


@pytest.fixture
def sociallogin(client, user_model):
    account = SocialAccount(provider="google")
    sociallogin = SocialLogin(account=account, user=user_model(),)
    session = client.session
    session["socialaccount_sociallogin"] = sociallogin.serialize()
    session.save()
    return sociallogin
