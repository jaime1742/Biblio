# Generated by Django 4.2.7 on 2023-11-19 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_perfilusuario_reviews_perfilusuario_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilusuario',
            name='reviews',
        ),
        migrations.AddField(
            model_name='perfilusuario',
            name='reviews',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.reseña'),
        ),
    ]
