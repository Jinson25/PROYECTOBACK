
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PostForm, PagoForm
from .carrito import Carrito
from .models import Post, Comment, Pago
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

def crear(request):
    if request.method == "POST" :
        post_form = PostForm(request.POST)
        if post_form.is_valid() :
            post_form.save()
            return redirect('PROYECTO:home')
    else :
        post_form = PostForm()

    return render(
        request , 'crearpost.html' ,
        {
            'post_form' : post_form
        }
    )
def editar(request, post_id) :
    post = get_object_or_404(Post, identifier=post_id)

    if request.method == "POST" :
        post_form = PostForm(request.POST , instance = post) 
        if post_form.is_valid() :
            post_form.save()
            return redirect('PROYECTO:home')
    else :
        post_form = PostForm(instance = post)

    return render(
        request , 'editar.html' ,
        {
            'post_form' : post_form
        }
    )

def eliminar(request , id) :
    post = get_object_or_404(Post , pk = id)

    if post :
        post.delete()

    return redirect('PROYECTO:home')


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
    return render(request, "rutas.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("PROYECTO:Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("PROYECTO:Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("PROYECTO:Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("PROYECTO:Tienda")

def pago (request):
    pagos = Pago.objects.all()
    return render(request, 'pago.html', {'pagos':pagos})

def crear_pago(request):
    if request.method == "POST" :
        pago_form = PagoForm(request.POST)
        if pago_form.is_valid() :
            pago_form.save()
            return redirect('PROYECTO:Pago')
    else :
        pago_form = PagoForm()

    return render(
        request , 'crearpago.html' ,
        {
            'pago_form' : pago_form
        }
    )
def editar_pago(request, id) :
    celular = get_object_or_404(Pago, id = id)

    if request.method == "POST" :
        pago_form = PagoForm(request.POST , instance = celular) 
        if pago_form.is_valid() :
            pago_form.save()
            return redirect('PROYECTO:Pago')
    else :
        pago_form = PagoForm(instance = celular)

    return render(
        request , 'editarpago.html' ,
        {
            'pago_form' : pago_form
        }
    )

def eliminar_pago(request , id) :
    pago = get_object_or_404(Pago , pk = id)

    if pago :
        pago.delete()

    return redirect('PROYECTO:Pago')