
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    full_name = models.CharField(max_length=100 , blank=True , null=True)
    address = models.TextField(max_length=300 , blank=True , null=True)
    country = models.CharField(max_length=100 , blank=True , null= True)
    city = models.CharField(max_length=100 , blank=True , null=True)
    zipcode = models.CharField(max_length=15 , blank=True , null= True)
    phone = models.CharField(max_length=16 , blank=True , null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"


