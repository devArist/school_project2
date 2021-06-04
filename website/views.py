from django.shortcuts import render
from . import models
from service import models as service_models

# Create your views here.
def home(request):
    sliders = models.Slider.objects.filter(status=True)
    about = models.About.objects.filter(status=True)
    about_bg = models.BackgroundImage.objects.filter(
        name='about bg', 
        status=True).first()
    gallery_bg = models.BackgroundImage.objects.filter(
        name='gallery bg', 
        status=True).first()
    contact_bg = models.BackgroundImage.objects.filter(
        name='contact bg',
        status=True).first()
    galleries = service_models.Gallery.objects.filter(status=True)
    return render(request, 'index.html', locals())