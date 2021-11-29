from django.contrib import admin

from .models import Account, Client, Lawyer, Location

admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Lawyer)
admin.site.register(Location)