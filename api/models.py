from django.core.validators import MinValueValidator
from django.db import models

class Gasto(models.Model):
    """
    Modelo que representa un gasto realizado por un usuario.
    Contiene información sobre el usuario, la categoría, el monto y la fecha del gasto.
    """
    usuario = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    fecha = models.DateTimeField(auto_now_add=True)
