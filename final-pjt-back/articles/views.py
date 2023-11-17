from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .serializers import PostListSerializer, CategorySerializer, PostSerializer, CommentSerializer
from .models import Category, Article, Comment

# Create your views here.
def article_list(request):
    pass


def article_detail(request):
    pass


def comments(request):
    pass