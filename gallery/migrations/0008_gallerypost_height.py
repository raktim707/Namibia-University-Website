# Generated by Django 3.2.8 on 2021-11-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_alter_gallerypost_imageorvideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerypost',
            name='height',
            field=models.IntegerField(default=300),
        ),
    ]