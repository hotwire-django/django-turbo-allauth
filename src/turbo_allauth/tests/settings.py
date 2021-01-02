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
    "turbo_allauth",
    "turbo_allauth.tests.testapp.apps.TestAppConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "turbo_response.middleware.TurboStreamMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "testapp.urls"

SITE_ID = 1
