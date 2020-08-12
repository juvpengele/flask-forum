<template>
    <div class="comment my-2">
        <div class="d-flex align-items-center">
            <img src="https://via.placeholder.com/40" class="rounded-circle mr-2">
            <h6 class="m-0">
                {{ comment.owner.name }}
            </h6>
        </div>
        <div class="comment-content">
            {{ comment.content }}
        </div>
        <div class="d-flex justify-content-end">
            <button class="btn" v-show="isOwner">
                <i class="las la-pencil-alt"></i>
            </button>
            <button class="btn btn-danger " @click="deleteComment" v-show="isOwner">
                <i class="las la-trash text-white"></i>
            </button>
        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        props: [
            'comment'
        ],
        methods: {
            deleteComment() {
                const url = `/api/comments/${this.comment.id}`;

                axios.delete(url)
                    .then(() => this.$emit('delete', this.comment))
                    .catch(e => console.log(e))
            }
        },
        computed: {
            isOwner() {
                return !! window.Auth && window.Auth.id === this.comment.owner.id
            }
        }
    }
</script>

<style>
    .comment {
        background: #fff;
        padding: 1rem
    }

    .comment-content {
        margin-top: .25rem;
        padding-left: 3rem;
    }
</style>