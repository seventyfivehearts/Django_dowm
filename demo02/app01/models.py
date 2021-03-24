
from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender_choices = (
        (1, 'male'),
        (2, 'female'),
        (3, 'others'),
    )
    gender = models.IntegerField(choices=gender_choices)


class Book(models.Model):
    title = models.CharField(max_length=32)
