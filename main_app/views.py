from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Saber, Crystal, Photo
from .forms import RepairingForm
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'saber-collection-141'

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

def add_photo(request, saber_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
		# uuid.uuid4().hex generates a random hexadecimal Universally Unique Identifier
    # Add on the file extension using photo_file.name[photo_file.name.rfind('.'):]
    key = uuid.uuid4().hex + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to saber_id or saber (if you have a saber object)
      photo = Photo(url=url, saber_id=saber_id)
      # Remove old photo if it exists
      saber_photo = Photo.objects.filter(saber_id=saber_id)
      if saber_photo.first():
        saber_photo.first().delete()
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('sabers_detail', saber_id=saber_id)