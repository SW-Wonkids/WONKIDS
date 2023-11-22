from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import PokemonSerializer
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def polls(request):
    print('request', request)
    print('user', request.user)
    print('request.data', request.data)

    if request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        
        if request.data.get('pokemon') == '피카츄':
            data = {'category': 0}
            serializer = PokemonSerializer(user, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        elif request.data.get('pokemon') == '파이리':
            data = {'category': 1}
            serializer = PokemonSerializer(user, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        elif request.data.get('pokemon') == '꼬부기':
            data = {'category': 2}
            serializer = PokemonSerializer(user, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)