from django.urls import  path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
      path('login/', views.login, name='login'),
      path('registration/', views.registration, name='registration'),
 
]
