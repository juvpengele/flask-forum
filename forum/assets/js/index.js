require("../scss/app.scss");
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
