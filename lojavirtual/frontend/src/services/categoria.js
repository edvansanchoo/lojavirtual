import { http } from "./config";

export default {

    getAllCategoria:() => {
        return http.get('categoria/Categoria/')
    }
}