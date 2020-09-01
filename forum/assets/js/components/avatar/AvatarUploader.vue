<template>
    <div>
        <label for="avatar-input" class="btn btn-primary">Upload</label>
        <input type="file" class="d-none" id="avatar-input" @change="handleProfilePictureChange">
    </div>
</template>

<script>
import axios from "axios";
export default {
    data() {
        return {

        }
    },
    methods: {
        handleProfilePictureChange(event) {
            this.readUploadedFile(event);

            this.uploadAvatar(event);
        },
        readUploadedFile(event) {
            const profileImage = event.target.files[0];

            if(! profileImage) {
                return ;
            }

            const reader = new FileReader();
            reader.onload = (fileEvent) => {
                this.fireUploadedFileEvent(fileEvent.target.result);
            };
            reader.onerror = function() {
                console.error("File could not be read! Code " + event.target.error.code);
            };

            reader.readAsDataURL(profileImage);
        },
        fireUploadedFileEvent(image) {
            EventDispatcher.fire("avatar-uploaded", image)
        },
        uploadAvatar(event) {

            const formData = new FormData();
            formData.append("avatar", event.target.files[0]);

            axios.post("/settings/avatar", formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            })
            .then(({data}) => {
                this.fireUploadedFileEvent(data.avatar);
            })
            .catch(error => console.log(error));
            
        }
    },
}
</script>