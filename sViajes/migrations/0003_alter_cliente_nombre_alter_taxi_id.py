# Generated by Django 4.2.6 on 2023-12-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sViajes', '0002_rename_preciokm_marca_precio_km_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taxi',
            name='id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Identificador'),
        ),
    ]
