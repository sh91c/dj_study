from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import path, include

from . import views
from .form import LoginForm

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(
        form_class=LoginForm,
        template_name='accounts/login_form.html'),
        name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]
