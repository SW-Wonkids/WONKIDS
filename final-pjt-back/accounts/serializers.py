from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    category = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=10
    )
    age = serializers.IntegerField(required=False)
    school = serializers.CharField(
        required=False,
        allow_blank=True,
        max_length=10
    )
    grade = serializers.IntegerField(required=False)
    classnum = serializers.IntegerField(required=False)
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'category': self.validated_data.get('category', ''),
            'age': self.validated_data.get('category', ''),
            'school': self.validated_data.get('category', ''),
            'grade': self.validated_data.get('category', ''),
            'classnum': self.validated_data.get('category', ''),
        }
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user


# 추가
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'category', 'age', 'school', 'grade', 'classnum')