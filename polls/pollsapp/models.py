from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="questions")
    question_text = models.CharField(max_length=200)


    def __str__(self) ->str:
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answers")
    answer_text = models.CharField(max_length=200)
    count  = models.IntegerField(default = 0)

    def __str__(self) ->str:
        return self.answer_text

