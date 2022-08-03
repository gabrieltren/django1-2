"""main_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog.views import (
    index,item_post, 
    login_user,login_submit,
    logout_user,register_user,
    register_submit, post_registre
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post/<id>', item_post, name='item_post'),
    path('login/', login_user, name='login'),
    path('login/submit', login_submit, name='login_submit'),
    path('logout/', logout_user, name='logout'),
    path('registre/', register_user, name='registre'),
    path('registre/submit', register_submit, name='register_submit'),
    path('registre_post/', post_registre, name='registre_post')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
