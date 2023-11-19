from django.db import models
from django.conf import settings

# Create your models here.
class Deposit(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    dcls_month = models.CharField(max_length=10)
    save_trm_6 = models.CharField(max_length=3, null=True)
    save_trm_12 = models.CharField(max_length=3, null=True)
    save_trm_24 = models.CharField(max_length=3, null=True)
    save_trm_36 = models.CharField(max_length=3, null=True)
    intr_rate_6 = models.CharField(max_length=5, null=True)
    intr_rate_12 = models.CharField(max_length=5, null=True)
    intr_rate_24 = models.CharField(max_length=5, null=True)
    intr_rate_36 = models.CharField(max_length=5, null=True)
    join_deny = models.TextField(null=True)
    join_way = models.TextField(null=True)
    spcl_cnd = models.TextField(null=True)


class Savings(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    fin_prdt_nm = models.TextField()
    dcls_month = models.CharField(max_length=10)
    save_trm_6 = models.CharField(max_length=3, null=True)
    save_trm_12 = models.CharField(max_length=3, null=True)
    save_trm_24 = models.CharField(max_length=3, null=True)
    save_trm_36 = models.CharField(max_length=3, null=True)
    intr_rate_6 = models.CharField(max_length=5, null=True)
    intr_rate_12 = models.CharField(max_length=5, null=True)
    intr_rate_24 = models.CharField(max_length=5, null=True)
    intr_rate_36 = models.CharField(max_length=5, null=True)
    join_deny = models.TextField(null=True)
    join_way = models.TextField(null=True)
    spcl_cnd = models.TextField(null=True)