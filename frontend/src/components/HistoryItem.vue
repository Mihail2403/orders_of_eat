<template>
    <div class="container">
        <div 
            class="row"
            style="
            
                background-color: rgb(239, 242, 245);
                margin: 4px 2px;
                padding: 4px;
                border-radius: 8px;
                "
        >
            <div class="row justify-content-center">
                {{ this.order.person.name }}
            </div>
            <div class="row" v-for="eat in this.order.Eats" :key="eat.id">
                <div class="col-md-10 col-8">{{ eat.eat.text }} - {{ eat.count }} шт.</div>
                <div class="col-md-2 col-4">
                    {{ eat.eat.price*eat.count }} руб.
                </div>
            </div>
            <div
                style="
                    border-top: 1px solid rgb(136, 136, 136);

                "
            ></div>
            <div class="row">
                <div class="col-md-10 col-8">
                    Итого:
                </div>
                <div class="col-md-2 col-4">
                    {{ this.fullPrice }} руб.
                </div>
            </div>
            <div 
                class="row justify-content-end"
                style="color: rgb(156, 156, 156);"
            >
                
                {{ this.dateOrder }}
            </div>
        </div>
    </div>
</template>


<script>
export default {
    data(){
        return {
            // Итоговая цена(цена всех заказаных блюд)
            fullPrice:0,
            // Сторока, означающая дату, указаную при заказе
            dateOrder:"",
            // Месяца для составления dateOrder
            month:[
                "января", 
                "февраля", 
                "марта", 
                "апреля", 
                "мая", 
                "июня", 
                "июля", 
                "августа", 
                "сентября", 
                "октября", 
                "ноября", 
                "декабря",
            ]
        }
    },
    props:{
        order:{
            type: Object,
            required: true
        }
    },
    mounted(){
        // Вычисление итоговой цены
        var eats = this.order.Eats
        for(let i = 0; i<eats.length; i++){
            this.fullPrice += eats[i].eat.price*eats[i].count
        }
        // Преобразование полученного с бэкенда числа в объект Date
        var dateLocal = new Date(this.order.date*86400000)
        // Сериализация Из объекта Data в строку, для удобного отображения
        this.dateOrder = `${dateLocal.getDate()} ${this.month[dateLocal.getMonth()]} ${dateLocal.getFullYear()} года`
    }
}
</script>


<style>

</style>