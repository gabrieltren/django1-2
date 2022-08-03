from django import forms
from .models import Post
class UserCreateforms(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=100)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    password1 = forms.CharField(max_length=150)
    password2 = forms.CharField(max_length=150)
    
    class Meta:
        widget ={
            'password1' : forms.PasswordInput(),
            'password2' : forms.PasswordInput(attrs={'class': 'form-control form-input', 'placeholder': 'Re-type password'})
        }
        
        
class PostModelForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'data', 'texto', 'imagem', 'usuario']