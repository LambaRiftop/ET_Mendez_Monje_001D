from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import ImagenViewSet

router = DefaultRouter()

# api/imagenes
router.register('imagenes', ImagenViewSet, basename='imagen')
urlpatterns = [
  
    path('', include(router.urls))
    # localhost/api/ -> router registered
    # router.urls
]
