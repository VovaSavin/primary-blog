# Generated by Django 3.1.5 on 2021-05-22 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0031_auto_20210516_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloger',
            options={'permissions': (('only_superuser', 'Send message to mail'),), 'verbose_name': 'Блоггер', 'verbose_name_plural': 'Блоггеры'},
        ),
    ]
