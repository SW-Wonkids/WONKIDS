from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Deposit, Savings

# API_KEY 가져오기
from django.conf import settings

import requests
from .serializers import DepositSerializer, SavingsSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
# 정기예금 데이터 가져오는 함수
@api_view(['GET', 'POST'])
def bank_list_deposit(request):
    API_KEY = settings.API_KEY
    deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    deposit_data = requests.get(deposit_url).json()
    
    for deposit_product in deposit_data.get('result').get('baseList'):
        # 이미 저장된 상품이 아닌 경우에 대해 
        fin_prdt_cd = deposit_product.get('fin_prdt_cd')
        if not Deposit.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
             
            # optionList 항목 중 동일 fin_prdt_cd 인 경우
            for deposit_option in deposit_data.get('result').get('optionList'):
                if deposit_option.get('fin_prdt_cd') == fin_prdt_cd:
                    # intr_rate 값이 NULL 인 경우 '-'로 대체
                    intr_rate = deposit_option.get('intr_rate')
                    if not intr_rate:
                        intr_rate = '-'
                    
                    save_trm = deposit_option.get('save_trm')
                    if save_trm in ("6"):
                        save_trm_6= deposit_option.get('save_trm')
                        intr_rate_6= deposit_option.get('intr_rate')
                    elif save_trm in ("12"):
                        save_trm_12= deposit_option.get('save_trm')
                        intr_rate_12= deposit_option.get('intr_rate')
                    elif save_trm in ("24"):
                        save_trm_24= deposit_option.get('save_trm')
                        intr_rate_24= deposit_option.get('intr_rate')
                    elif save_trm in ("36"):
                        save_trm_36= deposit_option.get('save_trm')
                        intr_rate_36= deposit_option.get('intr_rate')        

            save_deposit_data = {
                'fin_prdt_cd': fin_prdt_cd,
                'fin_prdt_nm': deposit_product.get('fin_prdt_nm'),
                'dcls_month': deposit_product.get('dcls_month'),
                'join_deny': deposit_product.get('join_deny'),
                'join_way': deposit_product.get('join_way'),
                'spcl_cnd': deposit_product.get('spcl_cnd'),
                'kor_co_nm':  deposit_product.get('kor_co_nm'),
                'save_trm_6':save_trm_6,
                'intr_rate_6': intr_rate_6,
                'save_trm_12':save_trm_12,
                'intr_rate_12':intr_rate_12,
                'save_trm_24': save_trm_24,
                'intr_rate_24':intr_rate_24, 
                'save_trm_36':save_trm_36,
                'intr_rate_36':intr_rate_36
            }

            # serializer 저장
            serializer = DepositSerializer(data=save_deposit_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    # return JsonResponse({'message':'true'})
    if request.method == 'GET':
        deposit_products = Deposit.objects.all()
        serializer = DepositSerializer(deposit_products, many=True)
    return Response(serializer.data)
    

# 적금 데이터 가져오는 함수     
@api_view(['GET', 'POST'])
def bank_list_savings(request):
    API_KEY = settings.API_KEY
    savings_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    savings_data = requests.get(savings_url).json()

    # 값이 없는 경우 '-'이 db에 저장되도록 설정한다.
    save_trm_6 = intr_rate_6 = save_trm_12 = intr_rate_12 = save_trm_24 = intr_rate_24 = save_trm_36 = intr_rate_36 = '-'
    for savings_product in savings_data.get('result').get('baseList'):

        # 이미 저장된 상품이 아닌 경우에 대해 
        fin_prdt_cd = savings_product.get('fin_prdt_cd')
        if not Savings.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():

            for savings_option in savings_data.get('result').get('optionList'):
                if savings_option.get('fin_prdt_cd') == fin_prdt_cd:
                  
                    save_trm = savings_option.get('save_trm')
                    if save_trm in ("6"):
                        save_trm_6= savings_option.get('save_trm')
                        intr_rate_6= savings_option.get('intr_rate')
                    elif save_trm in ("12"):
                        save_trm_12= savings_option.get('save_trm')
                        intr_rate_12= savings_option.get('intr_rate')
                    elif save_trm in ("24"):
                        save_trm_24= savings_option.get('save_trm')
                        intr_rate_24= savings_option.get('intr_rate')
                    elif save_trm in ("36"):
                        save_trm_36= savings_option.get('save_trm')
                        intr_rate_36= savings_option.get('intr_rate')  

            
            save_s_savings_data = {
                'fin_prdt_cd': fin_prdt_cd,
                'fin_prdt_nm': savings_product.get('fin_prdt_nm'),
                'dcls_month': savings_product.get('dcls_month'),
                'join_deny': savings_product.get('join_deny'),
                'join_way': savings_product.get('join_way'),
                'spcl_cnd': savings_product.get('spcl_cnd'),
                'kor_co_nm':savings_product.get('kor_co_nm'),
                'save_trm_6':save_trm_6,
                'intr_rate_6': intr_rate_6,
                'save_trm_12':save_trm_12,
                'intr_rate_12':intr_rate_12,
                'save_trm_24': save_trm_24,
                'intr_rate_24':intr_rate_24, 
                'save_trm_36':save_trm_36,
                'intr_rate_36':intr_rate_36
            }    
            # serializer 저장
            serializer = SavingsSerializer(data=save_s_savings_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()

    # 출력
    if request.method == 'GET':
        savings_products = Savings.objects.all()
        serializer = SavingsSerializer(savings_products, many=True)
    return Response(serializer.data)
    
    

@api_view(['GET'])
def bank_detail_deposit(request, bank_pk):
    bank_deposit = get_object_or_404(Deposit, pk=bank_pk)
    if request.method == 'GET':
        serializer = DepositSerializer(bank_deposit)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def bank_detail_savings(request, bank_pk):
    bank_savings = get_object_or_404(Savings, pk=bank_pk)
    if request.method == 'GET':
        serializer = SavingsSerializer(bank_savings)
        print(serializer.data)
        return Response(serializer.data)