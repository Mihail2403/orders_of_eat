<template>
  
  <div class="container">
    <h4 class="row justify-content-center">Заказ</h4>
    <div class="row justify-content-center">
      <select 
        v-model="selectedPers" 
        @change.prevent="console.log(selectedPers)"
        class="form-select" 
        aria-label="Default select example"
        aria-placeholder="Select"
        style="
          width: 80%;
          margin-top: 4px;
          
        "
      >
          <option
            v-for="person in persons" 
            :key="persons.indexOf(person)"
            @click.prevent=""
          >
            {{person.name}}
          </option>
        </select>
    </div>
    <div class="row justify-content-center">
      <select 
          v-model="selectedEat" 
          @change.prevent="addToBasket"
          class="form-select" 
          aria-label="Default select example"
          aria-placeholder="Select"
          style="
            width: 80%;
            margin-top: 4px;
          "
        >
            <option 
              v-for="eatItem in eats" 
              :key="eats.indexOf(eatItem)"
            >
              {{eatItem.text}}
            </option>
          </select>
      </div>
  </div>

  <div 
    v-for="eat in basket" 
    :key="eat.id"
  >
    <eat-item :eat-item="eat" @deleteFromBasket="deleteFromBasket"/>
  </div>

</template>

<script>
import EatItem from "@/components/eatItem.vue";

export default {
  components: {EatItem},
  data(){
    return {
      keyForBasket:0,
      selectedEat:'',
      selectedPers: '',
      persons:[
        {
          id:0,
          name:"Mic"
        },
        {
          id:1,
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
        {
          id:this.keyForBasketCom(),
          eat: {
            id:0,
            text:"hio",
            components: "Chicken",
            price: 12000
          }
        },
      ]
    }
  },
  methods: {
    addToBasket(){
      console.log(1)
      var curr_eat = {
        id: this.keyForBasketCom(),
        eat: this.eats.find(obj=>obj.text === this.selectedEat)
      }
      console.log(curr_eat)
      this.basket = [curr_eat, ...this.basket]
      console.log(this.basket)
      this.selectedEat=this.eats[0].text
    },
    deleteFromBasket(eatItem){
      this.basket = this.basket.filter(eat => eat !== eatItem)
    },
    keyForBasketCom() {
      this.keyForBasket += 1
      return this.keyForBasket
    }
  }
}
</script>

<style>
  select option {
    background-color: #212529;
    color:white;
  }
</style>