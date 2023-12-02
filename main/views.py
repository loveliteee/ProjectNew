from django.shortcuts import render
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect
from main import models
from main import forms

from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    popular_products = models.Product.objects.all()

    return render(request, 'main/index.html', context={
        'popular_products': popular_products,
    })

def about(request):
    return render(request, "main/about.html")

def categories(request):
    return render(request, "main/categories.html")

def profile(request):
    return render(request, "main/profile.html")

def cart(request):
    return render(request, "main/cart.html")

def orders(request):
    return render(request, "main/orders.html")

def settings(request):
    return render(request, "main/settings.html")

def product_index(request, id):
    product = models.Product.objects.filter(pk=id).first()
    return render(request, 'main/product_index.html', context={
        'product': product,
    })

def add_product(request):
    form = forms.ProductForm()

    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        vendor_code = request.POST.get("vendor_code")
        description = request.POST.get("description")
        image = request.FILES

        print("FFFF:", name,
                price,
                quantity,
                vendor_code,
                description, image
        )

        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('/')
        else:
            print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
            return render(request, 'main/add_product.html', context={
                'form': form
            })


    return render(request, 'main/add_product.html', context={
        'form': form
    })

# views.py


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index.html')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index.html')  # Замените 'home' на URL вашей домашней страницы
    else:
        form = CustomAuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
