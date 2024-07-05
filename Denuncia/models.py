from django.db import models
from uuid import uuid4

def upload_image_denuncia(instance, filename):
        return f'{instance.id_denuncia}-{filename}'

class Denuncia(models.Model):
        id_denuncia = models.UUIDField(primary_key=True, default=uuid4, editable=False)
        denunciaType = models.CharField(max_length=255)
        estado = models.CharField(max_length=50)
        cidade = models.CharField(max_length=50)
        bairro = models.CharField(max_length=50)
        numero = models.CharField(max_length=5)
        denuncia = models.CharField(max_length=1000)
        data = models.CharField(max_length=10)
        imagem = models.ImageField(upload_to=upload_image_denuncia, blank=True, null=True)
        