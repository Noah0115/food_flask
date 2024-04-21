<template>
  <div>
    <!-- -->
    <input type="text" ref="myElement" />
    <button @click="handleClick"></button>
  </div>
</template>

<script setup>
import { getCurrentInstance, ref, toRefs } from "vue";
const { proxy } = getCurrentInstance;
// 在组件中使用
// const myElement = ref(null)
function handleClick() {
  console.log(proxy);
}
</script>
