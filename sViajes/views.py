from rest_framework import viewsets

from .serializers import *
from .models import *
from rest_framework import viewsets

from .models import *
from .serializers import *


# Create your views here.

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class TaxiViewSet(viewsets.ModelViewSet):
    queryset = Taxi.objects.all()
    serializer_class = TaxiSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()

    serializer_class = ClienteSerializer


class SViajeViewSet(viewsets.ModelViewSet):
    queryset = SViaje.objects.all()

    serializer_class = SViajeSerializer
