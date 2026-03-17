from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nome', 'email', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Seu nome completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Seu melhor e-mail'}),
            'mensagem': forms.Textarea(attrs={'placeholder': 'Como podemos ajudar?', 'rows': 4}),
        }
