from django.contrib import admin
from lojavirtualapi.models import Produto
from lojavirtualapi.models import Categoria


class Produtos(admin.ModelAdmin):
    list_display=('id', 'nome', 'quantidade', 'preco', 'categoria')
    list_display_links = ('id', 'nome', 'categoria')
    search_fields = ('nome', 'categoria',)

class Categorias(admin.ModelAdmin):
    list_display=('id', 'nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)


admin.site.register(Produto, Produtos)
admin.site.register(Categoria, Categorias)