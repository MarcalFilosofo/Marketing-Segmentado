import { createApp } from "vue";
import VueGoogleHeatmap from 'vue-google-heatmap';

import App from "./App.vue";
import store from "./store";
import router from "./router";
import "./assets/css/nucleo-icons.css";
import "./assets/css/nucleo-svg.css";
import ArgonDashboard from "./argon-dashboard";

const appInstance = createApp(App);
appInstance.use(store);
appInstance.use(router);
appInstance.use(ArgonDashboard);
appInstance.use(VueGoogleHeatmap, {
    apiKey: 'AIzaSyDGuxB9seullyc14MZjcf1-OUQdZuzTBs4',
});
appInstance.mount("#app");

