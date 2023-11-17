from django.urls import path
from . import views


urlpatterns = [
    path('/', views.index),
    path('profile/', views.index),
    path('bank/', views.bank_list),
    path('bank/<int:bank_pk>/', views.bank_detail),
    path('bank/<int:bank_pk>/like/', views.bank_like),
    path('bank/map/', views.bank_map),
    path('bank/exchange_rate/', views.exchange_rate),
]