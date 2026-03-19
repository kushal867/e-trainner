from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import LoginForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('gym_list')

    next_url = request.GET.get('next') or request.POST.get('next')

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.user  # already authenticated in form
        login(request, user)

        messages.success(request, "Login successful")
        return redirect(next_url or 'gym_list')

    return render(request, "login.html", {
        "form": form,
        "next": next_url
    })


@require_POST
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('user:login')
