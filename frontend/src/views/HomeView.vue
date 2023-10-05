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
              {{eatItem.text}}
            </option>
          </select>
      <div
        v-for="eat in basket"
        :key="eat.id"
      >
        <eat-item :eat-item="eat" @deleteFromBasket="deleteFromBasket"/>
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
  </div>
</template>

<script>
import EatItem from "@/components/EatItem.vue";

export default {
  components: {EatItem},
  data(){
    return {
      startDate: Date.now()+1,
      date:null,
      keyForBasket:0,
      selectedEat:'',
      selectedPers: '',
      persons:[
        {
          id:0,
          name:"Выберите сотрудника"
        },
        {
          id:1,
          name:"Mic"
        },
        {
          id:2,
          name:"Nina"
        }
      ],
      eats: [
        {
          id:0,
          text:"Выберите блюдо",
          components: "",
          price: 0
        },
        {
          id:1,
          text:"hio1",
          components: "Chicken",
          price: 1000
        },
        {
          id:2,
          text:"hio2",
          components: "Chicken",
          price: 12000
        }
      ],
      basket:[
        // {
        //   id:this.keyForBasketCom(),
        //   eat: {
        //     id:0,
        //     text:"hio",
        //     components: "Chicken",
        //     price: 12000
        //   }
        // },
      ]
    }
  },
  methods: {
    addToBasket(){
      console.log(1)
      if(this.basket.length > 10){
        this.selectedEat=this.eats[0]
        return
      }
      var curr_eat = {
        id: this.keyForBasketCom(),
        eat: this.eats.find(obj=>obj === this.selectedEat)
      }
      console.log(curr_eat)
      this.basket = [curr_eat, ...this.basket]
      // enable or disable button
      this.enablOrNotSub()
      //
      console.log(this.basket)
      this.selectedEat=this.eats[0]
    },
    deleteFromBasket(eatItem){
      this.basket = this.basket.filter(eat => eat !== eatItem)
      this.enablOrNotSub()
    },
    keyForBasketCom() {
      this.keyForBasket += 1
      return this.keyForBasket
    },
    submitOrder(){
      // приводим страничку к первоначальному виду
      this.selectedPers = this.persons[0].name
      this.selectedEat = this.eats[0]
      this.basket = []
      this.date = null
      document.getElementById('sub').disabled = true
    },
    enablOrNotSub(){
      var butSub=document.getElementById('sub')
      if(this.selectedPers !== this.persons[0].name && this.date!==null && this.basket.length>0){
        butSub.disabled = false
      } else {
        butSub.disabled = true
        document.getElementById('sub').disabled = true
      }
    },
  },
  mounted() {
    this.selectedPers = this.persons[0].name
    this.selectedEat = this.eats[0]
  }
}
</script>

<style>
  select option {
    background-color: #212529;
    color:white;
  }
</style>