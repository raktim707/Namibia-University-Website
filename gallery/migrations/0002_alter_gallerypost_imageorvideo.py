# Generated by Django 3.2.8 on 2021-11-12 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='ImageOrVideo',
            field=models.FileField(upload_to='gallery/uploads', verbose_name='ImageOrVideo'),
        ),
    ]