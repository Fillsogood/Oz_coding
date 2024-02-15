from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    #models.Model
    # name = models.CharField(max_length=20)
    # description =models.TextField()
    # age = models.PositiveIntegerField(null=True)
    # gender = models.CharField(max_length=5)

    # def __str__(self):
    #     return self.name
    is_business = models.BooleanField(default=False)
    grade = models.CharField(max_length=10,default = "C")
    
    