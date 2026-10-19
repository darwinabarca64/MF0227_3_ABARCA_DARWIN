from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from catalogo.dominio import ProductoOferta


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    descuento = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(precio__gte=0),
                name="producto_precio_no_negativo",
            ),
            models.CheckConstraint(
                condition=models.Q(descuento__gte=0, descuento__lte=100),
                name="producto_descuento_entre_0_y_100",
            ),
        ]

    def calcular_precio_final(self) -> float:
        """Calcula el precio final aplicando el descuento del producto."""
        producto = ProductoOferta(
            self.nombre,
            float(self.precio),
            self.descuento,
        )
        return producto.precio_final()

    def __str__(self) -> str:
        return self.nombre
