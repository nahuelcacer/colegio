from django.db import models

# Create your models here.c

class Personal(models.Model):
    nombre = models.CharField(max_length=250)
    cbu = models.CharField(max_length=250)