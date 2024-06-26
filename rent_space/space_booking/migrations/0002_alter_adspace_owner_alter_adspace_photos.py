# Generated by Django 5.0.3 on 2024-03-27 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space_booking', '0001_initial'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adspace',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spaces_owned', to='user_management.user'),
        ),
        migrations.AlterField(
            model_name='adspace',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
