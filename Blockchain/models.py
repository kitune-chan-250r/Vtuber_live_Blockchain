from django.db import models

# Create your models here.

class Transaction(models.Model):
    liver = models.CharField(max_length=999, primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    startdatetime = models.CharField(max_length=100)
    stream_url = models.CharField(max_length=100)
    onair = models.BooleanField()
    audience = models.IntegerField()

class Chain(models.Model):
	index = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True)
	transactions = models.TextField()
	previous_hash = models.TextField()