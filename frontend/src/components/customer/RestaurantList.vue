<template>
  <v-container fluid>
    <v-layout row wrap>
      <v-container fluid grid-list-sm style="padding-bottom: 0">
        <v-layout row>
          <v-flex xs4>
            <v-card outlined fill-height>
              <v-img :src="picList[0]" contain>
              </v-img>
            </v-card>
          </v-flex>
          <v-flex xs8>
            <v-layout v-for="m in 2" :key="m" row wrap>
              <v-flex v-for="n in 4" :key="n" d-flex xs3>
                <v-card outlined>
                  <v-img :src="getPicture(m, n)" contain>
                  </v-img>
                </v-card>
              </v-flex>
            </v-layout>
          </v-flex>
        </v-layout>
        <v-layout row wrap>
          <v-flex xs3>
            <p class="address-text">当前地址： {{province}}{{city}}{{area}}
              <span v-if="!addressVisible" class="address-text" style="color: red" @click="addressVisible = true" >重新选择</span>
              <span v-if="addressVisible" class="address-text" style="color: red" @click="addressVisible = false" >收起</span>
            </p>
          </v-flex>
          <v-flex xs1>
          </v-flex>
        </v-layout>
        <v-layout row v-if="addressVisible">
          <v-flex xs6>
            <vue-address @on-change="selectAddress" :p="province" :c="city" :a="area"></vue-address>
          </v-flex>
          <!--<v-flex xs2>-->
            <!--<v-btn flat small @click="addressVisible = false">收起</v-btn>-->
          <!--</v-flex>-->
        </v-layout>
      </v-container>
    </v-layout>
    <v-layout row wrap>
      <v-container fluid grid-list-md :style="{'padding-top': addressVisible ? 0 : '20px'}">
        <v-toolbar dense>
          <v-toolbar-title>商家分类  </v-toolbar-title>
          <template v-for="(item, index) in categories">
            <v-btn :color="index === category ? 'primary' : 'normal'" small :key="index" @click="selectCategory(key)">{{item}}</v-btn>
          </template>
        </v-toolbar>
      </v-container>
    </v-layout>
    <v-layout>
      <v-container fluid grid-list-md>
        <v-layout v-for="m in line" :key="m" row wrap>
          <v-flex v-for="n in column" :key="n" d-flex xs4>
            <v-card v-if="getRestaurantIndex(m, n) < showList.length" @click="enterRestaurant(getRestaurant(m, n).id)">
              <v-container fluid grid-list-lg style="padding: 10px">
                <v-layout row>
                  <v-flex xs5>
                    <v-card-media :src="getRestaurant(m, n).image" height="120px" contain></v-card-media>
                  </v-flex>
                  <v-flex xs7>
                    <div>
                      <p class="subheading" style="text-align: left"><strong>{{getRestaurant(m, n).name}}</strong></p>
                      <p style="text-align: left">介绍：{{getRestaurant(m, n).description}}</p>
                      <p style="text-align: left">地址：{{getRestaurant(m, n).address}}</p>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
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
    this.loadRestaurant()
    this.loadCategories()
    this.loadPicList()
    this.showList = this.list.concat()
  },
  mounted () {
    this.scroll(this.list)
  },
  data: function () {
    return {
      picList: [],
      categories: ['全部商家', '快餐便当', '小吃夜宵', '饮品甜品'],
      category: 0,
      morePage: true,
      page: 0,
      pageSize: 8,
      list: [],
      showList: null,
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
       *     page: 1
       * }
       * response form: [{
       *     id: 1,
       *     name: '测试餐厅',
       *     description: 'dfhhyj',
       *     address: '南京大学第i食堂',
       *     type: 1,
       *     image: 'https://source.unsplash.com/random/120x120'
       * }]
       */
      this.$ajax.get('/restaurant', {
        params: {
          page: this.page + 1
        }
      }).then(res => {
        if (res.data.code === 0) {
          console.log('请求出错')
        } else {
          if (res.data.length > 0) {
            this.list.push(...res.data.data)
            this.page++
          } else {
            this.morePage = false
          }
        }
      })
    },
    loadCategories: function () {
      /**
       * response form: ['快餐便当', '小吃夜宵', '饮品甜品']
       */
      this.$ajax.get('/restaurant/categories').then(res => {
        if (res.data.code !== 0) {
          this.category = res.data.data
          this.category.splice(0, 0, '全部商家')
        }
      })
    },
    loadPicList: function () {
      /**
       * response form: ['image-link'] 每一项是图片链接，总共九项
       */
      this.$ajax.get('/restaurant/pictures').then(res => {
        if (res.data.code !== 0) {
          this.picList = res.data.data
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
      return this.picList[(m - 1) * 4 + n]
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
      console.log(id)
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
    scroll: function () {
      let isLoading = false
      window.onscroll = () => {
        // 距离底部20px时加载一次
        let bottomOfWindow = document.documentElement.offsetHeight - document.documentElement.scrollTop - window.innerHeight <= 10
        if (bottomOfWindow && isLoading === false && this.morePage) {
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
</style>
