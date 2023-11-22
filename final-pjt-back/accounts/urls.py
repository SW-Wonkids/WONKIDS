from django.urls import path, include

from . import views
urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('profile/', views.getuser, name='getuser'),
] 