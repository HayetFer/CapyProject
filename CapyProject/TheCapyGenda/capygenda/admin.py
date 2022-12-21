from django.contrib import admin
from capygenda.models import Diary, Todo
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    
    list_display = ('text',)


admin.site.register(Todo, MyAdmin)