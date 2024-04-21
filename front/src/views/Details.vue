<template>
  <div id="details">
    <!-- 头部 -->
    <div class="page-header">
      <div class="title">
        <p>{{ productDetails.name }}</p>
        
      </div>
    </div>
    <!-- 头部END -->

    <!-- 主要内容 -->
    <div class="main">
      <!-- 左侧商品轮播图 -->
      <div class="block">
        
        <img
          style="height: 560px; width: 560px; max-width: 100%"
          :src="productPicture"
          :alt="123"
        />
        <!-- </div> -->
      </div>
      <!-- 左侧商品轮播图END -->

      <!-- 右侧内容区 -->
      <div class="content">
        <h1
          class="name"
          style="
            font-size: 32px;
            color: #222;
            line-height: 42px;
            font-weight: 700;
            padding-top: 10px;
            margin-right: 40px;
          "
        >
          {{ productDetails.name }}
        </h1>
        <p
          class="intro"
          style="
            font-size: 16px;
            line-height: 26px;
            color: #666;
            font-weight: 400;
          "
        >
          烹饪难度：{{ productDetails.difficult }}
        </p>
        <!-- <p class="store">小米自营</p> -->
        <div class="price">
          <span>口味：{{ productDetails.flavour }}</span>
        </div>
        <div class="price">
          <span>烹饪时间：{{ productDetails.cost_time }}</span>
        </div>

        
        <div class="pro-list">
          <p class="price-sum">主料 : {{ productDetails.ingredients }}</p>
        </div>

        <div class="pro-list">
          <p class="price-sum">辅料 : {{ productDetails.accessories }}</p>
        </div>

        
      </div>
      <!-- 右侧内容区END -->
      <el-card class="box-card">
        <div slot="header" class="clearfix" style="font-size: 20px;font-weight: bold;">
          <span>{{ productDetails.name }}的做法</span>
        </div>
        <div
          v-for="index in Math.min(stepList.length, picList.length)"
          :key="index"
          class="text item"
        >
          <!-- 图片 -->
          <img
            :src="picList[index - 1]"
            :alt="'图片 ' + index"
            style="max-width: 100%; height: auto"
          />
          <!-- 步骤内容 -->
          <h3>
            {{ stepList[index - 1] }}
          </h3>
        </div>
      </el-card>
    </div>
    <!-- 主要内容END -->
  </div>
</template>
<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      dis: false, // 控制“加入购物车按钮是否可用”
      productID: "", // 商品id
      productDetails: "", // 商品详细信息
      productPicture: "", // 商品图片
      stepList: [],
      picList: [],
    };
  },
  created() {},
  // 通过路由获取商品id
  activated() {
    if (this.$route.query.productID != undefined) {
      this.productID = this.$route.query.productID;
    }
  },
  watch: {
    // 监听商品id的变化，请求后端获取商品数据
    productID: function (val) {
      this.getDetails(val);
      /* this.getDetailsPicture(val); */
    },
  },
  methods: {
    ...mapActions(["unshiftShoppingCart", "addShoppingCartNum"]),
    // 获取商品详细信息
    getDetails(val) {
      this.$http
        .post("/goods/goods_info", {
          id: val,
        })
        .then((res) => {
          if (res.data.code === 200) {
            this.$message.success(res.data.msg);
            this.productDetails = res.data.data[0];
            this.productPicture = this.productDetails.cover;
            this.stepList = this.productDetails.step;
            this.picList = this.productDetails.pic_path;
            /* console.log(this.picList); */
          }else{
            this.$message.error(res.data.msg);
          }
        })
        .catch((err) => {
          return Promise.reject(err);
        });
    },
  },
};
</script>
<style>
/* 头部CSS */
#details .page-header {
  height: 64px;
  margin-top: -20px;
  z-index: 4;
  background: #fff;
  border-bottom: 1px solid #e0e0e0;
  -webkit-box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.07);
  box-shadow: 0px 5px 5px rgba(0, 0, 0, 0.07);
}
#details .page-header .title {
  width: 1225px;
  height: 64px;
  line-height: 64px;
  font-size: 18px;
  font-weight: 400;
  color: #212121;
  margin: 0 auto;
}
#details .page-header .title p {
  float: left;
}
#details .page-header .title .list {
  height: 64px;
  float: right;
}
#details .page-header .title .list li {
  float: left;
  margin-left: 20px;
}
#details .page-header .title .list li a {
  font-size: 14px;
  color: #616161;
}
#details .page-header .title .list li a:hover {
  font-size: 14px;
  color: #ff6700;
}
/* 头部CSS END */

/* 主要内容CSS */
#details .main {
  width: 1225px;
  /* height: 900px; */
  padding-top: 30px;
  margin: 0 auto;
}
#details .main .block {
  float: left;
  width: 560px;
  height: 560px;
}
#details .el-carousel .el-carousel__indicator .el-carousel__button {
  background-color: rgba(163, 163, 163, 0.8);
}
#details .main .content {
  float: left;
  margin-left: 25px;
  width: 640px;
}
#details .main .content .name {
  height: 30px;
  line-height: 30px;
  font-size: 24px;
  font-weight: normal;
  color: #212121;
}
#details .main .content .intro {
  color: #b0b0b0;
  padding-top: 10px;
}
#details .main .content .store {
  color: #ff6700;
  padding-top: 10px;
}
#details .main .content .price {
  display: block;
  font-size: 18px;
  color: #ff6700;
  border-bottom: 1px solid #e0e0e0;
  padding: 25px 0 25px;
}
#details .main .content .price .del {
  font-size: 14px;
  margin-left: 10px;
  color: #b0b0b0;
  text-decoration: line-through;
}
#details .main .content .pro-list {
  background: #f9f9fa;
  padding: 30px 60px;
  margin: 50px 0 50px;
}
#details .main .content .pro-list span {
  line-height: 30px;
  color: #616161;
}
#details .main .content .pro-list .pro-price {
  float: right;
}
#details .main .content .pro-list .pro-price .pro-del {
  margin-left: 10px;
  text-decoration: line-through;
}
#details .main .content .pro-list .price-sum {
  color: #ff6700;
  font-size: 24px;
  padding-top: 20px;
}
#details .main .content .button {
  height: 55px;
  margin: 10px 0 20px 0;
}
#details .main .content .button .el-button {
  float: left;
  height: 55px;
  font-size: 16px;
  color: #fff;
  border: none;
  text-align: center;
}
#details .main .content .button .shop-cart {
  width: 340px;
  background-color: #ff6700;
}
#details .main .content .button .shop-cart:hover {
  background-color: #f25807;
}

#details .main .content .button .like {
  width: 260px;
  margin-left: 40px;
  background-color: #b0b0b0;
}
#details .main .content .button .like:hover {
  background-color: #757575;
}
#details .main .content .pro-policy li {
  float: left;
  margin-right: 20px;
  color: #b0b0b0;
}

/* 主要内容CSS END */
</style>
