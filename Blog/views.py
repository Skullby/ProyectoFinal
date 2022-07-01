from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

from Blog.forms import UserRegistrationForm

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



