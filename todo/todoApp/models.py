from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class todo(models.Model):
    title=models.CharField(max_length=30)
    desc=models.TextField()
    date=models.DateTimeField(auto_now=True)
    User= models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title