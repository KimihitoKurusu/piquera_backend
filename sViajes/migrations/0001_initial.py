# Generated by Django 4.2.6 on 2023-11-29 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contPer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sViajes.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tiempoKm', models.IntegerField(verbose_name='TiempoPorKilometro')),
                ('precioKM', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='PrecioPorKilometro')),
            ],
        ),
        migrations.CreateModel(
            name='SViaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservaDate', models.DateTimeField()),
                ('recogidaDate', models.DateTimeField()),
                ('destino', models.CharField(max_length=100)),
                ('cantPersonas', models.IntegerField(default=1)),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=6)),
                ('completado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sViajes.cliente', verbose_name='Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ViajeFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sViajes.factura', verbose_name='Factura')),
                ('viaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sViajes.sviaje', verbose_name='Viaje')),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Identificador')),
                ('capacidad', models.IntegerField(default=2)),
                ('chofer', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=1)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sViajes.marca')),
            ],
        ),
        migrations.AddField(
            model_name='sviaje',
            name='taxi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sViajes.taxi', verbose_name='Taxi'),
        ),
    ]
