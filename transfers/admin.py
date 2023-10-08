from django.contrib import admin
from .models import Client, Transfer

# Enregistrez les modèles dans le panneau d'administration
class trasfertModelAdmin(admin.ModelAdmin):
    list_display = ('sender','recipient','amount','code')

admin.site.register(Client)
admin.site.register(Transfer,trasfertModelAdmin)

