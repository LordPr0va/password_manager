"""password_manager URL Configuration

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
from django.urls import path, include

import app.views
import app.actions

urlpatterns = [
    path('', app.views.index),
    path('home', app.views.home, name='home'),

    path('accounts/', include("django.contrib.auth.urls")),
    path('register', app.views.register, name="register_url"),

    path('cred/', app.views.add_form, name='addcreds'),
    path('cred/addcred_action', app.actions.add_cred),
    path('cred/delcred_action', app.actions.delcred, name='delcred_action'),

    path('admin/', admin.site.urls),
]
