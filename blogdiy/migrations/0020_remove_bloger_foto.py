# Generated by Django 3.1.5 on 2021-03-13 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0019_auto_20210313_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloger',
            name='foto',
        ),
    ]