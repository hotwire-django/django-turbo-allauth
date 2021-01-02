# Django
from django.urls import reverse

# Third Party Libraries
import pytest
from pytest_django.asserts import assertTemplateUsed

pytestmark = pytest.mark.django_db


class TestLoginView:
    def test_get(self, client):
        resp = client.get(reverse("account_login"))
        assert resp.status_code == 200
        assert b'id="login-form"' in resp.content
        assertTemplateUsed(resp, "account/_login.html")

    def test_post_unsuccessful(self, client):
        resp = client.post(
            reverse("account_login"), {"login": "rando", "password": "random-pass",},
        )

        assert resp.status_code == 200
        assert b'target="login-form"' in resp.content
        assertTemplateUsed(resp, "account/_login.html")

    def test_post_successful(self, client, user, test_password):
        resp = client.post(
            reverse("account_login"),
            {"login": user.username, "password": test_password,},
        )
        print(resp.content)
        assert resp.url == "/"


class TestSignupView:
    def test_get(self, client):
        resp = client.get(reverse("account_signup"))
        assert resp.status_code == 200
        assert b'id="signup-form"' in resp.content
        assertTemplateUsed(resp, "account/_signup.html")

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
        assert resp.status_code == 200
        assert b'target="signup-form"' in resp.content
        assertTemplateUsed(resp, "account/_signup.html")

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
        assert resp.status_code == 200
        assert b'id="add-email-form"' in resp.content

    def test_add_email_unsuccessful(self, client, login_user):
        resp = client.post(
            reverse("account_email"), {"action_add": "true", "email": "bad-email"}
        )
        assert resp.status_code == 200
        assert b'target="add-email-form"' in resp.content

    def test_add_email_successful(self, client, login_user):
        url = reverse("account_email")
        resp = client.post(url, {"action_add": "true", "email": "tester-2@gmail.com"})
        assert resp.url == url
        assert login_user.emailaddress_set.count() == 2


class TestPasswordResetView:
    def test_get(self, client):
        resp = client.get(reverse("account_reset_password"))
        assert resp.status_code == 200
        assert b'id="password-reset-form"' in resp.content

    def test_post_unsuccessful(self, client):
        resp = client.post(
            reverse("account_reset_password"), {"email": "bad-email.com"}
        )
        assert resp.status_code == 200
        assert b'target="password-reset-form"' in resp.content

    def test_post_successful(self, client, user):
        resp = client.post(reverse("account_reset_password"), {"email": user.email})
        assert resp.url == reverse("account_reset_password_done")
