from django import forms
from django.forms import ModelForm
from .models import Art

class UploadArtForm(forms.ModelForm):
    class Meta:
        model =  Art
        fields =  ('title', 'category', 'image', 'price', 'image')