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
  created() {
    this.createName();
  },
  methods: {
    createName() {
      this.name = "张三";
      console.log(this.name)
    },
  },
};
</script>
<style scoped>
</style>