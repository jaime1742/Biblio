<<<<<<< Updated upstream
from django.shortcuts import render
=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import User, Vehiculo
from django.contrib.auth import login
from django.db import IntegrityError
from .forms import UserRegistrationForm
from .models import Vehiculo
>>>>>>> Stashed changes

# Create your views here.
