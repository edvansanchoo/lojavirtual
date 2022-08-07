<h1>Projeto Loja Virtual</h1>




<h2><font color="black">Back-End</font></h2>


<h3>Comandos e Frameworks Utilizados n</h3>
<br>
<h4>Para baixar as dependencias do projeto:</h4>
  <pre>python3 -m venv ./venv</pre>

<h4>Para executar a venv:</h4>
  <pre>source vemv/bin/activate</pre>


<h4>Para Instalar o Django depois de executar a venv:</h4>
  <pre>pip install django</pre>

<h4>Caso queira ter certeza das depencias que estão sendo usadas:</h4>
  <pre>pip freeze</pre>

<h4>Para criar a aplicação do djando-admin:</h4>
("config" foi o nome que eu escolhi pode ser outro caso deseje)
  <pre>django-admin startproject config .</pre>

<h4>Para Executar o Servidor:</h4>
  <pre>python manager.py runserver</pre>

# --------------------------------------------------------------------------

<h4>Para não precisar derrubar o server, abra outro terminal</h4>
<h4>&emsp;entre na venv:</h4>
  <pre>source vemv/bin/activate</pre>

<h4>&emsp;Para criar a aplicação:</h4>
  <pre>python manage.py startapp lojavirtualapi</pre>

# --------------------------------------------------------------------------

<h4>Após ter os seus models ccriados, faça a migração para o banco de dados
  <p>Nesse caso estamos usando o Mysqlite</h4>

<h4>(Necessário para poder realizar a contrução das tabelas do banco)
<p>No arquivo config/settings.py
  <p>&emsp;&emsp;Na parte dos INSTALLED_APPS adicione o nome do seu app
  <p>&emsp;&emsp;Nesse caso o nosso foi lojavirtualapi</h4>

<h4>Para fazer a criação das tabelas no banco:
  <pre>python manager.py makemigrations</pre>
<p>e depois:
  <pre>python manager.py migrate</pre>

<h4>Para instalar o django-rest-framework</h4>
  <pre>Link da Documentação:  https://www.django-rest-framework.org/</pre>
  <pre> pip install djangorestframework</pre>

# --------------------------------------------------------------------------

<h4>Para criar um usuario de acesso ao Djando-admin:</h4>
  <pre>python manager.py createsuperuser</pre>
  
  <pre>Link de acesso: http://127.0.0.1:8000/admin/</pre>
# --------------------------------------------------------------------------

<h2><font color="black">EndPoints da API</font></h2>

<h3>PRODUTO:</h3>
<br>

GET:
  <pre>
  ListAllProduto: http://127.0.0.1:8000/produto/Produto/
  FilterByIdProduto: http://127.0.0.1:8000/produto/Produto/3/
  FilterByNomeProduto: http://127.0.0.1:8000/produto/Produto/?nome=Arroz
  FilterByCategoriaProduto: http://127.0.0.1:8000/produto/Produto/?categoria=5
  </pre>
  
POST:
  <pre>
  SaveProduto: http://127.0.0.1:8000/produto/Produto/
  JSON:
  {
    "nome": "Picanha",
    "preco": "60.90",
    "quantidade": 500,
    "categoria": 5
  }
  </pre>
    
PUT:
  <pre>
  UpdateProduto: http://127.0.0.1:8000/produto/Produto/8/
  JSON:
    {
      "id": 8,
      "nome": "Picanha",
      "preco": "60.90",
      "quantidade": 300,
      "categoria": 5
    }
  </pre>
    
DELETE:
  <pre>
  DeleteProduto: http://127.0.0.1:8000/produto/Produto/8/
  </pre>
    

# -------------------------------------------------------------------------
<h3>CATEGORIA:</h3>

GET:
  <pre>
  ListAllCategoria: http://127.0.0.1:8000/categoria/Categoria
  FilterByIdCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  FilterByNomeCategoria: http://127.0.0.1:8000/categoria/Categoria/?nome=Higiene
  </pre>
POST:
  <pre>
  SavaCategoria: http://127.0.0.1:8000/categoria/Categoria/
  JSON:
    {
      "nome": "Pets em Geral"
    }
  </pre>
    
PUT:
  <pre>
  UpdateCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  JSON:
    {
      "id": 2,
      "nome": "Limpeza Geral"
    }
  </pre>
    
DELETE:
  <pre>
  DeleteCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  </pre>


