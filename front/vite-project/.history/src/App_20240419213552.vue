<template>
  <div>
    <!-- -->
    <input type="text" ref="myElement" />
    <button @click="handleClick"></button>
  </div>
</template>

<script setup>
import { ref, toRefs } from "vue";
getC
// 在组件中使用
const myElement = ref(null)
function handleClick(){
  console.log(myElement.value);
}

</script>
