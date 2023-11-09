from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Vehiculo(models.Model):
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=100)
    # imagen = models.ImageField()
    anho = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.marca} {self.modelo} {self.anho}'



class Reseña(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    calificacion = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comentario = models.TextField()

    def __str__(self) -> str:
        return f'Reseña de {self.vehiculo} por {self.usuario}'
    
class MensajeDirecto(models.Model):
    remitente = models.ForeignKey(User, related_name='remitente', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='destinatario', on_delete=models.CASCADE)
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"De {self.remitente} a {self.destinatario}: {self.asunto}"

    