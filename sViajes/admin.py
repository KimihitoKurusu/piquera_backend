from django.contrib import admin

# Register your models here.

from .models import Marca, Taxi, Cliente, SViaje

admin.site.register(Marca)
admin.site.register(Taxi)
admin.site.register(Cliente)
admin.site.register(SViaje)