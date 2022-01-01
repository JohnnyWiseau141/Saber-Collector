from django.forms import ModelForm
from .models import Repairing

class RepairingForm(ModelForm):
  class Meta:
    model = Repairing
    fields = ['date', 'part']