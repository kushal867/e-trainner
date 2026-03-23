from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .forms import LoginForm


def user_login(request):
    if request.user.is_authenticated:
        return redirect('gym_list')

    next_url = request.GET.get('next') or request.POST.get('next')

    form = LoginForm(request, data=request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)

        # Prevent open redirect attacks
        if next_url and url_has_allowed_host_and_scheme(
            url=next_url,
            allowed_hosts={request.get_host()},
            require_https=request.is_secure()
        ):
            redirect_url = next_url
        else:
            redirect_url = 'gym_list'

        messages.success(request, "Login successful")
        return redirect(redirect_url)

    return render(request, "login.html", {
        "form": form,
        "next": next_url
    })


@require_POST
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect('users:login')
