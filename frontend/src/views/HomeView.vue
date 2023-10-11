<template>
  <div class="container">
    <h4 class="row justify-content-center">Заказ</h4>
    <div class="row justify-content-center">
      
      <select
        v-model="selectedPers"
        @change.prevent="enablOrNotSub"
        class="form-select"
        aria-label="Default select example"
        aria-placeholder="Select"
        style="
          width: 80%;
          margin-top: 4px;
          border: 2px solid #212529;
        "
      >
          <option
            v-for="person in persons"
            :key="persons.indexOf(person)"
          >
            {{person.name}}
          </option>
        </select>
    </div>
    <div class="row justify-content-center">
      <select
          id="selectEats"
          v-model="selectedEat" 
          @change.prevent="addToBasket"
          class="form-select" 
          aria-label="Default select example"
          aria-placeholder="Select"
          style="
            width: 80%;
            margin-top: 4px;
            border:2px solid #212529;
          "
        >
            <option 
              v-for="eatItem in eats"
              :value="eatItem"
              :key="eats.indexOf(eatItem)"
            >
              {{eatItem.name}}
            </option>
          </select>
      <div
        v-for="eat in basket"
        :key="eat.id"
      >
        <eat-item :eat-item="eat" @deleteFromBasket="deleteFromBasket"/>
      </div>
      <div class="row justify-content-end">
      </div>
      <div
          class="row justify-content-end"
          style="width: 80%"
      >
        <VueDatePicker
                  v-model="date"
                  :enable-time-picker="false"
                  :min-date="Date.now()"
                  :start-date="startDate"
                  ignore-time-validation
                  @update:model-value="enablOrNotSub"
                  style="
                    margin-top: 4px;
                    width: 150px;
                  "
              />
          <button
              disabled
              id="sub"
              class="btn"
              style="
                margin-top: 4px;
                width:130px;
                border: 2px solid #212529;
              "
              @click.prevent="submitOrder"
          >
            Заказать
          </button>
      </div>
    </div>
    <div v-if="this.message.length>0">
      <message-item :message="{title:'Успешно', discription:'Заказ добавлен.'}"/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import EatItem from "@/components/EatItem.vue";
import MessageItem from '@/components/MessageItem.vue';


export default {
  components: {EatItem, MessageItem},
  data(){
    return {
      message:"",
      // поле для настройки валидации выбора даты
      startDate: Date.now()+1,
      // здесь будет лежать выбраная дата
      date:null,
      // переменная для метода keyForBasketCom
      keyForBasket:0,
      // модель для выбора Блюда
      selectedEat:'',
      // модель для выбора Сотрудника
      selectedPers: '',
      // Массив сотрудников, которые будут помещены в select
      persons:[
        {
          id:0,
          name:"Выберите сотрудника"
        },
      ],
      // Массив блюд, которые будут помещены в select
      eats: [
        {
          id:0,
          name:"Выберите блюдо",
          components: "",
          price: 0
        },
        {
          id:1,
          name:"МНЕ ПОВЕЗЕТ",
          components:"",
          price:0
        }
      ],
      // корзина
      basket:[]
    }
  },
  methods: {
    addToBasket(){
      // если в корзине больше 10 блюд - вы не сможете добавить еще чтото
      if(this.basket.length >= 10){
        this.selectedEat=this.eats[0]
        return
      }
      var curr_eat = {}
      // При выборе "МНЕ ПОВЕЗЕТ"
      if(this.selectedEat === this.eats[this.eats.length - 1]){
        while(this.basket.length<10){
          // генерация объекта блюда
          curr_eat = {
            id: this.keyForBasketCom(),
            eat: this.eats.filter(obj=> obj!==this.eats[0] && obj!==this.eats[this.eats.length-1])[Math.floor(Math.random() * (this.eats.length-2))]
          }
          // добавление в локальную корзину
          this.basket = [curr_eat, ...this.basket]
          // запуск метода, включающего или выключающего кнопку
          this.enablOrNotSub()
          // возвращение select к изначальному виду 
          this.selectedEat=this.eats[0]
        }
      } else {
        // генерация объекта блюда
        curr_eat = {
          id: this.keyForBasketCom(),
          eat: this.eats.find(obj=>obj === this.selectedEat)
        }
        // добавление в локальную корзину
        this.basket = [curr_eat, ...this.basket]
        // запуск метода, включающего или выключающего кнопку
        this.enablOrNotSub()
        // возвращение select к изначальному виду 
        this.selectedEat=this.eats[0]
      }

    },

    deleteFromBasket(eatItem){
      this.basket = this.basket.filter(eat => eat !== eatItem)
      // запуск метода, включающего или выключающего кнопку
      this.enablOrNotSub()
    },

    // метод для генерации :key для v-for
    keyForBasketCom() {
      this.keyForBasket += 1
      return this.keyForBasket
    },

    submitOrder(){
      // Отправка заказа на бэкенд
      axios.post(
        'http://localhost:8000/api/v1/order/',
        {
            "date": Math.floor(+this.date / 86400000),
            "worker_id":this.persons.find(obj=>obj.name === this.selectedPers).id,
            "eats": this.basket
        }
      ).then(
          response => {
            try{
              if(response.data.status === "good"){
                this.message = response.data.order.worker
                console.log(this.message)
              }
            }catch(e){
              console.log(e)
            }
          }
        ) 

      // приводим страничку к первоначальному виду
      this.selectedPers = this.persons[0].name
      this.selectedEat = this.eats[0]
      this.basket = []
      this.date = null
      this.keyForBasket = 0
      document.getElementById('sub').disabled = true
    },
    
    // метод включающий или выключающий кнопку
    enablOrNotSub(){
      // кнопка отправки заказа на сервер
      var butSub=document.getElementById('sub')
      // проверка на валидность заказа, и если не валиден - конпка не нажмется
      if(this.selectedPers !== this.persons[0].name && this.date!==null && this.basket.length>0){
        butSub.disabled = false
      } else {
        butSub.disabled = true
      }
    },
  },
  mounted() {
    // помещение начальных значений  в select-ы
    this.selectedEat = this.eats[0]
    this.selectedPers = this.persons[0].name
    // инициализация списков сотрудников и блюд для select-ов данными с сервера
    axios.get(
      'http://localhost:8000/api/v1/worker-list/'
      ).then(
        response => {
          this.persons = [this.persons[0], ...response.data]
        }).catch(
          err => console.log(err)
        )
    axios.get(
      'http://localhost:8000/api/v1/eat-list/'
      ).then(
        response => {
          console.log(response)
          var iWouldLuck = this.eats[1]
          this.eats = [this.eats[0], ...response.data]
          iWouldLuck.id = this.eats.length
          this.eats = [...this.eats, iWouldLuck]
        }).catch(
          err => console.log(err)
        )
      }
    }
</script>

<style>
  select option {
    background-color: #212529;
    color:white;
  }
</style>