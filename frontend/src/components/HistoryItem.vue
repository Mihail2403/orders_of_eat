<template>
    <div class="container">
        <div 
            class="row"
            style="
                margin: 4px 2px;
                padding: 4px;
                border: 2px solid black;
                "
        >
            <div class="row">
                {{ this.order.person.name }}
            </div>
            <div class="row" v-for="eat in this.order.Eats" :key="eat.id">
                {{ eat.eat.text }}
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return {
            listOfEats: new Map()
        }
    },
    props:{
        order:{
            type: Object,
            required: true
        }
    },
    mounted(){
    }
}
</script>


<style>

</style>