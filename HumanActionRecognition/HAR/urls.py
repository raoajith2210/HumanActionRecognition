from django.urls import path
from .views import camera_view

urlpatterns = [
    path('', camera_view, name='camera_view'),
]
