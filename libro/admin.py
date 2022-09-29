from django.contrib import admin
from .models import Afiliado

class AfiliadosAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

# Register your models here.
admin.site.register(Afiliado, AfiliadosAdmin) 