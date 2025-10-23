from django.db import models

class Estudiante(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    programa = models.CharField(max_length=100)
    semestre = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ['programa', 'nombre']

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"


class Docente(models.Model):
    identificacion = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    departamento = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100, blank=True, null=True)
    disponible_para_tutorias = models.BooleanField(default=True)

    class Meta:
        ordering = ['departamento', 'nombre']

    def __str__(self):
        return self.nombre
