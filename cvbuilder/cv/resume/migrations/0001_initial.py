# Generated by Django 4.1.2 on 2022-11-21 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="First",
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
                ("name", models.CharField(max_length=20, null=True)),
                ("profession", models.CharField(max_length=20, null=True)),
                ("aboutyou", models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
