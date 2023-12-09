from django.shortcuts import render, redirect, HttpResponseRedirect
from main import models
from main import forms
from django.db.models import Q
from django.urls import reverse
from .models import Product

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    popular_products = Product.objects.filter(popular=True)
    new_products = Product.objects.filter(new=True)
    categories = models.ProductCategory.objects.all()
    context={
        'popular_products': popular_products,
        'new_products': new_products,
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, "main/about.html")

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


def search_products(request):
    query = request.GET.get('q')

    if query:
        # Используйте Q-объекты для выполнения поиска по нескольким полям
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(category__name__exact=query)
        )
    else:
        products = Product.objects.all()

    return render(request, 'main/search_results.html', {'products': products, 'query': query})


def categories(request):
    products = models.Product.objects.all()
    categories = models.ProductCategory.objects.all()
    
    context={
            'products': products,
            'categories': categories,
        }
    return render(request, 'main/categories.html', context)