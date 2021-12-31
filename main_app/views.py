from django.shortcuts import render
from .models import Saber


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
  return render(request, 'sabers/detail.html', { 'saber': saber })