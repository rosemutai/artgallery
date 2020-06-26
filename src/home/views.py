from django.shortcuts import render
from .models import Art
# Create your views here.


def home_screen_view(request):
  context = {}

  return render(request,"home/home.html")

def featured_art(request):
  arts_featured = Art.objects.filter(featured = True)
  return render(request, 'home/snippets/featured.html', {'arts_featured': arts_featured})