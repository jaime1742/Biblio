from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError


@login_required
def index(request):
    return render(request, 'index.html', {
        'users': 'HOLA',
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('/')
            except IntegrityError:
                return render(request, 'registration/signup.html', {"form": UserCreationForm, "error": "Este usuario ya existe."})

        return render(request, 'registration/signup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})
