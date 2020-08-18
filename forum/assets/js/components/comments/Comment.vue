<template>
    <div class="comment my-2">
        <div class="d-flex align-items-center">
            <img :src="comment.owner.profile_picture" class="rounded-circle mr-2" width="25">
            <h6 class="m-0">
                {{ comment.owner.name }}
            </h6>
        </div>
        <div class="comment-content">
            <textarea v-model="content" class="form-control mb-2" v-show="editing"></textarea>
            <div v-if="! editing">
                {{ comment.content }}
            </div>

        </div>
        <div class="d-flex justify-content-end">
            <div class="d-flex" v-if="! editing">
                <button class="btn btn-light mr-2" v-show="isOwner" @click="showEditionInput">
                    <i class="las la-pencil-alt"></i>
                </button>
                <button class="btn btn-light " @click="deleteComment" v-show="isOwner">
                    <i class="las la-trash text-danger"></i>
                </button>
            </div>
            <div class="d-flex" v-if="editing">
                <button class="btn btn-light text-danger mr-2" v-show="isOwner" @click="hideEditionInput">
                    Cancel
                </button>
                <button class="btn btn-light text-primary" v-show="isOwner"
                    @click.prevent="updateComment"
                >
                    Save
                </button>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        props: [
            'comment'
        ],
        data() {
            return {
                editing: false,
                content: ""
            }
        },
        methods: {
            endpoint() {
                return `/api/comments/${this.comment.id}`;
            },
            deleteComment() {
                axios.delete(this.endpoint())
                    .then(() => {
                        this.$emit('delete', this.comment)
                    })
                    .catch(e => console.log(e))
            },
            showEditionInput() {
                this.content = this.comment.content;
                this.editing = true;
            },
            hideEditionInput() {
                this.editing = false;
            },
            updateComment() {
                this.$emit('update', { ...this.comment, content: this.content });
                this.editing = false;

                axios.patch(this.endpoint(), { content: this.content })
                    .then(({data}) => {
                        this.$emit('update', data)
                    })
                    .catch(error => console.log(error));
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
        padding-left: 2rem;
    }
</style>