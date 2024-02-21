# from rest_framework import serializers
# from.models import TrainModel

# class TrainModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TrainModel
#         fields = '__all__'

from rest_framework import serializers
from .models import BotResponse

class BotResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotResponse
        fields = '__all__'


