from django.test import TestCase

from catalogo.dominio import ProductoOferta


class ProductoOfertaTests(TestCase):
    def test_precio_final_aplica_descuento(self):
        producto = ProductoOferta("Producto de prueba", 100.0, 20)

        self.assertEqual(producto.precio_final(), 80.0)

    def test_lista_productos_responde_y_renderiza_plantilla(self):
        response = self.client.get("/productos/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "catalogo/lista_productos.html")
