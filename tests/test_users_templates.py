import pytest
from django.contrib.auth.models import User
from pytest_django.asserts import assertTemplateUsed


class TestTemplates:
    """Tests user templates."""

    def test_user_register_uses_template(self, client):
        response = client.get("/users/register/")
        assertTemplateUsed(response, "registration/register.html")

    def test_user_login_uses_template(self, client):
        response = client.get("/users/login/")
        assertTemplateUsed(response, "registration/login.html")

    def test_user_logged_out_uses_template(self, client):
        response = client.post("/users/logout/")
        assertTemplateUsed(response, "registration/logged_out.html")

    @pytest.mark.django_db
    def test_user_delete_user_uses_template(self, client):
        user_credentials = {"username": "testuser", "password": "secret"}
        user = User.objects.create(**user_credentials)
        client.force_login(user)

        response = client.get("/users/delete_user/")
        assertTemplateUsed(response, "users/delete_user.html")
