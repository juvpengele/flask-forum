require("../scss/app.scss");
import Vue from "vue";

require('./bootstrap');
require('./utils');

Vue.component('example-component', require('./components/ExampleComponent.vue').default);

const app = new Vue({
    el: "#root",
});