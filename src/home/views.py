from django.shortcuts import render, get_object_or_404
from .models import Art
from home.forms import UploadArtForm
from django.http import HttpResponseRedirect

# Create your views here.


def home_screen_view(request):
  arts_featured = Art.objects.filter(featured = True)
  return render(request,"home/home.html",{ 'arts_featured': arts_featured})
  

# def featured_art(request):
#   return render(request, 'home/featured.html', {})


def upload_art_view(request):
  submitted = False
  if request.method == "POST":
    upload_form = UploadArtForm(request.POST)
    if upload_form.is_valid():
      upload_form.save()
      print(upload_form)
      return HttpResponseRedirect('/upload_art_view/?submitted=True')
     
  else:
     upload_form = UploadArtForm()
     if 'submitted' in request.GET:
       submitted = True
  return render(request, 'upload_art.html', {'upload_form': upload_form, 'submitted': submitted})
