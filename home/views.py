from django.shortcuts import render, redirect, get_object_or_404
from .models import Gym, Product
from .forms import GymForm, ProductForm

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
    if request.method == 'POST':
        form = GymForm(request.POST, instance=gyms)
        if form.is_valid():
            form.save()
            return redirect('gym_list')
    else:
        form = GymForm(instance=gyms)
    return render(request, "gym_edit.html", {"form": form})


#for delete
def gym_delete(request, id):
    gyms = Gym.objects.get(id=id)
    gyms.delete(request)
    return redirect(gym_list)


#for product

def product_list(request):
    gyms = Product.objects.all()
    context = {
       "gym":gyms
    }
    return render(request, "index.html", context)

#create_product

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return redirect('product_list')
    else:
        form = ProductForm()
        return render(request, "create_product.html", {"form":form})

#Product edit
def product_edit(request, id):
    gyms = Product.objects.get(id=id)
    form = ProductForm(instance=gyms)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else:
            form = ProductForm()
            return render(request, "product_edit.html", {"form":form})

#product_delete
def product_delete(request, id):
    gyms = Product.objects.get(id=id)
    gyms.delete(request)