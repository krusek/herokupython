from django.contrib import admin

from .models import Project
from .models import Ticket
from .models import TicketTime

admin.site.register(Project)
admin.site.register(Ticket)
admin.site.register(TicketTime)

