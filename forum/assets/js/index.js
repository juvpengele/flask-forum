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
    const primaryFilter = $("#primary-filter");
    const secondaryFilter = $("#secondary-filter");

    function _primaryFilterValue(primaryFilterValue) {
        if(primaryFilterValue === "recent") {
            return null
        }

        return `${primaryFilterValue}=true`;
    }

    function _secondaryFilterValue(secondaryFilterValue) {
        if(secondaryFilterValue === "all") {
            return null;
        }

        return `filter=${secondaryFilterValue}`;
    }

    function filterLink() {
        let url = window.location.origin + "/";
        let queryParams;

        let primaryFilterValue = _primaryFilterValue(primaryFilter.val());
        let secondaryFilterValue = _secondaryFilterValue(secondaryFilter.val());

        if(primaryFilterValue === null || secondaryFilterValue === null) {
            if(primaryFilterValue !== null) {
                queryParams = primaryFilterValue;
            }

            if(secondaryFilterValue !== null) {
                queryParams = secondaryFilterValue;
            }
        } else {
            queryParams = `${primaryFilterValue}&${secondaryFilterValue}`;
        }


        if(queryParams) {
            return url + "?" + queryParams;
        }

        return url;
    }

    function _redirect() {
        const url = filterLink();

        if(window.location.href !== url) {
            window.location.href = url;
        }
    }

    primaryFilter.on("changed.bs.select",  _redirect);
    secondaryFilter.on("changed.bs.select", _redirect);
});
