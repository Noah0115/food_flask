<template>
  <div>
    <!-- -->
    {{ name }}
  </div>
</template>
import { $set } from 'vue'
this.$set(this.obj, 'b', 2)

<script>
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
    },
  },
};
</script>
<style scoped>
</style>