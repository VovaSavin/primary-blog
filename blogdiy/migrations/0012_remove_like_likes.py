# Generated by Django 3.1.5 on 2021-03-11 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0011_auto_20210311_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='likes',
        ),
    ]
