# Generated by Django 4.0.3 on 2022-03-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi_model',
            name='bmi',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='bmi_model',
            name='fat',
            field=models.TextField(),
        ),
    ]
