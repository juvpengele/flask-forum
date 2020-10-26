require("../scss/app.scss");
require('bootstrap-select');

import Vue from "vue";


require('./bootstrap');
require('./utils');

Vue.component('comments', require('./components/comments/Comments.vue').default);
Vue.component('avatar-uploader', require('./components/avatar/AvatarUploader.vue').default);
Vue.component('avatar', require('./components/avatar/Avatar.vue').default);


const vueEvent = new Vue();
window.EventDispatcher = new class {
    fire(event, data = null) {
        vueEvent.$emit(event, data);
    }

    listen(event, handler) {
        vueEvent.$on(event, handler)
    }
}


const app = new Vue({
    el: "#root",
});


$(document).ready(function() {
    $('.select').selectpicker();
    $("#primary-filter").on("changed.bs.select",  function (event) {
        let url = window.location.origin + "/";

        if(event.target.value === "popular") {
            url = url + "?popular=true"
        }

        if(window.location.href !== url) {
            window.location.href = url;
        }
    })
});