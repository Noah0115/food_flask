<template>
  <div>
    <!-- -->
    <input type="text" ref="myElement" />
    <button @click="handleClick"></button>
  </div>
</template>

<script setup>
import { getCurrentInstance, ref, toRefs } from "vue";

// 在组件中使用
// const myElement = ref(null)
const handleClick()=> {
  const _this = getCurrentInstance();
  console.log(_this.root);
}
</script>
