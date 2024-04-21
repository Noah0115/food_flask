<template>
  <div>
    <!-- -->
  </div>
</template>

<script setup>
import Field from "./components/Field.vue";
import useTabbarStore from "./store/tabbarStore";
const store =useTabbarStore()
// const {isTabbarShow} =useTabbarStore()
// store 是一个reactive包装的对象，结构之后可以拿到值，但是失去了响应式
const {}=storeTorefs(store)
</script>
