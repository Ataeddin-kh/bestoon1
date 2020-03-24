from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expence(models.Model):
    text = models.CharField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User)
    date = models.DateTimeField()
