<template>
  <div>
    <input type="text" v-model="state.mytext">
    <button @click="onClick">add</button>
    <ul>
      <li v-for="(data,index) in state.datalist" :key="data">
        {{ data }}
        <button @click="handelDel(index)">del</button>
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
      state.datalist.push(state.mytext)
      state.mytext=''
    }
    const handelDel
    return {
      obj,
      onClick,
      state
    };
  },
};
</script>
