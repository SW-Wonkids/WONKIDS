from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('profile/', views.index),
    path('bank_deposit/', views.bank_list_deposit),
    path('bank_savings/', views.bank_list_savings),
    # path('bank_deposit/<int:bank_pk>/', views.bank_detail_deposit),
    # path('bank_savings/<int:bank_pk>/', views.bank_detail_savings),
    path('bank_deposit/<int:bank_pk>/like/', views.bank_like_deposit),
    path('bank_savings/<int:bank_pk>/like/', views.bank_like_savings),
    path('bank/map/', views.bank_map),
    path('bank/exchange_rate/', views.exchange_rate),
]