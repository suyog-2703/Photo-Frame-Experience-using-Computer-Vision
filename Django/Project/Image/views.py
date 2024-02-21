from django.shortcuts import render, redirect
from .forms import ImageUploadForm

def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_upload_success')
    else:
        form = ImageUploadForm()

    return render(request, 'image_upload.html', {'form': form})

def image_upload_success(request):
    return render(request, 'image_upload_success.html')
