from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Gasto


# Serializador que se encarga de registrar el usuario que podra obtener un token para consumir la API
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )


class GastoSerializer(serializers.ModelSerializer):
    """
        Serializador para el modelo Gasto.

        Este serializador se encarga de convertir los objetos Gasto a formato JSON
        y viceversa. También valida los datos de entrada y asegura que los campos
        tengan los valores correctos.

        Campos:
            - id (integer): Identificador único del gasto. Es autogenerado.
            - usuario (string): Nombre del usuario asociado al gasto.
            - categoria (string): Categoría del gasto.
            - monto (decimal): Monto del gasto (debe ser positivo).
            - fecha (datetime): Fecha y hora en que se registró el gasto.
        """

    class Meta:
        model = Gasto
        fields = '__all__'

    def validate_monto(self, value):
        """
        Valida que el monto del gasto sea mayor que cero.

        El monto no puede ser negativo o cero. Esta validación es importante
        para asegurar que los registros de gastos sean correctos.

        Args:
            value (decimal): El valor del campo 'monto' proporcionado.

        Raises:
            serializers.ValidationError: Si el valor es menor o igual a cero.
        """
        if value <= 0:
            raise serializers.ValidationError("El monto debe ser mayor que cero.")
        return value

    def validate_usuario(self, value):
        """
        Valida que el nombre del usuario no esté vacío.

        Asegura que siempre se registre un nombre de usuario asociado al gasto.

        Args:
            value (string): El nombre del usuario proporcionado.

        Raises:
            serializers.ValidationError: Si el campo 'usuario' está vacío.
        """
        if not value.strip():
            raise serializers.ValidationError("El campo 'usuario' no puede estar vacío.")
        return value

    def validate_categoria(self, value):
        """
        Valida que la categoría no sea demasiado larga.

        Este campo debe tener un máximo de 50 caracteres para mantener
        la consistencia en la base de datos.

        Args:
            value (string): El valor de la categoría proporcionada.

        Raises:
            serializers.ValidationError: Si la categoría supera los 50 caracteres.
        """
        if len(value) > 50:
            raise serializers.ValidationError("La categoría no puede exceder los 50 caracteres.")
        return value
