<template>
  <div>
    <!-- -->
  </div>
</template>

<script setup>
import { onBeforeMount } from "vue";
import Field from "./components/Field.vue";
import useTabbarStore from "./store/tabbarStore";
const store =useTabbarStore()
// const {isTabbarShow} =useTabbarStore()
// store 是一个reactive包装的对象，结构之后可以拿到值，但是失去了响应式
const {isTabbarShow}=storeTorefs(store)
onBeforeMount(()=>{
    store.isTabbarShow=false
    store.$patch
})
</script>
