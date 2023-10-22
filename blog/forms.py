from django import forms
from .models import Post, Comentario

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'contenido']
        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
    #name = forms.CharField(max_length=100, label='Tu nombre')
    #body = forms.CharField(widget=forms.Textarea, label='Comentario')