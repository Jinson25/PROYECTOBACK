
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect

from .carrito import Carrito
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from PROYECTO.models import Producto
# Create your views here.
def home(request):
    data = Post.objects.all()
    return render(request,'home.html', {'posts':data})
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, identifier=post_id)
    return render(request, 'post_detail.html', {'post':post})

@login_required(login_url="PROYECTO:home")
def like(request):
    post_id = request.GET['post_id']
    post = get_object_or_404(Post, identifier=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user) 
        liked=True
    post.save
    likes = post.likes.count()
    response = JsonResponse ({'liked': liked, 'likes': likes})
    return response 

@login_required(login_url='PROYECTO:home')
def comment(request):
    post_id = request.GET['post_id']
    post = get_object_or_404(Post, identifier=post_id)
    comment_data = request.GET['comment']
    comment = Comment(post=post, user=request.user, body=comment_data)
    comment.save()
    response = JsonResponse({'comment': comment_data})
    return response  

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "post_detail.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")