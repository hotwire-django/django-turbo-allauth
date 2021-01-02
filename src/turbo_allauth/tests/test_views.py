# Django
from django.urls import reverse

# Third Party Libraries
import pytest

pytestmark = pytest.mark.django_db


class TestLogin:
    def test_get(self, client):
        resp = client.get(reverse("account_login"))
        assert resp.status_code == 200
        assert b'id="login-form"' in resp.content
