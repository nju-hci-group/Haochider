<template>
  <div>
    <div style="background-color: #1E89E0">
      <el-row>
        <el-col :span="4" style="margin-top: 1%">
          <img :src="require('../../assets/logo.png')" width="140" height="70" @click="gotoHome()" style="cursor: pointer"/>
        </el-col>
        <el-col :span="4" style="margin-top: 1.4%; margin-left: -3%">
          <span style="color: white; font-size: 26px" >| 收银台</span>
        </el-col>
        <el-col :span="16" style="margin-top: 1%;"  >
         <!-- <el-steps :space="200" :active="3" align-center="" style="float: right;width: 60%">
            <el-step title="选择商品"></el-step>
            <el-step title="确认订单信息"></el-step>
            <el-step title="成功提交订单"></el-step>
          </el-steps>-->
        </el-col>
      </el-row>
    </div>
    <div align="left" style="margin-left: 2%;">
      <el-card :body-style="{ padding: '3px'}" shadow="hover" style="width: 100%;padding-right: 5%; margin-top: 0%">
        <div style="padding: 6px">
          <div>
            <div style="font-size:18px; margin-left: 5%; font-family: 微软雅黑;font-weight: bold">
              订单详情
            </div>
            <el-collapse style="margin-left: 5%">
              <el-collapse-item title="外卖订单" style="" name="1">
                <div>{{this.restaurantName}}</div>
                <div>{{this.username}}</div>
                <div>{{this.tel}}</div>
                <div>{{this.address}}</div>
                <div>-</div>
                <div v-for="item in this.foods">{{item}}</div>
              </el-collapse-item>
            </el-collapse>
          </div>
        </div>
      </el-card>
      <el-card :body-style="{ padding: '3px'}" shadow="hover" style="width: 100%;padding-right: 5%; margin-top: 1%">
        <div style="padding: 6px">
          <div>
            <div style="font-size:18px; margin-left: 5%; margin-top: 1%; font-family: 微软雅黑;font-weight: bold">
              请选择支付方式
              <el-divider></el-divider>
              <el-row style="margin-bottom: 1%">
                <el-col :span="2">
                  <div style="font-size: 15px; font-weight: normal; font-family: 等线">第三方支付</div>
                </el-col>
                <el-col :span="4" style="margin-left: -1%">
                  <div style="font-size: 15px; color: red">￥{{this.sumPrice}}</div>
                </el-col>
              </el-row>
              <div>
                <el-radio v-model="radio1" label="1" border style="width: 150px; height: 50px">
                  <div style="margin-top: -20%; margin-left: 20%">
                    <img :src="require('../../assets/ali.png')" width="40" height="30"/>
                    <div style="margin-top: -25%; margin-left: 40%">支付宝</div>
                  </div>
                </el-radio>
                <el-radio v-model="radio1" label="2" border style="width: 150px; height: 50px">
                  <div style="margin-top: -20%; margin-left: 20%">
                    <img :src="require('../../assets/wechat.png')" width="40" height="30"/>
                    <div style="margin-top: -25%; margin-left: 40%">微信支付</div>
                  </div>
                </el-radio>
              </div>
              <el-divider></el-divider>
              <el-button type="danger" @click="pay()">确认支付</el-button>
              <el-dialog
                title="扫码支付"
                :visible.sync="dialogVisible"
                width="30%"
              >
                <p align="center">
                  <img :src="require('../../assets/timg.jpg')" width="200" height="200"/>
                </p>
              </el-dialog>
            </div>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'CheckStand',
    data() {
      return {
        rid: '',
        dialogVisible : false,
        sumPrice: 0,
        restaurantName:'',
        username:'',
        tel:'',
        address:'',
        foods:[],
        radio1:0
      }
    },

    mounted(){
      this.getOrder();
    },

    methods:{
      gotoHome(){
        this.$router.push('/customer/home');
      },

      pay: function () {
        this.dialogVisible = true;

        let orderItems = localStorage.getItem("payItems");
        orderItems = JSON.parse(orderItems);
        let newOrder = {
          rid: this.rid,
          price: this.sumPrice,
          orders: []
        };
        for (let i = 0; i < orderItems.length; i++) {
          if (orderItems[i].food !== "配送费" && orderItems[i].food !== "优惠") {
            newOrder.orders.push(orderItems[i]);
          }
        }

        this.$ajax({
          url: '/restaurant/order/post',
          method: 'post',
          data: JSON.stringify(newOrder),
        }).then(res => {
          console.log(res.data);
          setTimeout(this.gotoHome, 10000);

        });
      },

      getOrder() {
        this.sumPrice = localStorage.getItem("price");
        let order = localStorage.getItem("orderInfo");
        order = JSON.parse(order);
        this.rid = order.rid;
        console.log(this.rid);

        this.$ajax({
          url: '/restaurant/get',
          method: 'get',
          params: {
            'rid': this.rid
          }
        }).then(res => {
          this.restaurantName = res.data.data['name'];
          this.username = "蔡徐坤";
          this.tel = "15189585960";
          this.address = "江苏省南京市鼓楼区南京大学";
          let orderItems = localStorage.getItem("payItems");
          orderItems = JSON.parse(orderItems);

          let orders = [];

          Object.keys(orderItems).forEach(function (key) {
            let name = orderItems[key].food;
            let num = orderItems[key].number;
            if (name !== "配送费" && name !== "优惠"){
              orders.push(name + "  x" + num + '\n');
            }
          });
          this.foods = orders;
        });

    //   this.restaurantName = "水林间（南京紫峰店）";

      }
    }
  }
</script>

<style scoped>
  .el-collapse-item__header {
    border-bottom-color: dodgerblue;
  }
</style>
