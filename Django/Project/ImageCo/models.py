from django import forms
from .models import ImageCoordinate


class ImageUploadForm(forms.ModelForm):
    x_coordinate = forms.IntegerField()  # Add this line
    y_coordinate = forms.IntegerField()  # Add this line

    class Meta:
        model = ImageCoordinate
        fields = ['image', 'x_coordinate', 'y_coordinate']
