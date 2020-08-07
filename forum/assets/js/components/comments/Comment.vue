<template>
    <div class="comment">
       {{ comment.content }}
    </div>
</template>

<script>
export default {
    props: [
        'comment'
    ]
}
</script>

<style>
    .comment {
        background: #fff;
        padding: 1rem
    }
</style>