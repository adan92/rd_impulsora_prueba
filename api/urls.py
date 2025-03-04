from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import GastoViewSet, UserRegisterView

# Se registran todas las vistas basadas en ViewSet (CRUD automático)
router = DefaultRouter()
router.register(r'gastos', GastoViewSet)

# Incluye todas las URLs generadas por el router (para CRUD de 'gastos' y otras vistas registradas)
urlpatterns = [
    path('', include(router.urls)), # Rutas automáticas generados por defaultRouter
    path('register/', UserRegisterView.as_view(), name='register'),  # Registro de usuario
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Obtención de JWT
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refresco de token JWT
]
