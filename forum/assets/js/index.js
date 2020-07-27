require("../scss/app.scss");
import Vue from "vue";

require('./bootstrap');
require('./utils');

Vue.component('comments', require('./components/comments/Comments.vue').default);

const app = new Vue({
    el: "#root",
});