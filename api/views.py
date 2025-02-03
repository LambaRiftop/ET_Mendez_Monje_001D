from rest_framework import viewsets
from core.models import Imagen
from .serializers import ImagenSerializer

class ImagenViewSet(viewsets.ModelViewSet):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
