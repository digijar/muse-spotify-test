import { createRouter, createWebHistory } from 'vue-router'
import ReplayView from '../views/ReplayView.vue'
import BlendView from '../views/BlendView.vue'
import LoginView from '../views/LoginView.vue'
import AccountView from '../views/AccountView.vue'
import LoginAuthView from '../views/LoginAuthView.vue'
import SignUpView from '../views/SignUpView.vue'
import Test from '../views/Test.vue'
import GroupBlend from '../views/GroupBlendView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/replay',
      name: 'replay',
      component: ReplayView,
      meta: {
        needsAuth: true
      }
      
    },
    {
      path: '/blend',
      name: 'blend',
      component: BlendView,
      meta: {
        needsAuth: true
      }
    },
    {
      path: '/account',
      name: 'account',
      component: AccountView,
      meta: {
        needsAuth: true
      }
    },
    {
      path: '/loginauth',
      name: 'loginauth',
      component: LoginAuthView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/groupblend',
      name: "groupblend",
      component: GroupBlend,
      meta: {
        needsAuth: true
      }
    },

    {
      path: '/test/:id',
      name: "Test",
      component: Test
    }
  ]
})

router.beforeEach((to,from,next)=>{
  if(to.meta.needsAuth && sessionStorage.getItem("access_token")==null){
    next("/loginauth");
  } else {
    next();
  }
})

export default router
