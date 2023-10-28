from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from api.serializers import UserSerializer,CategoriaCursoSerializer, CursoSerializer, EstudianteSerializer,FavoritoSerializer, InscripcionSerializer, NotificacionSerializer


from usuario.models import Usuario
from aplicacion.models import Estudiante, Favorito, Inscripcion,Notificacion

from aplicacion.models import Estudiante,CategoriaCurso, Curso
from django.contrib.auth import get_user_model
from rest_framework import generics







# Create your views here.

# Extender el schema nos permite manipular OPEN API con lo que trabaja spectacular
# Nos permite hacer cambios.
@extend_schema_view(
    list=extend_schema(description='permite obtener lista usuarios.'),
    retrieve=extend_schema(description='permite obtener un usuario.'),
    create=extend_schema(description='permite crear un usuario.'),
    update=extend_schema(description='permite actualizar un usuario.'),
    destroy=extend_schema(description='permite eliminar un usuario.'),
)
# Definimos nuestra clase, viewset nos permite trabajar con modelos, hace los dif.metodos
# GET, POST, PUT, DELETE = List, retrieve, update, destroy
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuario.objects.all()
    
    #lookup_field = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id
    #lookup_url_kwarg = 'id' #esto es para que cuando se haga una peticion se pueda buscar por id


User = get_user_model()

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IsSuperUserOrCustomPermission(BasePermission):
    message = "No está autorizado para realizar esta acción."

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.user.is_superuser:
                return True  # Los superusuarios tienen acceso completo
            # Agrega lógica personalizada para otros permisos aquí
            # Por ejemplo, verifica si el usuario tiene un permiso específico
        return False  # Usuario no autorizado

# En tus vistas, usa el decorador personalizado o anula `has_permission` como sigue:

from rest_framework.views import APIView

class CustomView(APIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrCustomPermission]

    def get(self, request):
        # Aquí colocas tu lógica de vista personalizada
        return Response({"message": "Puedes ver esta vista porque eres superusuario o tienes un permiso especial."}, status=status.HTTP_200_OK)


#–--------------PARA REGISTRO -----------------
class CategoriaCursoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaCurso.objects.all()
    serializer_class = CategoriaCursoSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class InscripcionViewSet(viewsets.ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer
