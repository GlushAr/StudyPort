import {domain} from "../constants";
import axios from "axios";

export default class FirstService {
    static async GetFirstList() {
        const response = await axios.get(`${domain}/first`)
        return response.data
    }

    static async create(name, type) {
        const response = await axios.post(`${domain}/first`, {
            full_name: name,
            type: type
        })
        return response.data
    }

}
