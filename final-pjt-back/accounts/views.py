from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET'])
def getuser(request):
  user = get_object_or_404(get_user_model(), username=request.user)
  serializer = CustomUserSerializer(user)
  return Response(serializer.data, status=status.HTTP_200_OK) 
