# Generated by Django 3.0 on 2021-12-05 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oc_lettings_site', '0002_auto_20211205_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oc_lettings_site_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
