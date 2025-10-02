from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # built-in form 정리하기!! 각각 어떤역할을 헀는지도 정리해야함
from django.contrib.auth import login as auth_login
from .models import User

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)