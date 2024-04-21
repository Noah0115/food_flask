<template>
  <div>
    <!-- -->
    {{ this.name }}
    <input v-model="name">
  </div>
</template>
  
  <script>
export default {
  data() {
    return {};
  },
  watch()
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