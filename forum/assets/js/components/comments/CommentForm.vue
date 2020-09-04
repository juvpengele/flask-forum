<template>
    <div class="my-4 bg-white px-2 py-3">
        <form method="POST" @submit.prevent="handleSubmit" v-if="canComment">
            <div class="d-flex align-items-start">
                <img :src="auth.profilePicture" class="rounded-circle mr-2" width="50"/>
                <div class="flex-1">
                    <textarea class="form-control" placeholder="Your comment..." v-model="content">
                    </textarea>
                </div>
            </div>
            <div class="d-flex justify-content-end mt-2">
                <button class="btn btn-primary btn-sm">Add a comment</button>
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
                auth: window.Auth
            }
        },
        methods: {
            handleSubmit() {
                axios.post(`/api/threads/${this.threadId}/comments`, {content: this.content})
                    .then(({data}) => {
                        this.content = "";
                        this.$emit('submit', data);
                    })
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
</style>