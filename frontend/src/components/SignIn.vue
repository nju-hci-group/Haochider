<template>
  <v-layout class="outer-layout" justify-center>
    <v-flex xs1 sm2 md4></v-flex>
    <v-flex>
      <!----------------- Logo ------------------>
      <v-layout my-4 justify-center>
        <v-img
          :src="require('../assets/logo.png')"
          max-height="80"
          max-width="200"
        ></v-img>
      </v-layout>
      <!----------------- Login Card ------------------->
      <v-layout>
        <v-card flat width="500">
          <v-card-title primary-title>
            <v-layout row wrap justify-center>
              <h1>登录</h1>
            </v-layout>
          </v-card-title>
          <v-divider/>
          <v-card-text>
            <v-form ref="signInForm" lazy-validation>
              <v-layout row wrap justify-start mx-4>
                <v-text-field
                  label="电子邮件"
                  :rules="emailRules"
                  v-model="username"
                ></v-text-field>
              </v-layout>
              <v-layout row wrap justify-start mx-4>
                <v-text-field
                  label="密码"
                  type="password"
                  v-model="pwd"
                ></v-text-field>
              </v-layout>
              <v-layout row wrap align-center justify-end mx-4 my-2>
                <v-flex>
                  <v-btn color="success" large @click="signIn" block>
                    <h3>立即登录</h3>
                  </v-btn>
                </v-flex>
              </v-layout>
            </v-form>
            <v-layout mx-4>
              <v-flex>
                <h4>或使用关联的社交账户登录</h4>
              </v-flex>
            </v-layout>
            <v-layout mx-4 my-2>
              <v-flex mr-2>
                <v-btn color="primary" large block>
                  <h3>使用QQ登录</h3>
                </v-btn>
              </v-flex>
              <v-flex ml-2>
                <v-btn color="primary" large block>
                  <h3>使用微信登录</h3>
                </v-btn>
              </v-flex>
            </v-layout>
            <v-layout mx-4 mt-3>
              <v-flex>
                <router-link to="">忘记密码？</router-link>
              </v-flex>
            </v-layout>
          </v-card-text>
        </v-card>
      </v-layout>
      <!----------------- Sign Up Link ----------------->
      <v-layout mx-4 my-3>
        <v-flex>
          <v-btn dark to="/customer/sign-up" block flat>
            <h3>
              没有帐号？注册 &gt;
            </h3>
          </v-btn>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex xs1 sm2 md4></v-flex>
    <v-snackbar v-model="snackbar" top>
      {{errMsg}}
      <v-btn color="pink" flat @click="snackbar = ''">关闭</v-btn>
    </v-snackbar>
  </v-layout>
</template>

<script>
export default {
  name: 'SignIn',
  data: function () {
    return {
      userRoles: ['顾客', '商家', '管理员'],
      role: '顾客',
      username: '',
      pwd: '',
      emailRules: [],
      errMsg: '',
      snackbar: false
    }
  },
  methods: {
    signIn: function () {
      this.emailRules.push(email => !!email || '请输入电子邮件地址')
      this.emailRules.push(email => /.+@.+/.test(email) || '电子邮件地址格式不正确')
      if (this['$refs']['signInForm'].validate()) {
        this.customerSignIn()
      }
    },
    customerSignIn: function () {
      this.$ajax({
        url: '/customer/sign-in',
        method: 'post',
        params: {
          email: this.username,
          pwd: this.pwd
        }
      }).then((res) => {
        switch (res.data.data['result']) {
          case 0:
            this['$router'].push('/customer/home')
            this.errMsg = ''
            this.snackbar = false
            break
          case 1:
            this.errMsg = '帐号不存在'
            this.snackbar = true
            break
          case 2:
            this.errMsg = '密码错误'
            this.snackbar = true
            break
          default:
            this.errMsg = '未知错误'
            this.snackbar = true
            break
        }
      })
    }
  }
}
</script>

<style scoped>
.outer-layout {
  background-color: #1E89E0;
  width: 100%;
  height: 100%;
}
</style>
