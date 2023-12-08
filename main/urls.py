from django.urls import  path, include
from django.contrib import admin
from . import views



urlpatterns = [
    path('admin', admin.site.urls),
    path('users', include('users.urls')),
    path('', views.index, name='home'),
    path('products/<int:id>', views.product_index, name='product_index'),
    path('products/new', views.add_product, name='add_product'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('categories', views.categories, name='categories'),
    path('profile', views.profile, name='profile'),
    path('cart', views.cart, name='cart'),
    path('orders', views.orders, name='orders'),
    path('settings', views.settings, name='settings'),
    
    

  
]
