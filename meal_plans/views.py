"""Views for meal_plans app."""

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DeletePlanForm, PlanForm
from .models import Plan


def index(request):
    return render(request, "meal_plans/index.html")


@login_required
def plans(request):
    plans = Plan.objects.filter(owner=request.user).order_by("date")
    context = {"plans": plans}
    return render(request, "meal_plans/plans.html", context)


@login_required
def plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    check_plan_owner(request, plan)
    context = {"plan": plan}
    return render(request, "meal_plans/plan.html", context)


@login_required
def new_plan(request):
    if request.method != "POST":
        form = PlanForm()
    else:
        form = PlanForm(data=request.POST)
        if form.is_valid():
            new_plan = form.save(commit=False)
            new_plan.owner = request.user
            new_plan.save()
            return redirect("meal_plans:plans")

    context = {"form": form}
    return render(request, "meal_plans/new_plan.html", context)


@login_required
def edit_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    check_plan_owner(request, plan)

    if request.method != "POST":
        form = PlanForm(instance=plan)
    else:
        form = PlanForm(instance=plan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("meal_plans:plan", plan_id=plan.id)

    context = {"plan": plan, "form": form}
    return render(request, "meal_plans/edit_plan.html", context)


@login_required
def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    check_plan_owner(request, plan)

    if request.method != "POST":
        form = DeletePlanForm(instance=plan)
    else:
        form = DeletePlanForm(instance=plan, data=request.POST)
        if form.is_valid():
            plan.delete()
            return redirect("meal_plans:plans")

    context = {"plan": plan, "form": form}
    return render(request, "meal_plans/delete_plan.html", context)


def check_plan_owner(request, plan):
    if plan.owner != request.user:
        raise Http404
