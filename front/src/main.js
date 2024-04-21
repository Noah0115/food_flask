// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueRouter from 'vue-router'
import axios from 'axios'
import Element from 'element-ui'
import store from './store'
Vue.use(Element)
// import "./mock/index.js"
import VueECharts from "vue-echarts";
Vue.component("v-chart", VueECharts);
import 'echarts'
import ECharts from 'vue-echarts'
Vue.component('VueEcharts', ECharts)
/* console.log(ECharts) */
import '../node_modules/element-ui/lib/theme-chalk/index.css'
import '../src/assets/style.css'
import './theme/index.css'
import './assets/css/global.css'
import './assets/fonts/iconfont.css'
import VueQuillEditor from 'vue-quill-editor'

Vue.use(VueQuillEditor)
//导入富文本编辑器对应的样式
import 'quill/dist/quill.core.css' // import styles
import 'quill/dist/quill.snow.css' // for snow theme
import 'quill/dist/quill.bubble.css' // for bubble theme
import  inputDirective from 'vue-el-input-directive'
Vue.use(inputDirective)


Vue.config.productionTip = false
Vue.use(VueRouter)

// axios.defaults.baseURL = 'http://127.0.0.1:8000'
//axios.defaults.baseURL = 'http://82.156.147.153:8020'
axios.defaults.baseURL = 'http://82.156.147.153:8025'
// axios.defaults.baseURL = 'http://127.0.0.1:8025'
// axios.defaults.headers['Content-Type'] = 'multipart/form-data'
axios.defaults.headers['Content-Type'] = 'application/json'
// axios.defaults.withCredentials = true;
Vue.prototype.$http = axios

axios.interceptors.request.use(config =>{
  /* console.log(config) */
  config.headers.Authorization = window.sessionStorage.getItem('token')
  
  return config
},
error => {
  // 跳转error页面
  router.push({ path: "/error" });
  return Promise.reject(error);
})
// main.js or your entry point
router.beforeEach((to, from, next) => {
  // 如果该路由有meta信息
  if (to.meta && to.meta.title) {
    document.title = to.meta.title;
  } else {
    // 如果没有meta信息，可以设置一个默认标题
    document.title = '默认标题';
  }
  next();
});
// 全局拦截器,在进入需要用户权限的页面前校验是否已经登录
router.beforeResolve((to, from, next) => {
  let user = null;
  // 判断路由是否设置相应校验用户权限
  if (to.meta.requireAuth) {
    let userData = window.localStorage.getItem('user');
    
    if(userData!=''){
    user=JSON.parse(userData)
    }else{
      userData = "{\"is_admin\":false}";
      user=JSON.parse(userData)
      console.log("ssd",userData)
    }
    
    if (!user.is_admin) {
      // 没有登录，显示登录组件
      store.dispatch("setShowLogin", true);
      if (from.name == null) {
        //此时，是在页面没有加载，直接在地址栏输入链接，进入需要登录验证的页面
        next("/");
        return;
      }
      // 终止导航
      next(false);
      return;
    }
  }
  next();
});
// 全局自定义指令
/* Vue.directive('role', {
    inserted: (el, binding) => {
      const allowedRoles = binding.value;
      const userRole = store.state.userRole; // 从 Vuex 获取用户角色信息
      if (!allowedRoles.includes(userRole)) {
        el.parentNode.removeChild(el);
      }
    }
  }); */
// // 全局注册组件
Vue.component("App", App);

axios.interceptors.response.use(
  res => {
    if (res.data.code === "401") {
      // 401表示没有登录
      // 提示没有登录
      Vue.prototype.notifyError(res.data.msg);
      // 修改vuex的showLogin状态,显示登录组件
      store.dispatch("setShowLogin", true);
    }
    if (res.data.code === "500") {
      // 500表示服务器异常
      // 跳转error页面
      router.push({ path: "/error" });
    }
    return res;
  },
  error => {
    // 跳转error页面
    router.push({ path: "/error" });
    return Promise.reject(error);
  }
);

//全局组件
import MyMenu from './components/MyMenu';
Vue.component(MyMenu.name, MyMenu);
import MyList from './components/MyList';
Vue.component(MyList.name, MyList);
import MyLogin from './components/MyLogin';
Vue.component(MyLogin.name, MyLogin);
import MyUser from './components/MyUser';
Vue.component(MyUser.name, MyUser);
Vue.config.productionTip = false;
import MyRegister from './components/MyRegister';
Vue.component(MyRegister.name, MyRegister);
/* eslint-disable no-new */
new Vue({

    router,
    store, 
    render: h => h(App)
}).$mount('#app')
