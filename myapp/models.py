from django.db import models

# Create your models here.

class ShagufTask(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    revenue = models.IntegerField(default=0)


