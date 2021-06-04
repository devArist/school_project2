from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.FileField(upload_to='img')
    label = models.CharField(
        max_length=200, 
        verbose_name='titre'
        )
    price = models.FloatField(verbose_name='prix')
    number = models.IntegerField(verbose_name='numéro')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")
    date_update = models.DateTimeField(auto_now=True, verbose_name="date d'ajout")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.label
    
    class Meta:
        verbose_name = 'gallerie'