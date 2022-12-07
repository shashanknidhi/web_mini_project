# Generated by Django 4.1.4 on 2022-12-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patients",
            fields=[
                (
                    "name",
                    models.CharField(max_length=255, primary_key=True, serialize=False),
                ),
                ("contactno", models.CharField(max_length=10)),
                ("age", models.CharField(max_length=2)),
                ("reason", models.CharField(max_length=255)),
            ],
        ),
    ]
