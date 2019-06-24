<template>
  <el-row>
    <el-col :span="4">
      <el-menu
        default-active="3-2"
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
      <div align="left" style="margin-top: 5%; margin-left: 5%;">
        <label style="font-size:20px;">
          地址管理
        </label>
        <el-divider></el-divider>
      </div>
      <div align="left" style="margin-left: 5%;">
        <el-row>
          <el-col :span="7" v-for="(value,index) in addresses" :key="index" style="margin-right: 3%; margin-bottom: 3%">
            <el-card :body-style="{ padding: '3px'}" shadow="hover" style="width: 100%; height: 150px;padding-right: 5%">
              <div style="padding: 6px">
                <div>
                  <span style="font-size:18px; margin-left: 5%">{{username}}</span>
                  <el-button style="float: right; padding: 3px" type="text" @click="deleteAddress(index)">删除</el-button>
                  <el-button style="float: right; padding: 3px" type="text" @click="editAddress(index)">修改</el-button>
                  <el-dialog title="编辑地址" :visible.sync="editDialogFormVisible">
                    <el-form :model="form">
                      <el-form-item label="地址" :label-width="formLabelWidth">
                        <el-input v-model="form.address" autocomplete="off"></el-input>
                      </el-form-item>
                      <el-form-item label="手机号" :label-width="formLabelWidth">
                        <el-input v-model="form.tel" autocomplete="off"></el-input>
                      </el-form-item>
                    </el-form>
                    <div slot="footer" class="dialog-footer">
                      <el-button @click="cancelEditAddress()">取 消</el-button>
                      <el-button type="primary" @click="saveEditedAddress(index)">确 定</el-button>
                    </div>
                  </el-dialog>
                  <div style="margin-left: 5%; padding-top: 5%">{{value.address}}</div>
                  <div style="margin-left: 5%; padding-top: 3%">{{value.tel}}</div>
                </div>
                <div style="position: relative;top: 30px;">
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :span="7" style="margin-right: 3%; margin-bottom: 3%">
            <el-card :body-style="{ padding: '3px'}" shadow="hover" style="width: 100%; height: 150px;padding-right: 5%">
              <div style="padding: 6px">
                <div>
                  <el-button style="margin-left:30%;margin-top: 15%" type="text" @click="dialogFormVisible = true">点击添加新地址</el-button>
                  <el-dialog title="添加新地址" :visible.sync="dialogFormVisible">
                    <el-form :model="form">
                      <el-form-item label="地址" :label-width="formLabelWidth">
                        <el-input v-model="form.address" autocomplete="off"></el-input>
                      </el-form-item>
                      <el-form-item label="手机号" :label-width="formLabelWidth">
                        <el-input v-model="form.tel" autocomplete="off"></el-input>
                      </el-form-item>
                    </el-form>
                    <div slot="footer" class="dialog-footer">
                      <el-button @click="cancelAddAddress()">取 消</el-button>
                      <el-button type="primary" @click="addAddress()">确 定</el-button>
                    </div>
                  </el-dialog>
                </div>
                <div style="position: relative;top: 30px;">
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'UserInfo',
    data: function () {
      return {
        dialogFormVisible:false,
        editDialogFormVisible:false,
        form: {
          address:'',
          tel:''
        },
        formLabelWidth: '120px',
        username:'蔡徐坤',
        addresses:[{address:"江苏省南京市鼓楼区汉口路22号南京大学鼓楼校区陶园2舍407", tel:"15189585960"},
          {address:"江苏省南京市鼓楼区汉口路22号南京大学鼓楼校区费彝民楼", tel:"13770752307"},
          {address:"江苏省南京市鼓楼区汉口路22号南京大学鼓楼校区陶园2舍407", tel:"15189585960"},
          {address:"江苏省南京市鼓楼区汉口路22号南京大学鼓楼校区陶园2舍407", tel:"15189585960"},
          {address:"江苏省南京市鼓楼区汉口路22号南京大学鼓楼校区陶园2舍407", tel:"15189585960"},],
        tabPosition:'left',
        labelPosition: 'right',
        UserInfos:{
          avatar: 'https://inews.gtimg.com/newsapp_bt/0/7234467545/640',
          name: '蔡徐坤'
        }
      }
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

      getOrderDetail(){

      },

      orderAgain(){

      },

      editAddress(index){
        this.editDialogFormVisible = true;
        this.form =  Object.assign({}, this.addresses[index]);//拷贝对应地址
      },

      saveEditedAddress(index){
        this.editDialogFormVisible = false;
        this.addresses[index].tel = this.form.tel;
        this.addresses[index].address = this.form.address;
        this.form.address = "";
        this.form.tel = "";
      },

      cancelEditAddress(){
        this.editDialogFormVisible = false;
        this.form.address = "";
        this.form.tel = "";
      },

      deleteAddress(index){
        let restAddresses = this.addresses;
        let newAddresses = [];
        for (let i = 0; i < this.addresses.length; i++){
          if (i !== index){
            newAddresses.push(restAddresses[i]);
          }
        }
        this.addresses = newAddresses;
      },

      addAddress(){
        this.dialogFormVisible = false;
        this.addresses.push({address:this.form.address, tel:this.form.tel});
        this.form.tel = "";
        this.form.address = "";
      },

      cancelAddAddress(){
        this.dialogFormVisible = false;
        this.form.tel = "";
        this.form.address = "";
      }
    }
  }
</script>

<style>
  .text {
    font-size: 14px;
  }
  .item {
    margin-bottom: 18px;
  }

  .box-card {
    width: 30%;
  }
</style>
