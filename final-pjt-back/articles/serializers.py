from rest_framework import serializers
from .models import Category, Article, Comment
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    pokemon = CategorySerializer(read_only=True)
    class Meta:
        model = Article
        fields = ('pk', 'title', 'pokemon',)
        read_only_fields = ('user', )


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    pokemon = CategorySerializer(read_only=True)
    
    class CommentSerialzer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = '__all__'
            read_only_fields = ('user',)

    comment_set = CommentSerialzer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', )

        
class CommentSerializer(serializers.ModelSerializer):
    article = ArticleListSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)