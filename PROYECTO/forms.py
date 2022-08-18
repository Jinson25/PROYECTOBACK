from django.forms import ModelForm
from .models import Post, Pago

class PostForm(ModelForm) :
    class Meta :
        model = Post
        fields = '__all__' 
        
class PagoForm(ModelForm) :
    class Meta :
        model = Pago
        fields = '__all__' 