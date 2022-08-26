from django.contrib.auth.models import User
from django.db import models


class Plan(models.Model):
    """Models a meal plan."""

    date = models.DateField()
    breakfast = models.CharField(max_length=200, blank=True, default="")
    lunch = models.CharField(max_length=200, blank=True, default="")
    dinner = models.CharField(max_length=200, blank=True, default="")
    snack = models.CharField(max_length=200, blank=True, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
