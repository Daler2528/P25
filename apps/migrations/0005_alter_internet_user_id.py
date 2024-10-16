# Generated by Django 5.1.2 on 2024-10-13 17:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_internet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internet',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internet_profiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
