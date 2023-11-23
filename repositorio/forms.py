from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import CustomUser, Post

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required': 'required'
        })
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Repita su contraseña...',
            'id': 'password2',
            'required': 'required'
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'nombre', 'apellidos', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

            # Crear un post y asignar al usuario como autor
            Post.objects.create(author=user, title="Primer post", content="Contenido del primer post")

        return user





class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','content', 'image', 'pdf_file', 'video', 'categoria']


