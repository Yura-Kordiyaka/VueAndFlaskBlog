import {createApp} from 'vue'
import App from './App.vue'
import axios from "axios";
import router from './router'


/* import the fontawesome core */
import {library} from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {faUser,faThumbsUp,faThumbsDown,faUserSecret} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faUser,faThumbsUp, faUserSecret,faThumbsDown)

// createApp(App)
//     .component('font-awesome-icon', FontAwesomeIcon)
//     .mount('#app')

axios.defaults.baseURL = "http://localhost:5000/";

createApp(App).use(router).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
