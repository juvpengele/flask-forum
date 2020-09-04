<template>
    
    <img 
        :src="profilePicture" 
        :alt="auth.name + ' profile picture'" 
        :width="size"
        :height="size"
    />
    
</template>

<script>
export default {
    props: {
        size: {
            type: Number,
            required: false,
            default: 200
        }
    },
    data() {
        return {
            profilePicture: window.Auth.profilePicture
        }
    },
    mounted() {
        EventDispatcher.listen("avatar-uploaded", this.updateProfilePicture)
    },
    methods: {
        updateProfilePicture(url) {
            this.profilePicture = url;
        }
    },
    computed: {
        auth() {
            return window.Auth
        }
    }
}
</script>