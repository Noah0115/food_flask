<template>
  <div>
    <el-container>
      <!-- 顶部导航栏 -->
      <div class="topbar">
        <div class="nav">
          <ul>
            <li v-if="!this.$store.getters.getUser">
              <el-button type="text" @click="login">登录</el-button>
              <span class="sep">|</span>
              <el-button type="text" @click="register = true">注册</el-button>
            </li>
            <div v-else>
              <li v-if="this.$store.getters.getUser.is_admin">
                  <el-button type="text" @click="adminHome">进入管理员后台</el-button>
              </li> 
              <li>欢迎</li>
              <el-popover placement="top" width="180" v-model="visible">
                <el-button type="text" slot="reference">{{
                  this.username
                }}</el-button>
                <p>确定退出登录吗？</p>
                <div style="text-align: right; margin: 10px 0 0">
                  <el-button size="mini" type="text" @click="visible = false"
                    >取消</el-button
                  >
                  <el-button type="primary" size="mini" @click="logout"
                    >确定</el-button
                  >
                </div>
                
              </el-popover>

              <el-button type="text" @click="userinfo = true">修改个人资料</el-button>  
              
            </div>
          </ul>
        </div>
      </div>
      <!-- 顶部导航栏END -->
      <el-header>
        <el-menu
          :default-active="activeIndex"
          class="el-menu-demo"
          mode="horizontal"
          active-text-color="#409eff"
          router
        >
          <div class="logo">
            <router-link to="/">
              <!-- <img src="./assets/imgs/logo.png" alt /> -->
            </router-link>
          </div>
          <el-menu-item index="/">首页</el-menu-item>
          <el-menu-item index="/foods">所有美食</el-menu-item>
          <el-menu-item index="/analysis">美食分析</el-menu-item>
          <el-menu-item index="/notice">公告查看</el-menu-item>
          <div class="so">
            <el-input placeholder="请输入搜索内容" v-model="search">
              <el-button
                slot="append"
                icon="el-icon-search"
                @click="searchClick"
              ></el-button>
            </el-input>
          </div>
        </el-menu>
      </el-header>
      <!-- 登录模块 -->
      <MyLogin @sendUsername="getUsername"></MyLogin>
      <!-- 注册模块 -->
      <MyRegister :register="register" @fromChild="isRegister"></MyRegister>
      <MyUser :userinfo="userinfo" @fromChild="isUserinfo"></MyUser>
      <el-main>
        <!-- 路由占位符 -->
        <keep-alive>
          <router-view></router-view>
        </keep-alive>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import { mapGetters } from "vuex";
import ChildComponent from '@/components/MyLogin.vue'
export default {
  beforeUpdate() {
    this.activeIndex = this.$route.path;
  },
  components: {
    ChildComponent
  },
  data() {
    return {
      activeIndex: "", // 头部导航栏选中的标签
      search: "", // 搜索条件
      register: false, // 是否显示注册组件
      visible: false, // 是否退出登录
      admin: true,
      userinfo: false,//是否显示用户信息组件
      username: ''
    };
  },
  created() {
    // 获取浏览器localStorage，判断用户是否已经登录
    if (localStorage.getItem("user")) {
      // 如果已经登录，设置vuex登录状态
      this.setUser(JSON.parse(localStorage.getItem("user")));
      this.username = this.$store.getters.getUser.name
    }
  },
  computed: {
    ...mapGetters(["getUser", "getNum"])
  },
  methods: {
    ...mapActions(["setUser", "setShowLogin"]),
    login() {
      // 点击登录按钮, 通过更改vuex的showLogin值显示登录组件
      this.setShowLogin(true);
      // console.log(JSON.parse(localStorage.getItem("user")));
      // this.username=this.$store.getters.getUser.name
    },
    getUsername(data) {
      this.username=data  
    },
    // 退出登录
    logout() {
      this.visible = false;
      // 清空本地登录信息
      localStorage.setItem("user", "");
      // 清空vuex登录信息
      this.setUser("");
      this.$message.success("成功退出登录");

    },

    // 接收注册子组件传过来的数据
    isRegister(val) {
      this.register = val;
    },
    isUserinfo(val) {
      this.userinfo = val;
      this.setUser(JSON.parse(localStorage.getItem("user")));
      this.username = this.$store.getters.getUser.name
    },
    // 点击搜索按钮
    searchClick() {
      if (this.search != "") {
        // 跳转到全部商品页面,并传递搜索条件
        this.$router.push({ path: "/foods", query: { search: this.search } });
        this.search = "";
      }

    },
    adminHome() {
      this.$router.push({ path: "/adminhome" });
    },
    // receiveUsername(username) {
    //   console.log('sdasda',username)
    //   this.username = username;
    // }


  }
};
</script>
<style>
/* 全局CSS */
* {
  padding: 0;
  margin: 0;
  border: 0;
  list-style: none;
}
#app .el-header {
  padding: 0;
}
#app .el-main {
  min-height: 300px;
  padding: 20px 0;
}
#app .el-footer {
  padding: 0;
}
a,
a:hover {
  text-decoration: none;
}
/* 全局CSS END */

/* 顶部导航栏CSS */
.topbar {
  height: 40px;
  background-color: #3d3d3d;
  margin-bottom: 20px;
}
.topbar .nav {
  width: 1225px;
  margin: 0 auto;
}
.topbar .nav ul {
  float: right;
}
.topbar .nav li {
  float: left;
  height: 40px;
  color: #b0b0b0;
  font-size: 14px;
  text-align: center;
  line-height: 40px;
  margin-left: 20px;
}
.topbar .nav .sep {
  color: #b0b0b0;
  font-size: 12px;
  margin: 0 5px;
}
.topbar .nav li .el-button {
  color: #b0b0b0;
}
.topbar .nav .el-button:hover {
  color: #fff;
}
.topbar .nav li a {
  color: #b0b0b0;
}
.topbar .nav a:hover {
  color: #fff;
}
.topbar .nav .shopCart {
  width: 120px;
  background: #424242;
}
.topbar .nav .shopCart:hover {
  background: #fff;
}
.topbar .nav .shopCart:hover a {
  color: #ff6700;
}
.topbar .nav .shopCart-full {
  width: 120px;
  background: #ff6700;
}
.topbar .nav .shopCart-full a {
  color: white;
}
/* 顶部导航栏CSS END */

/* 顶栏容器CSS */
.el-header .el-menu {
  max-width: 1225px;
  margin: 0 auto;
}
.el-header .logo {
  height: 60px;
  width: 189px;
  float: left;
  margin-right: 100px;
}
.el-header .so {
  margin-top: 10px;
  width: 300px;
  float: right;
}
/* 顶栏容器CSS END */

/* 底栏容器CSS */
.footer {
  width: 100%;
  text-align: center;
  background: #2f2f2f;
  padding-bottom: 20px;
}
.footer .ng-promise-box {
  border-bottom: 1px solid #3d3d3d;
  line-height: 145px;
}
.footer .ng-promise-box {
  margin: 0 auto;
  border-bottom: 1px solid #3d3d3d;
  line-height: 145px;
}
.footer .ng-promise-box .ng-promise p a {
  color: #fff;
  font-size: 20px;
  margin-right: 210px;
  padding-left: 44px;
  height: 40px;
  display: inline-block;
  line-height: 40px;
  text-decoration: none;
  /* background: url("./assets/imgs/us-icon.png") no-repeat left 0; */
}
.footer .github {
  height: 50px;
  line-height: 50px;
  margin-top: 20px;
}
.footer .github .github-but {
  width: 50px;
  height: 50px;
  margin: 0 auto;
  /* background: url("./assets/imgs/github.png") no-repeat; */
}
.footer .mod_help {
  text-align: center;
  color: #888888;
}
.footer .mod_help p {
  margin: 20px 0 16px 0;
}

.footer .mod_help p a {
  color: #888888;
  text-decoration: none;
}
.footer .mod_help p a:hover {
  color: #fff;
}
.footer .mod_help p span {
  padding: 0 22px;
}
/* 底栏容器CSS END */
</style>
