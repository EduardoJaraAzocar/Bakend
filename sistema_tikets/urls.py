from django.urls import path, include
from rest_framework import routers
from sistema_tikets import views

enrutador = routers.DefaultRouter()

enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'departamentos', views.DepartamentoViewSet)
enrutador.register(r'prioridades', views.PrioridadViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'tickets', views.TicketViewSet)
enrutador.register(r'ticket-comentarios', views.TicketComentarioViewSet)
enrutador.register(r'ticket-adjuntos', views.TicketAdjuntoViewSet)

urlpatterns = [
    path('', include(enrutador.urls))
]