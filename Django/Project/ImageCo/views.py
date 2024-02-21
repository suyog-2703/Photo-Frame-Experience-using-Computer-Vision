import cv2
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm
from .models import ImageCoordinate  # noqa

def get_coordinates_from_image(image):
    # Placeholder function, replace with your actual logic to extract coordinates from the image
    # Example: Using OpenCV to get the center coordinates
    img = cv2.imread(image.path)
    height, width, _ = img.shape
    x_coordinate, y_coordinate = width // 2, height // 2
    return x_coordinate, y_coordinate

def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Get x_coordinate and y_coordinate from OpenCV or other logic
            x_coordinate, y_coordinate = get_coordinates_from_image(form.cleaned_data['image'])

            instance = form.save(commit=False)
            instance.x_coordinate = x_coordinate
            instance.y_coordinate = y_coordinate
            instance.save()

            return HttpResponseRedirect('success-url')  # Replace with your success URL
    else:
        form = ImageUploadForm()

    return render(request, 'file_upload.html', {'form': form})
