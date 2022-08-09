<template>
    <div id="nav">
        <router-link to="/">
            <img :src="logo" :alt="alt" id="logo">
        </router-link>
        <router-link to="/">Home</router-link> 
        <router-link to="/Produtos">Produtos</router-link>
        <router-link to="/Categorias">Categorias</router-link>
    </div>
</template>
<script>
export default {
    name: "Navbar",
    props: ["logo", "alt"]
}
</script>
<style scoped>
    #nav {
        background-color: #222;
        border-bottom: 4px solid #111;
        padding: 15px 50px;
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }

    #nav a {
        color: #FCBA03;
        text-decoration: none;
        margin: 12px;
        transition: .5s;
    }

    #nav a:hover {
        color: #FFF;
    }
</style>