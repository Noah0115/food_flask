<template>
  <div id="notice">
    <!-- 面包屑 -->
    <div class="breadcrumb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item to="/">首页</el-breadcrumb-item>
        <el-breadcrumb-item>所有公告</el-breadcrumb-item>
        <el-breadcrumb-item>公告列表</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 面包屑END -->
    <div class="main">
      <el-card class="box-card">
        <div v-if="pushList.length > 0" class="text item">
          <h1
            v-for="item in pushList"
            :key="item.id"
            class="title"
            @mouseover="changeColor(item.id, true)"
            @mouseout="changeColor(item.id, false)"
            @click="handleClick(item.content)"
            :style="{ color: isHovered === item.id ? 'blue' : 'black' }"
          >
            {{ item.title }}
            <hr class="line" />
          </h1>
        </div>

        <!-- 查窗口 -->
        <el-dialog
          title="查看公告详情"
          :visible.sync="showDialogVisible"
          width="50%"
          
          @close="showDialogClosed"
        >
          <div v-html="detail"></div>
        </el-dialog>
      </el-card>
    </div>
  </div>
</template>

<script>

export default {
  data() {
    return {
      isHovered: false,
      pushList: [],
      showDialogVisible: false,
      detail: '',

    };
  },

  created() {
    this.getPushList();
  },

  methods: {
    async getPushList() {
      //调用请求，第一个参数是请求地址
      const { data: res } = await this.$http.get("/back/get_all_news",);
      if (res.code !== 200) {

        return this.$message.error("获取推送列表失败");
      }
      this.pushList = res.data;

      console.log(this.pushList);
    },
    changeColor(itemId, value) {
      this.isHovered = value ? itemId : null;
    },
    handleClick(content) {
      // 处理点击事件，可以在这里执行您想要的操作
      this.detail = content
      this.showDialogVisible = true;


    },
    showDialogClosed() {
      this.showDialogVisible = false;
    },

  },

}

</script>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh; /* 使容器至少占满整个视口高度 */
}

.content {
  flex: 1; /* 使内容部分占满剩余空间 */
}
.box-card {
  /* 添加 el-card 样式 */
  background-color: #fff;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  padding: 20px;
  height: 890px;
  margin-top: auto;
  /* 添加您的其他样式 */
}
#notice {
  background-color: #f5f5f5;
}
/* 面包屑CSS */
#notice .main {
  width: 1225px;
  /* height: 900px; */
  padding-top: 30px;
  margin: 0 auto;
}
.el-tabs--card .el-tabs__header {
  border-bottom: none;
}
#notice .breadcrumb {
  height: 50px;
  background-color: white;
}
#notice .breadcrumb .el-breadcrumb {
  width: 1225px;
  line-height: 30px;
  font-size: 16px;
  margin: 0 auto;
}
/* 面包屑CSS END */
/* 添加自定义样式 */
.text.item {
  display: flex;
  flex-direction: column;
  align-items: left; /* 文本在垂直方向上居中 */
}

.title {
  margin-bottom: 100px;
  transition: color 0.3s; /* 添加颜色变化的过渡效果 */
  text-align: left; /* 文本在水平方向上居中 */
}
.line {
  border: 0;
  border-top: 1px solid #ccc; /* Add a 1px solid line below each title */
  margin-top: 5px; /* Adjust the margin based on your preference */
}
</style>