<template>
  <div>
    <!-- -->
    {{ this.name }}
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  mounted() {
    this.createName();
  },
  created: {
    createName() {
      this.name = "张三";
      console.log(this.name)
    },
  },
};
</script>
<style scoped>
</style>