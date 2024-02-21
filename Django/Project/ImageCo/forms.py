from django import forms
from .models import ImageCoordinate

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageCoordinate
        fields = ['image']
