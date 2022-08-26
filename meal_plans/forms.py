from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms

from .models import Plan


class PlanForm(forms.ModelForm):
    """Form for a plan."""

    class Meta:
        model = Plan
        fields = ["date", "breakfast", "lunch", "dinner", "snack"]
        widgets = {"date": DatePickerInput()}


class DeletePlanForm(forms.ModelForm):
    """Form to delete a plan."""

    class Meta:
        model = Plan
        fields = []
