from django.contrib import admin
from .models import Edicao, Cor, Tipo, Raridade, Card


# Register your models here.
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','nome_ingles','edicao','cor','tipo','raridade')
    list_display_links = ('id','nome','nome_ingles')
    list_filter = ('edicao__nome','cor__nome','tipo__nome','raridade__nome')
    list_per_page = 20
    search_fields = ('nome','nome_ingles')


admin.site.register(Edicao)
admin.site.register(Cor)
admin.site.register(Tipo)
admin.site.register(Raridade)
admin.site.register(Card, CardAdmin)

