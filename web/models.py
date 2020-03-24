from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expence(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
class Income(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
