# Generated by Django 5.1 on 2024-08-29 14:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="country",
            field=models.CharField(
                blank=True, default="Digital Citizen", max_length=30
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(default="User@gamers-united.com", max_length=40),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="first_name",
            field=models.CharField(default="Name", max_length=15),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="last_name",
            field=models.CharField(default="Lastname", max_length=15),
        ),
    ]