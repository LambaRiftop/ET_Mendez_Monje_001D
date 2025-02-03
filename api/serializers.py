from rest_framework import serializers
from core.models import Imagen

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = '__all__'
