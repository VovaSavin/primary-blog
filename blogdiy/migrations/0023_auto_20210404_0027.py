# Generated by Django 3.1.5 on 2021-04-03 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0022_blog_picture_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='picture_blog',
            field=models.ImageField(default='photo_blog/no-foto.png', upload_to='photo_blog/', verbose_name='Изображение'),
        ),
    ]
