<template>
  <div>
    <!-- -->
    <input type="text" ref="myElement"/>
    <button @click="handleClick"></button>
  </div>
</template>

<script setup>
import { ref, toRefs } from "vue";

// 在组件中使用
const myElement = ref(null);
handleClick(){
  console.log(myElement.value);
}

</script>
