from django.shortcuts import render
from .models import Art
# Create your views here.


def home_screen_view(request):
  arts_featured = Art.objects.filter(featured = True)
  return render(request,"home/home.html",{ 'arts_featured': arts_featured})
  

# def featured_art(request):
#   return render(request, 'home/featured.html', {})