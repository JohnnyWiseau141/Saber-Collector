from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello there, General Grevious, you coughdropping fudge-popper</h1>')

def about(request):
  return render(request, 'about.html')

def sabers_index(request):
  return render(request, 'sabers/index.html', { 'sabers': sabers})

class Saber:
  def __init__(self, owner, color, hilt, blades):
    self.owner = owner
    self.color = color
    self.hilt = hilt
    self.blades = blades

sabers = [
  Saber('Cal Kestis', 'blue', 'custom', 2),
  Saber('Obi-wan', 'blue', 'round-bottom', 1),
  Saber('Maul', 'red', 'long and techie', 2),
  Saber('Rey Skywalker', 'yellow', 'Black copy of Maul\'s hilt', 1),
]