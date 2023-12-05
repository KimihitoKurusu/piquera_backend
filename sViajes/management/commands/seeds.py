import random
import uuid
from faker import Faker
from django.core.management.base import BaseCommand
from sViajes.models import Marca, Taxi, Cliente, SViaje, Factura, ViajeFactura

fake = Faker()

class Command(BaseCommand):
    help = 'Seed data for myapp models'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding data...'))

        # Seed data for Marca model
        for _ in range(10):
            Marca.objects.create(
                nombre=fake.word(),
                tiempo_km=random.randint(1, 100),
                precio_km=random.uniform(1, 100)
            )

        # Seed data for Taxi model
        marcas = Marca.objects.all()
        for _ in range(10):
            Taxi.objects.create(
                id=uuid.uuid4(),
                marca=random.choice(marcas),
                capacidad=random.randint(1, 5),
                chofer=fake.name(),
                estado=random.choice(['A', 'B', 'C'])
            )

        # Seed data for Cliente model
        for _ in range(10):
            Cliente.objects.create(
                nombre=fake.name(),
                contPer=random.choice([True, False])
            )

        # Seed data for SViaje model
        taxis = Taxi.objects.all()
        clientes = Cliente.objects.all()
        for _ in range(10):
            SViaje.objects.create(
                cliente=random.choice(clientes),
                taxi=random.choice(taxis),
                reserva_date=fake.date_time_this_decade(),
                recogida_date=fake.date_time_this_decade(),
                destino=fake.word(),
                cant_personas=random.randint(1, 5),
                distancia=random.uniform(1, 100),
                completado=random.choice([True, False])
            )

        # Seed data for Factura model
        for _ in range(10):
            Factura.objects.create(
                cliente=random.choice(clientes),
                date=fake.date_this_decade(),
                precio=random.uniform(1, 100)
            )

        # Seed data for ViajeFactura model
        viajes = SViaje.objects.all()
        facturas = Factura.objects.all()
        for _ in range(10):
            ViajeFactura.objects.create(
                viaje=random.choice(viajes),
                factura=random.choice(facturas)
            )

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
