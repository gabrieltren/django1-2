from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    data = models.DateField(blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    imagem = models.ImageField(blank=True, null=True, upload_to='blog')
    usuario = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL, default=None
        )
    