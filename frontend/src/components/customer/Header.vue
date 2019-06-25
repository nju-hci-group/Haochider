<template>
  <HeaderBase>
    <template slot="left-part">
      <v-btn
        flat
        large
        @click="$router.push('/customer/home')"
      >
        <h3>首页</h3>
      </v-btn>
      <v-btn flat large @click="toOrders">
        <h3>我的订单</h3>
      </v-btn>
    </template>
    <v-btn flat large >
      <h3>我的客服</h3>
    </v-btn>
    <v-menu v-if="name" open-on-hover offset-y bottom>
      <v-btn flat slot="activator">
        <h3>{{name}}</h3>
        <v-icon>arrow_drop_down</v-icon>
      </v-btn>
      <v-list dense>
        <v-list-tile @click="$router.push('/customer/home/UserInfo')">
          <v-icon>person</v-icon>
          <v-list-tile-title>个人中心</v-list-tile-title>
        </v-list-tile>
        <v-list-tile @click="$router.push('/customer/home/AddressManage')">
          <v-icon>location_on</v-icon>
          <v-list-tile-title>我的地址</v-list-tile-title>
        </v-list-tile>
        <v-divider></v-divider>
        <v-list-tile @click="signOut">
          <v-icon>power_settings_new</v-icon>
          <v-list-tile-title>退出</v-list-tile-title>
        </v-list-tile>
      </v-list>
    </v-menu>
    <v-btn v-else flat @click="$router.push('/sign-in')">
      <v-icon>person</v-icon>
      <h4>登录/注册</h4>
    </v-btn>
  </HeaderBase>
</template>

<script>
import HeaderBase from '@/components/util/HeaderBase'
export default {
  name: 'CustomerHeader',
  components: {HeaderBase},
  props: {
    'name': String
  },
  data: function () {
    return {
    }
  },
  methods: {
    signOut: function () {
      this.$ajax({
        url: '/customer/sign-out',
        method: 'post'
      }).then(() => {
        this['$router'].push('/customer/home')
        window.location.reload()
      })
    },
    toOrders: function () {
      this.$ajax({
        url: '/customer/get',
        method: 'get'
      }).then(res => {
        if (res.data.data['AccessDenied'] === undefined) {
          this['$router'].push('/customer/home/MyOrders')
        } else {
          this['$router'].push('/sign-in')
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
