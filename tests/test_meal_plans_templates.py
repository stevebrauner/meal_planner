import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from meal_plans.models import Plan
from pytest_django.asserts import assertTemplateUsed


class TestTemplates:
    """Tests meal_plans templates."""

    def test_meal_plans_index_uses_template(self, client):
        response = client.get("/")
        assertTemplateUsed(response, "meal_plans/index.html")

    @pytest.mark.django_db
    def test_meal_plans_plans_uses_template(self, client):
        self.login_user(client)

        response = client.get("/plans/")
        assertTemplateUsed(response, "meal_plans/plans.html")

    @pytest.mark.django_db
    def test_meal_plans_plan_uses_template(self, client):
        owner = self.login_user(client)
        plan = self.create_plan(owner)

        response = client.get(f"/plans/{ plan.id }/")
        assertTemplateUsed(response, "meal_plans/plan.html")

    @pytest.mark.django_db
    def test_meal_plans_new_plan_uses_template(self, client):
        self.login_user(client)

        response = client.get("/new_plan/")
        assertTemplateUsed(response, "meal_plans/new_plan.html")

    @pytest.mark.django_db
    def test_meal_plans_edit_plan_uses_template(self, client):
        owner = self.login_user(client)
        plan = self.create_plan(owner)

        response = client.get(f"/edit_plan/{ plan.id }/")
        assertTemplateUsed(response, "meal_plans/edit_plan.html")

    @pytest.mark.django_db
    def test_meal_plans_delete_plan_uses_template(self, client):
        owner = self.login_user(client)
        plan = self.create_plan(owner)

        response = client.get(f"/delete_plan/{ plan.id }/")
        assertTemplateUsed(response, "meal_plans/delete_plan.html")

    def login_user(self, client):
        user_credentials = {"username": "testuser", "password": "secret"}
        user = User.objects.create(**user_credentials)
        client.force_login(user)
        return user

    def create_plan(self, owner):
        date = timezone.now()
        plan = Plan.objects.create(owner=owner, date=date)
        return plan
