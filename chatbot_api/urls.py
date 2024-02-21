from django.urls import path,include
from .views import BotResponseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'train', TrainModelVeiwset, basename='train_data_input')
router.register(r'bot-responses', BotResponseViewSet, basename='bot-responses')


urlpatterns = [
    path('', include(router.urls)),
    path('formatted-bot-response/', BotResponseViewSet.as_view({'get': 'api_formatter'}), name='bot-response'),
    path('bot-response/', BotResponseViewSet.as_view({'post': 'bot_post_response'}), name='bot-response'),

]