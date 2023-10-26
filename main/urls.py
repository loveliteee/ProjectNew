from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('profile', views.profile, name='profile'),
    path('cart', views.cart, name='cart'),
    path('orders', views.orders, name='orders'),
    path('settings', views.settings, name='settings'),
]
