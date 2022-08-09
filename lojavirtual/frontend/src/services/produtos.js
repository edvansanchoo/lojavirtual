import { http } from "./config";

export default {

    getAllProdutos:() => {
        return http.get('produto/Produto/')
    }
}