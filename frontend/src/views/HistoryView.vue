<template>
    <div>
        <history-item :order="listOfOrders[0]"/>
    </div>
</template>
  
<script>
import HistoryItem from '@/components/HistoryItem.vue'

export default {
    components:{HistoryItem},
    data() {
        return {
            listOfOrders: [{
                date: Date.now(),
                person: {
                    id: 1,
                    name: "Mic"
                },
                Eats: [
                    {
                        id: 0,
                        eat: {
                            id: 0,
                            text: "hio",
                            components: "Chicken",
                            price: 12000
                        }
                    },
                    {
                        id: 1,
                        eat: {
                            id: 0,
                            text: "hio",
                            components: "Chicken",
                            price: 12000
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