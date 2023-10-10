<template>
    <div class="container">
        <div 
            class="row justify-content-center" 
            style="
                background-color: rgba(127, 255, 212, 0.3);
                border-radius: 4px;
                "
        >
            {{ this.message.title }}
        </div>
    </div>
</template>

<script>
export default {
    props: {
        message: {
            type: Object, 
            required: true
        }
    }
}
</script>

<style>

</style>