from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_a = models.CharField(max_length =100)
    option_b = models.CharField(max_length =100)
    option_c = models.CharField(max_length =100)
    option_d = models.CharField(max_length =100)
    score_a= models.IntegerField()
    score_b = models.IntegerField()
    score_c = models.IntegerField()
    score_d = models.IntegerField()

    def __str__(self):
        return self.question_text
    
class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)

    def __str__(self):
        return f"User {self.user_id} - {self.question.question_text} ({self.selected_option})"
    

class CreditScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.user_id} - Score: {self.score}"



