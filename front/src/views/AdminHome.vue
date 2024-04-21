<template>
  <el-container class="el-cont" style="height: 100%">
    <el-header>
      <div>
        <!-- <img src="../assets/heima.png" alt=""  /> -->
        <span>美食数据分析可视化系统</span>
      </div>
      <el-button type="primary" @click="goToFrontend" style="margin-right: 20px;">返回前台</el-button>
    </el-header>
    <el-container>
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <div class="toggle-button" @click="toggleCollapse">|||</div>
        <!-- 菜单 -->
        <el-menu
          background-color="#333744"
          text-color="#fff"
          active-text-color="#409EFF"
          unique-opened
          :collapse="isCollapse"
          :collapse-transition="false"
          router
          :default-active="activePath"
        >
          <!-- 一级菜单 -->
          <el-submenu
            :index="item.id + ''"
            v-for="item in menulist"
            :key="item.id"
          >
            <!-- 模板 -->
            <template slot="title">
              <i :class="iconObj[item.id]"></i>
              <span>{{ item.authName }}</span>
            </template>
            <!-- 二级菜单 -->

            <el-menu-item
              v-for="subItem in item.children"
              :index="'/' + subItem.path"
              :key="subItem.id"
              @click="saveNavState('/' + subItem.path)"
            >
              <template slot="title">
                <i class="el-icon-menu"></i>
                <span>{{ subItem.authName }}</span>
              </template>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>

      <el-main>
        <!-- 路由占位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>

export default {
  data() {
    return {
      menulist: [{
        // 用户管理、美食管理、公告管理、美食数据爬取、美食数据可录入、数据统计、数据分析、安全退出系统
        authName: '用户管理',
        id: '125',
        children: [{
          authName: '用户列表',
          path: 'user',
        }
        ],

      },
      {
        authName: '美食管理',
        id: '145',
        children: [{
          authName: '美食列表',
          path: 'adminfood',
        }
        ],
      },
      {
        authName: '公告管理',
        id: '102',
        children: [{
          authName: '公告列表',
          path: 'adminnotice',
        }
        ],

      },
      {
        authName: '美食数据管理',
        id: '103',
        children: [{
          authName: '美食数据爬取',
          path: 'adminscraper',

        }
       /*  {
          authName: '美食数据可录入',
          path: 'admindata',

        } */
        , {
          authName: '数据统计与分析',
          path: 'adminanalysis',
        },
        ],

      },

      ],
      iconObj: {
        '125': 'el-icon-user-solid',
        '103': 'el-icon-s-promotion',
        '101': 'iconfont icon-shangpin',
        '102': 'el-icon-s-comment',
        '145': 'el-icon-s-data',
        '110': 'el-icon-s-tools'
      },
      isCollapse: false,
      //被激活的链接地址
      activePath: '',

      userid: '',
      userInfo: {

      },
      username: '',
      userpic: ''

    }
  },
  created() {

    // this.activePath = window.sessionStorage.getItem('activePath')
  },
  methods: {
    getUserId() {
      this.userid = sessionStorage.getItem('userid')
    },

    errorHandler() {
      return true
    },
    logout() {
      window.sessionStorage.clear();
      this.$router.push("/login");
    },
    /* 点击按钮切换折叠和展开 */
    toggleCollapse() {
      this.isCollapse = !this.isCollapse
    },
    //保存链接的激活状态
    saveNavState(activePath) {
      window.sessionStorage.setItem('activePath', activePath)
      this.activePath = activePath
    },
    handleCommand(command) {
      if (command === 'a') {
        this.$router.push("/info");
      } else {
        this.logout()
      }
    },
    filteredSubItems(children) {
      return children.filter(subItem => this.checkRole(subItem.role));
    },
    goToFrontend(){
      this.$router.push("/");
    }

  },


}
</script>

<style lang="less" scoped>
.el-cont {
  height: 100%;
}
.el-header {
  background-color: #373d41;
  display: flex;
  justify-content: space-between; //左右贴边对齐
  padding-left: 0; //左边距 清空，贴边
  align-items: center; //按钮居中
  color: #fff;
  font-size: 20px;
  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px; //图片与文字间距
    }
  }

  //纵向居中
}
.el-aside {
  background-color: #333744;
  .el-menu {
    border-right: none;
  }
}
.el-main {
  background-color: #eaedf1;
  padding-bottom: 0;
  
}

.iconfont {
  margin-right: 10px;
}

.toggle-button {
  background-color: #4a5064;
  font-size: 10px;
  line-height: 24px;
  color: #fff;
  text-align: center;
  letter-spacing: 0.2em; //字体间距
  cursor: pointer; //鼠标放上变小手
}
.userphoto {
  display: flex; //弹性模型
  justify-content: flex-end; //尾部对齐
  float: right;
}
</style>