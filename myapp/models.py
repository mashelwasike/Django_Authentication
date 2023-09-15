from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Information(models.Model):
    number = models.SlugField(unique=True)
    name = models.CharField(max_length=150)
    occupation = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    age = models.PositiveIntegerField(default=0)
    thumb = models.ImageField(default='default.png')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.number
    