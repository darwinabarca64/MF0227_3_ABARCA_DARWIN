from decimal import Decimal

from django.core.management.base import BaseCommand

from catalogo.models import Producto


class Command(BaseCommand):
    help = "Carga o actualiza los tres productos de comprobación del ejercicio."

    PRODUCTOS = (
        ("Teclado", Decimal("30.00"), 0, Decimal("30.00")),
        ("Ratón", Decimal("20.00"), 25, Decimal("15.00")),
        ("Monitor", Decimal("150.00"), 10, Decimal("135.00")),
    )

    def handle(self, *args, **options):
        for nombre, precio, descuento, precio_final in self.PRODUCTOS:
            producto, creado = Producto.objects.update_or_create(
                nombre=nombre,
                defaults={"precio": precio, "descuento": descuento},
            )
            accion = "Creado" if creado else "Actualizado"
            self.stdout.write(
                f"{accion}: {producto.nombre} - "
                f"{producto.precio:.2f} € - {producto.descuento}% - "
                f"{producto.calcular_precio_final():.2f} € "
                f"(esperado: {precio_final:.2f} €)"
            )
