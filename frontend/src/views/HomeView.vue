<template>
  <select v-model="selected" @change.prevent="console.log(selected)">
      <option v-for="person in persons" :key="persons.indexOf(person)">
        {{person.name}}
      </option>
    </select>
  <button @click.prevent="addToBasket">hbfh</button>
  <div v-for="eat in basket" :key="eat.id">
    <eat-item :eat-item="eat"/>
  </div>

</template>

<script>
import EatItem from "@/components/eatItem.vue";

export default {
  components: {EatItem},
  data(){
    return {
      selected: '',
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
          text:"hio",
          components: "Chicken",
          price: 12000
        },
        // {
        //   id:1,
        //   text:"hio",
        //   components: "Chicken",
        //   price: 12000
        // }
      ],
      basket:[
        {
          id:0,
          text:"hio",
          components: "Chicken",
          price: 12000
        },
      ]
    }
  },
  methods: {
    addToBasket(){
      this.basket = [{text:"c", price:12}, ...this.basket]
    }
  }
}
</script>

<style scoped>

</style>