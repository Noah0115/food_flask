<template>
  <div>
    <!-- -->
  </div>
</template>

<script setup>
import { onBeforeMount } from "vue";
import Field from "./components/Field.vue";
import useTabbarStore from "./store/tabbarStore";
import useCinemaStore from './store/cinemaStore'
const store =useTabbarStore()
// const {isTabbarShow} =useTabbarStore()
// store 是一个reactive包装的对象，结构之后可以拿到值，但是失去了响应式
const {isTabbarShow}=storeTorefs(store)
const cinema=useCinemaStore()
onBeforeMount(()=>{
    // store.isTabbarShow=false
    // 补丁式的合并
    store.$patch({
        isTabbarShow:false
    })
    // 设置为初始值
    store.$reset()
    //直接修改
    store.change(true)
})
</script>
