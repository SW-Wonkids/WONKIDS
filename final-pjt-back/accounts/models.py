from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    user_id = models.CharField(max_length=15, unique=True)
    user_email = models.EmailField(max_length=254)
    pokemon = models.CharField(max_length=10, blank=True, null=True)
    fin_prdt_cd = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'user_id' 