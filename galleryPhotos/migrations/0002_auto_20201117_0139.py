# Generated by Django 3.1.3 on 2020-11-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryPhotos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='imageDescription',
            field=models.CharField(max_length=450),
        ),
    ]
