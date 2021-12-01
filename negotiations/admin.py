from django.contrib import admin

from .models import Negotiation, Client, Lawyer

admin.site.register(Negotiation)
admin.site.register(Lawyer)
admin.site.register(Client)
