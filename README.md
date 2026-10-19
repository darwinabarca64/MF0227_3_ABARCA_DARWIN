# Tienda: gestión de productos

## Descripción

`tienda` es una aplicación web desarrollada con Django que utiliza la aplicación
`catalogo` para registrar y listar productos. Las clases de programación
orientada a objetos calculan el precio final de cada producto aplicando su
descuento porcentual.

## Requisitos previos

- Python instalado.
- Acceso a una consola en la raíz del proyecto, donde se encuentra
  `manage.py`.

## Instalación y ejecución

1. Crear un entorno virtual:

   ```powershell
   python -m venv venv
   ```

2. Activarlo. En Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   En macOS o Linux:

   ```bash
   source venv/bin/activate
   ```

3. Instalar Django:

   ```console
   pip install django
   ```

4. Aplicar las migraciones para crear las tablas de la base de datos:

   ```console
   python manage.py migrate
   ```

5. Cargar los tres productos de comprobación:

   ```console
   python manage.py cargar_productos_prueba
   ```

   El comando es seguro para repetir: crea los productos si no existen y
   actualiza sus valores si ya están registrados.

6. Iniciar el servidor local:

   ```console
   python manage.py runserver
   ```

7. Abrir `http://127.0.0.1:8000/productos/` para consultar el listado:

   | Nombre | Precio | Descuento | Precio final esperado |
   | :--- | ---: | ---: | ---: |
   | Teclado | 30 € | 0 % | 30 € |
   | Ratón | 20 € | 25 % | 15 € |
   | Monitor | 150 € | 10 % | 135 € |

8. Ejecutar las pruebas automatizadas:

   ```console
   python manage.py test catalogo
   ```

## Seguridad antes del despliegue

La configuración de desarrollo no se debe usar tal cual en producción:

- Establecer la variable de entorno `DJANGO_DEBUG=False`. Con la depuración
  activada, los errores pueden mostrar información interna de la aplicación.
- Definir `ALLOWED_HOSTS` con los dominios reales autorizados para servir el
  sitio mediante `DJANGO_ALLOWED_HOSTS`, separados por comas. No se debe
  aceptar cualquier host en producción.
- Definir `DJANGO_SECRET_KEY` en el entorno y no incluir su valor en el
  repositorio. Así se evita exponer una clave que Django utiliza para
  funciones de seguridad, como la firma de sesiones y otros datos.

Por ejemplo, en PowerShell se pueden establecer las variables para la sesión:

```powershell
$env:DJANGO_DEBUG = "False"
$env:DJANGO_SECRET_KEY = "<clave-secreta-segura>"
$env:DJANGO_ALLOWED_HOSTS = "tienda.example.com,www.tienda.example.com"
```

En macOS o Linux:

```bash
export DJANGO_DEBUG=False
export DJANGO_SECRET_KEY="<clave-secreta-segura>"
export DJANGO_ALLOWED_HOSTS="tienda.example.com,www.tienda.example.com"
```

La configuración de Django lee estas variables. Cuando `DJANGO_DEBUG=False`,
la aplicación no arranca si falta `DJANGO_SECRET_KEY` o
`DJANGO_ALLOWED_HOSTS`.
