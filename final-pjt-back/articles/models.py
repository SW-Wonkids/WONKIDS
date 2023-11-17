from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    pokemon = models.CharField(max_length=10)


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)