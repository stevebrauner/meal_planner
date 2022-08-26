from django.urls import path

from . import views

app_name = "meal_plans"
urlpatterns = [
    path("", views.index, name="index"),
    path("plans/", views.plans, name="plans"),
    path("plans/<int:plan_id>/", views.plan, name="plan"),
    path("new_plan/", views.new_plan, name="new_plan"),
    path("edit_plan/<int:plan_id>/", views.edit_plan, name="edit_plan"),
    path("delete_plan/<int:plan_id>/", views.delete_plan, name="delete_plan"),
]
