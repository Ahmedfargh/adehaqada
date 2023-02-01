# Generated by Django 4.1.5 on 2023-02-01 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("social", "0011_alter_media_uploaded_at_alter_post_uploaded_at"),
        ("personality", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="work_education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("work_name", models.CharField(max_length=50)),
                (
                    "worker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="social.user"
                    ),
                ),
            ],
        ),
    ]