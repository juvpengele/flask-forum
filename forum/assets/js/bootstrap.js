window.$ = require('jquery');
window.axios = require('axios');
require('popper.js');
require('bootstrap');

window.iziToast = require('izitoast');


let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRFToken'] = token.content;
} else {
    console.error("Missing CSRF Token");
}
