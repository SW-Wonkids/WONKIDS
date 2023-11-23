from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import PokemonSerializer
from django.contrib.auth import get_user_model

from banks.models import Deposit
from banks.models import Savings

from banks.serializers import DepositSerializer
from banks.serializers import SavingsSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def polls(request):
    if request.method == 'GET':
        user = get_object_or_404(get_user_model(), username=request.user)
        if user.category == '파이리':
            data = Savings.objects.order_by('?')[:4]
            serializer = SavingsSerializer(data, many=True)

            data = {
                'deposits': 'null',
                'savings':serializer.data,
            }
            return Response(data)
        
        elif user.category == '피카츄':
            data1 = Deposit.objects.order_by('?')[:2]
            data2 = Savings.objects.order_by('?')[:2]
            serializer1 = DepositSerializer(data1, many=True)
            serializer2 = SavingsSerializer(data2, many=True)

            data = {
                'deposits':serializer1.data,
                'savings':serializer2.data,
            }
            return Response(data)

        elif user.category == '꼬부기':
            data = Deposit.objects.order_by('?')[:4]
            serializer = DepositSerializer(data, many=True)

            data = {
                'deposits': serializer.data,
                'savings': 'null',
            }
            return Response(data)

        elif user.category == None:
            data = {
                'deposit': 'null',
                'savings': 'null'
            }
            return Response(data)


    elif request.method == 'POST':
        user = get_object_or_404(get_user_model(), username=request.user)
        pokemon = request.data.get('pokemon')
        data = {'category': pokemon}
        serializer = PokemonSerializer(user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)