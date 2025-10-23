from django.contrib import admin
from .models import Tutoria

@admin.register(Tutoria)
class TutoriaAdmin(admin.ModelAdmin):
    list_display = ('tema', 'estudiante', 'docente', 'materia', 'fecha', 'hora', 'estado')
    search_fields = ('tema', 'estudiante__nombre', 'docente__nombre', 'materia__nombre')
    list_filter = ('estado', 'materia', 'fecha')
