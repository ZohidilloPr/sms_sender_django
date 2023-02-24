from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.

class Phone(models.Model):
    phone = models.CharField(max_length=9, null=True, blank=True, unique=True)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=9, null=True, blank=True, unique=True)
    validate_code = models.IntegerField(default=0)  
    validate = models.BooleanField(default=False)  
    objects = BaseUserManager() 