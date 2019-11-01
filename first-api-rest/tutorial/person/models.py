from django.db import models
from rest_framework import serializers


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    married = models.BooleanField(default=False)


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age', 'gender', 'married']

