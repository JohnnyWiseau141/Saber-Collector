from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Saber, Crystal
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
  crystals_saber_doesnt_have = Crystal.objects.exclude(id__in = saber.crystals.all().values_list('id'))
  repairing_form = RepairingForm()
  return render(request, 'sabers/detail.html', {
    'saber': saber, 'repairing_form': repairing_form, 'crystals': crystals_saber_doesnt_have
  })

def add_repairing(request, saber_id):
  form = RepairingForm(request.POST)
  if form.is_valid():
    new_repairing = form.save(commit=False)
    new_repairing.saber_id = saber_id
    new_repairing.save()
  return redirect('sabers_detail', saber_id=saber_id)

def assoc_crystal(request, saber_id, crystal_id):
  Saber.objects.get(id=saber_id).crystals.add(crystal_id)
  return redirect('sabers_detail', saber_id=saber_id)

class SaberCreate(CreateView):
  model = Saber
  fields = ['owner', 'color', 'hilt', 'blades']

class SaberUpdate(UpdateView):
  model = Saber
  fields = ['color', 'hilt', 'blades']

class SaberDelete(DeleteView):
  model = Saber
  success_url = '/sabers/'

class CrystalCreate(CreateView):
  model = Crystal
  fields = '__all__'

class CrystalList(ListView):
  model = Crystal

class CrystalDetail(DetailView):
  model = Crystal

class CrystalUpdate(UpdateView):
  model = Crystal
  fields = ['type', 'color']

class CrystalDelete(DeleteView):
  model = Crystal
  success_url = '/crystals/'