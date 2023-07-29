from django.contrib.auth.models import User
from django.db import models

### created models for questions
class Questions(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

### created models for Answers
class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

### created models for Likes
class Likes(models.Model):
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
