from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('inicio/' , views.inicio, name="Inicio"),
    path('login/' , views.login_request, name="Login"),
    path('register/' , views.register, name="Register"),
    path('logout/' , LogoutView.as_view(template_name='Blog/logout.html'), name='Logout'),
]