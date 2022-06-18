from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Question(models.Model):
    userid = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.TextField(blank=True, null=True, max_length=1000)

class Company(models.Model):
    userid = models.IntegerField()
    company_name = models.CharField(max_length=100)

class ES(models.Model):
    userid = models.IntegerField()
    company_id  = models.IntegerField()
    question = models.CharField(max_length=100)
    answer = models.TextField(blank=True, null=True, max_length=1000)