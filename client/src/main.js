import {createApp} from 'vue'
import App from './App.vue'
import axios from "axios";
import Vuelidate from "vuelidate";
import router from './router'

axios.defaults.baseURL = "http://localhost:5000/";

createApp(App).use(router,Vuelidate).mount('#app')
