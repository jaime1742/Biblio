# Generated by Django 4.1.2 on 2023-11-27 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_vehiculo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]