from rest_framework import viewsets
from pedalConsciente.api import serializers
from Denuncia import models

class DenunciaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DenunciaSerializer
    queryset = models.Denuncia.objects.all()

