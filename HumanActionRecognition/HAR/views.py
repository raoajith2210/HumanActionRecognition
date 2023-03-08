from django.shortcuts import render

# Create your views here.

def camera_view(request):
    return render(request, 'camera.html')