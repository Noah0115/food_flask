<template>
  <div>
    <Field label="用户名" type="text" ref="yhm"></Field>
    <Field label="密码" type="password" ref="mm"></Field>
    <Field label="年龄" type="number"></Field>
    <button @click="handleClick">提交</button>
  </div>

</template>

<script>
import Field from "./components/Field.vue";
export default {
  components: {
    Field,
  },

  data() {
    return {
        title:'nihao'
    };
  },

  mounted() {},

  methods: {
    handleClick(){
        console.log(this.$refs.yhm.myvalue);
        
    }
  },
};
</script>
