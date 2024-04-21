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
const _this = getCurrentInstance();
// const myElement = ref(null)
const handleClick=()=> {
  
  console.log(_this.$ref['myElement']);
}
</script>
