from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    married = models.BooleanField(default=False)
