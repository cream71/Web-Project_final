import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=800)
    artist=models.CharField(max_length=800,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='posts')
    body=models.TextField()
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    tags=models.ManyToManyField('Tag')
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=100,default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self) :
        return str(self.title)
    
    class Meta:
        ordering = ['-created']

class LikedPost(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f'(self.user.username) : (self.title)'


class Tag(models.Model):
    name=models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author:{self.body[:30]}'
    
    class Meta:
        ordering = ['-created']

class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    body = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.author.username} : {self.body[:30]}'
        except:
            return f'no author:{self.body[:30]}'
    
    class Meta:
        ordering = ['-created']