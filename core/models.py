from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expression = models.CharField(max_length=500)
    result = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.user} - {self.expression} - {self.result}'
