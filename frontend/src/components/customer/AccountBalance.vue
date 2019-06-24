<template>
  <el-row>
    <el-col :span="4">
      <el-menu
        default-active="2"
        @select="handleSelect">
        <el-menu-item index="1">
          <i class="el-icon-menu"></i>
          <span slot="title">我的订单</span>
        </el-menu-item>
        <el-menu-item index="2">
          <i class="el-icon-menu"></i>
          <span slot="title">账户余额</span>
        </el-menu-item>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>我的资料</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="3-1">个人资料</el-menu-item>
            <el-menu-item index="3-2">地址管理</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
    <el-col :span="20">

    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'AccountBalance',
    data: function () {
      return {
        tabPosition:'left',
      }
    },

    methods:{
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        if (key === "1"){
          this.$router.push('/customer/home/MyOrders')}
        if (key === "2"){
          this.$router.push('/customer/home/AccountBalance')
        }
        if (key === "3-1"){
          this.$router.push('/customer/home/UserInfo')
        }
        if (key === "3-2"){
          this.$router.push('/customer/home/AddressManage')
        }
      },

    }
  }
</script>

<style>
  .el-row {
    margin-bottom: 20px;
  }
  .last-child {
    margin-bottom: 0;
  }
  .el-col {
    border-radius: 4px;
  }
  .bg-purple-dark {
    background: #99a9bf;
  }
  .bg-purple {
    background: #d3dce6;
  }
  .bg-purple-light {
    background: #e5e9f2;
  }
  .grid-content {
    border-radius: 4px;
    min-height: 36px;
  }
  .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
</style>
