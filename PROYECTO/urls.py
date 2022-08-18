from django.urls import path
from . import views
from PROYECTO.views import tienda, pago

app_name = 'PROYECTO'

urlpatterns = [
    path('', views.home, name='home'),
    path('post_detail/<uuid:post_id>', views.post_detail, name='post_detail'),
    path('crear/', views.crear, name ='crear'),
    path('editar<int:id>', views.editar, name ='editar'),
    path('eliminar/<int:id>' , views.eliminar, name='eliminar'),
    path('like/', views.like, name='like'),
    path('comment/', views.comment, name='comment'),
    path('rutas/', tienda, name="Tienda"),
    path('pago/', pago, name= 'Pago'),
    path('crearpago/',views.crear_pago, name ='crearpago'),
    path('editarp<int:id>',views.editar_pago, name ='editarpago'),
    path('eliminarp/<int:id>' ,views.eliminar_pago, name='eliminarpago')
    
]