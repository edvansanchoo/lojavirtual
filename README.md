<h1>Projeto Loja Virtual</h1>

<h3>Projeto Criado no Sitema Operacional: Linux Mint 20.3</h3>

<h2><font color="black">Front-End</font></h2>

<h3>Instalar NodeJS 16</h3>

<pre><code>
  Link do Site de tutorial:  https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04-pt

  cd ~
  curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh

  nano nodesource_setup.sh

  sudo bash nodesource_setup.sh

  sudo apt install nodejs

  node -v
</code></pre>

<h3>Instalar npm</h3>
<pre><code>sudo apt install npm -y</code></pre>

<h3>Instalar Vue CLI de Forma Global</h3>
<pre><code>sudo npm install -g @vue/cli</code></pre>

<h2><font color="black">Back-End</font></h2>


<h3>Comandos e Frameworks Utilizados</h3>
<br>
<h4>Para baixar as dependencias do projeto:</h4>
  <pre><code>python3 -m venv ./venv</code></pre>

<h4>Para executar a venv:</h4>
  <pre><code>source venv/bin/activate</code></pre>


<h4>Para Instalar o Django depois de executar a venv:</h4>
  <pre><code>pip install django</code></pre>

<h4>Caso queira ter certeza das depencias que estão sendo usadas:</h4>
  <pre><code>pip freeze</code></pre>

<h4>Para criar a aplicação do djando-admin:</h4>
("config" foi o nome que eu escolhi pode ser outro caso deseje)
  <pre>django-admin startproject config .</pre>

<h4>Para Executar o Servidor:</h4>
  <pre><code>python manager.py runserver</code></pre>

# --------------------------------------------------------------------------

<h4>Para não precisar derrubar o server, abra outro terminal</h4>
<h4>&emsp;entre na venv:</h4>
  <pre><code>source vemv/bin/activate</code></pre>

<h4>&emsp;Para criar a aplicação:</h4>
  <pre><code>python manage.py startapp lojavirtualapi</code></pre>

# --------------------------------------------------------------------------

<h4>Após ter os seus models criados, faça a migração para o banco de dados
  <p>Nesse caso estamos usando o SQLite</h4>

<h4>(Necessário para poder realizar a contrução das tabelas do banco)
<p>No arquivo config/settings.py
  <p>&emsp;&emsp;Na parte dos INSTALLED_APPS adicione o nome do seu app
  <p>&emsp;&emsp;Nesse caso o nosso foi lojavirtualapi</h4>

<h4>Para fazer a criação das tabelas no banco:
  <pre><code>python manager.py makemigrations</code></pre>
<p>e depois:
  <pre><code>python manager.py migrate</code></pre>

<h4>Para instalar o django-rest-framework</h4>
  <pre><code>Link da Documentação:  https://www.django-rest-framework.org/</code></pre>
  <pre><code> pip install djangorestframework</code></pre>

# --------------------------------------------------------------------------

<h4>Para criar um usuario de acesso ao Djando-admin:</h4>
  <pre><code>python manager.py createsuperuser</code></pre>
  
  <pre><code>Link de acesso: http://127.0.0.1:8000/admin/</code></pre>
# --------------------------------------------------------------------------

<h2><font color="black">EndPoints da API</font></h2>

<h3>PRODUTO:</h3>
<br>

GET:
  <pre><code>
  ListAllProduto: http://127.0.0.1:8000/produto/Produto/
  FilterByIdProduto: http://127.0.0.1:8000/produto/Produto/3/
  FilterByNomeProduto: http://127.0.0.1:8000/produto/Produto/?nome=Arroz
  FilterByCategoriaProduto: http://127.0.0.1:8000/produto/Produto/?categoria=5
  </code></pre>
  
POST:
  <pre><code>
  SaveProduto: http://127.0.0.1:8000/produto/Produto/
  JSON:
  {
    "nome": "Picanha",
    "preco": "60.90",
    "quantidade": 500,
    "categoria": 5
  }
  </code></pre>
    
PUT:
  <pre><code>
  UpdateProduto: http://127.0.0.1:8000/produto/Produto/8/
  JSON:
    {
      "id": 8,
      "nome": "Picanha",
      "preco": "60.90",
      "quantidade": 300,
      "categoria": 5
    }
  </code></pre>
    
DELETE:
  <pre><code>
  DeleteProduto: http://127.0.0.1:8000/produto/Produto/8/
  </code></pre>
    

# -------------------------------------------------------------------------
<h3>CATEGORIA:</h3>

GET:
  <pre><code>
  ListAllCategoria: http://127.0.0.1:8000/categoria/Categoria
  FilterByIdCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  FilterByNomeCategoria: http://127.0.0.1:8000/categoria/Categoria/?nome=Higiene
  </code></pre>
POST:
  <pre><code>
  SavaCategoria: http://127.0.0.1:8000/categoria/Categoria/
  JSON:
    {
      "nome": "Pets em Geral"
    }
  </code></pre>
    
PUT:
  <pre><code>
  UpdateCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  JSON:
    {
      "id": 2,
      "nome": "Limpeza Geral"
    }
  </code></pre>
    
DELETE:
  <pre><code>
  DeleteCategoria: http://127.0.0.1:8000/categoria/Categoria/2/
  </code></pre>


