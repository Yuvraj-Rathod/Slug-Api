from django.db import models

class Demo_Model(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

