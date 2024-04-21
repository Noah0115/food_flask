import Vue from 'vue'
import VueRouter from 'vue-router'
import Welcome from '../views/Welcome.vue'
import Users from '../views/Users.vue'
import AdminNotice from '../views/AdminNotice.vue'
import Reception from '../views/Reception.vue'
import ReceptionHome from '../views/Home.vue'
import Foods from '../views/Foods.vue'
import Details from '../views/Details.vue'
import Notice from '../views/Notice.vue'
import Analysis from '../views/Analysis.vue'
import AdminHome from '../views/AdminHome.vue'
import AdminFood from '../views/AdminFood.vue'
import AdminAnalysis from '../views/AdminAnalysis.vue'
import AdminScraper from '../views/AdminScraper.vue'
import AdminData from '../views/AdminData.vue'
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    //前台路由
    {
      path: '/',
      redirect: '/receptionhome',
      component: Reception,
      children: [
        {
          path: '/receptionhome', component: ReceptionHome, meta: {
            title: '美食分析系统'
          }
        },
        {
          path: '/foods', component: Foods, meta: {
            title: '美食分析系统'
          }
        },
        {
          path: '/foods/details', component: Details, meta: {
            title: '美食分析系统'
          }
        },
        {
          path: '/analysis', component: Analysis, meta: {
            title: '美食分析系统'
          }
        },
        {
          path: '/notice', component: Notice, meta: {
            title: '美食分析系统'
          }
        },
      ],

    },
    //管理员后台路由
    {
      path: '/adminhome',
      component: AdminHome,
      redirect: '/welcome',
      children: [
        {
          path: '/welcome', component: Welcome, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/user', component: Users, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/adminnotice', component: AdminNotice, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/adminfood', component: AdminFood, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/adminanalysis', component: AdminAnalysis, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/adminscraper', component: AdminScraper, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
        {
          path: '/admindata', component: AdminData, meta: {
            title: '美食分析系统后台',requireAuth: true
          }
        },
      ]
    },
    {
      path: '/reception',
      component: Reception,
    }

  ]
})
//挂载路由导航守卫
const VueRouterPush = VueRouter.prototype.push
VueRouter.prototype.push = function push (to) {
  return VueRouterPush.call(this, to).catch(err => err)
}

export default router
