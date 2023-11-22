from django.urls import path, include
from accounts.views import UserAPIView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('profile/', UserAPIView.as_view(), name='user-list'),
] 