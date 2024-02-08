
from django import forms
from django.forms import ModelForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'add comment...', 'size': '50'})
        }
        labels = {
            'body': ''
        }


@login_required
def comment_sent(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form =CommentCreateForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.author =request.user
            comment.parent_post = post
            comment.save()
        return redirect('POST', post.id)
    
    
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

class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'add reply...', 'class': '!text-sm'})
        }
        labels = {
            'body': ''
        }