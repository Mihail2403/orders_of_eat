<template>
    <div v-if="listOfOrders.length>0">
        <div 
            class="container">
            <div class="row" v-for="order in listOfOrders" :key="order.id">
                <history-item :order="order"/>
            </div>
        </div>
    </div>
    <div v-else>
        <message-item :message="{title:'Нет заказов'}"/>
    </div>
</template>
  
<script>
import axios from 'axios'
import HistoryItem from '@/components/HistoryItem.vue'
import MessageItem from '@/components/MessageItem.vue'
export default {
    components:{HistoryItem, MessageItem},
    data() {
        return {
            listOfOrders: []
        };
    },
    mounted() {
        axios.get(
            'http://localhost:8000/api/v1/history/'
        ).then(
            response => {
                this.listOfOrders = response.data['order_list']
            }
        )
        
        console.log(this.listOfOrders)
    },
}
</script>

<style>

</style>