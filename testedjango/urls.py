from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from databaseteste.api import viewsets as databaseviewsets
from index import IndexViewset

router = routers.DefaultRouter()
router.register(r"todos", databaseviewsets.DatabaseViewset, basename="todos")

router.register(r"indicadores", databaseviewsets.DatabaseViewIndicadores, basename="indicadores")
router.register(r"totalvendido", databaseviewsets.DatabaseViewTotalVendas, basename="totalvendido")
router.register(r"totalcategorias", databaseviewsets.DatabaseViewCategorias, basename="totalcategorias")
router.register(r"", IndexViewset, basename="index")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
