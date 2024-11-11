# Generated by Django 3.2.8 on 2022-02-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ark", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ark",
            name="commitment",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="ark",
            name="metadata",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="ark",
            name="url",
            field=models.URLField(blank=True, default=""),
        ),
    ]
