# Generated by Django 4.1.7 on 2024-11-14 20:48

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=cloudinary.models.CloudinaryField(
                blank=True,
                default="https://res.cloudinary.com/dqk6ad4tr/image/upload/v1731314077/default_profile_picture_d3apgy.png",
                max_length=255,
                null=True,
                verbose_name="image",
            ),
        ),
    ]
