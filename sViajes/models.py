from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tiempo_km = models.IntegerField(verbose_name="TiempoPorKilometro")
    precio_km = models.DecimalField(verbose_name="PrecioPorKilometro", decimal_places=2, max_digits=5)
    def __str__(self):
        return self.nombre
    

class Taxi(models.Model):
    id = models.CharField(verbose_name="Identificador", max_length=255, primary_key=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    capacidad = models.IntegerField(default=2)
    chofer = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    def __str__(self):
        return self.chofer
    

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contPer = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre    

class SViaje(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE)
    taxi = models.ForeignKey(Taxi, verbose_name="Taxi", on_delete=models.DO_NOTHING)
    reserva_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    recogida_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    destino = models.CharField(max_length=100)
    cant_personas = models.IntegerField(default=1)
    distancia = models.DecimalField(max_digits=6, decimal_places=2)
    completado = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.recogidaDate} {self.destino}"
