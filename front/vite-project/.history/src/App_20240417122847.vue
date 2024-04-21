<template>
  <div>
    <!-- -->
    <input type="text" name="" id="" v-model="mytext">
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  setup() {
    const mytext = ref();
    /* watch(mytext,(newValue,oldValue)=>{
        console.log('ajax',newValue);
        
    }) */
    watch(()mytext,(newValue,oldValue)=>{
        console.log('ajax',newValue);
        
    })
    return {
        mytext
    };
  },
};
</script>
