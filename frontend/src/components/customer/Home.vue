<template>
  <div>
    <CustomerHeader
      :name="info.name"
    ></CustomerHeader>
    <router-view></router-view>
  </div>
</template>

<script>
import CustomerHeader from '@/components/customer/Header'
export default {
  name: 'Home',
  components: {CustomerHeader},
  beforeMount: function () {
    this.$ajax({
      url: '/customer/info/get',
      method: 'get'
    }).then(res => {
      if (res.data.data['AccessDenied']) {
        this.$router.push('/')
      } else {
        this.info.name = res.data.data['name']
      }
    })
  },
  data: function () {
    return {
      info: {
        name: ''
      }
    }
  }
}
</script>

<style scoped>

</style>
