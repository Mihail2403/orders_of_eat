<template>
    <div class="container">
        <div class="row justify-content-end">
                <VueDatePicker
                    v-model="date"
                    :enable-time-picker="false"
                    ignore-time-validation
                    @update:model-value="selectDate"
                    style="
                        margin-top: 4px;
                        margin-bottom: 8px;
                        "
                />
            </div>
    </div>
    <div v-if="listOfOrdersToRender&&listOfOrdersToRender.length>0">

        <div class="container">
            <div class="row" v-for="order in listOfOrdersToRender.reverse()" :key="order.id">
                <history-item :order="order"/>
            </div>
        </div>
    </div>

    <div v-else>
        <message-item :message="
            {
                title:'Нет заказов',
                discription: ''
                }"
        />
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
            // здесь лежат закаы в том виде, что вернул бэкенд
            listOfOrders: [],
            // здесь будут лежать заказы, в зависимости от выбраной даты
            listOfOrdersToRender:[],
            // дата
            date:null,

        };
    },
    methods:{
        // поиск по дате
        selectDate(){
            if(this.date === null){
                this.listOfOrdersToRender = [...this.listOfOrders]
                return
            }
            this.listOfOrdersToRender = this.listOfOrders.filter(
                obj => obj.date === Math.floor(+this.date / 86400000))
        }
    },
    mounted() {
        // Получение истории заказов с бэкенда
        axios.get(
            'http://localhost:8000/api/v1/history/'
        ).then(
            response => {
                this.listOfOrders = response.data['order_list']
                this.listOfOrdersToRender = [...this.listOfOrders]
            }
        ).catch(
            err => console.log(err)
        )
    },
}
</script>

<style>

</style>