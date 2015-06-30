from django.contrib import admin 
from pecueshoes.apps.zapatos.models import Zapatos,Marca, Color,Material,Talla,Modelo

admin.site.register(Zapatos)
admin.site.register(Marca)
admin.site.register(Color)
admin.site.register(Material)
admin.site.register(Talla)
admin.site.register(Modelo)