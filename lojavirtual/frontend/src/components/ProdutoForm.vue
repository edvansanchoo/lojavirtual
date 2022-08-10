<template>
    <div>
        <p>Componente de Mensagem</p>
    <div>
        <form id="produto-form" @submit="salvarProduto">
            <div class="input-container">
                <label for="nome">Nome do Produto: </label>
                <input type="text" id="nome" name="name" v-model="produto.nome" placeholder="Digite o nome do Produto">
            </div>
            <div class="input-container">
                <label for="preco">Preço do Produto: </label>
                <input type="text" id="preco" name="preco" v-model="produto.preco" placeholder="R$:">
            </div>
            <div class="input-container">
                <label for="quantidade">Quantidade do Produto: </label>
                <input type="text" id="quantidade" name="quantidade" v-model="produto.quantidade" placeholder="Digite a quantidade de Produtos">
            </div>
            <div class="input-container">
                <label id="categoria-title" for="categoria">Escolha a Categoria do Produto: </label>
                <select name="categoria" id="categoria" v-model="produto.categoria">
                    <option value="">Selecione a categoria</option>
                    <option v-for="categoria in categoriadata" :key="categoria.id" :value="categoria.nome">{{categoria.nome}}</option>
                </select>
            </div>
            <div class="input-container">
                <input type="submit" class="submit-btn" value="Salvar Produto">
            </div>
        </form>
    </div>
    </div>
</template>

<script>
import Categoria from '../services/categoria'

export default {
    name: "ProdutoForm",
    data() {
        return {
            produto: {
                nome: null,
                preco: null,
                quantidade: null,
                categoria: null
            },
            categoriadata: []
        }
    },
    methods:{
        salvarProduto(){
            alert(this.produto.nome)
        }
    },
    mounted(){
        Categoria.getAllCategoria().then(resposta => {
            this.categoriadata = resposta.data
        })
    }
}
</script>
<style scoped>
    #produto-form {
        max-width: 400px;
        margin: 0 auto;
    }
    .input-container {
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
        
    }
    label {
        font-weight: bold;
        margin-bottom: 15px;
        color: #222;
        padding: 5px 10px;
        border-left: 4px solid #FCBA03;
    }
    input, select {
        pad: 5px 10px;
        width: 300px;
        padding-bottom: 10px;
    }
    .categoria-title {
        width: 100%;
    }

    .submit-btn {
        background-color: #222;
        color: #FCBA03;
        font-weight: bold;
        border: 2px solid #222;
        padding: 10px;
        font-size: 16px;
        margin: 0 auto;
        cursor: pointer;
        transition: .5s;
    }

    .submit-btn:hover {
        background-color: transparent;
        color: #222;
    }

</style>