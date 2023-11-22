from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import User, Vehiculo
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import UserRegistrationForm
from .models import Vehiculo, Reseña
import os
from django.conf import settings
from .serializers import PerfilUsuarioSerializer


@login_required

def index(request):
    images_path = os.path.join(settings.BASE_DIR,'main', 'static', 'img')
    images = [image for image in os.listdir(images_path) if image.endswith(('jpg', 'jpeg', 'png'))]
    return render(request, 'index.html', {'user': request.user, 'images': images})

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


@login_required
@permission_required("User")
def lista_coches(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})


def filtro_coches(request):
    if request.method == 'GET':
        anho = request.GET.get('anho', '')
        modelo = request.GET.get('modelo', '')
        marca = request.GET.get('marca', '')

        vehiculos = Vehiculo.objects.filter(
            anho__icontains=anho,
            modelo__icontains=modelo,
            marca__icontains=marca
        )

        return render(request, 'lista_vehiculos.html', {'vehiculos': vehiculos})


@permission_required("admin")
def users_list(request):
    users = User.objects.all()
    serializer = PerfilUsuarioSerializer(users, many=True)
    context = {
        'users': serializer.data,
    }

    return render(request, 'users_list.html', context)


@login_required
def user_profile(request, pk):
    reseñas = Reseña.objects.filter(usuario=pk)
    context = {
        'reseñas': reseñas,
    }

    return render(request, 'user.html', context)


def add_email(request):
    if request.method == "POST":
        new_email = request.POST.get("new_email")
        request.user.email = new_email
        request.user.save()

        return redirect('/')

    return render(request, 'user.html')


@login_required
def update_username(request):
    if request.method == 'POST':
        new_username = request.POST.get('new_username')
        request.user.username = new_username
        request.user.save()

        return redirect('/')

    return render(request, 'user.html')
