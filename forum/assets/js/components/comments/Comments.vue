<template>
    <div>
        <CommentForm  :threadId="id" @submit="handleNewComment"/>
        <div class="my-3">
            <Comment v-for="comment in comments" :comment="comment" :key="comment.id"
                @delete="removeComment"
            />
        </div>
    </div>
</template>

<script>
import Comment from "./Comment.vue"
import CommentForm from "./CommentForm.vue"
import axios from "axios";

export default {
    components: {
        CommentForm, Comment
    },
    props: ['id'],
    data() {
        return {
            comments: []
        }
    },
    mounted() {
        this.fetchComments();
    },
    methods: {
        fetchComments() {
             axios.get(`/api/threads/${this.id}/comments`)
                .then(({data}) => this.comments = data)

        },
        handleNewComment(comment) {
            this.comments.unshift(comment)
        },
        removeComment(deletedComment) {
            this.comments = this.comments.filter((comment) => comment.id !== deletedComment.id);
        }
    },
}
</script>