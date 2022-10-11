from django.db import models

# Create your models here.
class userFrom(models.Model):
    username = models.CharField(max_length=50,  unique=True)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Quotes(models.Model):
    user =models.ForeignKey('userFrom', on_delete=models.PROTECT)
    quotes = models.TextField()