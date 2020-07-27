<template>
    <div>
        <CommentForm/>
        <Comment/>
    </div>
</template>

<script>
import Comment from "./Comment.vue"
import CommentForm from "./CommentForm.vue"

export default {
    components: {
        CommentForm, Comment
    },
    mounted() {
        console.log(window.Auth)
    }
}
</script>