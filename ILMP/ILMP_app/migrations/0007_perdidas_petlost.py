# Generated by Django 3.2.7 on 2022-10-10 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ILMP_app', '0006_auto_20221010_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='perdidas',
            name='petLost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ILMP_app.mascotas'),
        ),
    ]
