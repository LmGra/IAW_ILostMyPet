# Generated by Django 3.2.7 on 2022-10-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ILMP_app', '0009_auto_20221013_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuentros',
            name='genderFind',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
