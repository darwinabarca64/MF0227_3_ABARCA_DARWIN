from django.shortcuts import redirect, render

from catalogo.forms import ProductoForm
from catalogo.models import Producto


def lista_productos(request):
    productos = [
        {
            "producto": producto,
            "precio_final": producto.calcular_precio_final(),
        }
        for producto in Producto.objects.all()
    ]
    return render(
        request,
        "catalogo/lista_productos.html",
        {"productos": productos},
    )


def nuevo_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_productos")
    else:
        form = ProductoForm()

    return render(request, "catalogo/nuevo_producto.html", {"form": form})
