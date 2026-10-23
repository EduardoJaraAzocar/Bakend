from django.contrib import admin
from .models import (
    Usuario,
    Departamento,
    Prioridad,
    Estado,
    Ticket,
    TicketComentario,
    TicketAdjunto,
)
admin.site.register(Usuario)
admin.site.register(Departamento)
admin.site.register(Prioridad)
admin.site.register(Estado)
admin.site.register(Ticket)
admin.site.register(TicketComentario)
admin.site.register(TicketAdjunto)