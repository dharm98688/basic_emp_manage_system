# Generated by Django 4.2.9 on 2024-01-25 13:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="phone",
            field=models.CharField(max_length=11),
        ),
    ]