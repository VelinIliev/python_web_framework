# Generated by Django 4.2.1 on 2023-06-15 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web_tools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.AddField(
            model_name='employees',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
