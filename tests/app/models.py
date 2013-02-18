from django.db import models
from filefieldtools import upload_to


class Phone1(models.Model):
    title = models.CharField(max_length=100)
    price = models.FileField(upload_to=upload_to('phones/prices'))


class Phone2(models.Model):
    title = models.CharField(max_length=100)
    price = models.FileField(upload_to=upload_to('phones/prices', field_name='price'))