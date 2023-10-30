// src/plugins/axios.js
import axios from 'axios';

export default {
  install: (app, options) => {
    app.axios = axios.create({
      baseURL: options.baseURL
    });

    app.config.globalProperties.axios = app.axios;
    app.config.globalProperties.$http = app.axios;
  }
}

