from django.urls import path
from accounts.views import UserAPIView

urlpatterns = [
    path('api/users/', UserAPIView.as_view(), name='user-list'),
]