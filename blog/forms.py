from django import forms

from .models import Post, Novo, Mensage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

class NovoForm(forms.ModelForm):
    class Meta:
        model = Novo
        fields = ('title', 'text')

class MensageForm(forms.ModelForm):
    class Meta:
        model = Mensage
        fields = ('title', 'text')