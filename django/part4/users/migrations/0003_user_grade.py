# Generated by Django 5.0.2 on 2024-02-15 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_is_business"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="grade",
            field=models.CharField(default="C", max_length=10),
        ),
    ]
