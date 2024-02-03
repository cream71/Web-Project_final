from django import forms 
from .forms import *
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages 
# Create your views here.
def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag=get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
    categories = Tag.objects.all()
    context = {
        'posts' : posts,
        'categories' : categories,
        'tag': tag
    }
    return render(request, 'a_posts/home.html', context)


@login_required
def post_create_view(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # Save the form data and get the Post object
            post.author = request.user
            form.save()  # Save the form data to create the Post object
            post.tags.set(form.cleaned_data['tags'])
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form': form})
@login_required
def post_delete_view(request,pk):
    post = get_object_or_404(Post, id=pk, author=request.user)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted Successfully')
        return redirect('home')
    return render(request, 'a_posts/post_delete.html', {'post' : post})
@login_required
def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk, author=request.user)
    form = PostEditForm(instance=post)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home')


    context = {
        'post' : post,
        'form' : form
    }
    return render(request, 'a_posts/post_edit.html', context)



def post_page_view(request, pk):
  
    post = get_object_or_404(Post, id=pk)
    return render(request, 'a_posts/post_page.html',{'post': post})