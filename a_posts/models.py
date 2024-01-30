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
    tags=models.ManyToManyField('Tag')
    created=models.DateTimeField(auto_now_add=True)
    id=models.CharField(max_length=100,default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self) :
        return str(self.title)
    
    class Meta:
        ordering = ['-created']


class Tag(models.Model):
    name=models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name