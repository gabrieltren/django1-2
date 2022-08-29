import re
from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Post
from .forms import UserCreateforms, PostModelForm

def register_user(request):
    if request.user.is_anonymous:
        form = UserCreateforms()
        context ={
            "form": form,
        }
        return render(request, 'register.html', context)
    else:
        return redirect('/')

def register_submit(request):
    if request.POST:
        print(request.POST)
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create(
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    first_name=request.POST.get('first_name'),
                    last_name=request.POST.get('last_name'),
                )
                user.set_password(request.POST.get('password1'))
                user.save()
                login(request, user)
                return redirect('/')
            except:
                messages.error(request, 'Aconteceu algo errado')
                form = UserCreateforms(request.POST)
                context ={
                'form': form,
                }  
        else:
            messages.error(request, 'Senhas invalidas')
            form = UserCreateforms(request.POST)
            context ={
                'form': form,
            }
        return render(request, 'register.html', context)
    else:
        return redirect('/registe/')
@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')
    
def login_user(request):
    return render(request, 'login.html')

def login_submit(request):
    print(request.POST)
    if request.POST:
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        
        usuario = authenticate(username=usuario, password=senha)
        
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        
        else:
            messages.error(request, "Usuario ou senha Invalida !!!")
            
            return render(request, 'login.html')
    return redirect('/')
    

def index(request):
    print(dir(request.user))
    print(request.user.is_anonymous)
    post = Post.objects.all()
    
    context = {
        'post': post,
    }
    
    return render(request, 'index.html', context)

def item_post(request, id):
    
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
    }
    return render(request, 'item_post.html', context)

@login_required(login_url='/login/')
def post_registre(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post criado com sucesso")
            return redirect('/')
        else:
            messages.error(request, "Erro ao salvar o Post")
            context = {
                "form": form
            }
            return render(request, 'post_registre.html', context)
    else:
        form = PostModelForm()
        context = {
                "form": form
            }
        
        return render(request, 'post_registre.html', context)