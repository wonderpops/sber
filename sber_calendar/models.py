from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   sub_code = models.CharField(verbose_name="Код подразделения", max_length=100)
   position = models.CharField(verbose_name="Должность", max_length=100)