from django.shortcuts import render, redirect, get_object_or_404
from .models import Gym
from .forms import GymForm

# List all gyms
def gym_list(request):
    gyms = Gym.objects.all()
    context = {
        "gym":gyms
    }
    return render(request, "index.html", context)

from django.shortcuts import render, redirect
from .forms import GymForm

def gym_create(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gym_list')  # use the URL pattern name, not the view
    else:
        form = GymForm()

    return render(request, "gym_create.html", {'form': form})


def gym_edit(request, id):
    gyms = Gym.objects.get(id=id)
    form = GymForm(instance=gyms)
    if request.method == 'POST':
        form = GymForm(instance=gyms)
        if form.is_valid():
            form.save()
            return redirect(gym_list)
        else:
            form = GymForm(instance=gyms)
            return render(request, "gym_edit.html", {"form":form})

def gym_delete(request, id):
    gyms = Gym.objects.get(id=id)
    gyms.delete()
    return redirect(gym_list)