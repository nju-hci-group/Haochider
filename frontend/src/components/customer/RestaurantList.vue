<template>
  <v-container fluid pt-1>
    <v-layout mx-5>
      <v-flex xs3 mx-3>
        <p class="address-text">当前地址： {{province}}{{city}}{{area}}
          <span v-if="!addressVisible" class="address-text" style="color: red" @click="addressVisible = true" >重新选择</span>
          <span v-if="addressVisible" class="address-text" style="color: red" @click="addressVisible = false" >收起</span>
        </p>
      </v-flex>
      <v-flex xs1>
      </v-flex>
    </v-layout>
    <v-layout row v-if="addressVisible" mx-5>
      <v-flex xs6 mx-3>
        <vue-address @on-change="selectAddress" :p="province" :c="city" :a="area"></vue-address>
      </v-flex>
      <!--<v-flex xs2>-->
      <!--<v-btn flat small @click="addressVisible = false">收起</v-btn>-->
      <!--</v-flex>-->
    </v-layout>
    <!----------------- Recommendation Area ------------------->
    <v-layout mx-5 mt-4>
      <v-flex mx-3 shrink>
        <h2><strong>推荐菜品</strong></h2>
      </v-flex>
    </v-layout>
    <v-layout row wrap mx-5 mt-2 justify-space-between>
      <v-flex mx-3 shrink>
        <v-card width="300" hover style="cursor: pointer">
          <v-img
            :src="picList[0]"
            min-width="300"
            max-width="300"
            max-height="210"
            min-height="210"
          ></v-img>
        </v-card>
      </v-flex>
      <v-flex mx-3 shrink>
        <v-card width="300" hover style="cursor: pointer">
          <v-img
            :src="picList[1]"
            min-width="300"
            max-width="300"
            max-height="210"
            min-height="210"
          ></v-img>
        </v-card>
      </v-flex>
      <v-flex shrink ml-3>
        <v-container grid-list-sm style="padding: 0">
          <v-layout v-for="m in 2" :key="m" row wrap my-0>
            <v-flex v-for="n in 3" :key="n" mx-2>
              <v-card width="120" hover style="cursor: pointer">
                <v-img
                  :src="getPicture(m, n)"
                  min-width="120"
                  max-width="120"
                  min-height="90"
                  max-height="90"
                ></v-img>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-flex>
    </v-layout>
    <!--------------- Category Area ---------------->
    <v-layout row wrap mx-5 my-3>
      <v-flex mx-3 >
        <v-toolbar dense style="background-color: white" >
          <v-toolbar-title>商家分类</v-toolbar-title>
          <template v-for="(item, index) in categories">
            <v-btn
              :color="index === category ? 'primary' : 'normal'"
              small
              :key="index"
              @click="selectCategory(index)"
              flat
            >{{item}}</v-btn>
          </template>
        </v-toolbar>
      </v-flex>
    </v-layout>
    <!----------------- Shop Area ------------------>
    <v-layout mx-5>
      <v-flex>
        <v-layout v-for="m in line" :key="m" row wrap mb-3>
          <v-flex v-for="n in column" :key="n" d-flex mx-3>
            <v-card
              v-if="getRestaurantIndex(m, n) < showList.length"
              @click="enterRestaurant(getRestaurant(m, n).id)"
              style="cursor: pointer"
              hover
              width="300"
            >
              <v-layout my-2 mx-3>
                <v-img
                  :src="getRestaurant(m, n).image"
                  max-height="100"
                  min-height="100"
                  max-width="100"
                  min-width="100"
                ></v-img>
                <v-flex ml-2>
                  <h4 class="subheading" style="text-align: left; margin-bottom: 12px">
                    <strong>{{compressStr(getRestaurant(m, n).name, 13)}}</strong>
                  </h4>
                  <h4 style="text-align: left; margin-bottom: 12px">
                    配送费￥{{getRestaurant(m, n)['priceDelivery']}}
                  </h4>
                  <v-layout justify-start>
                    <template v-for="i in Array(Math.floor(getRestaurant(m, n)['stars'])).keys()">
                      <v-icon :key="i" color="yellow">star</v-icon>
                    </template>
                    <v-icon
                      v-if="getRestaurant(m, n)['stars'] > Math.floor(getRestaurant(m, n)['stars'])"
                      color="yellow"
                    >star_half</v-icon>
                  </v-layout>
                </v-flex>
              </v-layout>
            </v-card>
          </v-flex>
        </v-layout>
      </v-flex>
    </v-layout>
    <v-btn dark absolute fab right color="red" @click="backTop" style="margin: 20px; bottom: 0; position: fixed">
      <v-icon>keyboard_arrow_up</v-icon>
    </v-btn>
  </v-container>
</template>

<script>
import vueAddress from './address.vue'
export default {
  components: {
    vueAddress
  },
  name: 'RestaurantList',
  beforeMount: function () {
  },
  mounted () {
    this.loadRestaurant()
    this.loadCategories()
    this.loadPicList()
    this.scroll()
  },
  data: function () {
    return {
      picList: [],
      categories: [],
      category: 0,
      morePage: true,
      page: 0,
      pageSize: 30,
      list: [],
      showList: [],
      line: 2,
      column: 3,
      province: '江苏省',
      city: '南京市',
      area: '鼓楼区',
      addressVisible: false
    }
  },
  methods: {
    loadRestaurant: function () {
      /**
       * request param: {
       *     page: 1,
       *     pageSize: 6
       * }
       * response form: [{
       *     id: 1,
       *     name: '测试餐厅',
       *     priceDelivery: 1.5,
       *     stars: 5,
       *     type: 1,
       *     image: 'https://source.unsplash.com/random/120x120'
       * }]
       */
      this.$ajax.get('/restaurant', {
        params: {
          page: this.page + 1,
          pageSize: this.pageSize
        }
      }).then(res => {
        if (res.data.data.length > 0) {
          this.list.push(...res.data.data)
          for (let i = 0; i < this.list.length; i++) {
            this.list[i].type = parseInt(this.list[i].type, 10)
          }
          this.page++
        } else {
          this.morePage = false
        }
        this.showList = this.list.concat()
      })
    },
    loadCategories: function () {
      /**
       * response form: ['快餐便当', '小吃夜宵', '饮品甜品']
       */
      this.$ajax.get('/restaurant/categories').then(res => {
        this.categories = res.data.data
        this.categories.splice(0, 0, '全部商家')
      })
    },
    loadPicList: function () {
      /**
       * response form: ['image-link'] 每一项是图片链接，总共九项
       */
      this.$ajax.get('/restaurant/pictures').then(res => {
        let list = res.data.data
        for (let i of list) {
          this.picList.push(i['url'])
        }
      })
    },
    loadRestaurantMock: function () {
      for (let i = 0; i < 8; i++) {
        let r = Math.random()
        let c = '小吃夜宵'
        if (r < 0.35) c = '快餐便当'
        else if (r < 0.65) c = '饮品甜品'
        this.list.push({
          id: i,
          name: '测试餐厅' + i,
          description: 'dfhhyj',
          address: '南京大学第' + i + '食堂',
          type: c,
          image: 'https://source.unsplash.com/random/120x120?r=' + r
        })
      }
    },
    getPicture: function (m, n) {
      return this.picList[(m - 1) * 3 + n + 1]
    },
    selectCategory: function (key) {
      this.category = key
      if (key !== 0) {
        this.showList = this.list.filter(function isBigEnough (element, index, array) {
          return (element.type === key)
        })
      } else {
        this.showList = this.list.concat()
      }
    },
    getRestaurantIndex: function (m, n) {
      return (m - 1) * this.column + n - 1
    },
    getRestaurant: function (m, n) {
      return this.showList[this.getRestaurantIndex(m, n)]
    },
    enterRestaurant: function (id) {
      this['$router'].push('/customer/home/shop/' + id)
    },
    backTop: function () {
      document.body.scrollTop = 0
      document.documentElement.scrollTop = 0
    },
    selectAddress: function (address) {
      this.province = address.province
      this.city = address.city
      this.area = address.area
    },
    compressStr: function (name, limit) {
      if (name.length > limit) {
        return name.substr(0, limit - 1) + '...'
      } else {
        return name
      }
    },
    scroll: function () {
      let isLoading = false
      window.onscroll = () => {
        // 距离底部20px时加载一次
        let bottomOfWindow = document.documentElement.offsetHeight - document.documentElement.scrollTop - window.innerHeight <= 10
        if (bottomOfWindow && isLoading === false && this.morePage) {
          this.page = 0
          this.loadRestaurant()
          this.selectCategory(this.category)
          this.line = Math.floor(this.showList.length / 4) + 1
          isLoading = false
        }
      }
    }
  }
}
</script>

<style scoped>
.address-text {
  text-align: left;
  padding-top: 20px;
  margin-bottom: 0;
}
.container.grid-list-sm .layout .flex{
  padding: 3px 10px 23px 10px;
}
</style>
