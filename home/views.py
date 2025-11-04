from django.shortcuts import render, redirect
from .models import Gym, Product, Gym, GymReview
from .forms import GymForm, ProductForm, GymReviewForm


# List all gyms
def gym_list(request):
    gyms = Gym.objects.all()
    context = {
        "gyms": gyms
    }
    return render(request, "index.html", context)


# Create a new gym
def gym_create(request):
    if request.method == 'POST':
        form = GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gym_list')
    else:
        form = GymForm()
    return render(request, "gym_create.html", {"form": form})


# Edit an existing gym
def gym_edit(request, id):
    gym = Gym.objects.get(id=id)
    if request.method == 'POST':
        form = GymForm(request.POST, instance=gym)
        if form.is_valid():
            form.save()
            return redirect('gym_list')
    else:
        form = GymForm(instance=gym)
    return render(request, "gym_edit.html", {"form": form})


# Delete a gym
def gym_delete(request, id):
    gym = Gym.objects.get(id=id)
    gym.delete()
    return redirect('gym_list')




# List all products
def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "product_list.html", context)


# Create a new product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, "product_create.html", {"form": form})


# Edit 
def product_edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, "product_edit.html", {"form": form})


# Delete a product
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('product_list')





#Review
def gym_review_list(request):
    gyms = GymReview.objects.all()
    context = {
        "gym":gyms
    }
    return render(request, "GymReview_list.html", context)

#gym_create
def gymReview_create(request):
    if request.method == 'POST':
        form = GymReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gymReview_list")
    else:
        form = GymReviewForm()
    return render(request, "GymReview_create.html", {"form": form})

        

#gymReview_edit
def gymReview_edit(request, id):
    gym_review = GymReview.objects.get(id=id)
    if request.method == 'POST':
        form = GymReviewForm(request.POST, instance=gym_review)
        if form.is_valid():
            form.save()
            return redirect("gymReview_list")
    else:
        form = GymReviewForm(instance=gym_review)
    return render(request, "gymReview_edit.html", {"form": form})



#GymReview_delete
def gymReview_delete(request, id):
    gyms = GymReview.objects.get(id=id)
    gyms.delete()
    return redirect("Gym_list.html")

