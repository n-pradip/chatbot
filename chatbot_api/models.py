from django.db import models




class BotResponse(models.Model):
    response_type = models.CharField(max_length=128, null=True, blank=True)  # category
    user_input = models.CharField(max_length=128, null=True, blank=True)     # complete user input 
    bot_response = models.CharField(max_length=128, null=True, blank=True)   # what will the chatbot response
    required_words = models.CharField(max_length=128,null=True, blank=True) # user_keywords to focus

    def __str__(self) -> str:
        return f"{self.id} -- {self.response_type}"
