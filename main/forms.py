from django import forms
from main import models
from main.models import Product
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email',)  # Уберите 'date_of_birth'

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')