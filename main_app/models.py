from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PARTS = (
  ('I', 'Ion energy Cell'),
  ('P', 'Pressure Grip'),
  ('S', 'Stabilizing Ring')
)

class Crystal(models.Model):
  type = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
    return reverse('crystals_detail', kwargs={'pk': self.id})

# Create your models here.
class Saber(models.Model):
  owner = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  hilt = models.TextField(max_length=250)
  blades = models.IntegerField()
  crystals = models.ManyToManyField(Crystal)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.owner

  def get_absolute_url(self):
    return reverse('sabers_detail', kwargs={'saber_id': self.id})

  def fixed_for_today(self):
    return self.repairing_set.filter(date=date.today()).count() >= len(PARTS)

class Repairing(models.Model):
  date = models.DateField('Repair Date')
  part = models.CharField(
    max_length=1,
    choices=PARTS,
    default=PARTS[0][0]
  )

  saber = models.ForeignKey(Saber, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_part_display()} on {self.date}"

  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=250)
  saber = models.OneToOneField(Saber, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for saber_id: {self.saber_id} @{self.url}"


