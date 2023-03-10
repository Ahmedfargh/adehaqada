# Generated by Django 4.1.5 on 2023-02-02 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0012_alter_media_uploaded_at_alter_post_uploaded_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="user_background",
            field=models.ImageField(
                default="img/users/assassins_creed-wallpaper-1920x1200.jpg",
                upload_to="img/users/",
            ),
        ),
        migrations.AlterField(
            model_name="media",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 23, 32, 51, 323799)
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="uploaded_at",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 1, 23, 32, 51, 323799)
            ),
        ),
    ]
