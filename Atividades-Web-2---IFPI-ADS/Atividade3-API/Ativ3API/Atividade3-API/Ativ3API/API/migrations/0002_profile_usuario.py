# Generated by Django 2.2.3 on 2019-11-17 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='usuario',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
