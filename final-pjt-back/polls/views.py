from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import PokemonSerializer
from django.contrib.auth import get_user_model

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def polls(request):
    print('request', request)
    print('user', request.user)
    print('request.data', request.data)

    if request.method == 'GET':
        # 상위 10개를 가져오고 그 값을 적절한 비율로 넣기
        # 파이리 - 적금 10개 / 꼬부기 - 예금 10개 / 피카츄 - 적금 5개, 예금 5개
        pass

    elif request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        pokemon = request.data.get('pokemon')
        data = {'category': pokemon}
        serializer = PokemonSerializer(user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)