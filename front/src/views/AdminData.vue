<template>
  <div>
    <!-- 面包屑导航 -->
    <div class="breadcrumb1">
      <el-breadcrumb>
        <el-breadcrumb-item :to="{ path: '/welcome' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item>美食数据管理</el-breadcrumb-item>
        <el-breadcrumb-item>美食数据可录入</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <el-card>
      <el-button @click="datainit">数据初始化</el-button>
      <el-button>数据库导入</el-button>
    </el-card>
    <el-card body-style="height: 900px"> </el-card>
  </div>
</template>
  
  <script>


export default {
  data() {
    return {

    };
  },
  mounted() {

  },
  methods: {
    async datainit(){
      const { data: res } = await this.$http.get("/back/data_init");
      console.log(res)
    }

  },
  computed: {

  }
};
  </script>
  <style lang='less' scoped>
.breadcrumb1 .el-breadcrumb {
  font-size: 16px !important;
}
.el-table {
  margin-top: 20px;
}
.btns {
  display: flex; //弹性模型
  justify-content: flex-end; //尾部对齐
}
</style>