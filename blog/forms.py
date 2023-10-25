from django import forms
from .models import Post, Comentario, Etiqueta
class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, etiqueta):
        return "%s" % etiqueta.desc

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'autor', 'contenido', 'etiquetas']
    etiquetas = CustomMMCF(
        queryset=Etiqueta.objects.all(),
        widget=forms.CheckboxSelectMultiple, required=False)
    

class CommentForm(forms.ModelForm):
    email = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = Comentario
        fields = ['autor', 'email', 'contenido']
    #name = forms.CharField(max_length=100, label='Tu nombre')
    #body = forms.CharField(widget=forms.Textarea, label='Comentario')
