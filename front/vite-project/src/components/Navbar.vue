<template>
  <div class="nember1">
    <!--  <button v-show="leftShow" class="mybtn" @click="handleClick()">
      {{ title }}
    </button>
    <div>{{ left }}</div>
    <button v-bind="$attrs" >{{ 透传 }}</button>
    <button v-bind="$attrs" >{{ 透传 }}</button> -->
    <!-- <button v-bind="$attrs">
      展开折叠侧边栏
    </button> -->
    <button @click="handleClick">展开折叠侧边栏</button>
    <!-- <button @click="$emit('event',num)">测试按钮2</button> -->
    <div>vue3单文件</div>
  </div>
</template>
<script>
export default {
  // inheritAttrs:false,
  // props: ["title", "left", "right","leftShow","rightShow"],
  props: {
    title: String,
    left: [String, Number],
    right: {
      required: true,
      // 校验器
      validator(val) {
        return ["success", "warning", "danger"].includes(val);
      },
    },
    leftShow: {
      type: Boolean,
      default: true,
    },
    rightShow: Boolean,
  },
  data() {
    return {
      num: 1,
    };
  },
  methods: {
    handleClick() {
      // console.log("11");
      // this.$emit("event");
      this.$parent.$refs.mylayout.isShow=!this.$parent.$refs.mylayout.isShow
      console.log(this.$parent.$refs.mylayout.isShow)
    },
  },
};
</script>

<style scoped>
div {
  background: gray;
}
.number1 {
  display: flex;
  flex-direction: row;
}
.mybtn {
  flex: 1;
}
</style>
