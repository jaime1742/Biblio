from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class Marca(models.Model):
    marca = models.CharField(max_length=100)
    logo = models.ImageField()

    def __str__(self) -> str:
        return f'{self.marca}'

class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default='1')
    modelo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='')
    anho = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} {self.anho}'


class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField()

    def __str__(self) -> str:
        return f'Reseña de {self.vehiculo} por {self.usuario.username}'


class MensajeDirecto(models.Model):
    remitente = models.ForeignKey(User, related_name='remitente', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='destinatario', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"De {self.remitente} a {self.destinatario}: {self.asunto}"


class PerfilUsuario(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    reviews = models.ForeignKey(Reseña, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"{self.username}: {self.reviews}"
