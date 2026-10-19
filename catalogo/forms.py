from django import forms

from catalogo.models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descuento"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={"maxlength": "200", "placeholder": "Nombre del producto"}
            ),
            "precio": forms.NumberInput(
                attrs={"min": "0", "step": "0.01"}
            ),
            "descuento": forms.NumberInput(
                attrs={"min": "0", "max": "100", "step": "1"}
            ),
        }
