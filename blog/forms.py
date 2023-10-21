from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'contenido']
        

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label='Tu nombre')
    body = forms.CharField(widget=forms.Textarea, label='Comentario')