<template>
  <v-card :width="width" flat>
    <v-layout align-center>
      <!------------- Meal Image ------------->
      <v-img
        :src="meal.picSrc"
        width="100"
        height="100"
        max-width="100"
        max-height="100"
      ></v-img>
      <!------------ Meal Info --------------->
      <v-flex ml-3 mr-1 my-2>
        <v-tooltip top>
          <h3 class="text-sm-left" slot="activator">
            <b>{{compressStr(meal.name, 10)}}</b>
          </h3>
          <span>{{meal.name}}</span>
        </v-tooltip>
        <v-tooltip v-if="meal['desc'].length > 0" top>
          <h4 class="text-sm-left" slot="activator">
            {{compressStr(meal['desc'], 10)}}
          </h4>
          <span>{{meal['desc']}}</span>
        </v-tooltip>
        <v-tooltip v-else top>
          <h4 slot="activator">&ensp;</h4>
          <span>无菜品描述</span>
        </v-tooltip>
        <v-layout justify-space-between align-content-end>
          <h3 class="text-sm-left" style="color: red"><b>￥{{meal.price.toFixed(2)}}</b></h3>
          <!---------------- Number Ordered ----------------->
          <div
            v-if="cartItems[meal.id] !== undefined"
            style="margin: 0 10px"
          >
            <NumInput
              v-model="cartItems[meal.id]"
              @input="clearIfZero(cartItems, meal.id)"
            ></NumInput>
          </div>
          <v-btn v-else flat icon small style="margin: 0 10px"
                 @click="$set(cartItems, meal.id, 1)"
          >
            <v-icon color="primary">add_circle</v-icon>
          </v-btn>
        </v-layout>
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
import NumInput from '@/components/util/NumInput'
export default {
  name: 'MealCard',
  components: {NumInput},
  props: {
    meal: Object,
    cartItems: Object,
    width: Number
  },
  methods: {
    clearIfZero: function (items, mid) {
      if (items[mid] === 0) {
        this.$delete(this.cartItems, mid)
      }
    },
    compressStr: function (name, limit) {
      if (name.length > limit) {
        return name.substr(0, limit - 2) + '...'
      } else {
        return name
      }
    }
  }
}
</script>

<style scoped>

</style>
