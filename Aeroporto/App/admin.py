from django.contrib import admin
from App.models import Aereo, Aeroporto, Personale, Turni, Volo, Admin

# Register your models here.
admin.site.register(Volo)
admin.site.register(Aeroporto)
admin.site.register(Personale)
admin.site.register(Aereo)
admin.site.register(Turni)
admin.site.register(Admin)