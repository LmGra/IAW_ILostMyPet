# Generated by Django 3.2.7 on 2022-10-05 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ILMP_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
