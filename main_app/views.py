from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Saber
from .forms import RepairingForm


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def sabers_index(request):
  sabers = Saber.objects.all()
  return render(request, 'sabers/index.html', { 'sabers': sabers })

def sabers_detail(request, saber_id):
  saber = Saber.objects.get(id=saber_id)
  repairing_form = RepairingForm()
  return render(request, 'sabers/detail.html', {
    'saber': saber, 'repairing_form': repairing_form
  })

def add_repairing(request, saber_id):
  form = RepairingForm(request.POST)
  if form.is_valid():
    new_repairing = form.save(commit=False)
    new_repairing.saber_id = saber_id
    new_repairing.save()
  return redirect('sabers_detail', saber_id=saber_id)

class SaberCreate(CreateView):
  model = Saber
  fields = '__all__'

class SaberUpdate(UpdateView):
  model = Saber
  fields = ['color', 'hilt', 'blades']

class SaberDelete(DeleteView):
  model = Saber
  success_url = '/sabers/'