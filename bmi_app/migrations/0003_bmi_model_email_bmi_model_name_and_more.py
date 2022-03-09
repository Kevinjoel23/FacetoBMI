# Generated by Django 4.0.3 on 2022-03-09 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmi_app', '0002_alter_bmi_model_bmi_alter_bmi_model_fat'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmi_model',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bmi_model',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bmi_model',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
