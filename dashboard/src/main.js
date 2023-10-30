// src/main.js
import { createApp } from 'vue'
import App from './App.vue';
import axiosPlugin from './plugins/axios';
import router from './plugins/router';
import 'bootstrap/dist/css/bootstrap.css';

createApp(App)
  .use(axiosPlugin, { baseURL: 'http://localhost:8000' })
  .use(router)
  .mount('#app');
