from django.contrib import admin
from .models import Materia

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'docente', 'creditos')
    search_fields = ('codigo', 'nombre', 'docente__nombre')
    list_filter = ('creditos',)
