from django.contrib import admin
from chamadaApp.models import Cliente,Plano,Telefone,Categoria

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Plano)
admin.site.register(Telefone)
admin.site.register(Categoria)