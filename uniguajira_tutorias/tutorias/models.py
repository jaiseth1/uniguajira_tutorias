from django.db import models
from usuarios.models import Estudiante, Docente
from materias.models import Materia

class Tutoria(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    tema = models.CharField(max_length=200)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='tutorias')
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, related_name='tutorias')
    materia = models.ForeignKey(Materia, on_delete=models.PROTECT, related_name='tutorias')
    fecha = models.DateField()
    hora = models.TimeField()
    duracion_minutos = models.PositiveIntegerField(default=60)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-fecha', 'hora']
        unique_together = ('docente', 'fecha', 'hora')

    def __str__(self):
        return f"Tutoria: {self.tema} - {self.estudiante.nombre} / {self.docente.nombre} - {self.fecha} {self.hora}"
