# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField

from .helpers import *


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)

class BlogModel(models.Model):
    User=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=1000)
    content=FroalaField()
    cover_image=models.ImageField(upload_to='blog')
    slug=models.SlugField(max_length=1000,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    summary = models.TextField(default='To read more click read more')

    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.summary=self.summary+'.....'
        self.slug=generate_slug(self.title)
        super(BlogModel,self).save(*args,**kwargs)
