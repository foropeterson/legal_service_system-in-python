from django.contrib import admin
from .models import Client, Lawyer, Case, Appointment, Document

admin.site.register(Client)
admin.site.register(Lawyer)
admin.site.register(Case)
admin.site.register(Appointment)
admin.site.register(Document)
