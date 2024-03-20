import requests
import re
import random
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import BotResponse, FaqsModel
from .serializers import BotResponseSerializer, FaqsSerializer

class BotResponseViewSet(viewsets.ModelViewSet):
    queryset = BotResponse.objects.all()
    serializer_class = BotResponseSerializer

    @action(detail=False, methods=['get'])
    def api_formatter(self, request):
        response_data = []
        queryset = self.get_queryset()

        for instance in queryset:
            user_input = instance.user_input
            if user_input:
                user_input_list = [word.strip() for word in user_input.split(',') if word.strip()]
            else:
                user_input_list = []

            response_dict = {
                'id': instance.id,
                'response_type': instance.response_type,
                'user_input': user_input_list,
                'bot_response': instance.bot_response,
                'required_words': instance.required_words.split(',') if instance.required_words else []
            }
            response_data.append(response_dict)

        return Response(response_data, status=status.HTTP_200_OK)

    @staticmethod
    def random_string():
        random_list = [
            "Please try writing something more descriptive.",
            "Oh! It appears you wrote something I don't understand yet",
            "Do you mind trying to rephrase that?",
            "I'm terribly sorry, I didn't quite catch that.",
            "I can't answer that yet, please try asking something else."
        ]
        return random.choice(random_list)

    @action(detail=False, methods=['POST'])
    def bot_post_response(self, request, *args, **kwargs):
        input_string = request.data.get("input_string")  # Accessing data using request.data
        
        if input_string.lower() == 'what':
            return Response("Please complete the question", status=status.HTTP_200_OK)

        split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
        score_list = []

        response_data = self.api_formatter(request)  # Utilizing the api_formatter method to get response data

        for response in response_data.data:  # Accessing the data attribute of the Response object
            response_score = 0
            required_score = 0
            required_words = response["required_words"]

            if required_words:
                for word in split_message:
                    if word in required_words:
                        required_score += 1

            if required_score == len(required_words):
                for word in split_message:
                    if word in response["user_input"]:
                        response_score += 1

            score_list.append(response_score)

        best_response = max(score_list)
        response_index = score_list.index(best_response)

        if best_response != 0:
            return Response(response_data.data[response_index]["bot_response"], status=status.HTTP_200_OK)

        return Response(self.random_string(), status=status.HTTP_200_OK)
    
class FaqsViewset(viewsets.ModelViewSet):
    queryset = FaqsModel.objects.all()
    serializer_class = FaqsSerializer