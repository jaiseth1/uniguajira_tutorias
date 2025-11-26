 Tutorías Uniguajira - Proyecto de ejemplo

 1. RESUMEN EJECUTIVO
Nombre del aplicativo: Tutorías Uniguajira

Nombres de los integrantes: Jaiseth Rafael Barros Ojeda

Problema que aborda
Los estudiantes de la Universidad de La Guajira enfrentan dificultades para acceder, registrar y hacer seguimiento de las tutorías académicas. Falta un sistema unificado que permita a la administración, docentes y estudiantes coordinar citas, llevar historial de sesiones y generar reportes.

 propuesta
Una aplicación web ligera para gestionar tutores, estudiantes y sesiones de tutoría, con registro de sesiones, historial y exportación de la base de datos para análisis. Es un prototipo que puede extenderse con autenticación, roles, generación de reportes y notificaciones.

Alcance principal (módulos clave)
- Gestión de Tutores (crear, listar).
- Gestión de Estudiantes (crear, listar).
- Registro de Sesiones de Tutoría (fecha/hora, tutor, estudiante, notas).
- Exportación de base de datos (descarga de SQLite).
- Interfaz web simple para demostración y pruebas.

Tecnologías usadas
- Python 3.x
- Flask (microframework web)
- SQLite (base de datos embebida)
- HTML / CSS (Jinja2 templates)
- Pillow (para generar diagramas estáticos incluidos en /docs)
- (Opcional) Git y GitHub para control de versiones


2. DESCRIPCIÓN DE LA NECESIDAD
Situación actual (dolor, ineficiencias, riesgos).
- Las tutorías se coordinan manualmente (email/Whatsapp), sin registro centralizado.
- No hay historial accesible fácilmente.
- Riesgo de repetición o pérdida de seguimiento de estudiantes.
- Dificultad administrativa para generar estadísticas sobre uso de tutorías.

Usuarios afectados
- Administración: necesita informes y control del programa.
- Docentes/Tutores: coordinar y registrar sesiones.
- Estudiantes: solicitar y consultar tutorías y su historial.

Beneficios esperados al resolverlo
- Centralizar la información para mejor seguimiento académico.
- Facilitar la asignación y registro de tutorías.
- Obtener datos para toma de decisiones y mejora del servicio.


## 3. REQUERIMIENTOS

### 3.1 Requerimientos Funcionales (RF)
1. RF1: El sistema debe permitir al administrador o tutor registrar tutores (nombre, correo).
2. RF2: El sistema debe permitir registrar estudiantes (nombre, código, programa).
3. RF3: El sistema debe permitir registrar sesiones de tutoría (tutor, estudiante, fecha/hora, notas).
4. RF4: El sistema debe listar tutores, estudiantes y sesiones recientes.
5. RF5: El sistema debe permitir exportar la base de datos SQLite con los datos registrados.
6. RF6: (Extensión) El sistema podrá generar reportes PDF o CSV de sesiones por rango de fecha.

### 3.2 Requerimientos No Funcionales (RNF)
- Rendimiento: Las consultas de listados deben responder en menos de 3 segundos en una instancia ligera.
- Usabilidad: La interfaz debe permitir realizar las acciones principales en máximo 3 clics.
- Seguridad: (Prototipo) No se incluye autenticación; en producción se requiere HTTPS y almacenamiento seguro de contraseñas.
- Disponibilidad: En despliegue real se espera un SLA alto; en el prototipo local se ejecuta bajo demanda.
- Restricciones: El prototipo está implementado en Python 3 y Flask; la base de datos es SQLite para facilidad de despliegue.

---

## 4. DISEÑO DE DATOS
Se incluyen las siguientes entidades principales:

- Tutor (id, name, email, created_at)
- Student (id, name, code, program, created_at)
- Session (id, tutor_id, student_id, date, notes, created_at)

Relaciones:
- Un Tutor puede tener N Sessions (1:N).
- Un Student puede tener N Sessions (1:N).
- Cada Session pertenece a un Tutor y a un Student (N:1 hacia cada).

En el directorio `/docs` se incluye un diagrama ER simple (`er_diagram.png`).

---

## 5. ARQUITECTURA, PATRONES DE DISEÑO
Patrón: Arquitectura en capas simple (MVC ligero).
- Modelos: definidos por tablas SQLite (`app/schema.sql`).
- Vistas: templates Jinja2 en `app/templates`.
- Controladores: rutas y lógica en `app/app.py`.

Este prototipo sigue un patrón de "microservicio" monolítico pequeño (aplicación Flask + DB embebida) adecuado para demostración o pruebas.

---

## 6. ANEXOS Y EVIDENCIAS
- Capturas en `/docs` y diagrama ER (`er_diagram.png`).
- El código fuente está en `app/`.
- Pasos para ejecutar en **Desarrollo local**:
  1. Clonar el repositorio.
  2. Crear un entorno virtual: `python -m venv venv && source venv/bin/activate` (o `venv\Scripts\activate` en Windows).
  3. Instalar dependencias: `pip install -r requirements.txt`
  4. Ejecutar: `python app/app.py`
  5. Entrar a `http://127.0.0.1:5000/` y usar el enlace `/init` para inicializar la base de datos.


