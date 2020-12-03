<template>
    <div class="my-4 bg-white px-2 py-3">
        <form method="POST" @submit.prevent="handleSubmit" v-if="canComment">
            <div class="d-flex align-items-start">
                <img :src="auth.profilePicture" class="rounded-circle mr-2" width="50"/>
                <div class="flex-1">
                    <textarea class="form-control" placeholder="Your comment..." v-model="content" @keydown="clearInput('content')"></textarea>
                    <span class="text-danger" v-if="errors.has('content')">{{ errors.get("content")}}</span>
                </div>
            </div>
            <div class="d-flex justify-content-end mt-2">
                <button class="btn btn-primary btn-sm form-btn" :disabled="isSending">
                    <span v-if="! isSending" class="text-white">
                        Add comment
                    </span>
                    <span class="text-white" v-else>Commenting... <i class='las la-circle-notch la-spin text-white'></i></span>
                </button>
            </div>
        </form>
        <div v-else>
            <div class="text-center" v-html="restrictionMessage">
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    import Errors from "../../utils/Errors";

    export default {
        props: {
            threadId: {
                type: Number,
                required: true
            }
        },
        data() {
            return {
                content: "",
                auth: window.Auth,
                errors: new Errors(),
                isSending: false
            }
        },
        methods: {
            handleSubmit() {
                this.isSending = true;

                axios.post(`/api/threads/${this.threadId}/comments`, {content: this.content})
                    .then(({data}) => {
                        this.content = "";
                        this.$emit('submit', data);
                    })
                    .catch(error => this.errors.record(error.response.data))
                    .finally(() => this.isSending = false)
            },
            clearInput(key) {
                if(this.errors.has(key)) {
                    this.errors.clear(key);
                }
            }
        },
        computed: {
            canComment() {
                return  !! window.Auth && window.Auth.email_verified;
            },
            restrictionMessage() {
                
                if(! window.Auth) {
                    return `
                        To comment, you must <a href="/login">login</a>
                    `
                }

                if(! window.Auth.email_verified){
                    return `You must validate your email to comment`
                }

                return ""
            }
        }
    }
</script>

<style>
    .flex-1 {
        flex: 1;
    }

    .form-btn {
        min-width: 120px;
    }
</style>