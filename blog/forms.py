from django import forms
from django.forms import ValidationError
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
    
    def clean_contenido(self):
        data = self.cleaned_data['contenido']
        if len(data) < 20:
            raise ValidationError(
                "El mensaje debe contener mas de 20 caracteres")
        return data
    
    def clean_autor(self):
        data = self.cleaned_data['autor']
        if any(char.isdigit() for char in data):
            raise ValidationError("El autor no puede contener números.")
        return data

    

class CommentForm(forms.ModelForm):
    email = forms.EmailField(label='Correo Electrónico')

    class Meta:
        model = Comentario
        fields = ['autor', 'email', 'contenido']
    #name = forms.CharField(max_length=100, label='Tu nombre')
    #body = forms.CharField(widget=forms.Textarea, label='Comentario')
