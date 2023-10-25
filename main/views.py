from django.shortcuts import render, redirect


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, "main/about.html")

def categories(request):
    return render(request, "main/categories.html")

def profile(request):
    return render(request, "main/profile.html")