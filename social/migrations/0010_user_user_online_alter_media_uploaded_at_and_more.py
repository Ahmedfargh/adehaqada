# Generated by Django 4.1.5 on 2023-02-01 14:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0009_user_user_password_alter_media_uploaded_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_online",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="media",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 6, 57, 29, 792687)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 6, 57, 29, 792687)
            ),
        ),
    ]
