<template>
  <div>
    <!-- -->
    {{ this.name }}
    <input v-model="name">
  </div>
</template>
  
  <script>
import { log } from 'echarts/types/src/util/log.js';

export default {
  data() {
    return {};
  },
  watch(){
    name(){
        console.log('111');
        
    }
  },
  created() {
    this.createName();
  },
  methods: {
    createName() {
      this.name = "张三";
    //   console.log(this.set);
    // this.set(this.someObject, "name", 2);
    },
  },
};
</script>
  <style scoped>
</style>