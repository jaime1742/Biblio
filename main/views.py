from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import UserRegistrationForm


@login_required
def index(request):
    return render(request, 'index.html', {
        'users': 'HOLA',
    })


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']

            if password == password_confirm:
                try:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()
                    login(request, user)
                    return redirect('/')
                
                except IntegrityError:
                    return render(request, 'registration/signup.html', {'form': form, 'error': 'Este usuario ya existe.'})
            
            return render(request, 'registration/signup.html', {'form': form, 'error': 'Las contraseñas no coinciden'})
    
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})
