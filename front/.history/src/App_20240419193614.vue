<template>
  <div>
    <!-- -->
    {{ this.name }}
    <input v-model="">
  </div>
</template>
  
  <script>
export default {
  data() {
    return {};
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