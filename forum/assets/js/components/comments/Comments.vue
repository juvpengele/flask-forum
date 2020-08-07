<template>
    <div>
        <CommentForm/>
        <Comment v-for="comment in comments" :comment="comment" :key="comment.id"/>
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

        }
    }
}
</script>