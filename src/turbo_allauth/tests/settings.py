# Standard Library
import pathlib

SECRET_KEY = "o7pb3_ibyl@3%jhc85qj*dgh5etxmzxpg89%$85$#v92&8e0ub"
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "mem_db"},
}
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [pathlib.Path(__file__).parent.absolute() / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": False,
            "context_processors": [],
            "builtins": [],
            "libraries": {},
        },
    }
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "turbo_allauth.tests.testapp.apps.TestAppConfig",
]

ROOT_URLCONF = "testapp.urls"
