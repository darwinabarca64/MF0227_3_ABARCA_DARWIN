"""Clases de dominio para representar productos y aplicar descuentos."""

from decimal import Decimal


Precio = float | Decimal


class ProductoBase:
    """Representa un producto con nombre y precio original."""

    def __init__(self, nombre: str, precio: Precio) -> None:
        """Inicializa el producto y rechaza precios negativos."""
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.nombre = nombre
        self.precio = precio

    def precio_final(self) -> Precio:
        """Devuelve el precio original, sin aplicar descuentos."""
        return self.precio


class ProductoOferta(ProductoBase):
    """Representa un producto al que se aplica un descuento porcentual."""

    def __init__(
        self, nombre: str, precio: Precio, descuento: int = 0
    ) -> None:
        """Inicializa el producto y valida que el descuento esté entre 0 y 100."""
        if not 0 <= descuento <= 100:
            raise ValueError("El descuento debe estar entre 0 y 100")

        super().__init__(nombre, precio)
        self.descuento = descuento

    def precio_final(self) -> Precio:
        """Devuelve el precio tras aplicar el descuento porcentual."""
        if isinstance(self.precio, Decimal):
            porcentaje_restante = Decimal(100 - self.descuento) / Decimal(100)
            return self.precio * porcentaje_restante

        return self.precio * (100 - self.descuento) / 100
