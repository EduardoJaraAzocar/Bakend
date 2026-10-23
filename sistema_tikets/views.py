from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializer


def bienvenida(request):
    return render(request, "bienvenida.html")


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializer.UsuarioSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = models.Departamento.objects.all()
    serializer_class = serializer.DepartamentoSerializer


class PrioridadViewSet(viewsets.ModelViewSet):
    queryset = models.Prioridad.objects.all()
    serializer_class = serializer.PrioridadSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = models.Estado.objects.all()
    serializer_class = serializer.EstadoSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = models.Ticket.objects.all()
    serializer_class = serializer.TicketSerializer


class TicketComentarioViewSet(viewsets.ModelViewSet):
    queryset = models.TicketComentario.objects.all()
    serializer_class = serializer.TicketComentarioSerializer


class TicketAdjuntoViewSet(viewsets.ModelViewSet):
    queryset = models.TicketAdjunto.objects.all()
    serializer_class = serializer.TicketAdjuntoSerializer