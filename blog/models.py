from django.conf import settings
from django.db import models

from markdownx.models import MarkdownxField

# Create your models here.
from django.utils.datetime_safe import datetime

class Category(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name

class KeyWord(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    main_image_url = models.ImageField(max_length=250, blank=True)
    body = MarkdownxField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    keywords = models.ManyToManyField('KeyWord', related_name='posts', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RecipePost(Post):
    dish = models.ManyToManyField("recipes.Dish", related_name="recipe")


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)