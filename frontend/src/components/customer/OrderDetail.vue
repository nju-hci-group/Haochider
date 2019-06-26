<template>
  <el-row>
    <el-col :span="4">
      <el-menu
        default-active="1"
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
      <div>
        <div align="left" style="margin-left: 2%;">
          <el-row>
            <el-card :body-style="{ padding: '3px'}" shadow="never" style="width: 100%; height: 600px">
                <el-row>
                  <el-col :span="12">
                    <div :body-style="{ padding: '3px'}" style="width: 100%; height: 500px;padding-right: 5%">
                      <div style="padding: 6px">
                        <div>
                          <span style="font-size:18px; margin-left: 5%; font-family: 微软雅黑,serif;font-weight: bold">订单详情</span>
                          <el-divider></el-divider>
                          <el-row>
                            <el-col :span="4" style="margin-left: 5%">
                              <img :src="RestaurantInfos.avatar"  width="50" height="50"  style="border-radius: 50%; cursor:pointer;margin-left: 5%" @click="gotoRestaurant() " />
                            </el-col>
                            <el-col :span="12">
                              <div style="font-size: large; padding-top: 7%">{{RestaurantInfos.name}}</div>
                            </el-col>
                          </el-row>
                          <div style="margin-left: 4%">
                            <el-table
                              :data="shoppingCartTableData"
                              style="width: 100%"
                            >
                              <el-table-column
                                prop="food"
                                label="商品"
                              >
                              </el-table-column>
                              <el-table-column
                                prop="number"
                                label="份数"
                                width="150"
                                align="center"
                              >
                              </el-table-column>
                              <el-table-column
                                prop="price"
                                label="小计(元)"
                                align="right">
                              </el-table-column>
                            </el-table>
                          </div>
                          <el-row>
                            <span style="font-size: 40px; color: red; float: right">￥{{this.sumPrice}}</span>
                          </el-row>
                          <el-row>
                            <span style="float: right">共{{this.sumNumber}}份商品</span>
                          </el-row>
                        </div>
                        <div style="position: relative;top: 30px;">
                        </div>
                      </div>
                    </div>
                  </el-col>
                  <el-col :span="12">
                    <div :body-style="{ padding: '3px'}" style="width: 100%; height: 500px;padding-right: 5%">
                      <div style="padding: 6px">
                        <div>
                        <span style="font-size:18px; margin-left: 5%; font-family: 微软雅黑,serif;font-weight: bold;">
                          配送信息
                        </span>
                          <el-form ref="form" :model="orderForm" label-width="80px" style="margin-left: 5%; margin-top: 2%">
                            <el-form-item label="订单状态:">
                              <span>{{orderForm.state}}</span>
                            </el-form-item>
                            <el-form-item label="联系人:">
                              <span>{{orderForm.username}}</span>
                            </el-form-item>
                            <el-form-item label="联系电话:">
                              <span>{{orderForm.tel}}</span>
                            </el-form-item>
                            <el-form-item label="收货地址:">
                              <span>{{orderForm.address}}</span>
                            </el-form-item>
                            <el-form-item label="送达时间:">
                              <span>{{orderForm.arriveTime}}</span>
                            </el-form-item>
                            <el-form-item label="订单备注:">
                              <span>{{orderForm.note}}</span>
                            </el-form-item>
                          </el-form>
                        </div>
                        <div style="position: relative;top: 30px;">
                        </div>
                      </div>
                    </div>
                  </el-col>
                </el-row>
              </el-card>
          </el-row>
        </div>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'OrderDetail',
    data() {
      return {
        buttonText : '确认下单',
        isLoading : false,
        pickerOptions: {
          start: '08:30',
          step: '00:15',
          end: '18:30',
          disabledDate(time) {
            return time.getTime() > Date.now();
          }
        },
        arriveTime: '',
        value: '',
        dialogFormVisible: false,
        form: {
          address:'',
          tel:''
        },
        orderForm: {
          state: '已送达',
          username:'蔡徐坤',
          tel:'15189585960',
          address:'江苏省南京市鼓楼区南京大学陶园2舍407',
          arriveTime:'尽快送出',
          note: '无备注'
        },
        shoppingCartTableData:[],
        sumPrice:0,
        sumNumber:0,
        RestaurantInfos:{
          rid: '',
          avatar: '',
          name: '',
        }
      }
    },

    created(){
      this.getOrderDetail();
    },

    methods:{
      gotoRestaurant(){
        this.$router.push('/customer/home/shop/'+this.RestaurantInfos.rid);
      },

      getOrderDetail(){
        let order = localStorage.getItem("order");
        order = JSON.parse(order);
        console.log(order);
        let foods = order.cartItems;
        let price = 0;
        for (let i = 0; i < foods.length; i++){
          this.shoppingCartTableData.push({food: foods[i].name, number: foods[i].num, price: "￥" + (foods[i].price * foods[i].num).toFixed(2), singlePrice: foods[i].price});
          price += (foods[i].price * foods[i].num);
        }
        this.sumNumber = foods.length;
        this.sumPrice = order.price;
        this.RestaurantInfos.avatar = order.avatar;
        this.RestaurantInfos.name = order.rname;
        this.RestaurantInfos.rid = order.rid;

        let delivery = 0;

        this.$ajax({
          url: '/restaurant/get',
          method: 'get',
          params: {
            'rid': this.RestaurantInfos.rid
          }
        }).then(res => {
          delivery = res.data.data['priceDelivery'];
          this.shoppingCartTableData.push({food: "配送费", number: "", price: "￥" + delivery, singlePrice: 0});

          price = price + delivery;
          let discount = price - this.sumPrice;
          this.shoppingCartTableData.push({food: "优惠", number: "", price: "-￥" + discount.toFixed(0), singlePrice: 0});
        });
      },

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

    }
  }
</script>

<style scoped>

</style>
