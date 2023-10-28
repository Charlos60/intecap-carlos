from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import *
from . import views 

from api.views import UserViewSet
from rest_framework.routers import DefaultRouter

# Creamos un enrutador para manejar las rutas de los viewsets
router = routers.DefaultRouter()

# Registra tus viewsets en el enrutador
router.register(r'categorias', CategoriaCursoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'estudiantes', EstudianteViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'inscripciones',InscripcionViewSet)
router.register(r'notificaciones', NotificacionViewSet)


route = ExtendedSimpleRouter()
route.register(r'user', UserViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger'),
    path('tokenLogin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/register', UserRegisterView.as_view(), name='user_register'),
    path('', include(route.urls)),
    
    # Incluye las rutas generadas por el enrutador DefaultRouter
    path('', include(router.urls)),
]
