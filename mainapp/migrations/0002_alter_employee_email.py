# Generated by Django 4.1.2 on 2023-03-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email",
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
