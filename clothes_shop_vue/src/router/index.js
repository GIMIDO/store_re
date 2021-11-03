import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Clothes from '../views/Clothes.vue'
import Category from '../views/Category.vue'
import Cart from '../views/Cart.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Account from '../views/Account.vue'
import Checkout from '../views/Checkout.vue'
import Success from '../views/Success.vue'
import store from '../store'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',

    component: () => import('../views/About.vue')
  },
  {
    path: '/:category_slug/:clothes_slug/',
    name: 'Clothes',
    component: Clothes
  },
  {
    path: '/:category_slug/',
    name: 'Category',
    component: Category
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: Success
  },
  {
    path: '/account',
    name: 'Account',
    component: Account,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/cart/checkout',
    name: 'Checout',
    component: Checkout,
    meta: {
      requireLogin: true
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({name: 'LogIn', query: {to: to.path}});

  }
  else {
    next()
  }
})

export default router
