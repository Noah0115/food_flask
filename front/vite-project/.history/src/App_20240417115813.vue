<template>
  <div>
    {{ obj.name }}
    {{ objName }}
    <!-- -->
  </div>
</template>

<script>
import { computed, reactive } from 'vue'
export default {
    function Search(params) {
        
    }
    setup(){
        const state = reactive({
            datalist:[]
        })
        setTimeout(()=>{
            state.datalist="aaa","as","sss"
        })
        const objName = computed(()=>obj.name+"杀杀杀")
        return{
            
        }
    }
}
</script>
