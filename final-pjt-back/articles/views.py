from django.shortcuts import render
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import ArticleListSerializer, CategorySerializer, ArticleSerializer, CommentSerializer
from .models import Category, Article, Comment
# authentication_class 데코레이터 사용
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

# Create your views here.
@authentication_classes([TokenAuthentication, BasicAuthentication])
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializers = ArticleListSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        # pokemon = Category.objects.get(pk=request.data.get('pokemon'))
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


def article_detail(request):
    pass


def comments(request):
    pass