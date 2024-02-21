# from django.urls import path
# from . import views
# urlpatterns=[
#     path('',views.home, name="home"),
#     path('add', views.add, name="add")
# ]


# registration/urls.py
from django.urls import path
from .views import registration_view

urlpatterns = [
    path('register1/', registration_view, name='registration_view'),
    # Add other paths as needed
]
