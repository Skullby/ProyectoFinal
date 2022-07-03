from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from Blog.forms import UserEditForm, UserRegistrationForm
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import DeleteView , UpdateView, CreateView

from Blog.models import Post

# Create your views here.

def inicio(self):

    plantilla = loader.get_template('inicio.html')
    documento = plantilla.render()

    return HttpResponse(documento)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request , data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username = usuario,  password = contra)

            if user is not None:
                login(request , user)

                return render(request, "Blog/bienvenido.html" , {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "Blog/bienvenido.html" , {'mensaje':"Error, datos incorrectos"})

        else:
             return render(request, "Blog/bienvenido.html" , {'mensaje':"Error, formulario erroneo"})
    form = AuthenticationForm()

    return render(request , "Blog/login.html" , {'form':form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "Blog/bienvenido.html" , {'mensaje' : "Usuario Creado"})

    else:
        form = UserRegistrationForm()

    return render(request, "Blog/register.html" , {"form":form})

@login_required
def perfil(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'Blog/perfil.html', args)

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.last_name = info['last_name']
            usuario.first_name = info['first_name']
            usuario.save()

            return render(request,"Blog/bienvenido.html")

    else:
        form = UserEditForm(initial = {'email':usuario.email})

    return render(request, "Blog/editarPerfil.html", {"form":form , "usuario":usuario})


class BlogList(LoginRequiredMixin,ListView):
    model = Post
    template_name = "Blog/blogList.html"


class BlogDetail(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "Blog/blogDetail.html"


class BlogPost(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "Blog/createBlog.html"
    success_url = "/inicio/"
    fields = ['titulo' , 'cuerpo' , 'autor']


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "Blog/confirmDelete.html"
    success_url = "/inicio/"