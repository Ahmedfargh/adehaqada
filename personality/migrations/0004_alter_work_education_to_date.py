# Generated by Django 4.1.5 on 2023-02-02 07:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("personality", "0003_work_education_from_date_work_education_to_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="work_education",
            name="to_date",
            field=models.DateField(
                default=datetime.datetime(2023, 2, 1, 23, 32, 51, 323799)
            ),
        ),
    ]
