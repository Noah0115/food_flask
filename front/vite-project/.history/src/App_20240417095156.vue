<template>
  <div><!-- -->{{ obj.myname }}</div>
  <button @click="onClick">nihao</button>
</template>

<script>
import { reactive } from "vue";
export default {
  setup() {
    const obj = reactive({
      myname: "kersi",
      mayage: 100,
    });
    const onClick=()=>{

    }
    return {
      obj,
    };
  },
};
</script>
