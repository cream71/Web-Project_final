
from django import forms
from django.forms import ModelForm

from .models import *


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image','body','tags']
        labels = {
            'body' : 'Facilities',
            'tags' :'Category',
            'image':'Image'
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows':1, 'placeholder': 'Add details of location..', 'class': 'font1 text 4xl'}),
        
            'tags' : forms.CheckboxSelectMultiple() ,       
        }


class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body','tags']
        labels = {
            'body' : '',
            'tags' :'Category'

        }
        widgets={
            'body' : forms.Textarea(attrs={'rows':3 , 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple() , 
        }