# Generated by Django 3.1.3 on 2020-11-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryPhotos', '0002_auto_20201117_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='images', upload_to='images/'),
        ),
    ]