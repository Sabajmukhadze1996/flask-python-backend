from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    main_image = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)


class Tag(models.Model):
    title = models.CharField(max_length=50)


class Menu(models.Model):
    title = models.CharField(max_length=100)
    position_number = models.IntegerField()
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

