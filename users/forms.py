from django import forms
from django.contrib.auth.models import User


class DeleteUserForm(forms.ModelForm):
    """Form to delete a user."""

    class Meta:
        model = User
        fields = []
