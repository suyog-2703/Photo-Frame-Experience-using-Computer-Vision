from django.urls import path
from .views import image_upload, image_upload_success

urlpatterns = [
    path('upload/', image_upload, name='image_upload'),
    path('upload/success/', image_upload_success, name='image_upload_success'),
]
