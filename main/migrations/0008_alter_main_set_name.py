# Generated by Django 3.2.8 on 2021-10-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211023_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=30),
        ),
    ]
