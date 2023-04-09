from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    friendliness = models.IntegerField()
    trainability = models.IntegerField()
    shedding_amount = models.IntegerField()
    excercise_needs = models.IntegerField()


class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', related_name='dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favourite_food = models.CharField(max_length=200)
    favourite_toy = models.CharField(max_length=200)
