# Generated by Django 4.2.6 on 2023-12-07 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sViajes', '0006_factura_viajefactura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='viajefactura',
            name='factura',
        ),
        migrations.RemoveField(
            model_name='viajefactura',
            name='viaje',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='ViajeFactura',
        ),
    ]