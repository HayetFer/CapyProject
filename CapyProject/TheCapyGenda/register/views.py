from django.shortcuts import render, redirect
from .forms import MyAuthForm, Registering
# Create your views here.
def register(response):

    if response.method == "POST":
        form=Registering(response.POST)
        if form.is_valid():
            form.save()
        





    else:
        form=Registering()
        


    
    return render(response, 'register/register.html', {"form":form})




