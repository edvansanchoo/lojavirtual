from unicodedata import category
from rest_framework import viewsets
from lojavirtualapi.models import Produto
from lojavirtualapi.models import Categoria
from lojavirtualapi.serializer import ProdutoSerilizer
from lojavirtualapi.serializer import CategoriaSerilizer


class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerilizer
    def get_queryset(self):
        queryset = Produto.objects.all()
        categoria = self.request.query_params.get('categoria')
        nome = self.request.query_params.get('nome')
        
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        elif nome:
            queryset = queryset.filter(nome=nome)

        return queryset

class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerilizer  

    def get_queryset(self):
        queryset = Categoria.objects.all()
        nome = self.request.query_params.get('nome')
        
        if nome:
            queryset = queryset.filter(nome=nome)

        return queryset
