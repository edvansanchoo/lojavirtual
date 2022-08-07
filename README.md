<h1>Projeto Loja Virtual</h1>




<h2><font color="black">Back-End</font></h2>


<h3>Comandos e Frameworks Utilizados no</h3>
<br>
<h4>Para baixar as dependencias do projeto:</h4>
  <br><code>&emsp;&emsp;&emsp;python3 -m venv ./venv</code>

<h4>Para executar a venv:</h4>
  <br><code>&emsp;&emsp;&emsp;source vemv/bin/activate</code>


<h4>Para Instalar o Django depois de executar a venv:</h4>
  <br><code>&emsp;&emsp;&emsp;pip install django</code>

<h4>Caso queira ter certeza das depencias que estão sendo usadas:</h4>
  <br><code>&emsp;&emsp;&emsp;pip freeze</code>

<h4>Para criar a aplicação do djando-admin:</h4>
("config" foi o nome que eu escolhi pode ser outro caso deseje)
  <br><code>&emsp;&emsp;&emsp;django-admin startproject config .</code>

<h4>Para Executar o Servidor:</h4>
  <br><code>&emsp;&emsp;&emsp;python manager.py runserver</code>

# --------------------------------------------------------------------------

<h4>Para não precisar derrubar o server, abra outro terminal</h4>
<h4>&emsp;entre na venv:</h4>
  <br><code>&emsp;&emsp;&emsp;source vemv/bin/activate</code>

<h4>&emsp;Para criar a aplicação:</h4>
  <br><code>&emsp;&emsp;&emsp;python manager.py startapp lojavirtualapi</code>

# --------------------------------------------------------------------------

<h4>Após ter os seus models ccriados, faça a migração para o banco de dados
  <br>Nesse caso estamos usando o Mysqlite</h4>

<h4>(Necessário para poder realizar a contrução das tabelas do banco)
<br>No arquivo config/settings.py
  <br>&emsp;&emsp;Na parte dos INSTALLED_APPS adicione o nome do seu app
  <br>&emsp;&emsp;Nesse caso o nosso foi lojavirtualapi</h4>

<h4>Para fazer a criação das tabelas no banco:
  <br><code>&emsp;&emsp;&emsp;&emsp;python manager.py makemigrations</code>
<br>e depois:
  <br><code>&emsp;&emsp;python manager.py migrate</code></h4>

# --------------------------------------------------------------------------

<h4>Para criar um usuario de acesso ao Djando-admin:</h4>
  <br><code>&emsp;&emsp;&emsp;python manager.py createsuperuser</code>
  
  Link de acesso: 
    <br>&emsp;&emsp;&emsp;http://127.0.0.1:8000/admin/

# --------------------------------------------------------------------------

<h2><font color="black">EndPoints da API</font></h2>

<h3>PRODUTO:</h3>
<br>

GET:
  <br>&emsp;ListAllProduto: http://127.0.0.1:8000/produto/Produto/
  <br>&emsp;FilterByIdProduto: http://127.0.0.1:8000/produto/Produto/3/
  <br>&emsp;FilterByNomeProduto: http://127.0.0.1:8000/produto/Produto/?nome=Arroz
  <br>&emsp;FilterByCategoriaProduto: http://127.0.0.1:8000/produto/Produto/?categoria=5
  
POST:
  <br>&emsp;SaveProduto: http://127.0.0.1:8000/produto/Produto/
  <br>&emsp;&emsp;JSON:
  <code><br>&emsp;&emsp;&emsp;{
    <br>&emsp;&emsp;&emsp;&emsp;"nome": "Picanha",
    <br>&emsp;&emsp;&emsp;&emsp;"preco": "60.90",
    <br>&emsp;&emsp;&emsp;&emsp;"quantidade": 500,
    <br>&emsp;&emsp;&emsp;&emsp;"categoria": 5
  <br>&emsp;&emsp;&emsp;}</code>
    
PUT:
  <br>&emsp;UpdateProduto: http://127.0.0.1:8000/produto/Produto/8/
  <br>&emsp;&emsp;JSON:
  <code><br>&emsp;&emsp;&emsp;{
    <br>&emsp;&emsp;&emsp;&emsp;"id": 8,
    <br>&emsp;&emsp;&emsp;&emsp;"nome": "Picanha",
    <br>&emsp;&emsp;&emsp;&emsp;"preco": "60.90",
    <br>&emsp;&emsp;&emsp;&emsp;"quantidade": 300,
    <br>&emsp;&emsp;&emsp;&emsp;"categoria": 5
  <br>&emsp;&emsp;&emsp;}</code>
    
DELETE:
  <br>&emsp;DeleteProduto: http://127.0.0.1:8000/produto/Produto/8/
    

# -------------------------------------------------------------------------
<h3>CATEGORIA:</h3>

GET:
  <br>&emsp;ListAllCategoria: http://127.0.0.1:8000/categoria/Categoria
  <br>&emsp;FilterByIdCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  <br>&emsp;FilterByNomeCategoria: http://127.0.0.1:8000/categoria/Categoria/?nome=Higiene
  
POST:
  <br>&emsp;SavaCategoria: http://127.0.0.1:8000/categoria/Categoria/
  <br>&emsp;&emsp;JSON:
  <code>{
    <p>"nome": "Pets em Geral"
  }</code>
    
PUT:
  <br>&emsp;UpdateCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  <br>&emsp;&emsp;JSON:
  <code><br>&emsp;&emsp;&emsp;{
    <br>&emsp;&emsp;&emsp;&emsp;"id": 2,
    <br>&emsp;&emsp;&emsp;&emsp;"nome": "Limpeza Geral"
  <br>&emsp;&emsp;&emsp;}</code>
    
DELETE:
  <br>&emsp;DeleteCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  
