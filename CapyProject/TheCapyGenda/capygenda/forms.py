# blog/forms.py
from django import forms

from . import models
from capygenda.models import Diary, Todo


class DiaryForm(forms.ModelForm):
    class Meta :
        model = models.Diary
        fields=['title','description' ]

class TodoForm(forms.ModelForm):
    
    text = forms.CharField(label='')
    class Meta :
        model = models.Todo
        fields=['text' ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Add a to-do !'
        self.fields['text'].required = False 