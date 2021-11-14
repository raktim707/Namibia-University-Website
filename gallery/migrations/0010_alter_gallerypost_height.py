# Generated by Django 3.2.8 on 2021-11-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_alter_gallerypost_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerypost',
            name='height',
            field=models.CharField(choices=[('col-sm-4', 'col-sm-4'), ('col-sm-8', 'col-sm-8')], default='col-sm-4', max_length=10),
        ),
    ]