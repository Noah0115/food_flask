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
function handleClick() {
  const { proxy } = getCurrentInstance();
  console.log(proxy);
}
</script>
