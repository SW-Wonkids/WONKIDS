from django.urls import path
from . import views


urlpatterns = [
    path('bank_deposit/', views.bank_list_deposit),  # 정기예금 데이터 출력
    path('bank_savings/', views.bank_list_savings),  # 적금 데이터 출력 
    path('bank_deposit/<int:bank_pk>/', views.bank_detail_deposit),
    path('bank_savings/<int:bank_pk>/', views.bank_detail_savings),
]