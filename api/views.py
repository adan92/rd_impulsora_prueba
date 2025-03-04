from rest_framework import viewsets, permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GastoSerializer, UserRegisterSerializer
from .models import Gasto


class UserRegisterView(APIView):
    """
    Vista encargada de manejar el registro del usuario
    """
    permission_classes = [permissions.AllowAny]  # No necesita que este autenticado el usuario para usarlo

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GastoViewSet(viewsets.ModelViewSet):
    """
    Vista para manejar operaciones CRUD sobre los gastos.
    Permite crear, listar, actualizar y eliminar gastos.
    """
    queryset = Gasto.objects.all().order_by('-fecha')
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return super().get_object()
        except:
            raise NotFound("El gasto no existe.")
