from django import forms
#from .models import Post

#class PostForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ['titulo', 'contenido', 'autor']
class PostForm(forms.Form):
    titulo = forms.CharField(label='Titulo', max_length=100)
    autor = forms.CharField(label = 'Autor', max_length=50)
    contenido = forms.CharField(widget=forms.Textarea())
    