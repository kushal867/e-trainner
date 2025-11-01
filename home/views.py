from django.shortcuts import render, redirect, get_object_or_404
from .models import Gym, Product, GymReview
from .forms import GymForm, ProductForm, GymReviewForm  


def gym_list(request):
    data = Gym.objects.all()
    context = {
        "gyms": data
    }
    return render(request, "index.html", context)


def gym_create(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gym_list')  
    else:
        form = GymForm()

    return render(request, "gym_create.html", {"form": form})


def gym_edit(request, id):
    data = Gym( id=id)
    if request.method == 'POST':
        form = GymForm(request.POST, instance=id)
        if form.is_valid():
            form.save()
            return redirect('gym_list')
    else:
        form = GymForm(instance=id)

    return render(request, "gym_edit.html", {"form": form})


def gym_delete(request, id):
   data = Gym(id=id)
   data.delete()
   return redirect('gym_list')
