from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    token =models.CharField(max_length=48)
    def __str__(self):
        return "{}-token".format(self.user)
class Expence(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)
class Income(models.Model):
    text = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    def __str__(self):
        return "{}-{}".format(self.date,self.amount)
