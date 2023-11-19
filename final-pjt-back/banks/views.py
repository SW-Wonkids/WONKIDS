from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
# from .serializers import PostListSerializer, CategorySerializer, PostSerializer, CommentSerializer
from .models import Deposit, Savings
# API_KEY 가져오기
from django.conf import settings


# Create your views here.
def index(request):
    pass
    


def profile(request):
    pass


def bank_list(request):
    API_KEY = settings.API_KEY



def bank_detail(request):
    pass


def bank_like(request):
    pass


def bank_map(request):
    pass


def exchange_rate(request):
    pass