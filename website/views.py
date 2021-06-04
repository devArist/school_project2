from django.shortcuts import render
from . import models
from service import models as service_models
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def checkup(request):
    success = True
    text = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')

        if email.isspace() or email == '' or name.isspace() or name == '' or message.isspace() or message == '':
            success = False
            text = 'Veuillez remplir les champs vides'
        elif not re.fullmatch('(\w\.?)+@(\w\.?)+\.[A-Za-z]{2,3}', email):
            success = False
            text = 'Veuillez saisir un email valide'
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", name):
            success = False
            text = 'Veuillez saisir un nom valide'
        else:
            contact = models.Contact(name=name, message=message, email=email)
            contact.save()
            text = 'Votre message a bien été enregistré'

    datas = {
        'success':success,
        'text':text
    }

    return JsonResponse(datas, safe=False)
