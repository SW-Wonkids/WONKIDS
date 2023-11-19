from rest_framework import serializers
from .models import Deposit, Savings
from django.contrib.auth import get_user_model

## product, option에 해당하는 serializer를 field로 나누어 설정 
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields='__all__'


# 적금 데이터 받을 serializer 
class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields='__all__'
        


# class DepositOptionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Deposit
#         fields = ('save_trm_6', 'save_trm_12', 'save_trm_24', 'save_trm_36', 'intr_rate_6', 'intr_rate_12', 'intr_rate_24','intr_rate_36')
