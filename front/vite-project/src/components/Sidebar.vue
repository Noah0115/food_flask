<template>
  <div>
    <ul>
        <li v-for="data in datalist" :key="data">
        {{ data }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      datalist:["首页","权限管理","个人中心"]
    };
  },

  mounted() {
    
  },

  methods: {
    
  },
};
</script>
<style scoped>
div{
    width: 100px;
}
li{
    padding: 10px;
    text-align: center;
}
</style>