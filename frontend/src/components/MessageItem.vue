<template>
    <div 
        class="container" 
        style="
            background-color: rgba(127, 255, 212, 0.2);
            border-radius: 4px;
            padding: 4px;
            margin-top: 14px;
            "
    >
        <div 
            class="row justify-content-center"
            style="font-size: large;"    
        >
            {{ this.message.title }}
        </div>
        <div class="row justify-content-center" style="word-spacing: normal;">
            {{ this.message.discription }}
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