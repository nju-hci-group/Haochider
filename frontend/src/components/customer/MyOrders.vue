<template>
  <el-row>
    <el-col :span="4">
      <el-menu
        default-active="1"
        default-openeds="['2']"
        @select="handleSelect"
       >
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
      <el-table
        :data="orderData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
        style="width: 100%"
       >
        <el-table-column
          prop="time"
          label="下单时间"
          width="180">
        </el-table-column>
        <el-table-column
          prop="content"
          label="订单内容"
          width="480">
          <template slot-scope="scope">
            <el-row>
              <el-col :span="4">
                <img :src="scope.row.avatar"  width="50" height="50"  style="border-radius: 50%; cursor:pointer" @click="gotoRestaurant(scope.$index, scope.row) " />
              </el-col>
              <el-col :span="12">
                <div style="padding-top: 7%; ">{{scope.row.content}}</div>
              </el-col>
            </el-row>
          </template>
        </el-table-column>
        <el-table-column
          prop="price"
          label="支付金额（元）">
        </el-table-column>
        <el-table-column
          prop="state"
          label="状态">
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              @click="getOrderDetail(scope.$index, scope.row)">订单详情
            </el-button>
            <br>
            <el-button
              size="mini"
              type="danger"
              @click="orderAgain(scope.$index, scope.row)">再来一份
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <div style="text-align: center;margin-top: 30px;">
        <el-pagination
          background
          layout="prev, pager, next"
          :total="total"
          @current-change="current_change">
        </el-pagination>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'MyOrders',
    data: function () {
      return {
        opened : false,
        tabPosition:'left',
        orderData: [],
        total: 11,
        pagesize:10,
        currentPage:1
      }
    },

    mounted(){
      this.getOrders();
    },

    methods:{
      gotoRestaurant(index, row){
        this.$router.push('/customer/home/shop/'+row.rid);
      },

      current_change:function(currentPage){
        this.currentPage = currentPage;
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

      //跳转至订单详情
      getOrderDetail(index, row){
        console.log(row);
        localStorage.setItem("order", JSON.stringify(row));
        this.$router.push('/customer/home/OrderDetail');
      },

      //跳转至再来一单支付界面
      orderAgain(index, row){
        localStorage.setItem("orderInfo", JSON.stringify(row));
        this.$router.push('/customer/CheckOut');
      },

      getOrders() {
        /**
         * response form: [
         * {
         *    id: 1
         *    time: '2018-02-14 17:45:00'
         *    avatar: 'XXXX',
         *    rid,
         *    rname,
         *    price: 92.93,
         *    orders:{
         *        'xxx': {name: 'abc', price: 20.233, num: 1}, // key是菜品编号
                  'xxxx': {name: 'bbc', price: 30.23, num: 1},
                  'xxxxx': {name: 'cbc', price: 40.23, num: 1},
         *    },
         *    state: '订单已完成|订单已取消|等',
         *    contents: '',
         * }
         * ]
         */
        this.$ajax({
          url: '/customer/orders/get',
          method: 'get'
        }).then(res => {
          console.log(res.data);
          if (res.data['AccessDenied']) {
            this.$router.push('/')
          } else {
            this.orderData = res.data.data;
            for (let i = 0; i < this.orderData.length; i++){
              let foods = this.orderData[i].orders;
              let name = "";
              let num = 0;
              Object.keys(foods).some(function(key){
                name = foods[key].name;
                num = foods[key].num;
                if (name !== ""){
                  return true;
                }
              });

              this.orderData[i].content = name + num + "份等" + foods.length + "个菜品";
              if (this.orderData[i].avatar.substring(this.orderData[i].avatar.length - 3) === 'png'){
                this.orderData[i].avatar = "https://fuss10.elemecdn.com/" + this.orderData[i].avatar + '.png';
              }else {
                this.orderData[i].avatar = "https://fuss10.elemecdn.com/" + this.orderData[i].avatar + '.jpeg';
              }
              console.log(this.orderData[i].content);
              console.log(this.orderData[i].avatar)
            }

            this.total = this.orderData.length;
          }
        });

/*
        this.orderData = [
          {
            id: 1,
            rid:'12345',
            rname: '水林间（南京紫峰店）',
            time: '2019-06-06 10:43',
            content: '',
            orders :[{name: 'abc', price: 20.233, num: 1}, // key是菜品编号，value是数量
              {name: 'bbc', price: 30.23, num: 1},
              {name: 'cbc', price: 40.23, num: 1},],
            price: 70.69,
            state: '订单已完成',
            avatar : 'e/5d/4a731a90594a4af544c0c25941171jpeg'
          },
          {
            id: 2,
            rid:'12345',
            rname: '水林间（南京紫峰店）',
            time: '2019-06-05 10:43',
            content:'',
            orders :[{name: 'x', price: 20.233, num: 1}, // key是菜品编号，value是数量
              {name: 'y', price: 30.23, num: 1},
              {name: 'z', price: 40.23, num: 1},],
            price: 70.69,
            state: '订单已完成',
            avatar : 'e/5d/4a731a90594a4af544c0c25941171jpeg'

          },];
*/
      }
    }
  }
</script>

<style>

</style>
