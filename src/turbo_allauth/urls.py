from django.urls import include, path, re_path

from .views import account, socialaccount

urlpatterns = [
    path("login/", account.login, name="account_login",),
    path("signup/", account.signup, name="account_signup",),
    path("password/change/", account.password_change, name="account_change_password",),
    path("password/set/", account.password_set, name="account_set_password",),
    path("password/reset/", account.password_reset, name="account_reset_password",),
    re_path(
        r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        account.password_reset_from_key,
        name="account_reset_password_from_key",
    ),
    path("email/", account.email, name="account_email",),
    path("social/signup/", socialaccount.signup, name="socialaccount_signup",),
    path("", include("allauth.urls")),
]
