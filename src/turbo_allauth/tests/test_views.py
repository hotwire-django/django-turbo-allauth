# Standard Library
import http

# Django
from django.urls import reverse

# Third Party Libraries
import pytest

pytestmark = pytest.mark.django_db


class TestLoginView:
    def test_get(self, client):
        resp = client.get(reverse("account_login"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_unsuccessful(self, client):
        resp = client.post(
            reverse("account_login"), {"login": "rando", "password": "random-pass",},
        )

        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_successful(self, client, user, test_password):
        resp = client.post(
            reverse("account_login"),
            {"login": user.username, "password": test_password,},
        )
        assert resp.url == "/"


class TestSignupView:
    def test_get(self, client):
        resp = client.get(reverse("account_signup"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_unsuccessful(self, client):
        resp = client.post(
            reverse("account_signup"),
            {
                "username": "tester",
                "email": "bad-email",
                "password1": "bad-pass",
                "password2": "bad-pass-match",
            },
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_successful(self, client, user_model):
        resp = client.post(
            reverse("account_signup"),
            {
                "username": "tester",
                "email": "tester@gmail.com",
                "password1": "good-pass-1234",
                "password2": "good-pass-1234",
            },
        )

        assert resp.url == "/"
        user = user_model.objects.get(username="tester")
        assert user.check_password("good-pass-1234")


class TestEmailView:
    def test_get(self, client, login_user):
        resp = client.get(reverse("account_email"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_add_email_unsuccessful(self, client, login_user):
        resp = client.post(
            reverse("account_email"), {"action_add": "true", "email": "bad-email"}
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_add_email_successful(self, client, login_user):
        url = reverse("account_email")
        resp = client.post(url, {"action_add": "true", "email": "tester-2@gmail.com"})
        assert resp.url == url
        assert login_user.emailaddress_set.count() == 2


class TestPasswordResetView:
    def test_get(self, client):
        resp = client.get(reverse("account_reset_password"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_unsuccessful(self, client):
        resp = client.post(
            reverse("account_reset_password"), {"email": "bad-email.com"}
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_successful(self, client, user):
        resp = client.post(reverse("account_reset_password"), {"email": user.email})
        assert resp.url == reverse("account_reset_password_done")


class TestPasswordSetView:
    def test_get_if_usable_password(self, client, login_user):
        resp = client.get(reverse("account_set_password"))
        assert resp.url == reverse("account_change_password")

    def test_get(self, client, login_user_with_unusable_password):
        resp = client.get(reverse("account_set_password"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_unsuccessful(self, client, login_user_with_unusable_password):
        resp = client.post(
            reverse("account_set_password",),
            {"password1": "badpass", "password2": "badpass-1"},
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY


class TestPasswordResetFromKeyView:
    def test_get_and_post(self, client, user, password_reset_kwargs):
        """Do everything in one test run to preserve session"""
        resp = client.get(
            reverse("account_reset_password_from_key", kwargs=password_reset_kwargs)
        )
        assert resp.url == reverse(
            "account_reset_password_from_key",
            kwargs={**password_reset_kwargs, "key": "set-password"},
        )

        resp = client.get(
            reverse(
                "account_reset_password_from_key",
                kwargs={**password_reset_kwargs, "key": "set-password"},
            )
        )
        assert resp.status_code == http.HTTPStatus.OK

        resp = client.post(
            reverse(
                "account_reset_password_from_key",
                kwargs={**password_reset_kwargs, "key": "set-password"},
            ),
            {"password1": "bad-testpass", "password2": "bad-testpass-2",},
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

        resp = client.post(
            reverse(
                "account_reset_password_from_key",
                kwargs={**password_reset_kwargs, "key": "set-password"},
            ),
            {"password1": "good-testpass-1", "password2": "good-testpass-1",},
        )
        assert resp.url == reverse("account_reset_password_from_key_done")


class TestSocialSignup:
    def test_get(self, client, sociallogin):
        resp = client.get(reverse("socialaccount_signup"))
        assert resp.status_code == http.HTTPStatus.OK

    def test_post_unsuccessful(self, client, sociallogin):
        resp = client.post(
            reverse("socialaccount_signup"), {"email": "bad-email", "username": ""}
        )
        assert resp.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY

    def test_post_successful(self, client, sociallogin, user_model):
        resp = client.post(
            reverse("socialaccount_signup"),
            {"email": "good-email@gmail.com", "username": "tester"},
        )
        assert resp.url == "/"
        user = user_model.objects.get(username="tester")
        assert user.email == "good-email@gmail.com"
