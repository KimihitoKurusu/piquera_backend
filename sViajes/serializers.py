from rest_framework import serializers

from .models import Marca, Taxi, Cliente, SViaje, Factura, ViajeFactura

class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'

class TaxiSerializer(serializers.ModelSerializer):

    marca_id = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all())

    class Meta:
        model = Taxi
        fields = ['id', 'marca_id', 'capacidad', 'chofer', 'estado']

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

class SViajeSerializer(serializers.ModelSerializer):

    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    taxi = serializers.PrimaryKeyRelatedField(queryset=Taxi.objects.all())

    class Meta:
        model = SViaje
        fields = [
            'cliente',
            'taxi',
            'reserva_date',
            'recogida_date',
            'destino',
            'cant_personas',
            'distancia',
            'completado'
            ]
