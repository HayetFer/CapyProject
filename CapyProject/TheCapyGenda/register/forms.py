from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Create your models here.


class Registering(UserCreationForm):

    email=forms.EmailField()
    

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={
            
            "username":None,
            
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Email' 
        self.fields['username'].widget.attrs['placeholder'] = 'Username' 
        self.fields['password1'].widget.attrs['placeholder'] = 'Password' 
        self.fields['password2'].widget.attrs['placeholder'] = 'Password verification' 
        self.fields['email'].widget.attrs['class'] = 'form-control' 

class MyAuthForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']
    def __init__(self, *args, **kwargs):
        super(MyAuthForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
        self.fields['username'].label = False
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}) 
        self.fields['password'].label = False