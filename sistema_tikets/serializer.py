from rest_framework import serializers

from . import models


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'rol', 'created_at')
        # Se excluye la contraseña para que no se exponga en la API


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departamento
        fields = ('__all__')
        # __all__ serializa todos los atributos de la clase/modelo


class PrioridadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prioridad
        fields = ('__all__')


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estado
        fields = ('__all__')


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = ('__all__')


class TicketComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TicketComentario
        fields = ('ticket', 'usuario', 'mensaje', 'es_interno', 'created_at')
        # De esta forma decidimos qué atributos se serializan


class TicketAdjuntoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TicketAdjunto
        fields = ('ticket', 'nombre_archivo', 'ruta_archivo', 'created_at')