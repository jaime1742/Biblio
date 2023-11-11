from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


@login_required
def index(request):
    return render(request, 'index.html', {
        'users': 'HOLA',
    })
