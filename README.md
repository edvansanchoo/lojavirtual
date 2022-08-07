<h1>Projeto Loja Virtual</h1>




<h2><font color="black">Back-End</font></h2>


<h3>Comandos e Frameworks Utilizados no</h3>
<br>
<h4>Para baixar as dependencias do projeto:</h4>
  <p><code>&emsp;&emsp;&emsp;python3 -m venv ./venv</code>

<h4>Para executar a venv:</h4>
  <p><code>&emsp;&emsp;&emsp;source vemv/bin/activate</code>


<h4>Para Instalar o Django depois de executar a venv:</h4>
  <p><code>&emsp;&emsp;&emsp;pip install django</code>

<h4>Caso queira ter certeza das depencias que estão sendo usadas:</h4>
  <p><code>&emsp;&emsp;&emsp;pip freeze</code>

<h4>Para criar a aplicação do djando-admin:</h4>
("config" foi o nome que eu escolhi pode ser outro caso deseje)
  <p><code>&emsp;&emsp;&emsp;django-admin startproject config .</code>

<h4>Para Executar o Servidor:</h4>
  <p><code>&emsp;&emsp;&emsp;python manager.py runserver</code>

# --------------------------------------------------------------------------

<h4>Para não precisar derrubar o server, abra outro terminal</h4>
<h4>&emsp;entre na venv:</h4>
  <p><code>&emsp;&emsp;&emsp;source vemv/bin/activate</code>

<h4>&emsp;Para criar a aplicação:</h4>
  <p><code>&emsp;&emsp;&emsp;python manager.py startapp lojavirtualapi</code>

# --------------------------------------------------------------------------

<h4>Após ter os seus models ccriados, faça a migração para o banco de dados
  <p>Nesse caso estamos usando o Mysqlite</h4>

<h4>(Necessário para poder realizar a contrução das tabelas do banco)
<p>No arquivo config/settings.py
  <p>&emsp;&emsp;Na parte dos INSTALLED_APPS adicione o nome do seu app
  <p>&emsp;&emsp;Nesse caso o nosso foi lojavirtualapi</h4>

<h4>Para fazer a criação das tabelas no banco:
  <p><code>&emsp;&emsp;&emsp;&emsp;python manager.py makemigrations</code>
<p>e depois:
  <p><code>&emsp;&emsp;python manager.py migrate</code></h4>

# --------------------------------------------------------------------------

<h4>Para criar um usuario de acesso ao Djando-admin:</h4>
  <p><code>&emsp;&emsp;&emsp;python manager.py createsuperuser</code>
  
  Link de acesso: 
    <p>&emsp;&emsp;&emsp;http://127.0.0.1:8000/admin/

# --------------------------------------------------------------------------

<h2><font color="black">EndPoints da API</font></h2>

<h3>PRODUTO:</h3>
<br>

GET:
  <p>&emsp;ListAllProduto: http://127.0.0.1:8000/produto/Produto/
  <p>&emsp;FilterByIdProduto: http://127.0.0.1:8000/produto/Produto/3/
  <p>&emsp;FilterByNomeProduto: http://127.0.0.1:8000/produto/Produto/?nome=Arroz
  <p>&emsp;FilterByCategoriaProduto: http://127.0.0.1:8000/produto/Produto/?categoria=5
  
POST:
  <p>&emsp;SaveProduto: http://127.0.0.1:8000/produto/Produto/
  <p>&emsp;&emsp;JSON:
  <code><p>&emsp;&emsp;&emsp;{
    <p>&emsp;&emsp;&emsp;&emsp;"nome": "Picanha",
    <p>&emsp;&emsp;&emsp;&emsp;"preco": "60.90",
    <p>&emsp;&emsp;&emsp;&emsp;"quantidade": 500,
    <p>&emsp;&emsp;&emsp;&emsp;"categoria": 5
  <p>&emsp;&emsp;&emsp;}</code>
    
PUT:
  <p>&emsp;UpdateProduto: http://127.0.0.1:8000/produto/Produto/8/
  <p>&emsp;&emsp;JSON:
  <code><p>&emsp;&emsp;&emsp;{
    <p>&emsp;&emsp;&emsp;&emsp;"id": 8,
    <p>&emsp;&emsp;&emsp;&emsp;"nome": "Picanha",
    <p>&emsp;&emsp;&emsp;&emsp;"preco": "60.90",
    <p>&emsp;&emsp;&emsp;&emsp;"quantidade": 300,
    <p>&emsp;&emsp;&emsp;&emsp;"categoria": 5
  <p>&emsp;&emsp;&emsp;}</code>
    
DELETE:
  <p>&emsp;DeleteProduto: http://127.0.0.1:8000/produto/Produto/8/
    

# -------------------------------------------------------------------------
<h3>CATEGORIA:</h3>

GET:
  <p>&emsp;ListAllCategoria: http://127.0.0.1:8000/categoria/Categoria
  <p>&emsp;FilterByIdCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  <p>&emsp;FilterByNomeCategoria: http://127.0.0.1:8000/categoria/Categoria/?nome=Higiene
  
POST:
  <p>&emsp;SavaCategoria: http://127.0.0.1:8000/categoria/Categoria/
  <p>&emsp;&emsp;JSON:
  <code><p>&emsp;&emsp;&emsp;{
    <p>&emsp;&emsp;&emsp;&emsp;"nome": "Pets em Geral"
  <p>&emsp;&emsp;&emsp;}</code>
    
PUT:
  <p>&emsp;UpdateCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  <p>&emsp;&emsp;JSON:
  <code><p>&emsp;&emsp;&emsp;{
    <p>&emsp;&emsp;&emsp;&emsp;"id": 2,
    <p>&emsp;&emsp;&emsp;&emsp;"nome": "Limpeza Geral"
  <p>&emsp;&emsp;&emsp;}</code>
    
DELETE:
  <p>&emsp;DeleteCategoria: http://127.0.0.1:8000/categoria/Categoria/2/






