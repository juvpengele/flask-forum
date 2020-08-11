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
            <i class="las la-pencil-alt"></i>
            <span></span>
        </div>
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

    .comment-content {
        margin-top: .25rem;
        padding-left: 3rem;
    }
</style>