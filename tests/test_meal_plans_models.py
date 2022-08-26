import pytest
from django.contrib.auth.models import User
from django.utils import timezone

from meal_plans.models import Plan


class TestModels:
    """tests Plan model."""

    @pytest.mark.django_db
    def test_plan(self):
        date = timezone.now()
        owner = User.objects.create()
        breakfast = "breakfast"
        lunch = "lunch"
        dinner = "dinner"
        snack = "snack"
        plan = Plan.objects.create(
            owner=owner,
            date=date,
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner,
            snack=snack,
        )
        assert plan.date == date
        assert plan.owner == owner
        assert plan.breakfast == breakfast
        assert plan.lunch == lunch
        assert plan.dinner == dinner
        assert plan.snack == snack
        assert plan.__str__() == date.__str__()
