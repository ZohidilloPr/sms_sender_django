from django.db import models

# Create your models here.

class ConfirmPassword(models.Model):
    phone = models.CharField(max_length=9)
    sms_code = models.IntegerField()
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone