<template>
  <div class="home" id="home" name="home">
    <!-- 轮播图 -->
    <div class="block">
      <el-carousel height="460px">
        <el-carousel-item v-for="item in carousel" :key="item.carousel_id">
          <img
            style="height: 460px"
            :src="require(`@/assets/PHOTO/${item.imgPath}`)"
            :alt="item.describes"
          />
        </el-carousel-item>
      </el-carousel>
    </div>
    <!-- 轮播图END -->
    <div class="main-box">
      <div class="main">
        <!-- 家常菜展示区域 -->
        <div class="homefood">
          <div class="box-hd">
            <div class="title">家常菜</div>
          </div>
          <div class="box-bd">
            <!-- <div class="promo-list">
              <router-link to>
                <img src="../assets/PHOTO/jcc.jpg" />
              </router-link>
            </div> -->
            <div class="promo-list">
              <ul>
                <li>
                  <img src="../assets/PHOTO/jcc.jpg" />
                </li>
                <li>
                  <img src="../assets/PHOTO/jcc1.jpg" />
                </li>
              </ul>
            </div>
            <div class="list">
              <MyList :list="homefoodList" :isMore="true"></MyList>
            </div>
          </div>
        </div>
        <!-- 家常菜展示区域END -->
        <!-- 海鲜菜展示区域 -->
        <div class="seafood">
          <div class="box-hd">
            <div class="title">海鲜</div>
          </div>
          <div class="box-bd">
            <!-- <div class="promo-list">
              <router-link to>
                <img src="../assets/PHOTO/jcc.jpg" />
              </router-link>
            </div> -->
            <div class="promo-list">
              <ul>
                <li>
                  <img src="../assets/PHOTO/hx1.png" />
                </li>
                <li>
                  <img src="../assets/PHOTO/hx2.jpg" />
                </li>
              </ul>
            </div>
            <div class="list">
              <MyList :list="seafoodList" :isMore="true"></MyList>
            </div>
          </div>
        </div>
        <!-- 海鲜菜展示区域END -->
        <!-- 甜品点心展示区域 -->
        <div class="seafood">
          <div class="box-hd">
            <div class="title">甜品点心</div>
          </div>
          <div class="box-bd">
            <!-- <div class="promo-list">
              <router-link to>
                <img src="../assets/PHOTO/jcc.jpg" />
              </router-link>
            </div> -->
            <div class="promo-list">
              <ul>
                <li>
                  <img src="../assets/PHOTO/tp1.jpg" />
                </li>
                <li>
                  <img src="../assets/PHOTO/tp2.jpg" />
                </li>
              </ul>
            </div>
            <div class="list">
              <MyList :list="sweetfoodList" :isMore="true"></MyList>
            </div>
          </div>
        </div>
        <!-- 甜品点心展示区域END -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FoodHome",

  data() {
    return {
      carousel: [
        {
          carousel_id: 1,
          imgPath: "P1.jpg",
          describes: "123456",
        },
        {
          carousel_id: 2,
          imgPath: "P2.jpg",
          describes: "123456",
        },
        {
          carousel_id: 3,
          imgPath: "P3.jpg",
          describes: "123456",
        },
        {
          carousel_id: 4,
          imgPath: "P4.jpg",
          describes: "123456",
        },
      ],
      homefoodList: [
        {
          id: "1",
          name: "红烧排骨",
          cover: "jcc1.jpg",
          flavour: "咸鲜味",
          difficult: "初级入门",
        },
        {
          id: "2",
          name: "史",
          cover: "jcc1.jpg",
          flavour: "史66",
          difficult: "简单",
        },
        {
          id: "3",
          name: "史",
          cover: "jcc1.jpg",
          flavour: "史66",
          difficult: "简单",
        },
        {
          id: "4",
          name: "红烧排骨",
          cover: "jcc1.jpg",
          flavour: "咸鲜味",
          difficult: "初级入门",
        },
        {
          id: "5",
          name: "史",
          cover: "jcc1.jpg",
          flavour: "史66",
          difficult: "简单",
        },
        {
          id: "6",
          name: "史",
          cover: "jcc1.jpg",
          flavour: "史66",
          difficult: "简单",
        },
        {
          id: "7",
          name: "红烧排骨",
          cover: "jcc1.jpg",
          flavour: "咸鲜味",
          difficult: "初级入门",
        },
      ],
      seafoodList:"",
      sweetfoodList:""
    };
  },
  created() {
    this.getfoodList();
  },
  mounted() {},

  methods: {
    getfoodList() {
      this.$http.get("/index/get_food_index", {}).then((res) => {
        // console.log('sd',res);
        if (res.data.code === 200) {
          this.homefoodList = res.data.data[0];
          this.seafoodList = res.data.data[1];
          this.sweetfoodList = res.data.data[2];
          this.$message.success(res.data.msg)
        
        }else{this.$message.error(res.data.msg)}
      });
    },
  },
};
</script>

<style scoped>
@import "../assets/css/index.css";
.title {
  font-family: 'YourPreferredFont', sans-serif; /* 替换成你喜欢的字体，如 'Arial', 'Helvetica', 'Georgia' 等 */
  font-size: 24px; /* 字体大小 */
  font-weight: bold; /* 字体粗细，可根据需要调整 */
  color: #333; /* 字体颜色，可根据需要调整 */
  /* 添加其他样式属性 */
}

</style>
