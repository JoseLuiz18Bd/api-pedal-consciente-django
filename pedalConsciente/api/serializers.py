from rest_framework import serializers
from Denuncia import models

class DenunciaSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Denuncia
            fields = '__all__'
