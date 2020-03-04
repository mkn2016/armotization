import Vue from "vue";
import './plugins/fontawesome'

import BootstrapVue from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

Vue.use(BootstrapVue)

new Vue({
  router,
  store,
  components: {App},
  render: h => h(App)
}).$mount("#app");
