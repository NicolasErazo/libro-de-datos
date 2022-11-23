from django.contrib import admin
from .models import Afiliado
from .models import Usuario

class AfiliadosAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


# Register your models here.
admin.site.register(Afiliado, AfiliadosAdmin) 
admin.site.register(Usuario) 
