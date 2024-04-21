<template>
  <div>
    <input type="text" v-model="">
    <button @click="onClick">add</button>
    <ul>
      <li v-for="data in datalist" :key="data">
        {{ data }}
      </li>
    </ul>



  </div>
</template>

<script>
import { reactive } from "vue";
export default {
  setup() {
    const state = reactive({
      mytext: "kersi",
      datalist: ["sds","sda","aaa"],
    });
    const obj = reactive({
      myname: "kersi",
      mayage: 100,
    });
    const onClick=()=>{
      console.log("1123")
    }
    return {
      obj,
      onClick,
      state
    };
  },
};
</script>
