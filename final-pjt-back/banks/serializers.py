from rest_framework import serializers
from .models import Deposit, Savings
from django.contrib.auth import get_user_model
# 정기예금
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields='__all__'


# 적금
class SavingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings
        fields='__all__' 


#  정기예금 상세정보
# class DepositDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailDeposit
#         fields='__all__'
  

# 적금 상세정보
# class SavingsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailSavings
#         fields='__all__' 