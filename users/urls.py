from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from users.views import ( UserLoginView, UserProfileView,
                         UserRegistrationView)

app_name = 'users'

urlpatterns = [
      path('login/', views.login, name='login'),
      path('registration/', UserRegistrationView.as_view(), name='registration'),
      path('profile/', UserProfileView.as_view(), name='profile'),
      path('logout/', LogoutView.as_view(), name='logout'),
      
]
