from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'title', 'subtitle']
    list_display_links = ['title', 'subtitle']

    def display_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
    
    display_image.short_description = 'image'


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'subtitle', 'description']
    list_display_links = ['title', 'subtitle', 'description']


@admin.register(models.BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'name']
    list_display_links = ['display_image', 'name']

    def display_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
    display_image.short_description = 'image'


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    list_display_links = ['name', 'email', 'message']