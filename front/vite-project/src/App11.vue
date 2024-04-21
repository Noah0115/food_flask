<template>
  <div class="root">
    <!-- <Navbar @click="handleClick" ></Navbar> -->
    <!-- <Navbar  ref="mynavbar"></Navbar> -->
    <Navbar></Navbar>

    <!--  <Navbar class="navbar" title="影院"></Navbar>
    <Navbar class="navbar" title="我的"></Navbar> -->
    <Layout ref="mylayout"></Layout>
    <!-- <button @click="handleClick">测试</button>
    <input ref="myinput"> -->
  </div>
</template>

<script>

import Layout from "./components/Layout.vue";
import Navbar from "./components/Navbar.vue";
export default {
  components: {
    Navbar,
    Layout,
  },
  data() {
    return {
      isShow: true,
      proobj: {
        title: "首页",
        left: "返回",
        right: "首页",
        leftShow: true,
        rightShow: false,
      },
    };
  },

  mounted() {},

  methods: {
    myclick() {
      console.log("123");
    },
    handleClick() {
      console.log(this.$refs.mynavbar);
      
      /* this.isShow = !this.isShow; */
    },
    handleEvent() {
      this.isShow = !this.isShow;
    },
    handleEvent2(data){
      console.log('sdas',data);
    }
  },
};
</script> 
<style>
* {
  margin: 0;
  padding: 0;
}
.root {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.navbar {
  height: 70px;
}
.layout {
  flex: 1;
  display: flex;
}
</style>
