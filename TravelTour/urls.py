from argparse import Namespace
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from PROYECTO.views import agregar_producto, eliminar_producto, restar_producto, tienda, limpiar_carrito, crear_pago, editar_pago, eliminar_pago


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PROYECTO.urls', namespace="PROYECTO")),
    path('', include('users.urls', namespace="users")), 
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
