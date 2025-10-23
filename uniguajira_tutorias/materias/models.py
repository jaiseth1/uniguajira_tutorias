from django.db import models
from usuarios.models import Docente

class Materia(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=120)
    creditos = models.PositiveIntegerField()
    docente = models.ForeignKey(Docente, on_delete=models.SET_NULL, null=True, related_name='materias')

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
