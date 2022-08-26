"""Views for users app."""

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .forms import DeleteUserForm


def register(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("meal_plans:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)


@login_required
def delete_user(request):
    user_to_delete = request.user
    if request.method != "POST":
        form = DeleteUserForm(instance=user_to_delete)
    else:
        form = DeleteUserForm(instance=user_to_delete, data=request.POST)
        if form.is_valid():
            user_to_delete.delete()
            messages.info(request, "Your account has been deleted.")
            return redirect("meal_plans:index")

    context = {"form": form}
    return render(request, "users/delete_user.html", context)
