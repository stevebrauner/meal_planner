import pytest
from django.contrib.auth.models import User


class TestView:
    """Tests for views for users app."""

    @pytest.mark.django_db
    def test_register(self, client):
        response = client.get("/users/register/")
        assert response.status_code == 200

        data = {"username": "testuser", "password": "secret"}
        response = client.post("/users/register/", data)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_user(self, client):
        response = client.get("/users/delete_user/")
        assert response.status_code == 302

        user_credentials = {"username": "testuser", "password": "secret"}
        user = User.objects.create(**user_credentials)
        client.force_login(user)
        users = User.objects.all()
        assert len(users) == 1
        response = client.post("/users/delete_user/")
        users = User.objects.all()
        assert len(users) == 0
