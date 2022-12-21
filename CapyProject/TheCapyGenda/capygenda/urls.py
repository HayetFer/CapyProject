from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from TheCapyGenda import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name='home'),
    
    path('MyEntries/', views.MyEntries, name='entries'),
    path('deleteentry/<input_id>/', views.delete_entry, name='delete_entry'),
    path('delettodo/<inputtodo_id>/', views.delete_todo, name='delete_todo'),
   
   
]

