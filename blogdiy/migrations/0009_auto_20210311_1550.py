# Generated by Django 3.1.5 on 2021-03-11 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogdiy', '0008_auto_20210311_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='who',
        ),
        migrations.AddField(
            model_name='like',
            name='who',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
