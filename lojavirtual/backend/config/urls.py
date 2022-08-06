
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from lojavirtualapi.views import ProdutosViewSet
from lojavirtualapi.views import CategoriaViewSet
from rest_framework import routers


routerProduto = routers.DefaultRouter()
routerProduto.register(r'Produto', ProdutosViewSet, basename='Produto')

routerCategoria = routers.DefaultRouter()
routerCategoria.register(r'Categoria', CategoriaViewSet, basename='Categoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produto/', include(routerProduto.urls)),
    path('categoria/', include(routerCategoria.urls)),
]
