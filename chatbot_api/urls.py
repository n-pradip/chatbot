from django.urls import path,include
from .views import BotResponseViewSet,FaqsViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# router.register(r'train', TrainModelVeiwset, basename='train_data_input')
router.register(r'bot-responses', BotResponseViewSet, basename='bot-responses')
router.register(r'faqs', FaqsViewset, basename='frequently-asked-questions')



urlpatterns = [
    path('', include(router.urls)),
    path('formatted-bot-response/', BotResponseViewSet.as_view({'get': 'api_formatter'}), name='bot-response'),
    path('bot-response/', BotResponseViewSet.as_view({'post': 'bot_post_response'}), name='bot-response'),

]