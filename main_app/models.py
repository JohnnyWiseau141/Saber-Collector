from django.db import models
from django.urls import reverse

# Create your models here.
class Saber(models.Model):
  owner = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  hilt = models.TextField(max_length=250)
  blades = models.IntegerField()

  def __str__(self):
    return self.owner

  def get_absolute_url(self):
    return reverse('sabers_detail', kwargs={'saber_id': self.id})