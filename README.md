# Sistema de Tickets – Backend (Django + Django REST Framework)

API REST para la gestión de tickets de soporte: usuarios, departamentos, prioridades, estados, tickets, comentarios y adjuntos. Desarrollada con **Django** y **Django REST Framework**, con base de datos **MySQL**.

## Estructura del proyecto

```
Bakend-main/
├── manage.py
├── requirements.txt
├── .env                     # Variables sensibles (NO subir al repositorio)
├── motor_django/            # Proyecto Django (settings, urls, wsgi, asgi)
└── sistema_tikets/          # Aplicación principal
    ├── models.py            # Modelo de datos
    ├── serializer.py        # Serializadores DRF
    ├── views.py             # ModelViewSet por modelo
    ├── urls.py              # Router de la API
    ├── admin.py             # Registro de modelos en el admin
    ├── migrations/          # Migraciones
    ├── fixtures/            # Datos iniciales (JSON)
    └── templates/           # bienvenida.html, 404.html
```

## Requisitos

- Python 3.12 o superior
- MySQL 8 (o compatible) en ejecución
- Cliente de desarrollo de MySQL para compilar `mysqlclient`
  - Ubuntu/Debian: `sudo apt install libmysqlclient-dev pkg-config build-essential`
  - macOS: `brew install mysql pkg-config`
  - Windows: normalmente basta con `pip install` (usa ruedas precompiladas)

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Bakend-main
```

### 2. Crear y activar el ambiente virtual

```bash
python -m venv venv

# Linux / macOS
source venv/bin/activate

# Windows (PowerShell)
venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz (junto a `manage.py`):

```
SECRET_KEY='tu-clave-secreta-aqui'
```

> El archivo `.env` debe estar en `.gitignore`. Nunca subas claves ni contraseñas al repositorio.

### 5. Configurar la base de datos

Crear la base de datos y el usuario en MySQL:

```sql
CREATE DATABASE sistemaTikets CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'Usuario'@'localhost' IDENTIFIED BY 'mi_password';
GRANT ALL PRIVILEGES ON sistemaTikets.* TO 'Usuario'@'localhost';
FLUSH PRIVILEGES;
```

Estos valores coinciden con `DATABASES` en `motor_django/settings.py`. Si usas otros, edítalos allí.

### 6. Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear un superusuario (para el panel de administración)

```bash
python manage.py createsuperuser
```

### 8. Iniciar el servidor

```bash
python manage.py runserver
```

## Rutas disponibles

| Ruta | Descripción |
|---|---|
| `/` | Página de bienvenida |
| `/admin/` | Panel de administración de Django |
| `/sistema_tikets/` | Raíz de la API (listado de endpoints) |
| `/sistema_tikets/usuarios/` | CRUD de usuarios |
| `/sistema_tikets/departamentos/` | CRUD de departamentos |
| `/sistema_tikets/prioridades/` | CRUD de prioridades |
| `/sistema_tikets/estados/` | CRUD de estados |
| `/sistema_tikets/tickets/` | CRUD de tickets |
| `/sistema_tikets/ticket-comentarios/` | CRUD de comentarios de tickets |
| `/sistema_tikets/ticket-adjuntos/` | CRUD de adjuntos de tickets |

Cada endpoint admite:

| Método | Ruta | Acción |
|---|---|---|
| `GET` | `/<recurso>/` | Listar |
| `POST` | `/<recurso>/` | Crear |
| `GET` | `/<recurso>/<id>/` | Obtener uno |
| `PUT` / `PATCH` | `/<recurso>/<id>/` | Actualizar |
| `DELETE` | `/<recurso>/<id>/` | Eliminar |

Ejemplo:

```bash
curl -X POST http://127.0.0.1:8000/sistema_tikets/departamentos/ \
     -H "Content-Type: application/json" \
     -d '{"nombre_departamento": "Soporte TI", "descripcion": "Incidencias técnicas"}'
```

## Modelo de datos

| Modelo | Descripción | Relaciones principales |
|---|---|---|
| `Usuario` | Extiende `AbstractUser`; agrega `rol` (cliente, agente, administrador) | – |
| `Departamento` | Área responsable del ticket | – |
| `Prioridad` | Nivel (Baja, Media, Alta, Crítica) y tiempo SLA en horas | – |
| `Estado` | Abierto, En proceso, Pendiente, Resuelto, Cerrado | – |
| `Ticket` | Solicitud de soporte | FK a `Usuario` (solicitante y asignado), `Departamento`, `Prioridad`, `Estado` |
| `TicketComentario` | Mensaje del ticket; puede ser interno | FK a `Ticket` y `Usuario` |
| `TicketAdjunto` | Archivo adjunto del ticket | FK a `Ticket` |

Todos los modelos incluyen `created_at` y `updated_at`.

## Configuración de Django REST Framework

- `rest_framework` está registrado en `INSTALLED_APPS`.
- Formatos de fecha globales definidos en `REST_FRAMEWORK` (`settings.py`):
  - Salida de fecha y hora: `%Y-%m-%d %H:%M:%S`
  - Entrada de fecha y hora: `%d-%m-%Y %H:%M:%S`, `%d-%m-%Y` o ISO-8601
  - Fechas: `%d-%m-%Y`

## Control de versiones

Se recomienda usar un `.gitignore` con al menos:

```
venv/
.env
db.sqlite3
__pycache__/
*.pyc
media/
```

Flujo sugerido: commits pequeños y descriptivos, y push frecuente al repositorio remoto.

## Notas

- Los archivos de `fixtures/` deben coincidir con los campos actuales del modelo (`username`, `email`, `password`, `rol`, etc.) antes de cargarlos con `python manage.py loaddata <archivo>`.
- Para producción: poner `DEBUG = False`, restringir `ALLOWED_HOSTS` y mover las credenciales de la base de datos a variables de entorno.
