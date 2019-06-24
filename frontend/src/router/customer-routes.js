import SignUp from '@/components/customer/SignUp'
import Home from '@/components/customer/Home'
import ShopPage from '@/components/customer/ShopPage'
import OrderPlace from '@/components/customer/OrderPlace'
import CheckOut from '../components/CustomerPay/CheckOut'
import CheckStand from '../components/CustomerPay/CheckStand'
import AddressManage from '@/components/customer/AddressManage'
import MyOrders from '../components/customer/MyOrders'
// import AccountBalance from '../components/customer/AccountBalance'
import UserInfo from '../components/customer/UserInfo'
import OrderDetail from '../components/customer/OrderDetail'
import RestaurantList from '@/components/customer/RestaurantList'

export default [
  {
    path: '/customer/sign-up',
    name: 'CustomerSignUp',
    component: SignUp
  },
  // {
  //   path: '/customer/verify-email',
  //   name: 'EmailVerify',
  //   component: EmailVerify
  // },
  {
    path: '/customer/CheckOut',
    name: 'CheckOut',
    component: CheckOut
  },
  {
    path: '/customer/CheckStand',
    name: 'CheckStand',
    component: CheckStand
  },
  {
    path: '/customer/home',
    component: Home,
    children: [
      {
        path: 'MyOrders',
        name: 'MyOrders',
        component: MyOrders
      },
      {
        path: 'OrderDetail',
        name: 'OrderDetail',
        component: OrderDetail
      },
      // {
      //   path: 'AccountBalance',
      //   name: 'AccountBalance',
      //   component: AccountBalance
      // },
      {
        path: 'UserInfo',
        name: 'UserInfo',
        component: UserInfo
      },
      {
        path: 'AddressManage',
        name: 'AddressManage',
        component: AddressManage
      },
      {
         path: '',
         name: 'CustomerHome',
         component: RestaurantList
      },
      {
        path: 'shop/:rid',
        name: 'Shop',
        component: ShopPage
      },
      {
        path: 'order/place',
        name: 'OrderPlace',
        component: OrderPlace
      }
    ]
  }
]
