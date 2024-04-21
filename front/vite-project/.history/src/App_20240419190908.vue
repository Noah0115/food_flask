<template>
  <div>
    <!-- -->
    {{name}}
  </div>
</template>

<script>
export default {
  data() {
    return {    
    };
  },
  mounted() {
    this.createName()
    
  },
  methods: {
    createName(){
        this.name='张三'
    }
  },
};
</script>

<style scoped>

</style>