# Generated by Django 3.2.8 on 2021-11-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField()),
                ('occupation', models.TextField()),
                ('organization', models.TextField()),
                ('suburb', models.TextField()),
                ('address', models.CharField(default='-', max_length=50)),
                ('sptell', models.CharField(default='-', max_length=15)),
                ('spimage', models.TextField(default='-')),
            ],
        ),
    ]
