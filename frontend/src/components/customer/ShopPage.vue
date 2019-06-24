<template>
  <v-flex>
    <v-layout xs12 class="shop-header" align-center>
      <v-flex md1></v-flex>
      <!--------------- Shop Name & Address-------------------->
      <v-img
        :src="restaurant.avatarSrc"
        max-width="100"
        max-height="100"
        class="shop-avatar"
      >
      </v-img>
      <v-flex shrink mx-3>
        <h2 style="color: white; text-align: start">{{restaurant.name}}</h2>
        <h4 style="color: white; text-align: start">{{restaurant.address}}</h4>
        <v-layout justify-start>
          <template v-for="i in Array(Math.floor(restaurant.stars)).keys()">
            <v-icon :key="i" color="yellow">star</v-icon>
          </template>
          <v-icon v-if="restaurant.stars > Math.floor(restaurant.stars)" color="yellow">
            star_half
          </v-icon>
        </v-layout>
      </v-flex>
      <v-flex md1></v-flex>
      <!------- 起送价、配送费 ------->
      <v-flex>
        <v-layout justify-end>
          <v-flex md2>
            <h3 style="color: white">起送价</h3>
            <h2 style="color: white">{{restaurant.priceStart}}元</h2>
          </v-flex>
          <v-flex md2>
            <h3 style="color: white">配送费</h3>
            <h2 style="color: white">{{restaurant.priceDelivery}}元</h2>
          </v-flex>
          <v-flex md2></v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <!--------------- Menu and Shopping Cart --------------->
    <v-layout xs12 mb-5>
      <!---------------- Meal Type List ----------------->
      <v-flex v-if="!mealSearch.active" ml-5 shrink>
        <v-card elevation="5" class="sticky-box">
          <v-layout justify-end>
            <v-list class="type-list" dense>
              <template v-for="type in restaurant.types">
                <v-list-tile
                  :key="type"
                  :class="currentType === type ? 'type-selected': ''"
                  @click="afterTypeSelected(type)"
                >
                  <v-list-tile-content>
                    <v-list-tile-title class="text-xs-right">{{type}}</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </template>
            </v-list>
          </v-layout>
        </v-card>
      </v-flex>
      <v-flex v-else sm2></v-flex>
      <!---------------- Meal List ----------------->
      <v-flex sm6 ml-5 mr-0 my-3>
        <template v-if="!mealSearch.active">
          <template v-for="type in restaurant.types">
            <v-layout :key="'title-' + type" mt-4 mb-1 ml-3>
              <h2 :id="'h-' + type">{{type}}</h2>
            </v-layout>
            <v-card elevation="3">
              <v-layout :key="type" wrap>
                <template v-for="meal in restaurant.menu[type]">
                  <v-flex :key="meal.id" my-3 shrink mx-3>
                    <v-layout justify-center>
                      <MealCard
                        :meal="meal"
                        :cart-items="cartItems"
                        :width="mealCardWidth"
                      ></MealCard>
                    </v-layout>
                  </v-flex>
                </template>
              </v-layout>
            </v-card>
          </template>
        </template>
        <!--------------- Search Results ----------------->
        <template v-else>
          <v-layout align-center my-3>
            <v-flex shrink mx-3>
              <h3>搜索"<span style="color: red">{{mealSearch.key}}</span>"的结果</h3>
            </v-flex>
            <v-flex shrink mx-3>
              <a @click="clearSearchResult">返回所有菜品</a>
            </v-flex>
          </v-layout>
          <v-layout wrap>
            <template v-for="m in mealSearch.meals">
              <v-flex :key="m.id" mx-2 my-2>
                <MealCard
                  :meal="m"
                  :cart-items="cartItems"
                  :width="mealCardWidth"
                ></MealCard>
              </v-flex>
            </template>
          </v-layout>
        </template>
      </v-flex>
      <!------------ Search & Info -------------->
      <v-flex sm3 pt-3 mx-5>
        <v-layout>
          <v-text-field
            v-model="mealSearch.key"
            label="搜索菜品"
            append-icon="search"
            @keypress.enter="searchMeals"
          ></v-text-field>
        </v-layout>
        <v-layout mt-3>
          <p class="other-info" style="">注意事项：<br/>
            1.收到后尽快食用或放入冰箱冷冻保存<br/>
            2.包装内的干冰-70℃，杜绝手触摸或食用，不可放入冰箱等密闭空间，任其自然挥发即可<br/>
            3.订单生成后，不支持更改收货地址<br/>
            4.我们尽量在1小时左右为您送达，如遇交通堵塞或管制，路面积水或积冰，大风、大雨、冰雪、
            高温等不利天气或不可抗力，配送人员可能会延长您商品的配送时间。如需协助，请拨打4009870870专线<br/>
            5.目前暂不支持蛋糕裱字和代写祝福语</p>
        </v-layout>
      </v-flex>
      <!---------------- Shopping Cart ----------------->
      <v-card class="cart-card">
        <!----------------- Cart Item List ----------------------->
        <v-layout class="cart-item-list">
                                      <v-flex>
                                      <v-list dense>
                                      <v-list-tile>
                                      <v-layout justify-space-between align-center>
                                      <v-flex shrink>
                                      <h3><b>我的购物车</b></h3>
                                      </v-flex>
                                      <v-flex shrink>
                                      <v-btn flat small @click="clearCart">
                                      <v-icon color="red">delete_forever</v-icon>
                                      清空
                                      </v-btn>
                                      </v-flex>
                                      </v-layout>
                                      </v-list-tile>
                                      <template v-for="(num, mid) in cartItems">
                                      <v-divider :key="'d-' + mid"></v-divider>
                                      <v-list-tile :key="mid">
                                      <v-list-tile-content>
                                      <v-layout justify-space-between style="width: 200px">
                                      <v-flex grow align-self-center>
                                      <h4>{{compressStr(restaurant.mealDict[mid].name, 8)}}</h4>
                                      </v-flex>
                                      <v-flex shrink align-self-center>
                                      <NumInput
                                      v-model="cartItems[mid]"
                                      @input="clearIfZero(cartItems, restaurant.mealDict[mid].id)"
                                      ></NumInput>
                                      </v-flex>
                                      </v-layout>
                                      </v-list-tile-content>
                                      <v-list-tile-action>
                                      <h3>￥{{(restaurant.mealDict[mid].price * num).toFixed(2)}}</h3>
                                      </v-list-tile-action>
                                      </v-list-tile>
                                      </template>
                                      </v-list>
                                      </v-flex>
                                      </v-layout>
        <!----------------- Discount Area ----------------------->
        <v-layout justify-center class="promotion-area">
                                                     <template v-for="(discount, amount, index) in restaurant.promotions">
                                                     <span :key="amount">满{{amount}}减{{discount}}</span>
                                                     <span v-if="index < Object.keys(restaurant.promotions).length - 1" :key="index">，</span>
                                                     </template>
                                                     </v-layout>
        <!----------------- Action Area ----------------------->
        <v-layout>
               <v-btn dark class="cart-btn cart-btn-left">
               <v-flex>
               <v-layout justify-start px-3 align-center>
               <v-badge overlap color="red">
               <span v-if="cartItemCount > 0" slot="badge">
               {{cartItemCount}}
               </span>
               <v-icon>shopping_cart</v-icon>
               </v-badge>
               <template v-if="cost.after > 0">
               <h4>￥</h4>
               <h2><b>{{cost.after.toFixed(2)}}</b></h2>
               <h3>&nbsp;|</h3>
               </template>
               <h4 v-if="cost.before > cost.after">
               <s>￥{{cost.before.toFixed(2)}}</s>
               </h4>
               </v-layout>
               </v-flex>
               <v-flex shrink pr-3>
               <h5 v-if="restaurant.priceDelivery > 0">配送费<br>￥{{restaurant.priceDelivery.toFixed(2)}}</h5>
               <h5 v-else>免配送费</h5>
               </v-flex>
               </v-btn>
               <v-flex v-if="cost.after < restaurant.priceStart" style="background-color: #b6b8bf">
               <v-layout style="height: 50px" align-center justify-center>
               <h4><b>差{{(restaurant.priceStart - cost.after).toFixed(2)}}元起送</b></h4>
               </v-layout>
               </v-flex>
               <v-btn v-else class="cart-btn cart-btn-right" dark color="success" @click="gotoPlace">
               <h3><b>去结算 ></b></h3>
               </v-btn>
               </v-layout>
      </v-card>
    </v-layout>
    <!------------- Back to Top Button ------------->
    <v-btn v-if="backTop" large fixed icon right dark color="primary" style="top: 50%"
           @click="scrollToTop"
    >
      <v-icon>arrow_upward</v-icon>
    </v-btn>
  </v-flex>
</template>

<script>
import NumInput from '@/components/util/NumInput'
import MealCard from '@/components/customer/MealCard'
export default {
  name: 'ShopPage',
  components: {MealCard, NumInput},
  data: function () {
    return {
      restaurant: {
        id: this.$route.params['rid'],
        name: '',
        address: '',
        avatarSrc: '',
        priceStart: 0,
        priceDelivery: 0,
        stars: 0,
        promotions: {
          35: 10,
          40: 15,
          50: 20
        },
        types: [],
        menu: {},
        mealDict: {}
      },
      currentType: '',
      scrolling: false,
      mealCardWidth: 300,
      cartItems: {},
      backTop: false,
      mealSearch: {
        active: false,
        key: '',
        meals: []
      }
    }
  },
  computed: {
    cartItemCount: function () {
      let count = 0
      for (let c of Object.keys(this.cartItems)) {
        count += this.cartItems[c]
      }
      return count
    },
    cost: function () {
      let costBefore = 0
      for (let mid of Object.keys(this.cartItems)) {
        costBefore += this.restaurant.mealDict[mid].price * this.cartItems[mid]
      }
      let costLevel = 0
      for (let amount of Object.keys(this.restaurant.promotions)) {
        if (costBefore >= amount) {
          costLevel = amount
        } else {
          break
        }
      }
      let costAfter = costBefore
      if (costLevel > 0) {
        costAfter -= this.restaurant.promotions[costLevel]
      }
      return {
        before: costBefore,
        after: costAfter
      }
    }
  },
  beforeMount: function () {
    // load restaurant info
    this.$ajax({
      url: '/restaurant/get',
      method: 'get',
      params: {
        'rid': this.restaurant.id
      }
    }).then(res => {
      let r = this.restaurant
      r.name = res.data.data['name']
      r.priceStart = res.data.data['priceStart']
      r.priceDelivery = res.data.data['priceDelivery']
      r.avatarSrc = this.preprocessImgSrc(res.data.data['avatarSrc'])
      r.address = res.data.data['address']
      r.description = res.data.data['description']
      r.stars = res.data.data['stars']
    })
    // load meals
    this.$ajax({
      url: '/restaurant/get/meals',
      method: 'get',
      params: {
        'rid': this.restaurant.id
      }
    }).then(res => {
      /**
       * response form: [
       * {
       *    id: 'meal id',
       *    name: 'meal name',
       *    desc: 'meal description',
       *    price: 'meal price',
       *    type: 'meal type',
       *    picSrc: 'meal picture src'
       * }
       * ]
       */
      this.processMeals(res.data.data)
    })
  },
  mounted: function () {
    window.onscroll = () => {
      this.updateCurrentType()
      this.backTop = document.body.getBoundingClientRect().y < -200
    }
  },
  methods: {
    searchMeals: function () {
      if (this.mealSearch.key.length === 0) {
        this.clearSearchResult()
      } else {
        this.mealSearch.active = true
        this.mealSearch.meals.splice(0, this.mealSearch.meals.length)
        for (let mid of Object.keys(this.restaurant.mealDict)) {
          let m = this.restaurant.mealDict[mid]
          if (m['name'].includes(this.mealSearch.key)) {
            this.mealSearch.meals.push(m)
          }
        }
      }
    },
    clearSearchResult: function () {
      this.mealSearch.active = false
      this.mealSearch.key = ''
      this.mealSearch.meals.splice(0, this.mealSearch.meals.length)
    },
    afterTypeSelected: function (type) {
      this.scrolling = true
      // scroll to the corresponding header
      let target = document.getElementById('h-' + type)
      let offset = 65
      window.scrollTo({
        top: target.offsetTop - offset,
        left: window.screenX,
        behavior: 'smooth'
      })
      this.scrolling = false
    },
    scrollToTop: function () {
      this.scrolling = true
      window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth'
      })
      this.scrolling = false
    },
    compressStr: function (name, limit) {
      if (name.length > limit) {
        return name.substr(0, limit - 2) + '...'
      } else {
        return name
      }
    },
    clearIfZero: function (items, mid) {
      if (items[mid] === 0) {
        this.$delete(this.cartItems, mid)
      }
    },
    clearCart: function () {
      for (let mid of Object.keys(this.cartItems)) {
        this.$delete(this.cartItems, mid)
      }
    },
    preprocessImgSrc: function (src) {
      let prefix = 'https://fuss10.elemecdn.com/'
      if (src.substring(src.length - 3) === 'png') {
        return prefix + src + '.png'
      } else {
        return prefix + src + '.jpeg'
      }
    },
    /**
     * Preprocess meals to initialize restaurant[types, menu, mealDict]
     * and currentType.
     */
    processMeals: function (meals) {
      for (let m of meals) {
        m['picSrc'] = this.preprocessImgSrc(m['picSrc'])
        this.$set(this.restaurant.mealDict, m['id'], m)
        if (m['type'] in this.restaurant.menu) {
          this.restaurant.menu[m['type']].push(m)
        } else {
          this.restaurant.types.push(m['type'])
          this.$set(this.restaurant.menu, m['type'], [m])
        }
      }
      if (this.restaurant.types.length > 0) {
        this.currentType = this.restaurant.types[0]
      }
    },
    /**
     * Update current type upon window scrolling.
     */
    updateCurrentType: function () {
      if (this.scrolling) {
        return
      }
      let offset = 70
      let lastType
      for (let type of this.restaurant.types) {
        let h = document.getElementById('h-' + type)
        if (h.getBoundingClientRect().y < offset) {
          lastType = type
        } else if (lastType) {
          this.currentType = lastType
          return
        }
      }
    },
    gotoPlace: function () {
      let items = {}
      for (let mid of Object.keys(this.cartItems)) {
        let m = this.restaurant.mealDict[mid]
        items[mid] = {
          'name': m['name'],
          'price': m['price'],
          'num': this.cartItems[mid]
        }
      }
      window.localStorage.setItem('orderInfo', JSON.stringify({
        'rid': this.restaurant.id,
        'cartItems': items,
        'cost': this.cost
      }))
      this.$router.push('/customer/CheckOut')
    }
  }
}
</script>
<style scoped>
  .shop-header {
    background: url('http://shadow.elemecdn.com/faas/desktop/media/img/shop-bg.0391dd.jpg');
    height: 120px;
    width: 100%
  }
  .shop-avatar {
    border-radius: 50%;
    border: 4px solid rgba(255, 255, 255, .3);
  }
  .sticky-box {
    position: -webkit-sticky;
    position: sticky;
    top: 70px;
    bottom: 0;
  }
  .type-list {
    width: 150px;
    /*background-color: #ede8ef;*/
  }
  .type-selected {
    background-color: #1E89E0;
  }
  .cart-card {
    position: fixed;
    bottom: 10px;
    right: 10px;
    width: 370px;
  }
  .cart-item-list {
    border-top: 2px solid #2070ef;
    border-bottom: #898b92 1px solid;
  }
  .promotion-area {
    background-color: antiquewhite;
  }
  .cart-btn {
    margin: 0 0 0 0;
    height: 50px;
    border-radius: 0 0 0 0;
  }
  .cart-btn-left {
    width: 250px;
  }
  .cart-btn-right {
    width: 120px;
  }
  .other-info {
    text-align: start;
    letter-spacing: 3px;
    font: 15px Arial;
    color: #8f8e8e
  }
</style>
