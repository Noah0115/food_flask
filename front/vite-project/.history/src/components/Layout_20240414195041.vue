<template>
  <div>
    <Sidebar v-if="isShow"></Sidebar>
    <Content></Content>
  </div>
</template>
<script>
import Sidebar from "./Sidebar.vue";
import Content from "./Content.vue";
export default {
  props: {
    myShow: Boolean,
  },
  components: {
    Sidebar,
    Content,
  },
  data() {
    return {
      isShow: true,
    };
  },
};
</script>
