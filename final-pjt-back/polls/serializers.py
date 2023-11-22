from rest_framework import serializers
from django.contrib.auth import get_user_model

class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('category', )