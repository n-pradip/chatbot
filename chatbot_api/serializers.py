from rest_framework import serializers
from .models import BotResponse,FaqsModel

class BotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotResponse
        fields = '__all__'

class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqsModel
        fields=  '__all__'

