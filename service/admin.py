from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'label', 'number', 'price']
    list_filter = ['label', 'number', 'price']

    def display_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width=100px height=80px>'
        )
