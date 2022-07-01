from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasena' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contrasena' , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']
        help_texts = {k:"" for k in fields} 