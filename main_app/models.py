from django.db import models
from django.urls import reverse

PARTS = (
  ('I', 'Ion energy Cell'),
  ('P', 'Pressure Grip'),
  ('S', 'Stabilizing Ring')
)

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