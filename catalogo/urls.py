from django.urls import path

from catalogo import views


urlpatterns = [
    path("", views.lista_productos, name="lista_productos"),
    path("nuevo/", views.nuevo_producto, name="nuevo_producto"),
]
