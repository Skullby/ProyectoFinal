from unicodedata import name
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('inicio/' , views.inicio, name="Inicio"),
    path('login/' , views.login_request, name="Login"),
    path('register/' , views.register, name="Register"),
    path('logout/' , LogoutView.as_view(template_name='Blog/logout.html'), name='Logout'),
    path(r'^perfil/$', views.perfil, name="Perfil"),
    path('editarPerfil/' , views.editarPerfil, name="editarPerfil"),
    path('createBlog/', views.BlogPost.as_view(), name="Create"),
    path('blogList/', views.BlogList.as_view(), name="List"),
    path('blogDelete/<pk>', views.BlogDelete.as_view(), name="Delete"),
    path('blogDetail/<pk>', views.BlogDetail.as_view(), name="Detail"),
]