from django.urls import path, include

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'marca', MarcaViewSet)
router.register(r'taxi', TaxiViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'sviaje', SViajeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
