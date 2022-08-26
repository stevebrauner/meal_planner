import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from meal_plans.models import Plan


class TestView:
    """Tests for views."""

    def test_index(self, client):
        response = client.get("/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_plans(self, client):
        response = client.get("/plans/")
        assert response.status_code == 302

        self.login_user(client)
        response = client.get("/plans/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_plan(self, client):
        response = client.get("/plans/1/")
        assert response.status_code == 302

        owner = self.login_user(client)
        self.create_plan(owner)
        response = client.get("/plans/1/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_new_plan(self, client):
        response = client.get("/new_plan/")
        assert response.status_code == 302

        self.login_user(client)
        response = client.get("/new_plan/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_edit_plan(self, client):
        response = client.get("/edit_plan/1/")
        assert response.status_code == 302

        owner = self.login_user(client)
        plan = self.create_plan(owner)
        response = client.get("/edit_plan/1/")
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_plan(self, client):
        response = client.get("/delete_plan/1/")
        assert response.status_code == 302

        owner = self.login_user(client)
        self.create_plan(owner)
        response = client.get("/delete_plan/1/")
        assert response.status_code == 200
        response = client.post("/delete_plan/1/")
        plans = Plan.objects.all()
        assert len(plans) == 0

    def login_user(self, client):
        owner_credentials = {"username": "testuser", "password": "secret"}
        user = User.objects.create(**owner_credentials)
        client.force_login(user)
        return user

    def create_plan(self, owner):
        date = timezone.now()
        plan = Plan.objects.create(owner=owner, date=date)
        return plan
