# Generated by Django 4.1.2 on 2022-11-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("resume", "0002_first_bachelors_first_certificate1_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="first",
            name="photo",
            field=models.FileField(default=None, null=True, upload_to="image/"),
        ),
    ]
