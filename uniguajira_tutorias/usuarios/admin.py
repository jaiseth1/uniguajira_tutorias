from django.contrib import admin
from .models import Estudiante, Docente

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'programa', 'semestre', 'activo')
    search_fields = ('codigo', 'nombre', 'programa')
    list_filter = ('programa', 'semestre', 'activo')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('identificacion', 'nombre', 'departamento', 'especialidad', 'disponible_para_tutorias')
    search_fields = ('identificacion', 'nombre', 'departamento')
    list_filter = ('departamento', 'disponible_para_tutorias')
