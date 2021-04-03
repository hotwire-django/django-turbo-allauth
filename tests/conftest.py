# Standard Library
import pathlib
import uuid

# Django
from django.http import HttpResponse
from django.utils.functional import cached_property

# Third Party Libraries
import pytest

TEST_PASSWORD = "testpass1"


def pytest_configure():
    from django.conf import settings

    settings.configure(
        SECRET_KEY="seekret",
        DATABASES={
            "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "mem_db"},
        },
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": [pathlib.Path(__file__).parent.absolute() / "templates"],
                "APP_DIRS": True,
                "OPTIONS": {
                    "debug": False,
                    "builtins": [],
                    "libraries": {},
                    "context_processors": [
                        "django.template.context_processors.debug",
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.static",
                        "django.template.context_processors.tz",
                        "django.contrib.messages.context_processors.messages",
                    ],
                },
            }
        ],
        INSTALLED_APPS=[
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.sites",
            "turbo_allauth",
            "turbo_response",
            "allauth",
            "allauth.account",
            "allauth.socialaccount",
            "allauth.socialaccount.providers.google",
            "tests.testapp.apps.TestAppConfig",
        ],
        MIDDLEWARE=[
            "django.middleware.security.SecurityMiddleware",
            "django.contrib.sites.middleware.CurrentSiteMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.locale.LocaleMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.middleware.gzip.GZipMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ],
        ROOT_URLCONF="tests.testapp.urls",
        LOGIN_REDIRECT_URL="/",
        SITE_ID=1,
        SOCIALACCOUNT_PROVIDERS={
            "google": {
                "SCOPE": ["profile", "email",],
                "AUTH_PARAMS": {"access_type": "online",},
            }
        },
    )


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
    from django.contrib.auth import get_user_model

    return get_user_model()


@pytest.fixture
def user(user_model, test_password):

    user = user_model(username="tester", email="tester@gmail.com")
    user.set_password(test_password)
    user.save()
    return user


@pytest.fixture
def anonymous_user():
    from django.contrib.auth.models import AnonymousUser

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

    from allauth.account.forms import EmailAwarePasswordResetTokenGenerator
    from allauth.account.utils import user_pk_to_url_str

    default_token_generator = EmailAwarePasswordResetTokenGenerator()
    return dict(
        uidb36=user_pk_to_url_str(user), key=default_token_generator.make_token(user)
    )


@pytest.fixture
def sociallogin(client, user_model):
    from allauth.socialaccount.models import SocialAccount, SocialLogin

    account = SocialAccount(provider="google")
    sociallogin = SocialLogin(account=account, user=user_model(),)
    session = client.session
    session["socialaccount_sociallogin"] = sociallogin.serialize()
    session.save()
    return sociallogin
