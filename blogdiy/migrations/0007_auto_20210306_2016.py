# Generated by Django 3.1.5 on 2021-03-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0006_auto_20210302_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloger',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Возвраст'),
        ),
        migrations.AlterField(
            model_name='bloger',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='bloger',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
    ]
