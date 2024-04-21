<template>
  <div>
    <!-- -->
    <input type="text" ref="myElement"/>
    <button @click="handelecl"></button>
  </div>
</template>

<script setup>
import { ref, toRefs } from "vue";

// 在组件中使用
const myElement = ref(null);

console.log(myElement.value);
</script>
