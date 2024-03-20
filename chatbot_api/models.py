from django.db import models




class BotResponse(models.Model):
    response_type = models.CharField(max_length=128, null=True, blank=True)  # category
    user_input = models.CharField(max_length=128, null=True, blank=True)     # complete user input 
    bot_response = models.CharField(max_length=128, null=True, blank=True)   # what will the chatbot response
    required_words = models.CharField(max_length=128,null=True, blank=True) # user_keywords to focus

    class Meta:
        verbose_name = 'Train Data'
        verbose_name_plural = "Train Data"

    def __str__(self) -> str:
        return f"{self.id} -- {self.response_type}"
    

class DashboardImage(models.Model):
    image = models.ImageField(upload_to="dashboard_image")

    class Meta:
        verbose_name = "Dashboard Image"
        verbose_name_plural = "Dashboard Image"


class FaqsModel(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ"

    def __str__(self) -> str:
        return f"{self.id} .> {self.question}"


