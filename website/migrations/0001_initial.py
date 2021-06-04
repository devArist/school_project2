# Generated by Django 3.2.3 on 2021-06-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('subtitle', models.CharField(max_length=200, verbose_name='sous-tittre')),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name="date d'ajout")),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'a propos',
                'verbose_name_plural': 'a propos',
            },
        ),
        migrations.CreateModel(
            name='BackgroundImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name="date d'ajout")),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'image de fond',
                'verbose_name_plural': 'images de fond',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='titre')),
                ('email', models.EmailField(max_length=200, verbose_name='sous-tittre')),
                ('message', models.CharField(max_length=200)),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name="date d'ajout")),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='img')),
                ('title', models.CharField(max_length=200, verbose_name='titre')),
                ('subtitle', models.CharField(max_length=200, verbose_name='sous-tittre')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name="date d'ajout")),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name="date d'ajout")),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]