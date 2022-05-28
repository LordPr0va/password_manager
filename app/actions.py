from django.shortcuts import redirect

from app.models import Cred, Category


def add_cred(request):
    website = request.POST['website']
    username = request.POST['username']
    password = request.POST['password']
    category_id = request.POST['categories']
    category = Category.objects.filter(id=category_id).first()
    new_cred = Cred(website=website,
                    username=username,
                    password=password,
                    category_id=category,
                    user_id=request.user)

    new_cred.save()

    return redirect('home')


def delcred(request):
    cred_id = request.GET.get('cred_id')
    cred = Cred.objects.filter(id=cred_id).first()
    cred.delete()
    return redirect('home')
