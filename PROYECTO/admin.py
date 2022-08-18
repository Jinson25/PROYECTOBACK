from django.contrib import admin
from .models import Post, Comment, Producto, Pago

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Producto)
admin.site.register(Pago)