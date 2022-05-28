from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import loader

from app.models import Category, Cred


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required()
def home(request):
    template = loader.get_template('home.html')
    context = {
        'creds': Cred.objects.filter(user_id=request.user),
    }
    return HttpResponse(template.render(context, request))


@login_required()
def add_form(request):
    template = loader.get_template('addForm.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))

