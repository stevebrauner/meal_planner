import pytest
from django.contrib.auth.models import User
from users.forms import DeleteUserForm


class TestForm:
    """Tests user forms."""

    @pytest.fixture
    def user(self):
        data = {"username": "testuser", "password": "secret"}
        delete_user_form = DeleteUserForm(data=data)
        yield delete_user_form

    @pytest.mark.django_db
    def test_delete_plan_form_with_data(self, user):
        assert user.is_valid()
