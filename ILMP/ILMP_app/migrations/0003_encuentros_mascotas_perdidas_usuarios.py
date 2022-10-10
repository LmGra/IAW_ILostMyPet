# Generated by Django 3.2.7 on 2022-10-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ILMP_app', '0002_auto_20221005_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuentros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFind', models.CharField(max_length=200)),
                ('typeFind', models.CharField(max_length=200)),
                ('genderFind', models.CharField(max_length=200)),
                ('ubiFind', models.CharField(max_length=200)),
                ('infoFind', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPet', models.CharField(max_length=200)),
                ('namePet', models.CharField(max_length=200)),
                ('infoPet', models.CharField(max_length=200)),
                ('datePet', models.CharField(max_length=200)),
                ('typePet', models.CharField(max_length=200)),
                ('imgPet', models.CharField(max_length=200)),
                ('genderPet', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Perdidas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLost', models.CharField(max_length=200)),
                ('infoLost', models.CharField(max_length=200)),
                ('dateLost', models.CharField(max_length=200)),
                ('ubiLost', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsr', models.CharField(max_length=200)),
                ('nameUsr', models.CharField(max_length=200)),
                ('passUsr', models.CharField(max_length=200)),
                ('ubiUsr', models.CharField(max_length=200)),
                ('mailUsr', models.CharField(max_length=200)),
                ('tlfUsr', models.CharField(max_length=200)),
            ],
        ),
    ]
