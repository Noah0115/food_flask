<template>
  <div>
    <label>{{ label }}</label>
    <input :type="type" v-model="myvalue">
    <button @click="handleClick">点我啊</button>
  </div>
</template>

<script>
export default {
  props:{
    label:String,
    type:String
  },

  data() {
    return {
      myvalue:""
    };
  },

  mounted() {
    
  },

  methods: {
    handleClick(){
      console.log(this.$parent.title);
      console.log(this.$root.title);
    }
  },
};
</script>