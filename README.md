# Loja Virtual


#------------------------------------

Back-End

Comandos e Frameworks Utilizados

Para baixar as dependencias do projeto:
    - python3 -m venv ./venv

Para executar a venv:
    source vemv/bin/activate


Para Instalar o Django depois de executar a venv:
    pip install django

Caso queira ter certeza das depencias que estão sendo usadas:
    pip freeze

Para criar a aplicação do djando-admin:
("config" foi o nome que eu escolhi pode ser outro caso deseje)
    django-admin startproject config .

Para Executar o Servidor:
    python manager.py runserver

#-------------------------------------------------------------------

Para não precisar derrubar o server, abra outro terminal
entre na venv:
    source vemv/bin/activate

Para criar a aplicação:
    python manager.py startapp lojavirtualapi

#--------------------------------------------------------------------------

Após ter os seus models ccriados, faça a migração para o banco de dados
Nesse caso estamos usando o Mysqlite

(Necessário para poder realizar a contrução das tabelas do banco)
No arquivo config/settings.py
    Na parte dos INSTALLED_APPS adicione o nome do seu app
    Nesse caso o nosso foi lojavirtualapi

Para fazer a criação das tabelas no banco:
    python manager.py makemigrations
e depois:
    python manager.py migrate

#--------------------------------------------------------------------------

Para criar um usuario de acesso ao Djando-admin:
  python manager.py createsuperuser
  
  Link de acesso: 
    http://127.0.0.1:8000/admin/

#=========================================================================

EndPoint da API

PRODUTO:

GET:
  ListAllProduto: http://127.0.0.1:8000/produto/Produto/
  FilterByIdProduto: http://127.0.0.1:8000/produto/Produto/3/
  FilterByNomeProduto: http://127.0.0.1:8000/produto/Produto/?nome=Arroz
  FilterByCategoriaProduto: http://127.0.0.1:8000/produto/Produto/?categoria=5
  
POST:
  SaveProduto: http://127.0.0.1:8000/produto/Produto/
  JSON:
    {
      "nome": "Picanha",
      "preco": "60.90",
      "quantidade": 500,
      "categoria": 5
    }
    
PUT:
  UpdateProduto: http://127.0.0.1:8000/produto/Produto/8/
  JSON:
    {
      "id": 8,
      "nome": "Picanha",
      "preco": "60.90",
      "quantidade": 300,
      "categoria": 5
    }
    
DELETE:
  DeleteProduto: http://127.0.0.1:8000/produto/Produto/8/
    

#-------------------------------------------------------------------------
CATEGORIA:

GET:
  ListAllCategoria: http://127.0.0.1:8000/categoria/Categoria
  FilterByIdCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  FilterByNomeCategoria: http://127.0.0.1:8000/categoria/Categoria/?nome=Higiene
  
POST:
  SavaCategoria: http://127.0.0.1:8000/categoria/Categoria/
  JSON:
    {
      "nome": "Pets em Geral"
    }
    
PUT:
  UpdateCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  JSON:
    {
      "id": 2,
      "nome": "Limpeza Geral"
    }
    
DELETE:
  DeleteCategoria: http://127.0.0.1:8000/categoria/Categoria/2/






