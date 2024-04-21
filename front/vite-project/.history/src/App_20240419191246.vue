<template>
  <div>
    <!-- -->
    {{ name }}
  </div>
</template>

<script>
import { $set } from 'vue'


export default {
  data() {
    return {};
  },
  mounted() {
    this.createName();
  },
  methods: {
    createName() {
      this.name = "张三";
      this.$set(this, 'name', 2)
    },
  },
};
</script>
<style scoped>
</style>