from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('perfil/', views.signup, name='perfil'),
    path('coches/', views.lista_coches, name='lista_coches'),
    path('coches/filtro/', views.filtro_coches, name='filtro_coches'),
    path('api/users/', views.users_list, name='users-list'),
    path('api/user/<int:pk>/', views.user_profile, name='user-profile'),
    path('add_email/', views.add_email, name='add-email'),
    path('update-username/', views.update_username, name='update-username'),
    path('coches/<int:pk>', views.vehiculo_detalle, name='vehiculo_detalle'),
]
