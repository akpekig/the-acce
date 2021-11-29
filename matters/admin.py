from django.contrib import admin

from .models import Client, Contact, Lawyer, Location, Matter, Pretask

admin.site.register(Matter)
admin.site.register(Contact)
admin.site.register(Pretask)
admin.site.register(Location)
admin.site.register(Lawyer)
admin.site.register(Client)
