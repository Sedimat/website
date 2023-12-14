from django.shortcuts import render, redirect

from .forms import PhotoForm
from .models import Photo


# Create your views here.

def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery/index.html', {'photos': photos})


def upload(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')

    form = PhotoForm()
    return render(request, 'gallery/upload.html', {'form': form})