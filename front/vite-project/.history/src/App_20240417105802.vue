<template>
  <div>
    <input type="text" v-model="mytext"  ref="myinput"/>
    <button @click="onClick">add</button>
    <ul>
      {{
        myname
      }}
      <li v-for="(data, index) in datalist" :key="data">
        {{ data }}
        <button @click="handelDel(index)">del</button>
      </li>
    </ul>
  </div>
</template>

<script>
import { reactive, ref, toRef } from "vue";
export default {
  setup() {
    /* const state = reactive({
      mytext: "kersi",
      datalist: ["sds","sda","aaa"],
    }); */
    const mytext = ref("kersi");
    const datalist = ref(["sds","sda","aaa"]);
    const obj = reactive({
      myname: "kersi",
      mayage: 100,
    });
    const myinput=ref(null)
    
    const onClick = () => {
      datalist.value.push(mytext.value);
      mytext.value = "";
      console.log(myinput.value.value)
    };
    const handelDel = (index) => {
      datalist.value.splice(index, 1);
    };
    // const myname = ref("kerwin"); //会把基本类型 包装为 new Proxy({value:"kerwin"})
    return {
      onClick,
      myinput,
      handelDel,
      // myname:toRef(obj,"myname"),
      obj,
      mytext,
      datalist
    };
  },
};
</script>
