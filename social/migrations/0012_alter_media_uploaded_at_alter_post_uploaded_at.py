# Generated by Django 4.1.5 on 2023-02-01 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0011_alter_media_uploaded_at_alter_post_uploaded_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="media",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 7, 10, 25, 950130)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 7, 10, 25, 950130)
            ),
        ),
    ]
