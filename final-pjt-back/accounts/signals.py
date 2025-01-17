# 모든 사용자가 자동으로 생성된 토큰을 가지도록 하는 역할
# DRF 공식문서에서 이렇게 코드를 쓰라고 제공함

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
