<template>
  <el-row>
    <el-col :span="4">
      <el-menu
        default-active="3-1"
        default-openeds="['2']"
        @select="handleSelect">
        <el-menu-item index="1">
          <i class="el-icon-menu"></i>
          <span slot="title">我的订单</span>
        </el-menu-item>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-location"></i>
            <span>我的资料</span>
          </template>
          <el-menu-item-group>
            <el-menu-item index="2-1">个人资料</el-menu-item>
            <el-menu-item index="2-2">地址管理</el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-col>
    <el-col :span="20">
      <el-row>
        <div align="left" style="margin-top: 20px; margin-left: 20px;">
          <label style="font-size:20px;">
            个人资料
          </label>
          <el-divider></el-divider>
        </div>
        <el-col :span="8">
          <div align="left" style="margin-left: 30px;">
            <el-form :label-position="labelPosition" label-width="80px" :model="UserInfos" align="left">
              <el-form-item label="头像">
                <img :src="UserInfos.avatar"  width="100" height="100" />
              </el-form-item>
              <el-form-item label="用户名">
                <el-input v-model="UserInfos.name" style="width: auto" disabled="disabled"></el-input>
              </el-form-item>
              <el-form-item label="账户余额">
                <el-input v-model="UserInfos.balance" style="width: auto" disabled="disabled"></el-input>
              </el-form-item>
            </el-form>
          </div>
        </el-col>
        <el-col :span="16">
          <div id="myChart1" :style="{width:'600px', height:'400px'}" class="charts"></div>
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
  import echarts from 'echarts'

  export default {
    name: 'UserInfo',
    data: function () {
      return {
        disabled: true,
        tabPosition:'left',
        labelPosition: 'right',
        UserInfos:{
          avatar: 'https://inews.gtimg.com/newsapp_bt/0/7234467545/640',
          name: '蔡徐坤',
          balance: '10000',
        }
      }
    },

    mounted(){
      this.getUserStatistics();
    },

    methods:{
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
        if (key === "1"){
          this.$router.push('/customer/home/MyOrders')}
        if (key === "2-1"){
          this.$router.push('/customer/home/UserInfo')
        }
        if (key === "2-2"){
          this.$router.push('/customer/home/AddressManage')
        }
      },

      getUserStatistics() {
        let myChart = echarts.init(document.getElementById('myChart1'));
        // 绘制图表
        myChart.setOption({
          title: { text: '消费统计' },
          tooltip: {},
          legend: {
            data:['快餐便当', '小吃夜宵', '饮品甜品']
          },
          series : [{
            name: '消费金额',
            type:'pie',
            stack: '总量',
            // data:[nums.num1, nums.num2, nums.num3, nums.num4]
            data:[
              {value:120, name: "快餐便当"},
              {value:120, name: "小吃夜宵"},
              {value:120, name: "饮品甜品"},
              ]
          }]
        });
      },

      getOrderDetail(){

      },

      orderAgain(){

      },
    }
  }
</script>

<style>
</style>
