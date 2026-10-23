from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now as ahora
from django.db import models

class Usuario(AbstractUser):
    # Campos heredados: username, first_name, last_name, email, password, etc.
    rol = models.CharField('Rol', max_length=20, null=False, default='cliente')  # cliente, agente, administrador
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

class Departamento(models.Model):
    nombre_departamento = models.CharField('Nombre del departamento', max_length=100, null=False, unique=True)
    descripcion = models.TextField('Descripción', blank=True, default='')
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

class Prioridad(models.Model):
    nivel = models.CharField('Nivel', max_length=30, null=False, unique=True)  # Baja, Media, Alta, Crítica
    tiempo_sla_horas = models.IntegerField('Tiempo SLA (horas)', null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)
    
class Estado(models.Model):
    nombre_estado = models.CharField('Nombre del estado', max_length=50, null=False, unique=True)  # Abierto, En proceso, Pendiente, Resuelto, Cerrado
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

class Ticket(models.Model):
    titulo = models.CharField('Título', max_length=200, null=False)
    descripcion = models.TextField('Descripción', null=False)
    solicitante = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='tickets_solicitados')
    asignado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='tickets_asignados')
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT, related_name='tickets')
    prioridad = models.ForeignKey(Prioridad, on_delete=models.PROTECT, related_name='tickets')
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='tickets')
    fecha_cierre = models.DateTimeField('Fecha de cierre', null=True, blank=True)
    created_at = models.DateTimeField('Fecha Creación', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

class TicketComentario(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comentarios')
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='comentarios')
    mensaje = models.TextField('Mensaje', null=False)
    es_interno = models.BooleanField('Es interno', default=False)  # True = nota privada del equipo
    created_at = models.DateTimeField('Fecha Comentario', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)

class TicketAdjunto(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='adjuntos')
    nombre_archivo = models.CharField('Nombre del archivo', max_length=255, null=False)
    ruta_archivo = models.FileField('Archivo', upload_to='adjuntos/%Y/%m/')
    created_at = models.DateTimeField('Fecha Subida', default=ahora)
    updated_at = models.DateTimeField('Fecha Actualización', auto_now=True)