<template>
    <div 
        class="container">
        <div class="row" v-for="order in listOfOrders" :key="order.id">
            <history-item :order="order"/>
        </div>
    </div>
</template>
  
<script>
import HistoryItem from '@/components/HistoryItem.vue'

export default {
    components:{HistoryItem},
    data() {
        return {
            listOfOrders: [
                {
                    id: 0,
                    date: Date.now(),
                    person: {
                        id: 1,
                        name: "Mic"
                    },
                    Eats: [
                        {
                            id: 0,
                            count: 2,
                            eat: {
                                id: 0,
                                text: "hio",
                                components: "Chicken",
                                price: 12000
                            }
                        },
                        {
                            id: 1,
                            count:1,
                            eat: {
                                id: 1,
                                text: "hio1",
                                components: "Chicken",
                                price: 11000
                            }
                        }
                    ],
                },
                {
                    id: 1,
                    date: Date.now(),
                    person: {
                        id: 2,
                        name: "Nina"
                    },
                    Eats: [
                        {
                            id: 0,
                            count: 1,
                            eat: {
                                id: 0,
                                text: "hio",
                                components: "Chicken",
                                price: 12000
                            }
                        },
                        {
                            id: 1,
                            count:5,
                            eat: {
                                id: 1,
                                text: "hio1",
                                components: "Chicken",
                                price: 11000
                            }
                        }
                    ]
                }
            ]
        };
    },
    mounted() {
        
    },
}
</script>

<style>

</style>