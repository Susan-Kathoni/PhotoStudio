# Generated by Django 3.1.3 on 2020-11-17 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryPhotos', '0003_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
    ]
