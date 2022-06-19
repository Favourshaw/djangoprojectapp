from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

Shawghost = get_user_model()
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(Shawghost, on_delete=models.CASCADE, default="title")
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
