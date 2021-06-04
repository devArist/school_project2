from os import name
from django.db import models

# Create your models here.
class Slider(models.Model):
    image = models.FileField(upload_to='img')
    title = models.CharField(
        max_length=200, 
        verbose_name='titre'
        )
    subtitle = models.CharField(
        max_length=200, 
        verbose_name='sous-tittre'
        )
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    date_update = models.DateTimeField(auto_now=True, verbose_name="date d'ajout")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class About(models.Model):
    icon = models.CharField(max_length=200)
    title = models.CharField(
        max_length=200, 
        verbose_name='titre'
        )
    subtitle = models.CharField(
        max_length=200, 
        verbose_name='sous-tittre'
        )
    description = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    date_update = models.DateTimeField(auto_now=True, verbose_name="date d'ajout")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'a propos'
        verbose_name_plural = 'a propos'


class BackgroundImage(models.Model):
    CHOICES = (
        ('about_bg', 'la page about'),
        ('gallery_bg', 'la page gallerie'),
        ('contact_bg', 'la page contact'),
    )
    image = models.FileField(upload_to='img', verbose_name='image de fond')
    name = models.CharField(
        max_length=100, 
        choices=CHOICES, 
        verbose_name='Pour qelle page ?',
        null=True
        )
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    date_update = models.DateTimeField(auto_now=True, verbose_name="date d'ajout")
    status = models.BooleanField(default=True)

    def __str__(self):
        return 'image de fond'

    class Meta:
        verbose_name = 'image de fond'
        verbose_name_plural = 'images de fond'


class Contact(models.Model):
    name = models.CharField(
        max_length=200, 
        verbose_name='titre'
        )
    email = models.EmailField(
        max_length=200, 
        verbose_name='sous-tittre'
        )
    message = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    date_update = models.DateTimeField(auto_now=True, verbose_name="date d'ajout")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name