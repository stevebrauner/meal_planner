import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from meal_plans.forms import DeletePlanForm, PlanForm
from meal_plans.models import Plan


class TestForm:
    """Tests meal_plans forms."""

    @pytest.fixture
    def plan(self):
        data = self.plan_data()
        plan_form = PlanForm(data=data)
        yield plan_form

    @pytest.fixture
    def invalid_plan(self):
        data = dict()
        plan_form = PlanForm(data=data)
        yield plan_form

    @pytest.fixture
    def delete_plan(self):
        data = self.plan_data()
        delete_plan_form = DeletePlanForm(data=data)
        yield delete_plan_form

    @pytest.mark.django_db
    def test_plan_form_with_data(self, plan):
        assert plan.is_valid()

    @pytest.mark.django_db
    def test_plan_form_with_invalid_data(self, invalid_plan):
        assert invalid_plan.is_valid() is False

    @pytest.mark.django_db
    def test_delete_plan_form_with_data(self, delete_plan):
        assert delete_plan.is_valid()

    def plan_data(self):
        owner = User.objects.create(username="testuser", password="secret")
        date = timezone.now()
        breakfast = "breakfast"
        lunch = "lunch"
        dinner = "dinner"
        snack = "snack"

        Plan.objects.create(
            date=date,
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            snack=snack,
            owner=owner,
        )

        data = {
            "date": date,
            "breakfast": breakfast,
            "lunch": lunch,
            "dinner": dinner,
            "snack": snack,
            "owner": owner.pk,
        }

        return data
