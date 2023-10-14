from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
class UserForm(UserCreationForm):
    email=forms.EmailField( )
    class Meta:
        model=User
        fields=['username','email','password1','password2']

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your username'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'your email'
    }))
class AuthForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['email','password']
