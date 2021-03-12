# Generated by Django 3.1.5 on 2021-03-02 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogdiy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author_comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogdiy.bloger', verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='to_blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogdiy.blog', verbose_name='Для статьи'),
        ),
    ]
