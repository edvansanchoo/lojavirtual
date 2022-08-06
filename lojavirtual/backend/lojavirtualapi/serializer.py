from rest_framework import serializers
from lojavirtualapi.models import Produto
from lojavirtualapi.models import Categoria


class ProdutoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__' 


class CategoriaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__' 