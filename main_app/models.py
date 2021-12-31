from django.db import models

# Create your models here.
class Saber(models.Model):
  owner = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  hilt = models.TextField(max_length=250)
  blades = models.IntegerField()

  def __str__(self):
    return self.owner