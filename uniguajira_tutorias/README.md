# UniGuajiraTutor

Sistema de gestión de tutorías académicas — Universidad de La Guajira.

## Descripción
Aplicación Django para permitir a estudiantes agendar tutorías, gestionar disponibilidad de docentes y dar seguimiento a las sesiones.

## Estructura
- usuarios: modelos para Estudiante y Docente.
- materias: modelos para Materia y relación con Docente.
- tutorias: modelo Tutoria con control de estado y restricciones.

## Instrucciones rápidas

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Requisitos
- Python 3.9+
- Django 4.2+
