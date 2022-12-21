import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from . import forms
from .models import Diary, Todo


def welcome(request):

    return render(request, 'capygenda/welcome.html')

def MyEntries(request):
    articles=Diary.objects.filter(user=request.user).order_by('date')
    
    return render(request, 'capygenda/savedEntries.html', {'articles':articles})



@login_required(login_url='/login')
def home(request):
   
    
    MyToDo = Todo.objects.filter(user=request.user)
    formtoDo = forms.TodoForm()


    if request.method == 'POST' and 'todosub' in request.POST:
        
        formtoDo = forms.TodoForm(request.POST)
        if formtoDo.is_valid():
            todoit = formtoDo.save(commit=False)
            todoit.user = request.user
            todoit.save()

            


   
    form = forms.DiaryForm()


    if request.method == 'POST' and 'submitit' in request.POST:
        form = forms.DiaryForm(request.POST)
        if form.is_valid():
            description = form.save(commit=False)
            description.user = request.user
            description.save()
            

    if request.method == 'POST' and 'temp' in request.POST:
        city = request.POST['city']


        # source contain JSON data from API
        start_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=714ccabdac0cd0ee174631e1bb7c18c8&units=metric'

        url = start_url.replace(" ","%20")
        source = urllib.request.urlopen(url).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
             'city' : city,
            "temp": str(list_of_data['main']['temp']) + 'C',
            'feelsLike': str(list_of_data['main']['feels_like']) + 'C',
            'description': list_of_data['weather'][0]['description'],
            "humidity": str(list_of_data['main']['humidity']),
            'form': form, 'formtoDo': formtoDo, 'MyToDo': MyToDo, 'checked':'checked', 
        }


    else:
        data ={'form': form, 'formtoDo': formtoDo, 'MyToDo': MyToDo,'checked': 'checked'}
    return render(request, "capygenda/entries.html", data)




@login_required(login_url='/login')
def delete_entry(request, input_id):
    entryInput = get_object_or_404(Diary, pk=input_id)
    entryInput.delete()
    return redirect('home')
# Create your views here.


@login_required(login_url='/login')
def delete_todo(request, inputtodo_id):
    tododelete = get_object_or_404(Todo, pk=inputtodo_id)
    tododelete.delete()
    return redirect('home')


