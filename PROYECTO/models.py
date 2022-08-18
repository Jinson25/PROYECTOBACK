from pyexpat import model
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
import uuid

# Create your models here.

class Post(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        default='images/default.png'
    )
    published = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='network_post'
    )
    
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse("PROYECTO:post_detail", args=[str(self.identifier)])

    @property
    def get_comments(self):
        own_comments = Comment.objects.filter(post=self)
        return own_comments
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commets', null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user}-->{self.body} '

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} -> {self.precio} '
    
class Pago(models.Model):
    metodo = models.CharField(max_length= 100)
    valor = models.CharField(max_length= 50)
    guia = models.CharField(max_length= 100)
    fecha = models.CharField(max_length= 80)
    
    def __str__(self):
        return self.name