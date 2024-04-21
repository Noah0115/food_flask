<template>
  <div>
    <input type="text" v-model="state.mytext">
    <button @click="onClick">add</button>
    <ul>
      {{ myname }}
      <li v-for="(data,index) in state.datalist" :key="data">
        {{ data }}
        <button @click="handelDel(index)">del</button>
      </li>
    </ul>



  </div>
</template>

<script>
import { reactive, ref } from "vue";
export default {
  setup() {
    /* const state = reactive({
      mytext: "kersi",
      datalist: ["sds","sda","aaa"],
    }); */
    const mytext = ref({
      "kersi",
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
    const handelDel=(index)=>{
      state.datalist.splice(index,1)
    }
    const myname = ref("kerwin") //会把基本类型 包装为 new Proxy({value:"kerwin"})
    return {
     
      onClick,
      state,
      handelDel,
      myname,
      obj,
    };
  },
};
</script>
