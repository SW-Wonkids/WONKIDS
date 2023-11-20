from django.db import models
from django.conf import settings 

# 정기예금 상품정보
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

# 정기예금 옵션정보
# class DepositOption(models.Model):
#     fin_prdt_cd = models.TextField(unique=True)
#     fin_prdt_nm = models.TextField()
#     dcls_month = models.CharField(max_length=10)
#     save_trm_6 = models.CharField(max_length=3, null=True)
#     save_trm_12 = models.CharField(max_length=3, null=True)
#     save_trm_24 = models.CharField(max_length=3, null=True)
#     save_trm_36 = models.CharField(max_length=3, null=True)
#     intr_rate_6 = models.CharField(max_length=5, null=True)
#     intr_rate_12 = models.CharField(max_length=5, null=True)
#     intr_rate_24 = models.CharField(max_length=5, null=True)
#     intr_rate_36 = models.CharField(max_length=5, null=True)
#     join_deny = models.TextField(null=True)
#     join_way = models.TextField(null=True)
#     spcl_cnd = models.TextField(null=True)
# 적금
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

# 정기예금 상세정보
# class DetailDeposit(models.Model):
#     fin_prdt_cd = models.ForeignKey(Deposit, on_delete=models.CASCADE)
#     dcls_month = models.CharField(max_length=8)
#     kor_co_nm = models.TextField()
#     fin_prdt_nm = models.TextField()
#     join_deny = models.CharField(max_length=3)
#     join_way = models.TextField()
#     spcl_cnd = models.TextField()

# 적금 상세정보
# class DetailSavings(models.Model):
#     fin_prdt_cd = models.ForeignKey(Savings, on_delete=models.CASCADE)
#     dcls_month = models.CharField(max_length=8)
#     kor_co_nm = models.TextField()
#     fin_prdt_nm = models.TextField()
#     join_deny = models.CharField(max_length=3)
#     join_way = models.TextField()
#     spcl_cnd = models.TextField()