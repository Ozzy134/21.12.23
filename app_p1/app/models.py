from django.db import models

class Eat(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    namecat = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Zakaz(models.Model):
    eat = models.CharField(max_length=25)
    kolvo = models.IntegerField()
    price = models.IntegerField()
