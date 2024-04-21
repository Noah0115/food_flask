<template>
  <div>
    <!-- -->
    <div ref="myElement"></div>
  </div>
</template>

<script setup>
import { getCurrentInstance } from 'vue';
import { ref, toRefs } from 'vue'
 
// 在组件中使用
setup() {
  const myElement = ref(null)
 
  return {
    ...toRefs(myElement)
  }
}
</script>
