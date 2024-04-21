<template>
  <div class="goods" id="goods" name="goods">
    <!-- 面包屑 -->
    <div class="breadcrumb">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item to="/">首页</el-breadcrumb-item>
        <el-breadcrumb-item>所有美食</el-breadcrumb-item>
        <el-breadcrumb-item v-if="search">搜索</el-breadcrumb-item>
        <el-breadcrumb-item v-else>分类</el-breadcrumb-item>
        <el-breadcrumb-item v-if="search">{{ search }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 面包屑END -->
    <!-- 分类标签 -->
    <div class="nav">
      <div class="product-nav">
        <div class="title">分类</div>
        <el-tabs v-model="activeName" type="card">
          <el-tab-pane
            v-for="item in categoryList"
            :key="item.id"
            :label="item.type_name"
            :name="'' + item.id"
          />
        </el-tabs>
      </div>
    </div>
    <!-- 分类标签END -->

    <!-- 主要内容区 -->
    <div class="main">
      <div class="list">
        <MyList :list="product" v-if="product.length > 0"></MyList>
        <div v-else class="none-product">
          抱歉没有找到相关的商品，请看看其他的商品
        </div>
      </div>
      <!-- 分页 -->
      <div class="pagination">
        <el-pagination
          background
          layout="prev, pager, next"
          :page-size="pageSize"
          :total="total"
          :current-page="currentPage"
          @current-change="currentChange"
        ></el-pagination>
      </div>
      <!-- 分页END -->
    </div>
    <!-- 主要内容区END -->
  </div>
</template>

<script>


export default {
  data() {
    return {
      categoryList: "", //分类列表
      categoryID: [], // 分类id
      product: "", // 商品列表
      productList: "",
      total: 0, // 商品总量
      pageSize: 15, // 每页显示的商品数量
      currentPage: 1, //当前页码
      activeName: "-1", // 分类列表当前选中的id
      search: "", // 搜索条件
      searchResults: []
    };
  },
  created() {
    // 获取分类列表
    this.getCategory();
    this.getData()
  },
  activated() {
    this.activeName = "-1"; // 初始化分类列表当前选中的id为-1
    this.total = 0; // 初始化商品总量为0
    this.currentPage = 1; //初始化当前页码为1
    // 如果路由没有传递参数，默认为显示全部商品
    
    if (Object.keys(this.$route.query).length == 0) {
      this.categoryID = [];
      this.activeName = "0";
      return;
    }
    // 如果路由传递了categoryID，则显示对应的分类商品
    if (this.$route.query.food_type != undefined) {
      this.categoryID = this.$route.query.food_type;
      if (this.categoryID.length >= 1) {
        this.activeName = "" + this.categoryID;
      }
      return;
    }
    // 如果路由传递了search，则为搜索，显示对应的分类商品
    if (this.$route.query.search != undefined) {
      // console.log('qqqq', this.$route)
      // this.search = this.$route.query.search;
    }
  },
  watch: {


    activeName: function (val) {

      if (val != this.categoryID[0]) {
        if (val == 0) {
          this.categoryID = [];
        }
        if (val > 0) {
          this.categoryID = [Number(val)];
        }
        // 初始化商品总量和当前页码
        this.total = 0;
        this.currentPage = 1;
        // 更新地址栏链接，方便刷新页面可以回到原来的页面
        // console.log(typeof this.search)

        this.$router.push({
          path: "/foods",
          query: { food_type: this.categoryID },
        });


      }
    },
    // 监听搜索条件，响应相应的商品
    search: function (val) {
      if (val != "") {
        this.categoryID = []
        this.getProductBySearch();
        if (val != this.search) {
          this.$router.push({
            path: "/foods",
            query: { search: this.search },
          });
        }

      }
    },
    // 监听分类id，响应相应的商品
    categoryID: function (val) {

      if (val != "") {
        this.search = ''
        this.getData();
      }
    },
    // 监听路由变化，更新路由传递了搜索条件

    $route: function (val) {
      
      if (val.path == "/foods") {
        // 检查路由参数是否为空对象
        if (Object.keys(val.query).length === 0) {
          // 如果路由参数为空对象，则表示用户访问的是全部商品页面
          this.activeName = "0";
          this.categoryID = []; // 将 categoryID 设置为空数组
          this.currentPage = 1;
          this.getData();
        } else if (val.query.search != null) {
          // 如果有搜索参数，则表示用户进行了搜索
          this.activeName = "0";
          this.categoryID = []; // 将 categoryID 设置为空数组
          this.currentPage = 1;
          this.search = val.query.search;
          // console.log('1111111wd', this.search);
          // this.getProductBySearch();
        }
      }
    },

    // 在组件中监听路由的变化

  },
  mounted() { },

  methods: {
    // 返回顶部
    backtop() {
      const timer = setInterval(function () {
        const top =
          document.documentElement.scrollTop || document.body.scrollTop;
        const speed = Math.floor(-top / 5);
        document.documentElement.scrollTop = document.body.scrollTop =
          top + speed;

        if (top === 0) {
          clearInterval(timer);
        }
      }, 20);
    },
    // 页码变化调用currentChange方法
    currentChange(currentPage) {
      this.currentPage = currentPage;
      console.log(this.currentPage);
      if (this.search != "") {
        // this.getProductBySearch();
      } else {
        this.getData();
      }
      this.backtop();
    },

    // 向后端请求分类列表数据
    getCategory() {
      this.$http
        .get("/goods/alltypes")
        .then((res) => {
          // console.log(res);
          if (res.data.code === 200) {
            this.categoryList = res.data.data;


          }

        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
    getData() {
      const api =
        this.categoryID.length == 0 ? "/goods" : "/goods/goods_search_by_type";
      // 计算起始索引
      const startIndex = (this.currentPage - 1) * this.pageSize;
      // 计算结束索引
      const endIndex = startIndex + this.pageSize;
      this.$http
        .post(api, {
          food_type: this.categoryID[0],
        })
        .then((res) => {

          if (res.data.code === 200) {
            this.$message.success(res.data.msg)
            this.total = res.data.data.length;

            this.product = res.data.data.slice(startIndex, endIndex);
          } else { (this.$message.error(res.data.msg)) }
        });
    },
    handleSizeChange(newSize) {
      console.log(newSize);
      this.queryInfo.pagesize = newSize;
      this.getUserList();
    },
    // 通过搜索条件向后端请求商品数据
    getProductBySearch() {

      const startIndex = (this.currentPage - 1) * this.pageSize;
      // 计算结束索引
      const endIndex = startIndex + this.pageSize;
      this.$http
        .post("/index/food_search", {
          search_name: this.search,
        })
        .then((res) => {
          // console.log(res)

          this.searchResults = res.data;
          this.product = this.searchResults.slice(startIndex, endIndex);
          this.$message.success('搜索成功')

        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
  },
};
</script>

<style scoped>
.goods {
  background-color: #f5f5f5;
}
/* 面包屑CSS */
.el-tabs--card .el-tabs__header {
  border-bottom: none;
}
.goods .breadcrumb {
  height: 50px;
  background-color: white;
}
.goods .breadcrumb .el-breadcrumb {
  width: 1225px;
  line-height: 30px;
  font-size: 16px;
  margin: 0 auto;
}
/* 面包屑CSS END */

/* 分类标签CSS */
.goods .nav {
  background-color: white;
}
.goods .nav .product-nav {
  width: 1225px;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
}
.nav .product-nav .title {
  width: 50px;
  font-size: 16px;
  font-weight: 700;
  float: left;
}
/* 分类标签CSS END */

/* 主要内容区CSS */
.goods .main {
  margin: 0 auto;
  max-width: 1225px;
}
.goods .main .list {
  min-height: 650px;
  padding-top: 14.5px;
  margin-left: -13.7px;
  overflow: auto;
}
.goods .main .pagination {
  height: 50px;
  text-align: center;
}
.goods .main .none-product {
  color: #333;
  margin-left: 13.7px;
}
/* 主要内容区CSS END */
</style>
