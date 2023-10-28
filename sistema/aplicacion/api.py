from usuario.models import Usuario
from rest_framework import viewsets
from rest_framework.permissions import AllowAny  # Importar AllowAny desde rest_framework.permissions
from .serializers import projectSerializer

class projectViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [AllowAny]  # Usar AllowAny en lugar de permissions.AllowAny
    serializer_class = projectSerializer
